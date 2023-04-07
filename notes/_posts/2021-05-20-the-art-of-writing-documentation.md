---
title: "Better Software Documentation: Checklists and Best Practices"
description: "No one likes documentation. One could argue that good code is self-documenting. The argument would be a fair one. However, effective documentation not only helps understand code, but can also improve code. And many times, documention helps serve non-developers more than developers. So how do you write documentation that survives the test of time? Here are some ways to create better docs."
date: 2021-05-20
image: https://images.pexels.com/photos/357514/pexels-photo-357514.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=750&w=1260
tags:
  - code
  - documentation
layout: posts/blog
---

Up until recently, I'd considered documentation irksome and something for "hand-overs". I believed that clean, commented code should be self-documenting. Recent experiences have made me reconsider my opinion.

Say you have or are a new engineer on the team. With no clue about the tech stack, the terminology and the "tribal knowledge". So what happens in the absence of a "tribal"? Long, painful hours of reading code, following dependencies to try and distill out the intent.

Code is a bad way of documenting intent. Code is an implementation of intent. Documenting what code is supposed to do, in a language understandable to all, leads to better validation and visibility. Code can be buggy, but it is hard for validated, trusted documentation to be buggy.

Documentation is great for:

- effective onboarding
- effective debugging
- stakeholder management
- documenting the why, capturing decisions and reasoning
- retrospectives

This post outlines some things to consider while writing documentation.

##### Plan the structure

Good stories have good structure. They consider the audience and pace the information. Documentation is the story of your code. <u>The goal of documentation is to serve the reader. To provide answers. And to do that as effectively as possible.</u>

There is nothing more frustrating than going through large pieces of text, full of unexplained terminology - only to realise it wasn't relevant.

##### Add an outline

Add a list of contents at the outset, that'll allow the user to immediately navigate to the section most relevant to them.

##### Do not skip the introduction

Add an introduction, to set context and introduce stakeholders.

Goal of this section is to,

- allow the reader to quickly determine if this documentation is relevant to them,
- if they will get the information they are looking for and
- how to find required information fast

Here are some key points to include,

- Describe what the project is
- What does the project do
- What technology the project uses
- What are the key stakeholder workflows that the project affects
- How does it relate to the total infrastructure
- What does this documentation cover
- Who should read this documentation

This is good place to interlink with any parent/sibling documentation. Also provide links to any design documents, product specfications here.

This section helps identify the key stakeholders at this point - the main development teams, the consumers of this code and the business areas that the code affects. Elaborating on this section also helps the author of the documentation think about who their target audience is. This helps tailor the writing, add/subtract any details and missing context and ascertain.

##### Follow Progressive Information Disclosure

- Explain terminology, fundamental concepts building blocks early
- Keep information scannable - by using header heirarchy
- Information flow should be drilldown - broad to details

##### Overexplain - focus on the why

Whenever explaining logic, explain the rationale behind that logic. Documentation is a great place to capture business and technical intent in one place.

When explain technical architecture or decisions, always have a section that outlines the business (soft) requirement that led to that decision.

##### Use Templates

When explaining technical details, use templates.
Details about common software elements like databases, queues etc, should have the same layout of documentation. For eg, a queue can be described with a table, with the same headers, covering the same information.

This helps reduce cognitive load for the reader. Once they are used the format, they already know what to expect and where to look.

##### Practical Views

Add practical examples, expected payload formats wherever possible. For interactions and processes - outline the end-user impact, the design language and specify contracts

##### Use Visualizations - Diagrams, Tables and Tools

Diagrams, charts, tables etc help provide structure to information to make it easily scannable.

> A picture is worth a thousand words

- (Over) Use tables, schemas and diagrams
- Simplify - use only one per concept
- Name the diagrams, tables (be mindful of making it human-readable)
- Add legends to diagrams
- Use standard symbols for technical components (keep this consistent across all documentation)
- Identify and add diagrams for key workflows and critical paths
- If possible, embed videos
- Think about the layout - documentation doesn't need to be a boring, linear dump of colorless information

##### Complementary Sections

It is easy to forget the smaller details in the big picture of things. But keep the documention comprehensive, as much as possible. Adding simple sections for monitoring, links to dashboards, other documents that provide additional context, a glossary and an FAQ section as simple ways of achieving that goal.

##### <a name="maintenance"></a> Maintenance

Change is the only constant in the world.

Code will change. Intent will change. Technology will change. New features will get added. Here are some ways to ensure that documentation remains fresh and updated.

- Use documentation as an onboarding tool: For every new member on the team, use the documentation as a single entry point.
- Comment your code: Add inline comments and cross-link to documentation
- Plan for periodic syncs with other stakeholders; Have them draw out mentals models, to evaluate the efficiency of your documentation
