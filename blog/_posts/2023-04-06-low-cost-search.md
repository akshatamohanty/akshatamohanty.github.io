---
published: false
title: "Building Awen's Internal Search Engine"
description: We built an in-house text search service for 20 million records costing less than $1 / month.
date: 2023-04-06
layout: post
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

[Awen](https://awen.finance) is a machine learning startup that provides AI-powered underwriting tools to financial institutions. The underwriting process is a labour-intensive process requiring triangulation of data from multiple sources. Aggregating, processing and consuming large datasets to surface insights is critical to Awen's mission.

Awen compiles data from multiple sources. For our first use-case, we had a database of companies with 22 million records, containing rich information about their location, directors etc. We need to build way to effectively search this database by company name, location, promoter names' and other parameters.

Latency was critical because this was a background service. And if this took time, other AI models dependent on this data would be stalled and take longer. All insights from Awen's tools are realtime. Hence, a long latency wasn't an option.

This service would be a high traffic service with high volume of reads, but not as many writes.

### Estimations

For India alone, we had 21 million (active) entites. Assuming

### Evaluating Existing Options {#evaluation}

| Service            | Storage | Compute | Fixed Cost | Serverless                   |
| ------------------ | ------- | ------- | ---------- | ---------------------------- |
| OpenSearch         |         |         |            | Yes, with minimum commitment |
| Mongo Atlas Search |         |         |            | Coming Soon                  |
| Typesense          |         |         |            | No                           |
| ElasticSearch      |         |         |            | No                           |

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

Ideas to talk about:

1. what is text search and when do you want to use one?
2. current providers and comparisons.
3. our requirements.
4. why we decided to build it inhouse.
5. system diagram.
6. the ngram algorithm.
7. challenges.
   - ngram generation
   - memory errors
   - regeneration issues
8. final product - live demo.
9. takeaways
   - what it doesn't do
   - final costs
