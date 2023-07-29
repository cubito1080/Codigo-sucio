# Asymptotic notation:

The notations we use to describe the asymptotic running time of an algorithm
are defined in terms of functions whose domains are the set of natural numbers
N = {0, 1, 2,...}. Such notations are convenient for describing the worst-case
running-time function T (n), which is usually defined only on integer input sizes.


It is sometimes convenient, however, to abuse asymptotic notation in a variety of ways. For example, the notation is easily extended to the domain of real numbers
or, alternatively, restricted to a subset of the natural numbers. **It is important**, however, to understand the precise meaning of the notation so that when it is abused, it
is not misused. This section defines the basic asymptotic notations and also introduces some common abuses.

$$
\Theta notation
$$
 we found that the worst-case running time of insertion sort is
T (n) = (n2). Let us define what this notation means. For a given function g(n),
we denote by (g(n)) the set of function

$$
\Theta(g(n)) = f(n) \text{ if there exist positive constants } c_1, c_2, \text{ and } n_0 \text{ such that } 0 \leq c_1g(n) \leq f(n) \leq c_2g(n) \text{ for all } n \geq n_0.
$$



f (n) belongs to the set (g(n)) if there exist positive constants c1
and c2 such that it can be “sandwiched” between c1g(n) and c2g(n), for sufficiently large n. Because (g(n)) is a set, we could write “ f (n) E (g(n))”
to indicate that f (n) is a member of (g(n)). Instead, we will usually write
“ f (n) = (g(n))” to express the same notion.
