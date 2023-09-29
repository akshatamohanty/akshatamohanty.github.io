---
published: false
title: "Correct code by construction: Learnings from Programming Pearls"
description: "Easy access to development tools, quality assessment teams and fast deployment cycles come with the disadvatage of lazy programming. Code is machine language, means code runs in constraints. This articles delves into the paradigms of code checking and automatic verification."
date: 2023-07-02
layout: post
menu:
  - label: Automated Verification
    list:
      - label: What is automated verification?
        href: automated-verifiaction
      - label: Principles
        href: principles
  - label: Test Driven Development
    list:
      - label: What is TDD?
        href: tdd
      - label: Why is it hard?
        href: hard-tdd
  - label: In Practice
    list:
      - label: Binary Search Example
        href: binary-search
      - label: Implementing Tests
        href: tests
      - label: Run-Time Errors
        href: runtime-errors
---

# Introduction

Building a startup is challenging. You are constantly building prototypes. But those prototypes also need to meet a certain level of standard. If those prototypes are in traditional fields like Finance, then the importance of accuracy and reliability of those prototypes becomes even greater.

In my current company, we faced an issue of an increased number of bugs in our code. While facing a problem such as this, it is easy to zero them solution down to something like - "write better code". But what exactly is better code? And how do you ensure it?

Good code is code that does what it is supposed. Even better code is resilient, extendable and readable. Developers often get lazy, especially for easy code and outsource testing to QA.

what is the problem:

- writing code that is accurate, in a less-time consuming way

why do bugs happen

- incorrect mental model of what an external library does
- incorrect state of the code
- validation of inputs

validation of the problem

- personal exerpeince
- there's a whole field dedicated to it
- some fields require accuracy more than others - smart contracts, financial systems
- binary search required 4years to get a correct implementation

what is the solution:

- knowing methods of automated verification and the science behind programming
- implementing this with tests

what is automated verification

- the field of testing that a code is correct
- line by line analysis - checking the state of code in each state
- principles - assertions, sequential control structures, conditional control structures, iteration control structures, functions
- what is programming by contract

why is tdd important

- forces you to have a deep understanding of your code
- if you didnt, you wouldnt be able to write cases for it
- assertions catch violations and knowing the nature of the violation allows you to correct, without introducing more bugs
- tests also work very well as documentation
