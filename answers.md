  # CMPS 6610 Problem Set 01
## Answers

**Name:** Areen Khalaila
**Name:** akhalaila@tulane.edu


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a
  True, because $2^{n+1} = 2 \cdot 2^n$, so $2^{n+1} \in O(2^n)$.

  - 1b    
  False, because $2^{2n} grows faster than $2^{n}.
 
  - 1c
  False, because positive powers of n dominate logarithms.

  - 1d
  True, see above.

  - 1e
  False, $\sqrt{n} grows faster than any polylog.

  - 1f
  True, see above.

  - 1g
Let's assume, by contradiction that $f \in o(g(n))&$ and $f \in \omega(g)$.
For every $\varepsilon>0$ there exists $N_1$ such that $|f(n)| \le \varepsilon\, |g(n)|$ for all $n \ge N_1$.

And for every $M>0$ there exists $N_2$ such that $|f(n)| \ge M\, |g(n)|$ for all $n \ge N_2$

Take $\varepsilon=\tfrac{1}{3}$ and $M\\tfrac{1}{2}$, then for $n \ge N=\max\{N_1, N_2\}$ we must have both $|f(n)| \le \tfrac{1}{3}|g(n)|$ and $|f(n) \ge \tfrac{1}{2}|g(n)|$, a contradiction. therefore, $o(g(n))\cap \omega(g(n))=\varnothing$

2. **SPARC to Python**

  - 2b
  This function computes the greatest common divisor of its two arguments. 

  - 2c
  Work is O(log min(a,b)) and Span is Θ(log min(a,b)). Each recursive step does O(1) work and strictly reduces the smaller argument. The worse case follow the Fibonacci bound giving O(log min(a, b)) steps. Because there's only one recursive call per step, span equals the number of steps. 

3. **Parallelism and recursion**

  - 3b
  Each iteration does O(1) work and the loop is inherently sequential, and it's not parallel, therefore, the work and span are both O(n).

  - 3d
  Work: 2W(n/2)+c --> O(n)
  Span: 2S(n/2)+c --> O(n)

  - 3e
  Work: is still O(n)
  Span: O(log n)
  
4. **GCD**
