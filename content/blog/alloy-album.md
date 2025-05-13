---
title: _alloy_ the album
description: 90 minutes of feedback cymbal, saxophone multiphonics, and sine tones
draft: false
layout: single
featured_image: /images/multiphonic-81.jpg
date: 2025-05-09
tags: ["machine learning","feedback"]
---

After having performed [*alloy*](/works/alloy/) many times with [Kyle](http://www.jefferykylehutchins.com/), we decided to record a whole album of just feedback cymbal + saxophone multiphonics. 

**Track 1 from *alloy*:**

<audio controls>
  <source src="/audio/alloy-1.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

see the [code](https://github.com/tedmoore/alloy) referenced below.

## Multiphonic Similarity Lookup

The main technological idea behind the album was to use a system that would analyze the "pitch class content" of the feedback cymbal in real-time, find  the saxophone multiphonic with the most similar pitch class content, and display it to the saxophonist to perform, (perhaps) blending harmonically with the cymbal (I say perhaps because the microtonality of the cymbal *and* multiphonics makes for some juicy proximities). We've also performed live using this system.

### Making the Dataset

To create the dataset for this system we used recordings of the saxophone multiphonics listed in *The Techniques of Saxophone Playing* by Marcus Weiss and Giorgio Netti. The book has a compendium of multiphonics for soprano, alto, tenor, and bari, we just used alto and bari since we knew that's what we wanted to use on the album, however now that the code exists it would be very possible to add the other saxophones, or any instrument really for which there are many multiphonics recordings. Each multiphonic fingering is identified with an integer, however when a multiphonic fingering listed different expected pitches for different dynamics we added a letter to differentiate (1a, 1b, etc.).

All of the recordings were analyzed using SuperCollider's built in `Chromagram.kr` (yes, not the FluCoMa one, but you can read more about [Chroma here](https://learn.flucoma.org/reference/chroma/)). A max pooler with a leaky/decay coefficent (of 0.999) was used to give more weight to pitches that are *louder* in the multiphonic (by having their presence be around "longer" because of the decay). This was useful because the instability of multiphonics means they might vacillate between different focal pitches over a duration of time. If one pitch was quite loud but not present very often, I wanted a way for it to still register strongly in my analysis. After recording the chromagram analyses across time I took a weighted average of each pitch class (using [BufStats](https://learn.flucoma.org/reference/bufstats/) with a time series of amplitude analyses as the weights) to get a vector of 12 values representing the "average" pitch class content of the multiphonic. I fit this dataset to a [KDTree](https://learn.flucoma.org/reference/kdtree/) for fast nearest neighbor lookup.

### Assessment

In order to aurally assess the dataset (basically, does it sound like the analysis strategy described above worked?) I reduced it to two dimensions using [UMAP](https://learn.flucoma.org/reference/umap/) and clicked around to listen if the near points had similar pitch class content. This qualitative assessment showed that multiphonics that ended up with similar chroma vectors *did* sound to have similar pitch class content.

### Performance

In performance the signal from the feedback cymbal is analyzed in real-time using the same chroma analysis and max pooler. Thirty times per second this instantaneous analysis is sent to the KDTree to find the nearest chroma vector in the dataset of multiphonics. The multiphonic's fingering and expected pitches (as displayed in the Weiss Netti) is then shown on screen. In order to avoid too much flickering between different images, there is a confidence threshold, requiring the nearest neighbor lookup to consistently return the *same* multiphonic for many frames in a row before it is displayed (and then it slowly fades in to make it easier to look at). Also displayed to the saxophonist is the current pitch (transposed for the instrument) so they have the option of playing ordinario as well.

The nearest neighbor lookup works quite well: there are certainly correlations that emerge, tones that harmonize, and frequencies that resonate. As mentioned before, the inharmonic and non-equal-tempered nature of both the saxophone multiphonics and the feedback cymbal also lead to some juicy dissonances and beating patterns. All of these are lovely outcomes of using this system. Sometimes Kyle follows the displayed multiphonics and pitches closely leading to harmony and consonance, sometimes he ignores it or "fights" it, leading to dissonances and tension, all of which is, of course, part of musical form and development.

One of the takes that ended up on the album was a live room recording with both of us performing together in real-time, however most of the material was recorded separately one at a time. I recorded my cymbal part first, then Kyle listened to that through headphones while watching the real-time analysis display and recording the saxophone part. We realized that it would give us more control over the mix and allow for the multiphonic selection to be more pure (sometimes the saxophone sound would be picked by the cymbal microphone). 

## Adding some Sine Tones

After mixing the album to include the saxophone and feedback cymbal I thought it could use one more element to alloy the materials together. Because so much of the material is essentially sustained timbres, without much morphology, I wanted to extend this further by capturing and sustaining the timbres using [FluidSineFeature](https://learn.flucoma.org/reference/sinefeature/). Every so often, the code analyzing the recording takes a snapshot of the current sinusoidal resynthesis parameters (top 24 peaks of the spectrum). These frequencies and amplitudes are frozen and used to initialize a bank of 24 sustaining sine tone oscillators that swell up and down in volume. The frequencies of the oscillators are modulated ± 0.25 semitones *very* slowly to give some tuning variation and perhaps some slight morphology and/or beating. The amplitudes are adjusted according to their corresponding frequency's [A-weighted perceptual loudness compensation](https://en.wikipedia.org/wiki/A-weighting) so that higher frequencies don't get too piercing (this isn't completely necessary since the frequency/amplitude pairs are being draw from audio where the frequency contour has already been managed, however I found that adding this adjustment made it sound nicer!). I tweaked the parameters listening in real-time, but because it's 90 minutes of music I wanted to make a non-real-time rendering system using SuperCollider's NRT score feature. (I figured it would take less than 90 minutes for me to make the NRT version and do the rendering, which turned out to be true.)

Because the sinusoidal resynthesis is based on analysis of the feedback cymbal *and* saxophone multiphonics the sine waves really blend the two together, even further melding the two metals. The sustains fill in any gaps in the performance, making the whole album more sustained and cohesive. Many of my favorite parts of the album are when I truly can't tell what is generating a timbre: saxophone, cymbal, or sines. 