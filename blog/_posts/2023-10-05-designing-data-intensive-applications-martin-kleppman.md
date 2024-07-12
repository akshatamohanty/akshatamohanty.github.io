---
title: Designing Data Intensive Applications, Martin Kleppman
description: Foundational resource for understanding and building large scale systems.
date: 2023-10-05
layout: post
image: /assets/embeds/ddis/ddis-overview.png
wip: true
# menu:
#   - label: Overview
#     list:
#       - label: About the book
#         href: about
#   - label: Foundations
#     list:
#       - label: Basics
#         href: about
#       - label: Thinking about data
#         href: bitwise
#       - label: Querying data
#         href: odd-even
#       - label: Data transfer
#         href: performance
#       - label: Data privacy
#         href: math-slow
#   - label: Distributed data
#     list:
#       - label: Partitioning
#         href: about
#       - label: Duplication
#         href: bitwise
#       - label: Consensus
#         href: odd-even
#   - label: Deriving insights
#     list:
#       - label: Stream processing
#         href: about
#       - label: Batch processing
#         href: bitwise
#       - label: Future
#         href: odd-even
#   - label: Critical thoughts
#     list:
#       - label: About the book
#         href: about
---

## Introduction

This has been long quoted as a fundamental book every software engineer should read. And it did live upto my expectations. The book said it would discuss big ideas and what stood out to me was how well structured it was.

<br/><br/>

![Book Overview](/assets/embeds/ddis/ddis-overview.png "Designing Data Intensive Applications, Martin Kleppman")

## The three pillars of systems - reliabilty, scalability and measurability

_Reliability._
Error-proof. Tolerating hardware and software faults, human errors.
The system should continue to work correctly (performing the correct function at the desired level of performance) even in the face of adversity (hardware or software faults, and even human error).

_Scalability_
Measuring load and performance. Latency percentiles, throughput.
As the system grows (in data volume, traffic volume, or complexity), there should be reasonable ways of dealing with that growth. See “Scalability”.

_Maintainability_
Operability, simplicity and evolvability.
As more people work on it, to maintain and grow - they should be able to work on this productively.

Data Systems are painfully obvious. They need repeated implementations of the same type of functionality:

- Store and recover data - databases
- Memorize heavy computation - caches
- Search for data - search indexes
- Process data elsewhere asynchronous - data queues / stream processing
- Process large amounts of accumulated data - batch processing

## Thinking about data

Why are data models important?
Because they determine how we think about and understand the data at hand.

What is the main function of a data model?
To abstract away the complexities and inner workings of a given layer.
Describe the history of different data models.
Historically, we started with hierarchical data models. However, they didn’t capture entity-entity relationships well. Hence, in the 1970s, Edgar Codd proposed the SQL data models, with tuples and relationships between the tuples. This worked great for business transaction processing, and later for a lot of other applications. However, in the 2010s, developers felt restricted by the strictness of SQL schemas and explored more free-form data models like NoSQL, better known as Document databases. They worked well for capturing data with not many interlinks between the entities. Another database that came into popularity was Graph databases, for addressing the other spectrum of data, with many cross-links.

What are the different kinds of query languages?
Query languages are usually imperative or declarative. Declarative query languages declare what is required but do not map the data access method. Hence, they offer greater optimization for less flexibility. Conversely, imperative query languages offer much more flexibility and power at the cost of optimizations gained by specialized query engines.

What are the benefits of a document model?
Document databases are preferred for:
Higher scalability, larger datasets
High throughput write databases
Open source implementations
Flexible schemas
Complex query support
