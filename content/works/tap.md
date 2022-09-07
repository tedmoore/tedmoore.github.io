---
title: "tap"
draft: false
year: 2019
description: percussion trio and multimedia
layout: single-works
categories: ["composition"]
tags: ["multimedia"]
featuredimage: images/tap.jpg
---

{{< youtube-float DoVEwDdaLYQ 65 right >}} 
Commissioned by {{< el "line upon line percussion" "https://www.lineuponlinepercussion.org/" >}}  
recorded at UT Austin, January 12, 2019  

Composing _tap_ began by recording many sounds, gestures, and passages on my eurorack modular synthesizer and then organizing these recordings into a tape part for the piece. I then transcribed the rhythms and timbres of the tape part to create a tight synchronization between the the tape and percussion parts played by the ensemble. The video and lights were then composed to add to the intense synchrony.

To ensure the synchronization of all four mediums (performers, tape, video, & lights) I developed a system to compose all aspects of the piece in the {{< el Reaper "https://www.reaper.fm/" >}} (digital audio workstation) timeline. The tape part was constructed in Reaper normally. The instrumental parts were composed using MIDI triggering samples of drum hits. The lights were controlled by typing commands of a custom API into Reaper timeline markers, which were then sent over OSC to {{< el "SuperCollider" "https://supercollider.github.io/" >}}, parsed and sent to the lighting instruments. The video was coded in C++ using {{< el "openFrameworks" "https://openframeworks.cc/" >}} which was controlled and triggered similarly by markers in the Reaper timeline.

By having everything controllable in one timeline, I was able to fluidly manipulate the various aspects of the composition. While focusing one media component (the lights perhaps), any adjustments or creative ideas relating to other media could easily be perused and tested. The DMX lights used in the performance could be set up and watched in real-time while making adjustments to color, timing, even positioning. A light-control mock-up system was created in SuperCollider that allowed me to make adjustments if the lights were not available during a working session. 

[full score](/scores/tap_-_score_210611_01__with_tech_diagram_.pdf)

{{< figure src="/images/tap/tap-api.jpg" caption="Custom API for controlling lights used in _tap_" >}} 