---
title: Everyday principles of software development—Because once in a while we should all go back to basics.
description: 
date: 2024-05-12
tags:
  - software-engineering
layout: post
published: false
---

The purpose of software design, architecture and development is to translate requirements to software products. This is often a complex process rife with ambiguity.

Principles of software development exist to

- streamline this process,
- ensure quality and
- improve the overall efficiency
- of the software projects.

# BDUF (Big Design Upfront)

The process emphasizes the need for high-level planning first and progressive execution in small stages.

- Design the project first, create the flow of the diagram for a high-level overview of each moving part.
- Break down the overall design into stages, based on requirement priority.
- Develop from highest priority first.
- Use BDUF at every step.
- Follow the steps outlined in our plan to implement it.

# Measure twice, cut once

This principle says you must plan and prepare thoroughly and carefully before you take an action. **The requirement stage of the development life cycle can cause more than 50 percent of coding issues if not done correctly.**

- Double-check that all requirements have been covered and no extra requirements have been added.
- Develop high quality blueprints for high quality coding.
- Test your project from the start to ensure that it is working correctly.

# YAGNI (You Aren't Gonna Need It) Principle

In accordance with this principle, programmers should not include functionality unless it is absolutely necessary. Absence of YAGNI may lead to disorganized code and very extensive rework.
Don’t add dead code. Only add a few methods first.
Add more functionality ONLY as more needs arise.

# Occam’s Razor

One of my favourite principles, even in life. Named after English monk William of Ockham, this is similar to YAGNI, i.e don’t create extra entities unless they’re needed.

# Avoid premature optimization

> Premature optimization was said to be the root of all evil in programming.
> ~ Donald Knuth

Optimized code takes more time and effort. And more often than not when the most optimal approach is implemented, software requirements may often change, leading to wasted effort.

- Write the simplest, most obvious version first.
- Add a suite of regression tests to confirm the correctness of the whole system, if you have to optimize later.
- Before optimization, do a trade-off analysis to determine if an optimal better approach is required atop the simple approach.

# KISS (Keep It Simple, Stupid) Principle

Code should be as simple as possible. Simple code is easier to read, more maintainable, easier to test and debug. These can be translated into the following rules:

- Methods shouldn’t exceed 40-50 lines.
- All critical methods should have a commented doc.
- Use the Single responsibility principle - break up the code as you go. Use simple constructions without branching, deep nesting or complex class structure.

# Principle of Least Astonishment

Feature should not have a high-astonishment factor - it should not surprise the code reviewer or anyone else. Code should be intuitive and obvious. Create user-friendly features and comply with people’s expectations. Essentially, be as boring as you can.

# SOLID

SOLID is an acronym for the following principles in Object Oriented Design:

- **Single responsibility**; Each component should have only a single responsibility; it makes it easier to test, maintain and modify code; there is only a single place for DRY updates; it also helps in organization;
- **Open/closed**; in software, we work in stages - working on essentials first, and then additional requirements as the need arises; this principle states that new functionality should be added to code, without breaking existing code. Use composition and inheritance for this. Existing code should be closed for modification, as it would require too many code and test changes;
- **Liskov substitution**; all child/derived classes should be replaceable by their parents, without breaking code or affecting correctness. Use inheritance sparingly. Before inheritance, consider pre and post existence conditions for a class.
- **Interface segregation**; make very small interfaces with limited functionality. Clients shouldn’t depend on or use methods they don’t use.
- **Dependency inversion**; high level modules should NOT be dependent on lower level modules; they should rely on abstractions; abstractions should be independent of details;

# Law of Demeter

An object should never know the internal details of another object. This prevents tight coupling. Keep all components independent of each other.
Keep related classes in the same package.

# DRY (Don't Repeat Yourself) Principle

Code or processes should not be repeated. Code that is reusable, is tested better, more extensible and less buggy.
If the code has duplicate lines, extract the duplicate lines into a different function.
Automate any manual processes.

# Conclusion

This may seem like a LOT of principles. A deeper look however points to the same fundamentals - gather, assess and plan properly, to mindfully write clean code. And what is clean code? Clean code is,

- easy to understand and obvious to other developers.
- well-tested i.e passes all tests; if your code has 0% coverage, your code is dirty.
- doesn’t contain duplication.
- easier and cheaper to maintain.
- minimal number of classes and other moving parts.

# References

- [Principles and Patterns, Uncle Bob](http://labs.cs.upt.ro/labs/ip2/html/lectures/2/res/Martin-PrinciplesAndPatterns.PDF)
- [Principles of Software Development](https://www.turing.com/blog/principles-of-software-development-guide/)
- [Google's Tech Guide](https://techdevguide.withgoogle.com/paths/principles/)
- [Refactoring Guru](https://refactoring.guru/)
