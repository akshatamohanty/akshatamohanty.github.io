---
layout: post
group: blog
title: Understanding dynamic programming concepts with the coin-change example
summary: Dynamic Programming is a method of problem-solving where you breakdown the problems into smaller subproblems, similar to the original problem. It may or maynot use recursion.
date:   2018-06-06
categories: post
type: post
category: tech
---

# What is Dynamic Programming?

Dynamic Programming is a method of problem-solving where you breakdown the problems into smaller subproblems, similar to the original problem. It may or maynot use recursion. 

For example, the pet question to apply DP can be to get the nth term of the Fibonacci Series;
By definition, F(n) = F(n-1) + F(n-2)

```py
## recursive function
def fibonacci(n):
    if n == 1: return 1
    if n == 2: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)
    
    
# print 50th term
print( fibonacci(50) )
```

If I tabulate the iterations: 

| calling-function   |  dependency  |  dependency  | 
|---|---|---|
|  fib(50) |  fib(49) | fib(48)  | 
|  fib(49) |  fib(48) | fib(47)  | 
|  fib(48) |  fib(47) | fib(46)  | 
|  fib(47) |  fib(46) | fib(45) ... and so on | 

Notice how fib(48), fib(47)... are all repeated? Well, that's redundant. We can reduce this redundancy by saving the computed values in a lookup table. This saving of results, is known as **Memoization**

```py
## recursive function
def fibonacci(n):
    if n == 1: return 1
    if n == 2: return 1
    if n in lookup: return lookup[n]
    else:
      result = fibonacci(n-1) + fibonacci(n-2)
      lookup[n] = result
      return result
    
lookup = {}
# print 50th term
print( fibonacci(50) )
```
<br />

# How is it different from Divide and Conquer?
Divide and Conquer algorithms like split a problem into smaller problems, solve each of them and **combine** the results. Dynamic Programming on the other hand is used to solve problems with **overlapping subproblems**, for example, like in the Fibonacci term computation explained earlier, where the same subproblem was required multiple times.

<br />

# How to know if a problem can be solved with DP?

DP Problems usually have the following characteristics:
- For optimization problems, with a focus on arrangement or ordering of the elements
- They can be broken down into subproblems which as similar to the main problem
- The global optimum found using DP will usualy be more efficient and better than those found by typical heuristics

<br />

# Linear Partition Problem (work-in-progress)
This problem has been described in Steven Skiena, and took me no less than 3 hours to get my head around. Hence, the **attempt** to explain it... 


## Problem Statement: 
Suppose the job scanning through a shelf of books is to be split between k workers. To avoid the need to rearrange the books or separate them into piles, we can divide the shelf into k regions and assign each region to one worker.
What is the fairest way to divide the shelf up?

The first thing to understand is the 'fairest' way to divide the shelf up. The fairest way would be when all partitions are as close as possible to the sum of all pages divided equally amongst the workers. 

Let's start with a fair solutions - say there are 300 pages, and 3 workers. 

| Solution | Partition A | Partition B | Partition C | Average | max | min |
|---|---|---|---|---|---|---|
| Fairest |  100 | 100  | 100 | 100 | 100 | 100 |
| Less Fair | 101 | 100 |  99 | 100 | 101 | 99 |
| Least Fair | 120 | 110 |  70 | 100 | 120 | 70 |

Now, the criteria of evaluation would be to check how much further from the average are each of the partition assignments. However, the constraint that the total sum of pages is constant means that if one partition is say 50 more from the average, it would pull the other two away by a sum of 50 pages from the average, to keep the total number of pages the same. Hence, if the largest partition is smaller, the amount of deviation of the other partitions is also smaller. 

So, this problem can be redescribed as - partition the set of books in such a way, maximum of the partitions is the minimum of all solutions available, i.e, if each partition is pln_n, we need to find - 
min ( max(pln_1), max(pln_2), max(pln_3) .. )

Dynamic Programming is a systematic approach that evaluation all possible options; 

Say the books have the following number of pages:
S1 S2 S3 S4 S5 S6 S7 S8

Let the initial problem be - P(8, 3) i.e 8 elements with 3 partitions, which return the maximum of the partitions of the solution. 

And we put our first partition after S1 ...
 
S1 | S2 S3 S4 S5 S6 S7 S8 

There are two options now - either our optimum solution has a partition after S1 or... it doesn't.

Case 1: 
Our optimum solution has a partition after S1. Now S2, S3... S8, need to be divided by k-1 partitions in such a way, that the maxmimum of those partitions is minimum .... which is exactly the problem we are trying to solve - but with lesser elements and lesser partitions i.e P(7, 2)

Case 2: 
Our optimum solution doesn't have a partition after S1. So, we look at the next solution, we might have a partition after S2. And again this reduces to the same problem as the original problem - P(5, 2)

.. This goes on progressively till we reach the end of where the first partition might be placed.

Now, we need the minimum of Case 1 and Case 2

min ( P(7, 2), P(6, 2), P(5, 2) .. )

<br />

# Questions

https://www.codechef.com/ZCOPRAC/problems/ZCO14002 
```
# wip

def mt(s, st=0):
    if len(s) == 0:
        return 0
    
    min_time = []
    final = None
    if not (lookup[st] == None):
        return lookup[st]
    elif len(s) < 4:
        final = s[0]
    else:
        a = mt(s[1:], st+1)
        b = mt(s[2:], st+2)
        c = mt(s[3:], st+3)
        final = s[0] + min(a, b, c)
    lookup[st] = final
    return final


for test in range(12):
    days = input("Enter days")
    inp = input("Enter sequence")
    seq = [ int(z) for z in inp.split() ]
    lookup = [None]*len(seq)
    mt(seq)
    print(min(lookup[0:3]))

```

<br />

# Resources
- The Algorithm Design Manual - Steven Skiena
