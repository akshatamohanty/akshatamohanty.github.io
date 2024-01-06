---
published: false
title: Stacking software
description: How do you decide what to add to the stack?
date: 2024-01-02
layout: post
---

Multiple piece abstractions, compose together to create working software. But how do you decide which pieces to actually use? Here's my checklist of questions while constructing a stack?

## Purpose

- For what function am I considering a tool? Do I need to build a way for the user to interact with my code or do I need to persist some data?
- What are the deeper requirements for this function? Is it a data analytics dashboard or gaming portal?

## Performance

- What kind of load am I expecting i.e how many times will this get used? Is it a one-time feature or is it in the critical path for a production feature?
-

## What currently exists in my stack

## Familiarity versus time

## Ease of setup

I have found that the ease of setting up a development tool is a leading indicator of efficiency. Tools that can be easily setup are usually well-tested, peer reviewed, with robust documentation. If an installation takes me 2 hours, and unless it is a really niche - I am probably giving up and choosing something else.

Ease of setup also relates to the purchase process and/or pricing.

- takes a lot more time to install and adds 10 other dependencies
- doesn't work for other team members
- this includes budget: if I have to pitch to business stakeholders too hard, while it takes me a couple of hours to use smoething else, I will use something else.

## Well-supported

Choose tools that are actively maintained and well-supported by the developer community. Regular updates and a robust support ecosystem can prevent future headaches related to compatibility issues and security vulnerabilities.

- when was the last Github commit made
- is it dead in the archives
- is it soon to be dead?

## Feature Set and Quality of documention

Evaluate the tool's feature set to ensure it aligns with your project's requirements. A tool with an extensive range of capabilities might seem attractive, but consider whether it introduces unnecessary complexity or bloat. Conversely, a minimalist tool may lack essential features.

- quality of docs
- do you understand the feature set
- comparisons

## Size and performance

Size and performance are crucial considerations. While a tool may offer extensive functionality, it could also consume excessive system resources. Balance your requirements for performance against the tool's resource footprint to maintain optimal system performance.

- check out bloat

## Ease of reporting

Effective reporting capabilities can greatly aid in debugging and monitoring. Ensure that the tool provides comprehensive reporting features that meet your project's specific needs, as this can save time and effort in the long run.

- what do errors look like?
- give a glance to the stackoverflow answers

## Ease of integration

Interoperability with other tools and systems is vital for a seamless development workflow. Opt for tools that offer straightforward integration options, minimizing friction in your development process.

- how does it play with my other tools
- will I need to have a tool of a tool to make it play well?

---

Making informed decisions about development tools involves weighing trade-offs carefully. A tool's ease of setup, support, feature set, size, performance, reporting capabilities, and integration potential should all factor into your decision-making process. By considering these aspects, you can strike a balance that best suits your project's unique requirements, ensuring a smoother development journey and ultimately delivering a better end product.
