---
tag: certification
layout: post
title: Preparing for the Google Cloud Associate Engineer Exam
summary: What is the Google Cloud Associate Engineer exam about and how to ace it?
date: 2020-09-23
image: https://images.pexels.com/photos/167682/pexels-photo-167682.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260
credits: https://images.pexels.com/photos/167682/pexels-photo-167682.jpeg
badge: guide
---

## TLDR;

**Why take the Google Associate Cloud Engineer Exam?**
  - Holisitc introduction to cloud computing
  - Better end-to-end understanding of cloud-based infrastructure
  - "Signalling" - as proof of skills to potential recuiters

**How to prepare for the exam?**
  - **theory**: learn about the product offerings & their purpose
  - **decision-making**: picking the right product aligned to business goals
  - **practice**: familiarity with the actual commands and interface

<br/>
-----
<br/>

I recently took my Google Cloud Associate Engineer Exam (and passed)! Check out [my credential here.](https://www.credential.net/2c22d5df-2091-4f8f-98f1-4db1eedc8504)

It took a years' worth of procrastination and 3 weeks of panick-ed focused preparation. However, it has been an incredibly useful learning experience and I wish I would have gotten to it sooner.

<br/>

# What is a Cloud Engineer and why should you care?

I am a Fullstack Engineer and I've been working with GCP for almost two years now. My work is usually centered around feature development, hence my knowledge of GCP had been limited to very specific deployment or monitoring processes, directly used as part of my job.

Thus, my reasons for taking this exam was two-fold:
- to understand the underlying infrastructure architecture at my company better, and
- to be exposed to the whole array of solutions that GCP offered that I didn't directly get to work with

However, there are many other good reasons to take this exam.

For starters, let us look at the formal definition of what an Associate Cloud Engineer does.

> An Associate Cloud Engineer deploys applications, monitors operations, and manages enterprise solutions. This individual is able to use Google Cloud Console and the command-line interface to perform common platform-based tasks to maintain one or more deployed solutions that leverage Google-managed or self-managed services on Google Cloud.

It's succint and accurate. However, I feel the relevance of this exam goes beyond the scope of the role described above.

With the aggressive growth in the cloud engineering, GCP or any cloud platform is fast becoming an integral part of any software development pipeline. Getting familiar with this area is soon going to be as crucial as understanding version control.

Hence, the Google Cloud Associate Engineer Certification is great if you
- want to break into the tech industry as a Cloud Engineer / DevOps Engineer / System Architect
- want to augment your skills as a developer, even in other verticals such as frontend, backend, machine learning etc
- want to join or are joining a cloud-based company in any role and want more context
- want to code your own software-startup

Maybe you don't really **need** the cert for the last two, but paying money for something always acts as a good motivation to learn!

<br/>

# Starting Preparation

So, now that you've decided to go for it - the first thing is to book your examination. The cost of the exam is **USD 125**. The exam consists of 50 questions MCQs to be finished in 2 hours. Time-wise, the exam is forgiving. There's more than enough time if you know the content - I was able to go through my answers twice before submitting.

For budgeting, it could be slightly steep. However, given the increasing demand for cloud engineers - there seem to be more than enough funding opportunties. For me, passing the exam allowed me to use my education budget offered by my company. For women in Singapore, CodingGirlsSG is offering training as well as a funded attempt at the exam as part [Code with Cloud Programme](https://cloud.codinggirls.sg/). Google also offers discounts and promos pretty frequently, as part of various challenges.

I'd recommend booking the date **before** you start preparing - to combat procrastication (atleast marginally!). The date is easily changeable without any additional cost, for upto 72 hours before the exam. So, if you do get to that point un-prepared, you can still cost-freely procrastinate away!

Go ahead, book your exam [here](https://www.webassessor.com/).

Congratulations! Now that you have booked your exam, we need to build out our plan to prepare for this exam.

Minimally, you should go definitely through the following resources:

- [Google Cloud Associate Engineer Exam Guide](https://cloud.google.com/certification/guides/cloud-engineer)
- [Google Cloud Associate Engineer Practice Exam](https://cloud.google.com/certification/guides/cloud-engineer)
- [Dan Sullivan's Udemy Course](https://www.udemy.com/course/google-certified-associate-cloud-engineer-2019-prep-course/) or the [Official Guide](https://books.google.com.sg/books/about/Official_Google_Cloud_Certified_Associat.html?id=wwGQDwAAQBAJ&redir_esc=y)
- [Preparing for the Google Cloud Associate Cloud Engineer Exam - Coursera](https://www.coursera.org/learn/preparing-cloud-associate-cloud-engineer-exam)
- [GCP Products & Services](https://cloud.google.com/products), quickstarts & guides

<br/>

# The Mindset: 3 keys objectives

The GCP is not a straight-forward exam. It asks practical questions with a business context - questions that you might face on the job. Apart from just testing facts, it tests your ability put the knowledge into use to make decisions.

It is essential to keep this in mind while beginning your preparation.

## Theory

If you are new to GCP (even if you are not!), it's good to first get an overview of everything that you need to cover. Here's a checklist for that:

- [ ] Take a quick glance at the [Google Cloud Associate Engineer Exam Guide](https://cloud.google.com/certification/guides/cloud-engineer)
- [ ] Take the [Google Cloud Associate Engineer Practice Exam](https://cloud.google.com/certification/guides/cloud-engineer). This will help you understand the type and scope of questions asked.
- [ ] Complete the [Preparing for the Google Cloud Associate Cloud Engineer Exam](https://www.coursera.org/learn/preparing-cloud-associate-cloud-engineer-exam) from Coursera. It gives a quick, summarized overview of all the different products. Don't stress on learning every detail as of now - that will come with repeated exposure to all the different concepts.
- [ ] Go through [Dan Sullivan's Udemy Course](https://www.udemy.com/course/google-certified-associate-cloud-engineer-2019-prep-course/). It's about 4 hours and in my opinion, pure gold as preparation for this exam. Every word uttered is important and expect to go through this multiple times, as part of you prep.

**Digging Deeper**
You should now be pretty confident in the general lay-of-the-land. It's time to dig deeper into the details.

- [ ] This awesome [checklist by xyz]() lists out all the concepts and products you'll need to be familar with. You might need to update it if the syllabus has changed - but it will serve as a good tracking system.
- [ ] Start exploring the product documentation with the checklist on the side. For every offering, Google provides a ton of resources. But the most critical sections to building a solid understanding are (using Cloud Run as an example):
  - [product page](https://cloud.google.com/run),
  - [concepts](https://cloud.google.com/run/docs/concepts), and
  - [how-to-guides](https://cloud.google.com/run/docs/how-to)

For each product, go through the above sections **in order**, making a mental note of any critical facts (for eg, limitations or scale of input etc) and consolidate the how-to with [Qwiklabs](qwiklabs.com).

## Critical Thinking

If you've prepared well with the above, this should come easy. But I felt, I did have to go back to my fact-gathering to understand some key differences and purposes in using different products, while trying to correctly solve the business-type questions.

Here's an example of such a question:

> Some question
> Answer:

Some ways to get better at this are:

- [ ] Make a comparison table between products; one place to see all properties, key points to have better insight into what can be used where
- [ ] Read the different case-studies listed on the product overview page
- [ ] For any pratice questions, dig deeper into the incorrect options and try to understand why something is incorrect, as opposed to why something is correct

## Practice

Yay! You've made it! You are reasonably confident. But learning without practice is a deception.

So,
- [ ] Do atleast 2-3 mock tests - the number isn't important but what is important is to repeatedly take them till you can solve all with 100% accuracy. When you get something wrong, make a note about the section in which you got it wrong (storage, kubernetes, app engine etc) and revisit it armed with product documentation.
- [ ] Do relevant Qwiklabs, especially the Challenge Labs. As mentioned before, Google frequently offers multiple cloud challenges which allow you get access free study material like Coursera and Qwiklabs. Make use of that - it is a fun way to learn with others that have the same goal as you. For eg, the Google Majulah v2 is currently on right now!

<br />

# Final thoughts

Hopefully, this guide should help you ace the exam!

One to note is that the knowledge gained while preparing for this exam, is easily transferable to other cloud platforms too. The names of the products and interface would change but the key fundamentals and understanding of the different components within a cloud-based architecture would be the same.

So, go on, take the test and best of luck! Hope to see you soon on the other side!


<br />
<br />
