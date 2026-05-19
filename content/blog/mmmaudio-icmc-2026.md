---
title: ICMC Best Paper Award
description: The MMMAudio Computer Music Environment
draft: false
layout: blog-entry
featured_image: /images/mmmaudio-01.png
date: 2026-05-19
year: 2026
tags: ["machine-learning","software"]
---

Here's the paper {{< el "Sam Pluta" "https://www.sampluta.com/index.html" >}} and I presented at ICMC 2026 on [MMMAudio](https://spluta.github.io/MMMAudio/), a new computer music environment that we've created.

*{{< el "Read Full Paper" "https://github.com/spluta/MMMAudio/blob/main/resources/MMMAudioPaperICMC2026.pdf" >}}*

***abstract:***

*We introduce MMMAudio, a new audio creative coding environment designed to close the gap between instrument building and low-level DSP development while reducing the maintenance burden typical of monolithic, compiled systems. Contemporary computer music languages such as Max, Pure Data, and SuperCollider excel at graph-based instrument design but impose steep barriers when custom DSP is required, pushing users into C/C++ plugin workflows with unfamiliar APIs, build systems, and cross-platform complexities. MMMAudio addresses these issues by centering its programming model on Mojo for high-performance DSP and seamless Python–Mojo interoperability for tooling, AI, and scientific libraries. In MMMAudio, unit generators (UGens) are simple Mojo structs, enabling users to write, test, and distribute new UGens without leaving their code editor or contending with external build pipe-lines. This design simultaneously encourages new DSP creation, leverages Python’s mature ecosystem for machine learning and data processing, and exploits Mojo’s performance features (e.g., SIMD) for fast, real-time audio processing. We present the system’s architecture, programming model, and extension mechanisms.*