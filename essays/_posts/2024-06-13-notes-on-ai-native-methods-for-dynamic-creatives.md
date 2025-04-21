---
published: false
title: AI-native strategies to generate dynamic creative assets
description:
date: 2024-06-13
tags:
  - aiml
  - videos
  - svg
layout: post
---

LLMs have fast gained popularity for both directions of

## Description

The current approach from producing a video from a storyboard is algorithmically-driven, where we generate instructions to create a Lottie file with preset animations. The layout and animations are applied programmatically. However, this approach is not scalable and restricts us to only a limited type of videos.

To workaround the drawbacks in the other approach, this document explores AI-native strategies where we could be able to output videos directly, thereby allowing the models to be able to compose more innovative and complex storyboards.

The objectives of this research are:

- To identify technologies that exist for similar use-cases i.e video generation from prompts and specifications.
- To identify known pros and cons of the above technologies and limitations by reading on production use-cases and running experiments.
- To identify the process of implementing the above technologies in production.

## General Approach

A video is a linear combination of static or non-static assets. There are two ways to create these non-static assets:
One-shot (Text/Image -> video).
Combining static assets. (frame-by-frame rendering)
Animating static assets. (static assets, composed as Lottie, SVGs)

## Dynamic Asset Generation Tech

### One-shot

- Runway
- Hotshot
- Sora
- Veo
- Stable Video Diffusion

### Animation-based

- Keyframer

## Strategies

### Approach #1

Description
We stitch together videos, images and text to generate. Only the text is animated using ffmpeg.

Professional looking commercial ads.
Not the 2D graphic animated ads we had initially thought of.

Might be more expensive.
We continue with our current approach, with a frame-by-frame XML / Lottie based animation.

### Approach #2 (Current)

The approach to step-by-step animation application is the same as that taken by Keyframer and might be scalable in the future. Caveat - this is XML versus Lottie.

Participants were surprised by how well the LLM could interpret semantic prompts. Participant EP7, who used words like ‘morph,’ ‘shimmer,’ and ‘grow’ in his prompts, stated, “I was generally impressed by how ambiguous I could be with my descriptions of the animation. It usually picked the correct transform to use, or a reasonable transform to use.” This idea was echoed by EP8, who used the prompt Give me 3 designs where the clouds wiggle: “The fact that it got make the clouds wiggle in an interesting way, in a way that I was happy with, is kind of wild.” This was surprising especially to users who questioned whether they needed to use specific animation keywords: “I would be curious if I can use human language, like pulse or twinkle or if I have to use, like, turn and rotation—more technical words” (EP9).
Key difference
The animation is consumed AT asset creation level.
The animation is implemented AFTER assets.
Example
How to Make an AI Commercial with FREE AI Tools - Tutorial
Keyframer: Empowering Animation Design using Large Language Models - Apple Machine Learning Research
Intermediates
https://hotshot.co/shot/OYf8
https://hotshot.co/shot/OYfA
https://hotshot.co/shot/OYf9
https://hotshot.co/shot/OYf7
https://app.runwayml.com/video-tools/teams/admin423/ai-tools/gen-2
