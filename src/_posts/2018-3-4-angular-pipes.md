---
title: Angular Pipes - A summary
subtitle: The smart way to style your content
date: 03-4-2018
categories: post
tags: angular pipes
layout: post
---

While working on my projects, I often find situations when I need a piece of string to shorten itself and get appended by an ellipsis. This little piece of code does just that, as a pipe in Angular Applications. 


#### What is a Pipe?

Angular is awesome for displaying data! The two-way binding, the centralized data-services - they all make me sleep easy at night (most of the times!). Pipe is another such simple but powerful feature. Most of the time, you will store, retrive and manipulate raw data - numbers, dates, strings etc. If a person last logged in on April 3, 2018, the value is probably stored as 1522739114055 in your database. However, displaying this value directly to the user - might be a little ... uh... disturbing for the user, not to mention all the UX junkies who will haunt you in your dreams. So now, one way would be you could painfully write a function in your component.ts file, to convert your data values to human readable strings and add this function in every component that needs it. Or ... you could make a Pipe! And magically tranform your dates ... into awesome messages for your user! 


#### How to use a Pipe?

```
<div class="data"> {{ some_data | date: 'short'  }}</div>
```



| some_data        | result           | 
| ------------- |:-------------:|
| 1522739114055      | Apr 3, 2018 |



#### Key Takeaway 

This template is pretty much all you need to build a basic Angular pipe. Two key things to keep in mind - 
- Remember to include this pipe in your **declarations array** in the **app.module.ts** file.
- The **tranform** function is the hero of a pipe. This is where all the processing takes place. 
