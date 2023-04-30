---
title: Floored By Floor
description: In computing, flooring a number is a common operation. Pretty mundane, but the perks of working with big data is that mundane things get exciting. Big Data breaks language limits.
date: 2023-04-12
tags:
  - javascript
  - performance
layout: posts/default
menu:
  - label: Approaches
    list:
      - label: Using Math.floor
        href: math-floor
      - label: Using Bitwise Operators
        href: bitwise
        list:
          - label: ">>, >>> or ~~"
            href: bitwise
          - label: Why do bit operators work?
            href: bitwise-work
      - label: Using a custom algorithm
        href: odd-even
      - label: Performance Comparisons
        href: performance
      - label: "But why is Math.floor slow? (hint: modulo)"
        href: math-slow
---

Flooring a number is boring.

Javascript has a built-in `Math.floor`. Use that, and there's no reason to think.
That was until we found out it was **four times** more expensive than the alternatives. Quite a rabbit hole.

Here's what we were trying to do:

```
Find `c` where `c` is the closest interger less than `(a + b) / 2`.
```

Firstly, I'd never considered an alternative. So I was surprised to find so many.
More importantly - they aren't all the same.

## Approaches {#approaches}

### Use the builtin Math.floor {#math-floor}

There are two ways of doing this:

**Option 1**

`const midpoint = Math.floor((a + b)/2)`

**Option 2**

`const midpoint = a + Math.floor((b-a)/2)`

The second option is more commonly used as a way to avoid overflow errors. In Javascript, given that all numbers are represented as 64-bit floating point, it hardly matters thought.

Operationally, the **option 1 is 2 times faster than option 2**. // todo: why?

### Use Bitwise Operators {#bitwise}

Bit operators, like the name suggests, operate on the binary representations hence can be significantly faster. And, they make great shorthands.

So here's three ways we compared:

1. With Right Shift (`>>`), `const midpoint = a + b >> 1`
2. With Unsigned Right Shift (`>>>`) `const midpoint = a + b >>> 1`
3. With Not (`~~`), `const midpoint = ~~(a + b)`

#### Why do bitwise operators work? {#bitwise-work}

Shifting a bit by 1, means dividing a number by 2. Easy enough to understand. But why does this operation floor the number?
That was hardly intuitive.

We went back to the docs, and here's a clue:

> The Signed Right Shift Operator ( >> )
> Performs a sign-filling bitwise right shift operation on the left operand by the amount specified by the right operand.
> The production `ShiftExpression : ShiftExpression >> AdditiveExpression` is evaluated as follows:
>
> 1. Let lref be the result of evaluating ShiftExpression.
> 2. Let lval be GetValue(lref).
> 3. Let rref be the result of evaluating AdditiveExpression.
> 4. Let rval be GetValue(rref).
> 5. Let lnum be ToInt32(lval).
> 6. Let rnum be ToUint32(rval).
> 7. Let shiftCount be the result of masking out all but the least significant 5 bits of rnum, that is, compute rnum & 0x1F.
> 8. Return the result of performing a sign-extending right shift of lnum by shiftCount bits. The most significant bit is propagated. The result is a signed 32-bit integer.

See it yet?

Focus here:

> Let lnum be ToInt32(lval).

From [**ToInt32: (Signed 32 Bit Integer)**](https://262.ecma-international.org/5.1/#sec-9.5)

> The abstract operation ToInt32 converts its argument to one of 2^32 integer values in the range −2^31 through 2^31−1, inclusive. This abstract operation functions as follows:
>
> Let number be the result of calling ToNumber on the input argument.
> If number is NaN, +0, −0, +∞, or −∞, return +0.
>
> Let posInt be sign(number) \* floor(abs(number)).
>
> Let int32bit be posInt modulo 2^32; that is, a finite integer value k
> of Number type with positive sign and less than 2^32 in magnitude such that the mathematical difference of posInt and k is mathematically an integer multiple of 232.
>
> If int32bit is greater than or equal to 2^31, return int32bit − 2^32, otherwise return int32bit.

More closely,

> posInt modulo 2^32

> Let int be the mathematical value that is the same sign as number and whose magnitude is floor(abs(ℝ(number))).
> the 32-bit conversion floors the number internally before performing the operation

To https://262.ecma-international.org/5.1/#sec-9.6

Hence, all bitwise operators first convert the number into a 32-bit representation, unless it is explicitly a [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt).

This introduces the following caveats with working with bitwise operators:

1. With the signed right shift, it only works till 2 \*\* 31 - 1

```
 e.g 2147483648 >> 1 => -1073741824 \n
 However, `BigInt` with signed right shift always works
 2147483650n >> 1n => 1073741825n
 BigInt(Number.MAX_VALUE) >> 1n
 => 89884656743115785407263711865852178399035283762922…072361584369088590459649940625202013092062429184n
```

2. Unsigned right shift works till 2 \*\* 32 - 1, (Note: Unsigned right shift doesnt work with bigints)
   ```js
    4294967295 >>> 1 => 2147483647
    4294967296 >>> 1 => 0
   ```
3. ~~ only works for positive numbers.

### Custom Algorithm {#odd-even}

Given the limitation around handling `BigInt`s, we also tested our own formula.
Since the context here was only to find a rounded-off midpoint, this worked.

```js
const midpoint = (m + n) % 2 === 0 ? (m + n) / 2 : (m + n - 1) / 2;
```

This did reasonably well, though it wasn't as fast as Bitwise.

#### But why is Math.floor slow? {#math-slow}

> The mathematical function floor(x) yields the largest integer (closest to positive infinity) that is not larger than x.
> NOTE: floor(x) = x−(x modulo 1).

And here's the culprit: Modulo.

And why is modulo slow? Long story short, if you remember grade school math, division was just a way longer process than an addition or subtraction. For a more detailed explanation, check out the great Stackoverflow answers in the references!

### Performance Comparisons {#performance}

Finally, we took all our approaches and calculated time take for each:

| Iterations | `Math.floor (add)` | `Math.floor (subtract)` | `>>`  | `>>>` | `~~`  | Custom | Modulo |
| ---------- | ------------------ | ----------------------- | ----- | ----- | ----- | ------ | ------ |
| 100000     | 6ms                | 4ms                     | 1ms   | 3ms   | 2ms   | 6ms    | 8ms    |
| 1000000    | 23ms               | 54ms                    | 14ms  | 19ms  | 19ms  | 33ms   | 56ms   |
| 1000000    | 54ms               | 24ms                    | 14ms  | 18ms  | 19ms  | 24ms   | 57ms   |
| 1000000    | 58ms               | -                       | 14ms  | 19ms  | 19ms  | 26ms   | 65ms   |
| 1000000    | -                  | 56ms                    | 22ms  | 15ms  | 19ms  | 26ms   | 62ms   |
| 10000000   | 227ms              | 575ms                   | 151ms | 223ms | 222ms | 269ms  | 569ms  |

### Takeaways

1. Bitwise operators outperform `Math.floor` by roughly 2-4 times for all sample sizes.
2. Modulo sucks.
3. Our custom algorithm didn't do too badly, performing better than Math.floor.
4. There is some memoization (or magic!) happening with Math.floor. The first usage of Math.floor is slower and successive usage of Math.floor get faster.

### References

- https://262.ecma-international.org/12.0/#sec-touint32
- https://2ality.com/2012/04/number-encoding.html
- https://262.ecma-international.org/5.1/#sec-9.6
- https://262.ecma-international.org/5.1/#sec-11.7.2
- https://stackoverflow.com/questions/36228869/best-way-finding-the-middle-point
- https://stackoverflow.com/questions/5971645/what-is-the-double-tilde-operator-in-javascript
- https://stackoverflow.com/questions/27977834/why-is-modulus-operator-slow
