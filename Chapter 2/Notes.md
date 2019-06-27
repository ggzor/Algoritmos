# Notes

We use loop invariants to show the correctness of our algorithm. We must show three things about our loop invariant:

- **Initialization:** It is true prior the first iteration of the loop.
- **Maintenance:** It is true before an iteration of the loop, it remains true before the next iteration.
- **Finalization:** When the loop terminates the invariant give us a useful property that help us show that the algorithm is correct.

The divide and conquer approach involves three steps:

- **Divide:** the problem into smaller instances of the same problem.
- **Conquer:** the subproblems by resolving them recursively, if the problems are small enough, however, just solve them straightforwardly.
- **Combine:** the solutions of the subproblems into the solution of the original problem.
