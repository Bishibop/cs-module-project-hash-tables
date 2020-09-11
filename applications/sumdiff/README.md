```
Optimization Questions:
   Can I trade space for time?
   Can I use Hashes?
      Memoization / dp table
      Restructure problem
   Can I use a specialized datastructure?
   Can I use binary search? Can I eliminate half of the solution space on
      every iteration?
   If dp / recursive solution, can I pick better subproblems?

ordered list of > 4 integers

pick 4 for which:
   a + b + 3 = c - d

   c = a + b + d + 3

   a = - b - 3

you can pick the same number multiple times
Can you do this? Pick the same number multiple times?
Yes, See exampels in test cases

How can I use the fact that they're ordered?
How can I use the fact that they are no duplicates in the list?

The input is ordered, but the selection doesn't have to be

C > A || B || D
This would let me put a minimum on C. But that doesn't really help.


Brute force: try every option
Time: O(N^4)
Space: O(1) (Is this true? I'm not using space in a datastruture or variables
   but I'm using a bunch of space on the stack right? Certainly if this was
   recursive iteration.

   For every A in Input:
      For every B in Input:
         For every C in Input:
            For every D in Input:
               Test


Hash to restructure:
Time: O(N^2)
Space: O(N^2)

   For every A in Input:
      For every B in Input:
         Cache the result
         A+B+3: (A, B)

   For every C in Input:
      For every D in Input:
         Is C - D in Cache
         
For every A in Input:
   For every B in Input:

For every C in Input:
   For every D in Input:
      Test


```
# Equivalent Sums and Differences

This is a tricky one.

We have an ordered set of numbers `q`, which can have any numbers in it
(no duplicates).

Example:

```
q = (1, 3, 4, 7, 12)
```

And we have a function `f(x)`, which is defined as:

```
f(x) = x * 4 + 6
```

(written algebraically).

The question:

If you choose 4 numbers from `q`, call them `a`, `b`, `c`, and `d`:

What are the combinations of `f(a) + f(b)` that are algebraically
equivalent to the combinations of `f(c) - f(d)`?

That is, show all `a`, `b`, `c`, `d` for which this is true:

```
f(a) + f(b) = f(c) - f(d)
```

For the above `q`, we get this sample output:

```
f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18
```

The left column shows the `a`-`d` inputs to `f(x)`, and the right column
shows the result from the what `f(x)` returns for each of those.

No test script for this one. Keep in mind your output might be in a
different order than the above.
