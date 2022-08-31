---
title: research & software
draft: false
layout: single
---
# Software
{{% center 75 %}}  
_Much of my creative work involves creative coding, so here is just a selection of some tools that are bigger projects and/or may be useful and interesting to others. Checkout my [github](https://github.com/tedmoore) for more._
{{% /center %}}  
* [DJII](/research/djii) modular live electronic fx commissioned by improvising bassoonist [Dana Jessen](https://www.danajessen.com/) (2022) (SuperCollider)
* [Mel-Frequency Cepstral Coefficients (MFCC) Interactive Explanation](https://learn.flucoma.org/reference/mfcc/explain/) (2022) (p5.js)
* [Serge Modular Archive Instrument](/research/serge) (2021-22) (SuperCollider, Processing, & C++ openFrameworks)
* [Aluminum Forest](/works/aluminum-forest) (2021) (Arduino & Supercollider)
* [PlotXYColor](https://github.com/tedmoore/PlotXYColor) plotter for inspecting multi-dimensional data (2020) (SuperCollider)
* [JSON Writer](https://github.com/tedmoore/JSON-Writer-Supercollider) (2020) (SuperCollider)
* Audio-Reactive Modular Video Design (2019) (C++, openFrameworks, Supercollider)
* [Music Information Retrieval Tools](https://github.com/tedmoore/music-information-retrieval) (2019) (SuperCollider, superseded by [FluCoMa](https://www.flucoma.org/) tools)
* [Neural Network](https://github.com/tedmoore/NeuralNetwork) (client side) (2019) (SuperCollider, superseded by [FluCoMa](https://www.flucoma.org/) tools) (see a [performance](/works/shadow) of this in use)
* Module-Tensor: laptop improvisation software (2012-present) (SuperCollider) (see [performances](/improv) of this software in use)
* [Poisson Disc Sampling](https://github.com/tedmoore/poisson_sampling_n_dims) in N-Dimensional Space (2019) (Python)
* [Linear Assignment Algorithms](https://github.com/tedmoore/Linear-Assignment) Port (Munkres & Auction) (2019) (SuperCollider)
* [TSNE](https://github.com/tedmoore/tSNE-SuperCollider) Port (2019) (SuperCollider, mostly superseded by [FluCoMa](https://www.flucoma.org/)'s [UMAP](https://learn.flucoma.org/reference/umap/) and other dimensionality reduction algorithms)
* [Non-Real Time FFT & IFFT](https://github.com/tedmoore/FFTNRT) (client-side) (SuperCollider, superseded by [FluCoMa](https://www.flucoma.org/)'s [FluidBufSTFT](https://learn.flucoma.org/reference/stft/)) 
* Live Video & Audio Sampler (2017) (C++, openFrameworks, see a [performance](/works/still-motion) with this in use)
* ​[Voice Modulator](https://github.com/tedmoore/voice-modulator) for theater artist Eric F. Avery's production of _The Life and Death of Eric F. Avery_ (2016) (Supercollider)
* [LFO / Arpeggiator / Gate / Trigger](https://github.com/tedmoore/Endorphines-Shuttle-Control-for-SC) for Endorphin.es Shuttle Control (2016) (SuperCollider)
* [Microtonal Keyboard](https://github.com/tedmoore/Microtonal-Keyboard) (2016) (SuperCollider)​

# Writing
{{< columnrow >}}
{{% column 50 %}}
### "Polynomial Functions in Žuraj's Changeover" _Perspectives of New Music_ (2022)
A mathematical analysis of Vito Žuraj's orchestral work _Changeover_. Knowing that Žuraj composes using custom made computer-aided composition tools, this analysis reverse engineers some of the equations and algorithms that he may have used. A generative example using Žuraj's methods is included.
{{% /column %}}
{{< column >}}
{{< figure src="/images/zuraj_figure08.jpg" width="400px">}}
{{< /column >}}
{{< /columnrow >}}

{{< columnrow >}}
{{% column 60 %}}
### "Expression, Collaboration, and Intuition" _Wet Ink Archive_ (2022)
Wet Ink Ensemble asked me to share some thoughts on my use of artificial intelligence in my compositional and improvisational practice. The article describes some of my implementations of machine learning for music making, along with some broader thoughts about why I use these algorithms and what I think it might all mean.
{{% /column %}}
{{< column >}}
{{< figure src="/images/274.png" width="300px" link="https://archive.wetink.org/archive-06/expression-collaboration-and-intuition" >}}
{{< /column >}}
{{< /columnrow >}}

{{< columnrow >}}
{{% column 60 %}}
### _Human and Artificial Intelligence Alignment: AI as Musical Assistant and Collaborator_ (2021)
The research I conducted for my PhD included a series of creative projects applying cybernetic systems that use machine learning to my creative practice. I share four of these experiments here including many of the technical details of the implementation. I also share analyses of how I experience using AI for music making, offering a phenomenological understanding of artificial intelligence in the context of creative applications. The concluding section conveys why I choose to use machine learning in my practice, by comparing its use and effects to using randomness and complex systems.
{{% /column %}}
{{< column >}}
{{< figure src="/images/274.png" width="300px" link="https://archive.wetink.org/archive-06/expression-collaboration-and-intuition" >}}
{{< /column >}}
{{< /columnrow >}}


# Presentations

### CCL

{{< figure src="/images/00_resynth_buffer_with_activations.png#floatright" width="500px" link="https://learn.flucoma.org/learn/bufnmf/" >}}
### Non-negative Matrix Factorization for Spatial Audio (2020)  
Due to COVID-19 the 2020 Spatial Music Workshop in the Cube at Virginia Tech was cancelled, but the organizers invited alumni to give talks about some aspect of their work with spatial audio. I presented my use of non-negative matrix factorization (NMF) for audio decomposition and spatialization. See the {{< el "NMF overview" "https://learn.flucoma.org/learn/bufnmf/" >}} I created for the FluCoMa project. 

### Interference Patterns: analysis of interacting feedbacks in _hollow_ (2020)

This presentation analyzes the feedback system of my piece, hollow, which uses three large PVC tubes to create feedback at the resonant frequencies of the tubes. Through filtering, delay line modulation and serial feedback routing, various emergent sonic properties arise. Analysis of the resulting sounds provides some insight into the behaviors of the system.
​slides

{{< youtube-float jMZP_UF8gg0 80 right >}}
### Preserving User-Defined Expression through Dimensionality Reduction (2019)
This is a talk a I gave at the FluCoMa Plenary Session at CeReNeM at the University of Huddersfield in the UK. It demonstrates various machine learning algorithms implemented in my improvisation software and how I use those algorithms to explore new modes of expressivity.
video of talk
slides

### ​Machine Learning Applications for Live Computer Music Performance (2019)

Presentation at the University of Chicago Digital Media Workshop. This presentation demonstrates three uses of machine learning in live computer music performance: (1) using a neural network to classify no-input mixer timbres for light control, (2) a frequency modulation synthesizer that predictions synthesis parameters based on novel incoming spectra, and (3) a TSNE based dimensionality reduction system for low-dimensional control of synthesizers with high-dimensional parameters spaces.
slides

### Approaches to Live Performance and Composition with Machine Learning and Music Information Retrieval Analysis (2019)

This presentation offers three creative uses of machine learning: (1) using audio descriptor analysis and machine learning to organize grains of audio into a performable two dimensional space, (2) using a neural network to classify no-input mixer timbres for light control, and (3) using a traveling salesperson pathfinding algorithm to re-organize audio grains into a new sequence.
slides
