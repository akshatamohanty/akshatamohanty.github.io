---
title: "Text Similarity Algorithms"
description: Potato, potato. An algorithm developed in the 1950s, stills helps us correct our mistakes. While working on a project dealing with OCR and inevitably OCR erros, I came across Hamming Distance. Hamming distance is a measure between two strings of the same length.
date: 2023-03-02
layout: post
tags:
  - cs-basics
  - algorithms
published: false
---

> Distance Metrics
> They don't measure a physical distance between two points in space but the distance of two "codewords" in their relative abstract spaces.

Distance metrics are of great importance in error detection and correction and in machine learning.
Data transmission is easy these days. However, at the end of the data - all this data is still the same as years before - a huge set of 0s and 1s.

While working on a project using text input generated with OCR, a problem that we came across was trying to ascertain if Text A was equivalent to Text B.

For e.g

Text A: Hodor, Hodor
Text B: Hod0r, Hod0 r

This is a common mistake with OCR - badly read chracters, blank spaces.
