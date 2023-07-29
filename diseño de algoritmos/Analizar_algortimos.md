

# Analyzing algorithms 2.2


Analyzing an algorithm has come to mean predicting the resources that the algorithm requires. Occasionally, resources such as memory, communication bandwidth, or computer hardware are of primary concern, but most often it is computational time that we want to measure. Generally, by analyzing several candidate
algorithms for a problem, a most efficient one can be easily identified. Such analysis may indicate more than one viable candidate, but several inferior algorithms
are usually discarded in the process.

we will assume generic one proccesor for our studies, **random-access machine (RAM)**  In the RAM model, instructions are executed one after another, with no concurrent operations

The *RAM model contains instructions commonly found in real computers*: arithmetic (add, subtract, multiply, divide, remainder, floor, ceiling), data
movement (load, store, copy), and control (conditional and unconditional branch,
subroutine call and return).

We also assume a limit on the size of each word of data. For
example, when working with inputs of size n, we typically assume that integers are
represented by c lg n bits for some constant c ≥ 1. We require c ≥ 1 so that each
word can hold the value of n, enabling us to index the individual input elements,
and we restrict c to be a constant so that the word size does not grow arbitrarily


## Analysis of insertion sort

The time taken by the INSERTION-SORT procedure *depends* on the input: sorting a
thousand numbers takes longer than sorting three numbers. Moreover, INSERTION SORT can take different amounts of time to sort two input sequences of the same
size depending on how nearly sorted they already are.

The best **notion for input size** depends on the problem being studied. For many
problems, such as sorting or computing discrete Fourier transforms, the most natural measure is the number of items in the input—for example, the array size n
for sorting.

The **running time** of an algorithm on a particular input is the number of primitive
operations or “steps” executed. It is convenient to define the notion of step so
that it is as machine-independent as possible.

One line may take a different amount of time than another line, but
we shall assume that each execution of the ith line takes time ci , where ci is a
constant. This viewpoint is in keeping with the RAM model, and it also reflects
how the pseudocode would be implemented on most actual computers


time “cost”
of each statement and the number of times each statement is executed. For each
j = 2, 3,..., n, where n = length[A], we let tj be the number of times the while
loop test in line 5 is executed for that value of j. When a for or while loop exits in
the usual way (i.e., due to the test in the loop header), t


| Pseudocode | Cost | Times |
| --- | --- | --- |
| for j = 2 to A.length | c1 | n |
|   key = A[j] | c2 | n-1 |
|   // Insert A[j] into the sorted sequence A[1..j-1] | 0 | 0 |
|   i = j - 1 | c4 | n-1 |
|   while i > 0 and A[i] > key | c5 | ∑i=2 to n |
|     A[i+1] = A[i] | c6 | ∑i=2 to n |
|     i = i - 1 | c7 | ∑i=2 to n |
|   A[i+1] = key | c8 | n-1 |


The **running time of the algorithm is the sum of running times for each statement**
executed; a statement that takes ci steps to execute and is executed n times will
contribute cin to the total running time.5 To compute T (n), the running time of
INSERTION-SORT, we sum the products of the cost and times columns, obtaining:

$$
T(n) = c_1n + c_2(n-1) + c_3(n-1) + c_4 \sum_{j=2}^{n} \sum_{j=2}^{n} (c_{j-1}) + c_7 \sum_{j=2}^{n} (c_{j-1}) + c_8(n-1)
$$




## **Worst-case and average-case analysis**
In our analysis of insertion sort, we looked at both the best case, in which the input
array was already sorted, and the worst case, in which the input array was reverse
sorted. For the remainder of this book(introduction to algoritms), though, we shall usually concentrate on
26 Chapter 2 Getting Started
finding only the worst-case running time, that is, the longest running time for any
input of size n. We give three reasons for this orientation.

- The worst-case running time of an algorithm is an upper bound on the running
time for any input. Knowing it gives us a guarantee that the algorithm will never
take any longer. We need not make some educated guess about the running time
and hope that it never gets much worse

- For some algorithms, the worst case occurs fairly often. For example, in searching a database for a particular piece of information, the searching algorithm’s
worst case will often occur when the information is not present in the database.
In some searching applications, searches for absent information may be frequent

- The *“average case”* is often roughly as bad as the worst case. Suppose that we
randomly choose n numbers and apply insertion sort. How long does it take to
determine where in subarray A[1 . . j − 1] to insert element A[j]? On average,
half the elements in A[1 . . j − 1] are less than A[j], and half the elements are
greater. On average, therefore, we check half of the subarray A[1 . . j − 1], so
tj = j/2. If we work out the resulting average-case running time, it turns out to
be a quadratic function of the input size, just like the worst-case running time.



In some particular cases, we shall be interested in the **average-case** or **expected**
running time of an algorithm; in Chapter 5, we shall see the technique of **probabilistic analysis**, by which we determine expected running times. One problem
with performing an average-case analysis, however, is that it may not be apparent
what constitutes an “average” input for a particular problem. Often, we shall assume that all inputs of a given size are equally likely. In practice, this assumption
may be violated, but we can sometimes use a **randomized algorithm**, which makes
random choices, to allow a probabilistic analysis


## order of growth 

We used some simplifying abstractions to ease our analysis of the INSERTION SORT procedure. First, we ignored the actual cost of each statement, using the
constants ci to represent these costs. Then, we observed that even these constants
give us more detail than we really need: the worst-case running time is an2+bn+c
for some constants a, b, and c that depend on the statement costs ci .





