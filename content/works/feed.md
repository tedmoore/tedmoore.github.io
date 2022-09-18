---
title: feed
draft: false
year: 2018
description: bassoon, live processing, no-input-mixer, tape, and DMX lights
layout: single-works
categories: ["composition"]
tags: ["feedback","multimedia","lights"]
featured_image: /images/feed-duo.jpg
---

{{< youtube-float YR7me9SsLSE 60 right >}}
_feed_ was created in collaboration with bassoonist {{< el "Ben Roidl-Ward" "https://www.benroidlward.com/" >}} for {{< el "Experimental Sound Studio" "https://ess.org/">}}'s Oscillation Series.

_feed_ integrates multiple modes of real-time lighting control using custom tools that implement DMX parameterization, machine learning, music information retrieval, and Reaper sequencer integration. My DMX parameter control system is a family of OOP classes written in {{< el "SuperCollider" "https://supercollider.github.io/" >}} that can be implemented with any DMX compatible lights. It allows for user-defined parameter naming and contains built-in timed fades, LFO modulation, control bus following (for audio reactivity), and user-defined function control of individual parameters. In feed, four DMX lights are independently controlled via this system in three distinct ways: (1) Audio from a no-input mixer is analyzed using 23 audio descriptors, which are then sent to a neural network and classified as one of four distinct no-input mixer timbres. This classification is then used to switch between predetermined audio-descriptor parameter mappings, creating a strong connection between lighting parameterization and timbre. (2) Lighting scenes and time-based parametric functions are triggered manually by a user interface, allowing the performer to improvise light-based gesture and phrase without sound. (3) Timed lighting cues are precomposed to synchronize with a paired audio file whenever playback is triggered. These lighting cues are composed with a custom system integrating OSC messages sent from Reaper, however the real-time performance is executed in SuperCollider.​

I've presented on this work and the neural network classification system in a few [presentations](/research/#dmw-talk).
