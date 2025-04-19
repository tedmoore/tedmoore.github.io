---
title: Adapting _saccades_ for the Allosphere
description: using machine learning and equirectangular projection
draft: false
layout: single
featured_image: /images/binaryCanary.jpg
date: 2024-04-27
---

In spring of 2024 I was asked to present [_saccades_](/works/saccades) in the [Allosphere](https://allosphere.ucsb.edu/): at 360 degree video sphere with 60 channel surround sound at UC Santa Barbara. My saxophone playing collaborator [Kyle Hutchins](http://www.jefferykylehutchins.com/) was doing a west coast tour and was invited to play there. He though it would be cool to bring _saccades_ to this very tech-forward space and I thought it would be a fun challenge I wanted to make sure to take advantage of what they have.

## Sound Spatialization

The original work is only for stereo sound but now there were 60 channels to work with. I had the original Reaper sessions from the composing process so I could build off the stems that I had there. Also, when creating the video design for the first movement, I put a marker in Reaper at every onset for which I wanted to have a change of video design (a new set of stochastic parameters for the various video synths and source video playback). I realized I could use these markers to slice the stems _at_ these onsets and then place each one of these sound slices in a different speaker. 

I wrote some code in SuperCollider to consume the list of markers from Reaper, loop over each stem and create a new sound "slice" between all of the adjacent marker positions (including the beginning and end of the stems so the outer slices would not be missed). Rendering all of these many hundreds of slices to disk would not be a great idea for two reasons: (1) it would duplicate what I already have on disk and (2) I would need a way to know _when_ each slice was drawn from in the stem. Instead I used [James Bradbury](https://jamesbradbury.net/)'s awesome [ReaCollider](https://github.com/madskjeldgaard/ReaCollider) (extended by [Mads Kjeldgaard](https://madskjeldgaard.dk/)) to construct a Reaper session that would point at all the appropriate source audio files but place "items" (sound clips) in Reaper tracks at the appropriate spots in time. I was even able to begin each clip 30 milliseconds early and end them 30 milliseconds late with a 30 millisecond fade in and out to avoid any discontinuities in the individual speakers.

This all worked quite well to isolate musically-relevant sound clips to spatialize throughout the room, however manually positioning hundreds of clips in 60 speakers was not going to be the most appealing or interesting (or musically valuable) approach. 

## Equirectangular Video