---
published: false
title: "Startup Engineer #0: The Beginning"
description: Build for yourself, or build for others?
date: 2022-07-26
layout: post
tags:
  - startup
  - user
---

Four years back, I moved from `#research` into `#tech`. And the decision to not join a startup was deliberate.

The pace, growth and autonomy in a startup appealed to my nature. However, startups work fast. And working fast comes with trade-offs. I wanted to know the trade-offs.

So I took my time to learn from established large-scale systems, observe "best practices" at work and train with expert mentors and colleagues. Finally, a year back - I joined a startup.

This series has been long overdue.

But nevertheless, here I am, hoping to capture the engineering perspective of building an early-stage startup from scratch. There'll be war stories, hacks, errors, mysteries or just cool bits of technology. Honestly, this is mostly my personal technical retrospective as I navigate the unknown.

So without much ado, here's my first:

## Know your user.

We are building a 10x engineering org. (Or so we like to think!)
And DevOps is obviously one of the foundational pieces.

With that thought, we started our DevOps journey with a simple goal - dockerize our main backend. Purpose was to get consistent dev environments, onboard engineers faster. Happy Engineers = Happy Life!

So after 2 weeks of hacking, going up some knowledge curves and iterations - we managed to get it all dockerized...

... only to realize that the Docker experience is pretty questionable on Windows. 1 / 2 devs on our team are Windows users. Not Docker-fans and voted against it, when asked. So much for Developer Experience!

Know your user.

And live to learn another day!
