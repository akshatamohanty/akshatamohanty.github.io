---
title: "Chip Search: Awen's Internal Search Engine"
description: We built an in-house text search service for 20 million records costing less than $1 / month.
date: 2023-04-06
layout: posts/default
menu:
  - label: Context
    list:
      - label: Use Case & Contraints
        href: context
      - label: Evaluating existing options
        href: evaluation
      - label: Rationale for In-house
        href: rationale
  - label: Methodology
    href: method
    list:
      - label: ngrams
        href: ngram
        list:
          - label: heloo
            href: hello
          - label: world
      - label: system design
        list:
          - label: heloo
          - label: world
      - label: implementation
  - label: Challenges
    list:
      - label: Memory Issues
      - label: Edge Cases in Matching
      - label: Latency
      - label: Limitations of Lambda
  - label: Conclustion
    list:
      - label: Demo
      - label: Insights
---

### Building Awen's Internal Search Engine {#context}

[Awen](https://awen.finance) is a machine learning startup that provides AI-assisted underwriting tools to financial institutions. The underwriting process is an intensive process requiring triangulation of data from multiple sources. Aggregating, processing and consuming large datasets to surface insights is critical to Awen's mission.

Awen has a company database with 22 million records with details of enterprises across India. We need to build way to effectively search this database by company name, location, promoter names' and other parameters.

Latency was critical because this was a background service. And if this took time, other AI models dependent on this data would be stalled and take longer. All insights from Awen's tools are realtime. Hence, a long latency wasn't an option.

This service would be a high traffic service with high volume of reads, but not as many writes.

### Evaluating Existing Options {#evaluation}

| Service            | Storage | Compute | Fixed Cost |
| ------------------ | ------- | ------- | ---------- |
| OpenSearch         |         |         |            |
| Mongo Atlas Search |         |         |            |
| Typesense          |         |         |            |
| ElasticSearch      |         |         |            |

### Rationale for In-House Solution {#rationale}

Nostrud eiusmod esse occaecat eiusmod aliqua commodo quis eiusmod occaecat fugiat ea. Lorem incididunt voluptate dolore commodo duis minim pariatur mollit aute dolor irure. Ad esse est nisi labore velit elit. Et consectetur officia consectetur sit minim tempor consectetur eu nostrud reprehenderit laborum. Exercitation veniam sunt eiusmod velit exercitation ex deserunt quis ullamco dolor cupidatat laborum esse. Irure occaecat ad irure ut officia ea. Est esse nulla sunt ut et exercitation elit tempor quis Lorem.

Labore eu occaecat commodo do deserunt. Velit deserunt ullamco dolore exercitation minim in occaecat excepteur quis tempor adipisicing id. Dolore laborum aliquip elit occaecat non laboris incididunt enim eiusmod aliqua incididunt Lorem. Eiusmod aute deserunt amet magna Lorem occaecat mollit culpa tempor cupidatat ipsum.

### Methodology {#method}

Nisi labore ad cupidatat fugiat. Et cillum sunt irure ad eu ullamco enim laboris enim ea ea. Officia deserunt consequat irure laboris aute minim magna. Laboris aliqua adipisicing et consequat cillum ut dolor elit ut. Eu eu dolore nostrud incididunt cillum aliqua consectetur deserunt dolor proident sunt reprehenderit et velit. Et aliqua veniam adipisicing nisi labore veniam dolor dolor deserunt nulla amet in. Incididunt non id aliqua duis. Nostrud laboris dolore ex duis fugiat enim cillum nisi adipisicing in velit aliquip aliqua. Nostrud excepteur eiusmod dolor sint ex nisi sit consectetur ea commodo labore id.

#### System Design

#### How it works?

#### Ngrams: Storage & Computation {#ngram}

### Challenges {#hello}

#### Out of Memory

#### Matching

#### Latency

#### Limitations

### Conclusions

#### Demo

#### Insights

Cost was really cheap.
Results were good.
