---
title: Rendering Scores with Jinja Templates
description: automation with command line tools
draft: false
layout: single
featured_image: /images/jinja-screenshot.jpg
date: 2025-07-09
year: 2025
---

I used to create scores by exporting the Sibelius files as PDFs and then importing them into Adobe InDesign to add the cover, front matter, tech rider, etc. (I know it's possible to do all this *in* Sibelius... I like to have a bit more control on the layout, formatting, etc.) The issue I had with this was that if I changed any little thing in the score I had to go through the whole process of importing and exporting through InDesign. I even found some ways to script parts of the process (Adobe has a scripting interface to automate some tasks) but still found it onerous. As with other parts of my creative process I find it important to reduce friction wherever possible so that making changes (i.e., improvements) to the work is easy and *more likely* to happen. The workflow below makes this possible not only with changes in the score, but also allows simple text editing in the other materials that are all very quickly rendered into a final document.

I wanted to export the PDF(s) from Sibelius and then run one Terminal command to render the score document. Because this approach would automate the process, I realized I also could render multiple versions of teh score, for example, documents for individual movements and versions that are *anonymized* since some submission processes and such request anonymized documents. This also allowed me to render individual movements as separate documents in case a performer would only be performing one of them. Having all these documents export with a single command makes edits extremely effortless, while keeping all these varieties of documents up-to-date with each other.

The solution I came up with was to use {{< el "Markdown" "https://www.markdownguide.org/" >}} files for editing front matter (cover, performance notes, tech rider, etc.) which are used as {{< el "jinja templates" "https://jinja.palletsprojects.com/en/stable/" >}} to inject different information as needed before being rendered to PDF with {{< el "pandoc" "https://pandoc.org/" >}}. I then use {{< el "cpdf" "https://community.coherentpdf.com/" >}} to collate the various PDF files into one document. This all happens in a Python script (see below).

For example my work [*arco*](/works/arco) (2024) for violin, video, & tape is in five movements. The violin part for each movement is a different Sibelius file. The Python script below grabs those 5 PDFs and exports 12 documents: a complete score that includes all the movements, a score (including title page, front matter, etc.) for each of the five movements, and an anonymized version of all the previously listed files.

To see the templates used and other accoutrement see this {{< el "GitHub Repo" "https://github.com/tedmoore/score-docs-jinja" >}}. 

```python
import jinja2
import os

def render_template(template_file, context):
    loader = jinja2.FileSystemLoader(searchpath=".")
    env = jinja2.Environment(loader=loader)
    template = env.get_template(template_file)
    rendered_text = template.render(context)
    return rendered_text
        
def context_to_pdf(template_file, context, output_file):
    rendered_text = render_template(template_file, context)
    with open("temp.md", "w") as f:
        f.write(rendered_text)
    os.system(f'pandoc --pdf-engine=xelatex -i temp.md -o {output_file}')
    os.system('rm temp.md')
    
def replace_spaces(s):
    return s.replace(" ", "_")

def render_scores(anonymize):
    context_to_pdf("cover.jinja.md", {"redact": anonymize}, "cover.pdf")
    context_to_pdf("front-matter.jinja.md", {"redact": anonymize}, "front-matter.pdf")
    
    titles = ["cylinder lullaby I","acute","bezier","angle","cylinder lullaby II"]
    roman_numerals = ["I","II","III","IV","V"]
    
    for i, title in enumerate(titles):
        context = {
            "movementtitle": title,
            "romannumeral": roman_numerals[i],
            "redact": anonymize
        }
        context_to_pdf("movement-title-page.jinja.md", context, f"movement-title-page-{i+1}.pdf")
        
    system_call = 'cpdf cover.pdf front-matter.pdf '
    for i in range(5):
        system_call += f'movement-title-page-{i+1}.pdf ./../sibelius/mvt-{i+1}.pdf '
        
    if anonymize:
        system_call += '-o rendered-scores-anonymous/0-arco-ANONYMOUS.pdf'
    else:
        system_call += '-o rendered-scores/0-arco-by-Ted-Moore.pdf'
            
    os.system(system_call)
    os.system('rm cover.pdf')
    
    for i in range(5):
        system_call = f'cpdf movement-title-page-{i+1}.pdf front-matter.pdf ./../sibelius/mvt-{i+1}.pdf '
        title_no_spaces = replace_spaces(titles[i])
        if anonymize:
            system_call += f'-o rendered-scores-anonymous/{i+1}-{title_no_spaces}-ANONYMOUS.pdf'
        else:
            system_call += f'-o rendered-scores/{i+1}-{title_no_spaces}-by-Ted-Moore.pdf'
        os.system(system_call)
        os.system(f'rm movement-title-page-{i+1}.pdf')

    os.system('rm front-matter.pdf')
        
if __name__ == "__main__":
    render_scores(False)
    render_scores(True)
```