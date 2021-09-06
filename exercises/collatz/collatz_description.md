# Collatz conjecture

The **Collatz conjecture** is a conjecture in mathematics that concerns sequences defined as follows: start with any *positive integer n*. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

The conjecture is named after Lothar Collatz, who introduced the idea in 1937, two years after receiving his doctorate. It is also known as the 3n + 1 problem, the 3n + 1 conjecture, the Ulam conjecture (after Stanisław Ulam), Kakutani's problem (after Shizuo Kakutani), the Thwaites conjecture (after Sir Bryan Thwaites), Hasse's algorithm (after Helmut Hasse), or the Syracuse problem. The sequence of numbers involved is sometimes referred to as the hailstone sequence or hailstone numbers (because the values are usually subject to multiple descents and ascents like hailstones in a cloud), or as wondrous numbers.

## Task

Given number `n`, calculate its *total stopping time* (the first step of the sequence when number becomes 1) and the *maximum trajectory point* (the largest number in the sequence). For example, if `n` is 26, the hailstone sequence is `13, 40, 20, 10, 5, 16, 8, 4, 2, 1`, the total stopping time is 10, and the highest point is 40.

You have to implement function `collatz` and verify its correctness using the provided tests.

## References

- [Collatz conjecture - Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture)
- [The Simplest Math Problem No One Can Solve - Collatz Conjecture - YouTube](https://www.youtube.com/watch?v=094y1Z2wpJg)
