---
title: "quartet"
draft: false
year: 2021
description: quartet ensemble and video processing
layout: single-works
categories: ["composition"]
tags: ["multimedia"]
featuredimage: images/quartet.jpg
---

**_Musicologist {{< el "Jacob Hart" "https://jacob-hart.com/" >}} has written a nice article about this work. {{< el "Read it here" "https://learn.flucoma.org/explore/moore/" >}}._**

{{< vimeo-float 540621361 65 right >}}
_created with the [[Switch~ Ensemble]](http://www.switchensemble.com/):_  
Zach Sheets, flute  
T.J. Borden, cello  
Wei-Han Wu, piano  
Megan Arns, percussion

_quartet_ is a remote collaboration between myself and the [Switch~ Ensemble] designed to engage with the added technological mediation at play during the pandemic. The sonic source material of quartet is about two minutes of eurorack synthesizer recordings transcribed for the [Switch~ Ensemble] to record. These recordings were then subjected to data analysis using audio descriptors and machine learning algorithms using {{< el "FluCoMa" "https://www.flucoma.org" >}}. Approaching these acoustic and electronic sounds as _data_ for comparison and manipulation offered me new strategies for combining the material in expressive ways, finding form, and creating sonic relationships and audio-visual objects that I wouldn’t otherwise consider.

The audio manipulation and playback was all done in {{< el "SuperCollider" "https://supercollider.github.io/" >}} which set OSC messages about the currently playing sound to custom software created with {{< el "openFrameworks" "https://openframeworks.cc/" >}} in c++ that looked up what video frame to display on the screen. All the sections were recorded live using a {{< el "Syphon" "http://syphon.v002.info/" >}} Server and later edited together. 
