# The three-letter refined BMV trace lower bound in dimension three for five through nine other letters

**Byline:** Chain.Ren · Independent research  
**Version:** [proof-v1.0.0](https://github.com/Asakitan/refined-bmv-three-by-three/releases/tag/proof-v1.0.0) · 2026-11-27 (Australia/Sydney). OpenAI Codex contributed to the derivation, computation and exposition.

Let $\mathcal A_{n,3}(A,B)$ be the arithmetic mean of the traces of all $\binom{n+3}{3}$ ordered words in $n$ copies of $A$ and three copies of $B$. **Theorem.** For positive semidefinite complex Hermitian $3\times3$ matrices $A,B$ and $n=5,6,7,8,9$,
$$
\mathcal A_{n,3}(A,B)\ \ge\ \operatorname{Tr}\!\left[(A^{n/3}B)^3\right].
$$
In particular, if $H,K$ are Hermitian, then $\mathcal A_{n,3}(e^H,e^K)\ge\operatorname{Tr}e^{nH+3K}$. The latter trace-exponential statement also holds with the letter counts exchanged. [Hägele, §7(ii,iii)](https://arxiv.org/html/2611.00129v1) explicitly lists $(5,3)$ among the next open cases. We use the scalar reduction in that work; the new step is the single-chart integer coefficient certificate below. This proof is for the stated dimension and counts, not the unrestricted refined BMV conjecture.

## 1. From words to three scalar differences

For $N=\binom{n+2}{2}$ define the **scaled** kernel
$$
g(x,y,z)=\sum_{r+s+t=n} x^r y^s z^t-N(xyz)^{n/3},
$$
where the sum is over nonnegative integers. It is nonnegative by AM–GM: the mean of each exponent over all $N$ ordered compositions is $n/3$. Continuity covers zero arguments. Diagonalize $A$ with ordered eigenvalues $x_1\le x_2\le x_3$. By cyclicity, the word mean equals the uniform average of $\operatorname{Tr}(BA^rBA^sBA^t)$ over compositions: mark one of the three $B$'s in a word and read the other letters cyclically from there. Each composition has exactly $n+3$ choices for the marked position in a linearly indexed word; each word occurs three times.

Insert diagonal entries of $A$ in that expansion. Multiplying the difference in the theorem by $N$ gives a sum over ordered index triples, with weight $B_{ij}B_{jl}B_{li}$ times $g(x_i,x_j,x_l)$. All-equal triples contribute zero. Writing $V=B_{12}B_{23}B_{31}$, the sum of the others is
$$
3\sum_{p\ne q} B_{pp}|B_{pq}|^2 g(x_p,x_p,x_q)+6\operatorname{Re}(V)g(x_1,x_2,x_3).
$$
For fixed $q$, the two terms in the sum indexed by $p=i,j\ne q$ are together at least $2|V|\sqrt{g(x_i,x_i,x_q)g(x_j,x_j,x_q)}$: apply AM–GM and $\sqrt{B_{ii}B_{jj}}\ge |B_{ij}|$. Thus it suffices to have the sum of these three square roots at least $g(x_1,x_2,x_3)$. This is Hägele's single-triangle pairing, reproduced to fix the normalization.

## 2. Polynomial sufficient condition

Write $x=x_1,y=x_2,z=x_3$. Set
$$
a=g(x,x,z),\quad b=g(y,y,z),\quad h=g(x,y,z),\quad
Q=g(y,y,x)g(z,z,x)+g(x,x,y)g(z,z,y).
$$
The sum of the first two roots is at least $\sqrt Q$, and the last is $\sqrt{ab}$. Let
$$
D=h^2-ab,\qquad T=h(a+b)+2ab,\qquad P=QT^2-D^2(a+b)^2 .
$$
If $D\le0$ there is nothing to show. In the strict-interior case $0<x<y<z$, $a,b>0$. If $D>0$, then $\sqrt{ab}\ge 2ab/(a+b)$ implies
$$
h-\sqrt{ab}=\frac{D}{h+\sqrt{ab}}\le\frac{D(a+b)}{T}.
$$
So $P\ge0$ gives $\sqrt Q\ge h-\sqrt{ab}$ as required. The ordered closed cone, including vanishing or repeated eigenvalues, follows by continuity. This square-root reduction is Hägele's Lemma 6, here written homogeneously without fixing $z=1$.

## 3. One positive-increments chart covers the entire interior

Take $k=1$ if $3\mid n$, and $k=3$ otherwise. The expression $P(X^k,Y^k,Z^k)$ is a homogeneous polynomial of degree $6kn$ with integer coefficients. For $0<X\le Y\le Z$, scale by $X$ and write
$$
X'=1,\qquad Y'=1+u,\qquad Z'=1+u+v,\qquad u,v\ge0.
$$
Its sign is thus the sign of $P\big(1,(1+u)^k,(1+u+v)^k\big)$. In this chart the geometric-mean monomial in $g(I^k,J^k,K^k)$ is precisely $N(IJK)^{kn/3}$. Direct integer expansion gives:

| $n$ | $k$ | Degree bound $6kn$ | Nonzero coefficients | Negative coefficients |
|---:|---:|---:|---:|---:|
|5|3|90|3701|0|
|6|1|36|515|0|
|7|3|126|7400|0|
|8|3|144|9722|0|
|9|1|54|1262|0|

The [complete executable certificate](verify.py) builds each kernel from its defining composition sum, multiplies the bivariate polynomials over the integers, and checks the sign of **every** nonzero coefficient. For an auditable representation it stores $u^iv^j$ under the key $256i+j$. Every intermediate polynomial entering the construction has total degree at most $6kn\le144$, so adding exponent keys in products incurs no carry. A polynomial with no negative coefficient is nonnegative on the closed positive quadrant. No evaluation at sampled matrices or sampled eigenvalues is used. This proves the claimed evenly-spread-word inequality.

Finally the Araki–Lieb–Thirring trace comparison in [Hägele, Lemma 2](https://arxiv.org/html/2611.00129v1) gives $\operatorname{Tr}[(e^{nH/3}e^K)^3]\ge\operatorname{Tr}e^{nH+3K}$; explicitly it compares the symmetrized product at Trotter step $1/3$ to the limit at zero. Swapping the matrices preserves the word mean and exchanges the multiplicities in the exponent, proving the mirror statement. ∎
