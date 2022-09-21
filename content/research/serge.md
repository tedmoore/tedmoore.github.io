---
title: Serge Modular Archive Instrument
description: software for exploring vintage Serge sounds
year: 2022
draft: false
featured_image: /images/serge/serge-full.jpg
tags: ["software","machine learning"]
---

The _Serge Modular Archive Instrument_ (created in collaboration with {{< el "Jean Brazeau" "https://221a.ca/contributors/jean-brazeau/" >}}) is a sample-based computer emulation of selected patches on the vintage Serge Modular instrument that is housed at Simon Frasier University in Vancouver, Canada. The project is conceived of as both an instrument for sonic exploration and an archive of the sound worlds made by this 50+ year old instrument, including (or highlighting) all of the idiosyncrasies it has accumulated over the years.

{{< figure src="/images/serge/serge-plot.jpg#floatright" width="70%" >}}
### Recording & Analysis

For each patch included (currently there are five) we recorded tens of thousands of one-second samples of different parameter settings by systematically stepping through parameter combinations (sent to the Serge using the {{< el "Expert Sleepers ES-3" "https://www.expert-sleepers.co.uk/es3.html" >}}). These samples were then analyzed using the {{< el "FluCoMa" "https://www.flucoma.org/" >}} Toolkit for analyses such as {{< el pitch "https://learn.flucoma.org/reference/pitch/" >}}, {{< el "spectral descriptors" "https://learn.flucoma.org/reference/spectralshape/" >}}, {{< el "timbral descriptors" "https://learn.flucoma.org/reference/mfcc/" >}}, {{< el loudness "https://learn.flucoma.org/reference/loudness/" >}}, and more. The data set created is then reduced to two dimensions using {{< el PCA "https://learn.flucoma.org/reference/pca/" >}} and then {{< el UMAP "https://learn.flucoma.org/reference/umap/" >}}.

### Control 

These audio samples can then be accessed by navigating a two-dimensional plot (plus color), which can show the sound samples according to pitch, pitch confidence, loudness, spectral centroid, spectral flatness, or either of the two UMAP dimensions. Additionally, a skeuomorph of the Serge Modular highlights which knobs control the synthesis parameters used, allowing the user to imitate controlling the vintage instrument. Beneath the two-dimensional plot there is a step sequencer for storing chosen samples to be returned to in sequence.

All of the control parameters (including _x_ and _y_ plot navigation, skeuomorph knobs, and step sequencer) are controllable via MIDI and OSC allowing user defined control of the instrument.