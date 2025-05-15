---
title: Creating *quartet* 
description: a FluCoMa "etude"
draft: false 
layout: single 
featured_image: /images/quartet-umap.jpg 
date: 2021-04-24 
tags: ["machine learning","intermedia","video"]
---

*written/published May 14, 2025*

{{< youtube-float C0FBNLy4NCM 65 right >}}
I created [*quartet*](/works/quartet) in collaboration with the {{< el "[Switch Ensemble~]" "https://www.switchensemble.com/" >}} for the 2021 SEAMUS Conference which was held online because of the pandemic. Because I knew that the work's "premiere" would be held as a prerecorded video concert on YouTube, I decided to approach the work not as a live, electro-acoustic composition, but as a fixed-media, video-art piece that made use of the of the necessary technological mediation at play.

In this entry, I describe the process of creating the dataset of audio and video recordings and then the results of different machine learning processes applied to the media: concatenative synthesis using KNN lookup, timbre transfer using neural networks, and reorganizing the corpus into a time series based on similarity of audio analyses via dimensionality reduction and path-finding algorithms.

# Composing the Dataset

I composed about two minutes of music for flute, piano, cello, and percussion. The instrumentation was determined in conversation with the ensemble. As with many of my works around this time, the instrumental parts were composed by transcribing (by ear) a tape part composed first. This tape part was pieced together from excerpts of improvisations on a eurorack synthesizer. In some moments of the final version of the piece, the tape and instrumental parts are heard simultaneously.

**Excerpt of the tape part that was transcribed by ear to create the instrumental parts.**

<audio controls>
  <source src="/audio/quartet-tape-excerpt.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

Knowing that I was planning to create the video art through audio analysis, data science tools, and machine learning algorithms, I made some compositional choices with the aim of providing these algorithms with a diversity of sonic content in the hopes of finding more possible outcomes. The first minute of composed music was comprised of fast, dense, gestural music that would provide a lot of varying timbres and a diverse set of data points in close temporal proximity. The second minute consisted of primarily sustained notes in the cello, flute, and percussion (bowed vibraphone) mostly based around the pitches Gb and F (and just intonation shades of these pitches) spread out over multiple octaves. I knew that many of the machine learning approaches I would undertake were based on measures of distance/similarity between analysis vectors so I wanted to see how the diversity of the first minute would compare to the second minute, how the slight variations in pitch would compare to each other, and how "similarity" might be perceived by these algorithms across different octaves, timbres, and pitch classes.

Because this was a remote collaboration I sent the score, parts, and tape part to each of the performers and had them record the audio and video performance of their part to a click track (for later synchronization). After receiving all the media from the performers I edited the recordings so they could be played back synchronously as an ensemble, cleaned and de-noised any artifacts, and noted if and when performers were tacet in each recording (to avoid in later analysis).

Additionally, each performer received a different set of instructions to record some sounds based on text descriptions and/or imitating abstract audio recordings on their instrument. For example, I asked the percussionist to record takes using various auxiliary percussion instruments, the flute and cellist to record themselves attempting to imitate noisy synthesizer sounds, and the pianist to perform actions with and at the piano such as sit backwards, leave and enter the room, and adjust the lid.

**Examples of sounds that the performers were instructed to imitate.**

<audio controls>
  <source src="/audio/quartet-imitation-for-cello.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

<audio controls>
  <source src="/audio/quartet-imitation-for-everyone.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

Next, the audio recordings of the performers were sliced into 100 millisecond slices and each slice was analyzed with 105 audio descriptors seen in Figure 1. Because many of the descriptors are based on an FFT analysis and the 100 ms slices contain more than one STFT analysis frame, each descriptor was summarized as the mean analysis across all STFT frames in the slice. Most all of these analyses were conducted using the {{< el "FluCoMa Toolkit" "https://learn.flucoma.org/" >}} (two analyses: zero crossing and sensory dissonance were derived with Nick Collins' {{< el "SCMIR" "https://github.com/sicklincoln/SCMIR" >}}). Throughout the process, most of the audio analysis, machine learning, and audio playback was conducted in [SuperCollider](https://supercollider.github.io/). Different subsections of this data set were used for different sections of the work, as described below.

**Figure 1: All 105 audio descriptors used in the data set for *quartet***.

| Column   |&nbsp;&nbsp;&nbsp;&nbsp;Audio Descriptor(s)           |
|:---------|:-----------------------------------------------------|
| 0–39     |&nbsp;&nbsp;&nbsp;&nbsp;40 MFCCs                      |
| 40       |&nbsp;&nbsp;&nbsp;&nbsp;Spectral Centroid (Hz)        |
| 41       |&nbsp;&nbsp;&nbsp;&nbsp;Spectral Spread (Hz)          |
| 42       |&nbsp;&nbsp;&nbsp;&nbsp;Spectral Skewness             |
| 43       |&nbsp;&nbsp;&nbsp;&nbsp;Spectral Kurtosis             |
| 44       |&nbsp;&nbsp;&nbsp;&nbsp;Spectral Rolloff (Hz)         |
| 45       |&nbsp;&nbsp;&nbsp;&nbsp;Spectral Flatness (dB)        |
| 46       |&nbsp;&nbsp;&nbsp;&nbsp;Spectral Crest (dB)           |
| 47       |&nbsp;&nbsp;&nbsp;&nbsp;Frequency (Hz)                |
| 48       |&nbsp;&nbsp;&nbsp;&nbsp;Frequency Confidence (0–1)    |
| 49       |&nbsp;&nbsp;&nbsp;&nbsp;Loudness (dB)                 |
| 50       |&nbsp;&nbsp;&nbsp;&nbsp;True Peak (dB)                |
| 51       |&nbsp;&nbsp;&nbsp;&nbsp;Zero Crossing (Hz)            |
| 52       |&nbsp;&nbsp;&nbsp;&nbsp;Sensory Dissonance (0–1)      |
| 53–92    |&nbsp;&nbsp;&nbsp;&nbsp;40 Mel Bands                  |
| 93–104   |&nbsp;&nbsp;&nbsp;&nbsp;Chromagram (12 TET)           |

### Audio-Video Integration

Much of the audio-video playback is not sequential and/or not at the originally recorded speed. In order to display the correct video frames in real-time I sent [OSC](https://ccrma.stanford.edu/groups/osc/index.html) messages from SuperCollider to a bespoke [openFrameworks](https://openframeworks.cc/) application 30 times per second (to match the frame rate) indicating where on the screen to display which video frames(s). Because this openFrameworks application needed to have very fast access to any frame in many video files I found I needed to use the [HAP](https://hap.video/) video codec. Although ordering the appropriate video frames could have been done after audio rendering in non-real-time and later recombined with the audio, I choose to keep all my rendering in real-time in order maintain a fluid, fast, iterative workflow able to assess the audio-visual intrigue of the material in real-time. In order to capture an audio-video stream to disk, I used the [Syphon Server](https://syphon.github.io/).

### Non-Machine Learning Passages

Many passages in *quartet* are created not with machine learning approaches to the corpus, but instead by performing a custom instrument for digital audio-video "tape" manipulation. The recordings of the players are played back as four synchronized play heads. One knob manipulates the playback rate and direction (from -4x to -0.25x and 0.25x to 4x) of all four streams simultaneously allowing manipulation and exploration of the material. Additionally, four momentary toggle buttons loop the four performers respectively with a random tape length between 200 to 2000 ms at a random rate between 0.2x and 5x and a random direction (forward or backward). Improvising with the instrument revealed many interesting results which were then rehearsed and recorded for inclusion in various parts of the work.

# Machine Learning & Data Science Results

## Concatenative Synthesis

{{< youtube-float KSGT9Qxm61o 65 right >}}
The second section of the work (1:24-2:30) features concatenative synthesis using the acoustic instruments as the source and crunchy electronic sounds as the source. Passages of audio from each of these instrumentalists were selected to be a good fit for the aesthetic goal of this section. Some of the passages used were created by directing the instrumentalists to imitate the crunchy electronic sounds of the target. A subset of 16 descriptors was selected for use in this passage: the seven spectral analyses of FluidSpectralShape (spectral- centroid, spread, skewness, kurtosis, rolloff, flatness, and crest) plus MFCCs 1-9 (thus not including MFCC zero). The dataset of each instrumentalist was separately scaled and fit to a KDTree.

To determine similarity, the electronic is sound is analyzed in real-time for the same 16 descriptors. Each time an onset was detected (using SuperCollider's Onsets.kr with an FFT size of 512 and a threshold of 0.4.) in the electronic sound there was a random 1 in 8 chance of triggering a similarity lookup for each of the three instrumentalists. When triggered, the real-time analysis vector would be scaled by the instrumentalist's respective scaler and then passed to the KDTree for a nearest neighbor lookup in the 16 dimensional space. The nearest neighbor position in the instrumentalist recording would then be played back for a random duration between 300 and 1200 milliseconds (even though the original analysis was 100 ms) at a rate between 3 and 6 times the original speed. The sped up videos perceptually matched the fast "scorrevole" character of the electronic sound. While rendering the audio-visual media, the playback of the electronic sound was delayed by one hop size (1024 samples) to compensate for the real-time analysis and one control block to compensate for the latency of the KDTree lookup. Throughout this section, there is a manually executed fade of the electronic sounds becoming quieter while the sounds of the instrumentalists become louder. Perceptually this is hard to notice because of the sonic similarities and therefore is created as an exercise in considering the "similarity" between the target electronic sounds and the corpus of instrumental sounds.

Also throughout this section are interjections of loud synthesizer sounds displaying full screen moments of instrumentalists. These excerpts were created with the same process, although instead of triggering similarity lookups with onsets, similarity lookups occur 10 times per second (to match the 100 ms slices) while the target electronic sounds are above a threshold of -30 dBFS. The slices are played back for their native 100 ms duration at their native playback rate. These excerpts were rendered separately and then organized as interjections in the final compositional stages.

## Timbre Transfer

The next section (2:30-3:43) attempts analysis-resynthesis timbre transfer. Each of the four instrumentalists are seen playing a passage agnostic to what the others are playing, however, instead of hearing the recorded acoustic sound we hear electronic sounds that seem to track with our perceptual expectations of pitch, envelope, gesture, and even timbre.

Creating this section started by training neural networks to predict synthesis parameters from audio descriptors. Data sets were created by systematically stepping through the entirety of a quantized parameter space for a synthesis algorithm and recording the audio of each parameter combination. Audio analyses (MFCCs 1-13, FluidSpectralShape, FluidPitch, ZeroCrossing, and SensoryDissonance) were conducted on all the recorded audio and then paired with the synthesis parameters used. A multilayer perceptron was trained to predict the synthesis parameters from the corresponding audio descriptor analysis. Next the recorded audio of each instrumentalist was analyzed using the same descriptors and sent to the neural network for predictions. The predicted synthesis parameters were then used to synthesize audio, which is what is heard in the video. The loudness of the synthesized audio was controlled by loudness analysis of the source recording of the instrumentalist.

**Which synthesis algorithms were used for training and with which instrumentalist they were paired.**

| Instrument | &nbsp;&nbsp;&nbsp;&nbsp;Synthesis Algorithm |
|:-----------|:--------------------------------------------| 
| Flute | &nbsp;&nbsp;&nbsp;&nbsp;Simple Frequency Modulation |
| Piano | &nbsp;&nbsp;&nbsp;&nbsp;All 48 modes of the [MiBraids](https://github.com/v7b1/mi-UGens) SuperCollider UGen (mode changes randomly on each onset) |
| Percussion |&nbsp;&nbsp;&nbsp;&nbsp;One of the MiBraids modes |
| Cello |&nbsp;&nbsp;&nbsp;&nbsp;Imitation of an analog [Benjolin](https://scsynth.org/t/benjolin-inspired-instrument/1074/1) module |

While these synthesis algorithms will never be able to truly imitate the respective acoustic instruments, they make a compelling and entertaining effort. The instrumentalist is perceived to be (and literally is) controlling the synthesis algorithm with their playing. These correlations between pitch, envelope, gesture, and timbre are non-trivial enough to elicit musical expression through this algorithmic process.

## Path Finding

In mathematical graph theory and computer science the Traveling Salesperson Problem aims to find a path minimizing the cost of connecting a set of nodes in graph. This is often imagined as minimizing the distance a traveling salesperson needs to travel on a tour visiting many cities (graph nodes). For this section of *quartet* (6:44-9:15) I approached the data set of 100 ms audio slices as the nodes of a graph positioned in high dimensional space and used two strategies (described below) to minimize the required distance to create a path visiting each slice one time. The resulting path was then used as the temporal order for a reorganization of the sound slices. What is heard during this section are excerpts from the results of these two strategies selected and further reorganized to create musical form.

### Preprocessing

The data set used for this process started in 714 dimensional space by finding the seven statistical summaries (of [FluidBufStats](https://learn.flucoma.org/reference/bufstats/)) for the time series and first derivative across the slice for each of the first 51 descriptors in the table above. Next I removed any slices where the mean loudness of a slice was less than -60 dBFS. Lastly I standardized the data for each dimension to have a mean of zero and standard deviation of one.

Before applying the path finding algorithms, I chose to reduce the number of dimensions from 714 down to a more manageable number for a few reasons. First, this would enable the path finding algorithms to work more quickly. Secondly, using Principal Component Analysis (PCA) for this would likely marginalize any redundancy and/or noise in the data, focusing my multidimensional space on the greater variance, or important differences, between the data points. Using PCA I was able to reduce 714 dimensions to just 11 dimensions while preserving 99% of the variance in the dataset. Two important observations should be made here. The first is that reducing the data set to less than 2% of the original number of dimensions while maintaining 99% of the variance means that most all of the data in the data set was either redundant or noisy. The second observation is why this might be the case: because each time slice was only 100 ms long (4410 samples) and my analysis used an FFT size of 1024 and a hop size of 512, this resulted in a time series of each descriptor only 9 values long. The very small number of values in these time series makes the statistical summaries of FluidBufStats not very powerful measures for comparing data points likely creating a lot redundancy and noise in the data set. As this was one of my first "etudes" with FluCoMa, I wanted to try out all the possibilities and see what it could handle, but now I see how to better choose features.

### Path Finding Strategy 1: TSP-Solver {#tspsolver}

This dataset was then imported into Python and processed with the Python library [tsp-solver](https://pypi.org/project/python_tsp/), which attempts to find a sequence of sound slices that minimizes the distance traveled in the 11 dimensional PCA space. This sequence was then reimported to SuperCollider and played back in real time with an overlap of 4 (a new 100 ms sound slice was started every 25 ms) and each slice receiving a 30 ms fade in and fade out. The video was rendered in real-time as described above.

{{< youtube-float 20HOHmRj7Kg 65 right >}}
The visualization seen in the video shows the path (black line) in real-time as the sounds slices are heard and video clips are shown. The plot is a two dimensional projection of the 11 dimensional space created using the Uniform Manifold Approximation and Projection ([UMAP](https://learn.flucoma.org/reference/umap/)) algorithm. The colors of the points are the result of a [KMeans](https://learn.flucoma.org/reference/kmeans/) Clustering algorithm done in the 11 dimensional space, providing a visual peek into how clusters of points may be related to each other in higher dimensions. As the black line zigzags across the screen it often makes large jumps that seem out of line with the goal of TSP: to create a path as short as possible. It is important to remember that (1) the path was created in 11 dimensional space and it is now being visualized in two dimensional space, so what looks like a large jump on this UMAP projection might actually be a short distance in higher dimensions and (2) TSP attempts to create the shortest path it can, however, the Traveling Salesperson Problem is notoriously difficult, therefore it's "shortest path" may still end up having large jumps.

### Path Finding Strategy 2: UMAP

{{< youtube-float jdF4sW1aVDE 65 right >}}
The second strategy to create a path through the 11 dimensional space was to perform dimensionality reduction down to just one dimension using UMAP. The units of UMAP's output (in this case single value vectors: positions in one dimensional space) do not correspond to any musical parameter, however, the distance between points in the resulting one dimensional space does correspond to estimates of similarity (via neighbor relations). Rather than using this similarity in a creative way, I only sorted the slices according to their single value vector, collapsing any measure of adjacent slices' similarity or difference to each other, but preserving the macro ordering of slices into a sequence that can be played back. It should be noted here that while TSP explicitly attempts to create a sequence of slices that minimizes distance in the 11 dimensional space, this is not what UMAP is attempting to solve for (these differences are seen and heard in the results). UMAP performs dimensionality reduction by embedding all the data points into a lower dimensional space while attempting to preserving neighbor relations between points as well as the global structure of the data set. Similar to the TSP solution, a visualization shows the resulting sequence of points while hearing the slices and seeing the video excerpts.

### Comparing TSP-Solver and UMAP

**Source position and path ordering of TSP results.**

<figure>
  <img src="/images/quartet-tsp.jpg" alt="Plot of where each ordered slice came from in the TSP path solution." style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Plot of where each ordered slice came from in the TSP path solution.</figcaption>
</figure>

**Source position and path ordering of UMAP results.**

<figure>
  <img src="/images/quartet-umap.jpg" alt="Plot of where each ordered slice came from in the UMAP path solution." style="width: 100%;">
  <figcaption style="text-align: center; font-size: 0.9em;">Plot of where each ordered slice came from in the UMAP path solution.</figcaption>
</figure>

The figures above show where each slice in the path came from in its respective source file. Each point's position on the *x* axis shows its position through time in the path. The *y* position shows which sound file and where in the sound file it came from (higher on the *y* axis indicates earlier in the sound file).

Comparing the results of the two approaches both sonically and visually, the TSP algorithm moves between different timbres more quickly, often giving a sense of gestural transition between them. An initial sequence moves through a clear clustering of sustained pure sounds from the flute, cello (natural harmonics), and bowed vibraphone, before the path then begins rapidly changing between instruments, not always with clear sonic relationships or connections. These rapid changes create contours in dynamics, pitch, and timbre that imitate gestures or phrases a composer might write. (Of course this may be, in part, because the source material that these 100 millisecond slices are drawn from is recorded audio of musical gestures and phrases that a composer did write.) For example, the changing notes in the flute create a melodic contour (0:21-0:31 in the TSP visualization), which is also supported by pitches in the cello and piano. Additionally, changes in register, loudness, and timbre give the passage a dynamic energy that I find musically compelling. The quick changes between source files can be seen above. Although there is some clear clumping of certain sound files near the beginning, the path clearly jumps around somewhat frantically throughout most of the sequence. There are small clumps in various places where one section of one sound file seems to have been intensely focused on for a short period of time.

The video created with the UMAP algorithm has a very different musical sensibility to it. Unlike the TSP visualization, it does not have abrupt changes in timbre, instead creating longer trajectories of transformation that often cover a more homogenous body of sound. For example from 0:07 to about 0:40 the cello sound transforms from low forte arco notes to high squeally piano notes. The overall form of this video more clearly divides the instruments into different sections, beginning with the cello trajectory and then moving through large clusters of piano, flute, and percussion. Interestingly, the ending shows a similar clustering as the TSP video's beginning, clustering the pure sustained sounds from the flute, cello, and vibraphone. Unlike the image of the TSP positions and path orderings, in the UMAP plot, one can see the sound files more clearly clustered with themselves and even clustered with other sound files of similar timbres. The larger trajectories heard in the video can be observed as density crossfades between these clusters. Comparing the plots of the two algorithms, one can also observe similar tight clusters in specific sound files in different places in the the timeline (highlighted by colored boxes).

These two videos were edited to remove sections I did not like and reorganized to create composed form. Material from the TSP video was mostly used as gestural phrases and connective music, while material from the UMAP video was used for larger formal trajectories.

# Conclusion

When writing *quartet*, I set out to explore the FluCoMa toolkit, which had just recently come out, making many of these processes available in my native coding environment, SuperCollider. The toolkit instigated new ways of thinking about sound and my compositional process. Approaches to concatenative synthesis, timbre transfer, and similarity-based corpus reorganization led to interesting musical results that were organized into a larger form to create the final work.