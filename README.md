# TKHoward-Code-Challenge
Coding Challenge for Marcum group grad students given by Dr. Trevor K Howard

---
## Challenge:


Find the sum of all the multiples of 3 or 5 below 1000.

---
## Solution:


The sum of the multiples of any number, $a$, less than another number, $N$ can be determined mathematically. The multiples can be determined by dividing $N$ by $a$ and multiply all integers between 1 and the result by $a$. So, the sum of the multiples becomes $a$ multipled by the sum of the integers up to and including the number of multiples. The sum of all numbers up to a number, $n$, can be expressed as:
$$\frac{n(n+1)}{2}.$$
Using this method, the sum of the multiples of $a$ can be written as:
$$a \frac{x(x+1)}{2},$$
where $x=N/a$. The summation of the multiples of two different numbers, $a$ and $b$, is then quite easy; you just perform this calculation twice. However, summing the multipes of $a$ or $b$ together runs into an issue when a number is a multiple of both and is counted for each calculation. We can fix this issue by subtracting the sum of the multiples of $a*b$. The final solution can be seen below:
$$\frac{1}{2} [ax(x+1) + by(y+1) - abz(z+1)],$$
where $x=N/a$, $y=N/b$, and $z=N/(ab)$.

---
## The Code:
The script to solve this problem begins by defining a function that can calculate the sum of multiples for any two numbers and any maximum. The function first determines the number of multiples for each input using the `numpy.floor` function. Then, the function performs the summation described above. The variables are defined so the problem statement would read: *Find the sum of all the multiples of $a$ or $b$ below $n$*.

```python
sum_n = sum_multiple_multiples(a,b,n)
```

`a` is the first number, `b` is the second number, and `n` is the maximum number to be tested. For the challenge: `a=3`, `b=5`, and `n=999`.

```python
sum_1000 = sum_multiple_multiples(3,5,999)
```


---