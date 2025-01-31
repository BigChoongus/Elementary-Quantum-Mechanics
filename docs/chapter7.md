{% raw %}
---
layout: default
title: Chapter 7
mathjax: true
render_with_liquid: false
---

<script type="text/javascript">
MathJax = {
  tex: {
    packages: {'[+]': ['ams']},  // Enable AMS packages
    macros: {
      Answer: "{\\begin{tcolorbox}}",
      Answerend: "{\\end{tcolorbox}}",
      ket: ["|#1\\rangle", 1],
      bra: ["\\langle#1|", 1],
      ip: ["\\langle#1|#2\\rangle", 2],
      bip: ["\\left\\langle#1\\middle|#2\\right\\rangle", 2],
      qexp: ["\\langle#1\\rangle", 1],
      apos: ["``#1''", 1],
      sapos: ["`#1'", 1],
      elec: "e^{-}",
      uspin: "(\\uparrow)",
      dspin: "(\\downarrow)",
      lspin: "(\\leftarrow)",
      rspin: "(\\rightarrow)",
      ulspin: "(\\uparrow\\leftarrow)",
      urspin: "(\\uparrow\\rightarrow)",
      dlspin: "(\\downarrow\\leftarrow)",
      drspin: "(\\downarrow\\rightarrow)",
      R: "\\mathbb{R}",
      stab: "\\:\\:",
      mtab: "\\:\\:\\:",
      btab: "\\:\\:\\:",
      imp: "\\Rightarrow",
      doubimp: "\\Leftrightarrow",
      setof: ["\\{#1\\}", 1],
      infint: "\\int_{-\\infty}^{\\infty}",
      trans: ["\\mathcal{T}(#1)", 1],
      dd: ["\\delta(#1-#2)", 2],
      ipbig: ["\\langle#1|#2\\rangle", 2],
      talpha: "\\tilde{\\alpha}",
      op: ["|#1\\rangle\\langle#2|", 2],
      sop: ["|#1\\rangle\\langle#1|", 1],
      prop: ["\\mathcal{U}(#1,#2)", 2],
      propdagg: ["\\mathcal{U}^{\\dagger}(#1,#2)", 2],
      sip: ["\\langle#1|#1\\rangle", 1],
      optrip: ["\\langle#1|\\hat{#2}|#3\\rangle", 3],
      nhoptrip: ["\\langle#1|{#2}|#3\\rangle", 3],
      northexp: ["\\sum_{i=1}^{n}|#2\\rangle\\langle#2|#1\\rangle", 2],
      orthexp: ["\\sum_{#3=1}^{#4}|#2\\rangle\\langle#2|#1\\rangle", 4],
      schrodeq: "i\\hbar\\frac{\\partial \\Psi(x,t)}{\\partial t}=\\hat{H}\\Psi(x,t)",
      nd: ["\\frac{d#1}{d #2}", 2],
      snd: ["\\frac{d^{2}#1}{d#2^2}", 2],
      pd: ["\\frac{\\partial#1}{\\partial #2}", 2],
      spd: ["\\frac{\\partial^{2}#1}{\\partial #2^2}", 2],
      duac: "\\leftrightarrow",
      oip: ["\\left(#1,#2\\right)", 2],
      obip: ["\\left(#1,#2\\right)", 2],

      // Replacements for LaTeX Packages
      mathscr: ["\\mathscr{#1}", 1],  // From mathrsfs
      bbm: ["\\mathbbm{#1}", 1],  // From bbm
      bm: ["\\boldsymbol{#1}", 1],  // From bm
      gensymb: "\\degree",  // From gensymb
      indentfirst: "",  // No direct equivalent; use extra line breaks in Markdown

      // Handling Theorem Environments (From amsthm)
      theorem: ["\\textbf{Theorem:} \\textit{#1}", 1],
      lemma: ["\\textbf{Lemma:} \\textit{#1}", 1],
      corollary: ["\\textbf{Corollary:} \\textit{#1}", 1],
      definition: ["\\textbf{Definition:} \\textit{#1}", 1],
      proof: ["\\textbf{Proof:} #1", 1]
    }
  }
};
</script>


# Continuous Spectra

In this section, we take a huge leap forwards towards full physical
reality by finally loosening the discrete spectrum restraint which we
have been working under for the entire book so far. If we recall,
eigenvalues of observable operators represent physically measurable
valuables for those observables represented by those operators. Now,
quantum mechanics does show us that some observables can be discretely
distributed: most notably, energy as in the free particle solution.
However, we also know that some observables must never be able to be
discretely distributed. In particular, position being discretely
distributed would be a huge issue in any physical model, because it
would mean that us and any object moves by teleporting between discrete
positions with increments between them which we somehow cannot move
into. This is clearly nonsense; position must be continuous. Thus, we
must also be prepared to deal with continuous spectra in quantum
mechanics because, if nothing else, position eigenvalues must always be
in a continuous spectrum. In the end, position is not the only
observable which exhibits continuous spectra at all, but the
illustration is already there.

## A Conceptual Definition of Continuity

Clearly, as just established, some observables like position must take
infinite continuously distributed eigenvalues. Now, if we take the
eigenvalue definition: $$\Omega\ket{\omega}=\lambda\ket{\omega}$$ then
we can come to a clear realisation that we must also have infinite
eigenkets as well. This is a result of the fact that the number of
eigenvectors (eigenkets) must be greater than or equal to the number of
eigenvalues. Otherwise, if there were fewer eigenvectors than
eigenvalues, at least one eigenvector would correspond to multiple
different eigenvalues. Then this would be:
$$\Omega\ket{\omega}=\lambda\ket{\omega}$$ and
$$\Omega\ket{\omega}=\lambda'\ket{\omega}$$ but
$$\lambda\neq\lambda'\implies\lambda\ket{\omega}\neq\lambda'\ket{\omega}$$
so $$\Omega\ket{\omega}$$ would simultaneously be two different kets,
even though it is the same operator acting on the same input ket. Then,
$\Omega$ simply could not be a linear operator, as it would have two
outputs for a single input.\
\
So now that we have established the number of eigenvectors is greater
than (the degenerate case) or equal to (the non-degenerate case) the
number of eigenvalues, and we know that some observable operators take
infinite eigenvalues, we must have indeed infinite eigenvectors as well
in such cases.\
\
Now, consider what practical function a eigenket has. It is an
abstraction, so the answer is nothing in itself! The reason why an
eigenket is important is because it is interpreted as the eigenstate
where a corresponding eigenvalue has probability 1 of being measured.
Thus, as already described in our section on inner labelling when we
started with Dirac notation, we often just label eigenkets by that
eigenvalue they are connected to.\
\
Considering position eigenkets now, we would label them by
$$\ket{x_{0}}$$ being the eigenstate where a measurement of position
would yield position $x_{0}$ with certainty. We might also have for
example $$\ket{0}, \ket{L}$$ if we were working bounded in some length
$L$ where a position could not be further than distance $L$ away from
the other end we labelled position $0$. Now, we would never write:
$$\ket{L} > \ket{L/2} > \ket{0}$$ because kets are abstract vectors and
it makes no sense to compare their magnitudes with a sign. Yet at the
same time, that $\ket{L}>\ket{L/2}>\ket{0}$ would be easy to mistake as
somewhat valid, because $L$ is a positive distance so indeed the values
these kets represent themselves do satisfy $L>L/2>0$. We can see that
inner label confusion can occur when it comes to magnitudes, because if
we a label a ket by a specific value: usually an eigenket by an
eigenvalue, we can be tempted to compare the magnitudes of those inner
labels.\
\
What this pedantic clarification is to say is that $$\ket{L} > \ket{0}$$
is mathematically void, but there is some concept of comparing the
values labelling kets when it is a situation where values are labelling
kets. Specifically, this means that when we write $$\ket{x_{0}+dx},$$ we
can claim it is to $\ket{x_{0}}$ as $dx\to0$. Now, that technically
would not be correct syntax, considering kets cannot be infinitesimally
close if they do not have magnitudes and therefore the definitions of
and do not exist. However, the idea is that $\ket{x_{0}+dx}$ and
$\ket{x_{0}}$ may be infinitesimally close in that they represent
eigenstates of positions which are infinitesimally close to each other!
This is another case of the unfortunate semantic clarifications which
result when we need to postulate so many abstractions in bijections, but
at the same time, now that this is said, the reader should no longer
scratch their heads when I or other texts say rather than . Most
compendia would not make such clarifications, but I think it is useful
here.\
\
Now, then we can finally understand how continuity occurs in quantum
mechanics and in the abstract state spaces we are working in. While kets
cannot exhibit continuity, they can represent values exhibiting
continuity, and this can be seen as one and the same.\
\
The mathematical definitions of continuity are:

-   A variable $Z$ is continuous over an interval $[a,b]$ if:
    $$\forall\stab z=Z\in[a,b], \stab dz\to 0, \mtab z+dz\in[a,b].$$
    This is probably already intuitive and not much more needs to be
    said: simply, there is a continuum of values which exist such that
    no matter how infinitesimal a scale we go down to, we will not be
    able to distinguish values by a discernible increment.

-   A function $f(x)$ is continuous over $x$ if $x$ is a continuous
    variable and $$\forall x, \lim_{dx\to 0}f(x+dx)=f(x).$$ This means
    that there are no sudden jumps over infinitesimal intervals, and the
    graph of the function is *smooth*.

### Infinities

A discussion on continuity necessarily involves a thought about
infinities. The issue herein is that the mathematics of infinities is
rather inaccessible; in fact, all we primarily need to understand is
this extremely simplistic idea of $\infty + 1 \ngtr \infty$. I want to
stray as far from these sums including infinities and arithmetic numbers
as I can, and this is achievable to us in quantum mechanics. Quite
simply, the less thought here, the better.\
\
The one clarification I would like to make is on the comparison between
discrete and continuous spectra in an infinite dimensional vector
space.\
\
If a vector space is infinite dimensional, then, we know that the basis
of that space-- that is, the set of linearly independent vectors in that
space-- must have infinite cardinality (there are infinite basis
vectors), by definition of dimensionality. The state space, we know, is
an example of a vector space of infinite dimensions, and is critical to
our study. Now, if we compare discretely distributed and continuously
distributed eigenbases, we must make the clarification of how an
infinite dimensional space can be spanned by both discrete bases and
continuous bases. A reader might be surprised by this. If dimensionality
is to do with the number of linearly independent basis vectors we can
accommodate in the space, how could it be that one basis could be
discrete and still have all the maximum number of basis vectors, while
another basis is continuous? There is a sense, which is not unfounded,
that the very point of continuous sets is that they have infinite
elements between discrete points, and so they must have more elements
than any discrete set.\
\
This idea is countered by the question . Of course, we know there are
infinite integers-- that is, after all, the point of having the entity
infinity in the first place: if we keep on going through the consecutive
positive integers we reach infinity. Can we say that there are more
decimals than integers? In feeling, perhaps, but this is not
mathematically rigorous. The idea is in fact of **countable and
uncountable infinities**.\
\
A countable infinity is an infinity where one can hypothetically number
each of those infinite elements. The positive integers are natural for
demonstrate this, because they are already numbered- the integer 1 is
the first element, the integer 2 the second, and so on, but yet they are
definitely infinite in number. On the other hand, all decimal numbers
constitute an uncountable infinity- we cannot number them since we could
by definition always produce at least 1 decimal between the decimal we
have numbered to be the first and the decimal we have numbered to be the
second.\
\
This answers our question of how discrete and continuous basis can both
span the same vector spaces. If a continuous basis spans a space, there
must be infinite basis vectors, which is why the space is infinite
dimensional. However, we could also span the space with a discrete
basis, which has a *countably* infinite number of basis vectors rather
than an uncountably infinite one. A continuous basis cannot span a
finite dimensional vector space, but a discrete basis can span both
finite and infinite dimensional vector spaces depending on what bases we
are considering. Discrete and finite are not synonyms, even though we
might consider them to be. Thus what might appear confusing in regards
to these discrete versus continuous bases is in fact answered by the
idea that uncountable infinities are not larger in magnitude than
countable infinities since both of them are infinite! Perhaps this
section may be simplified, but quite frankly I am not interested in
entering such fringe discussions which are extremely unimportant to our
learning of quantum mechanics, and doubt the reader is either, so we can
close this discussion.

## Continuous Wavefunctions

Having a continuous case in our work will necessitate that some of our
old summation and matrix notation seems defunct, because thinking of
summing infinite terms or infinitely large matrices is not natural.
However, the generalisation to infinite dimensions is in fact quite
fine. Starting with infinitely sized matrices, We can consider the
position basis for example to be column kets represented by
$$\ket{x_{i}}\duac
\begin{bmatrix}0 \\ 0 \\ \vdots \\ 1 \\ \vdots \\ 0 \\ \end{bmatrix}$$
with the unity in the $i$'th row, $0$ elsewhere, and infinite rows.
Clearly, they constitute an orthonormal basis and the actual number of
rows of the vector is already not of much concern.\
\
Meanwhile, in continuous cases, we can simply replace the sum terms we
have been using with integrals-- infinite sums over continuous
variables-- instead! This is an idea which generalises both in
continuous cases and to infinities: the idea of an integral is that we
are taking the sum of values separated by increments when that increment
approaches $0$: thereby an infinite sum over infinitesimally different
(continuous) values.\
\
For the inner product, we have thus far used sums for our
multiplications in Dirac notation: we set up a column entity, which we
called a ket, and a row entity, a bra, and we simply multiplied them
together, but matrix multiplication in finite dimensions is an algorithm
which is essentially a sum of $n$ values: $$\begin{bmatrix}
a_{1} & a_{2} & \dots & a_{n}
\end{bmatrix}\times \begin{bmatrix}
b_{1}\\
b_{2}\\
\vdots\\
b_{n}\\
\end{bmatrix}=\sum_{i=1}^{n}a_{i}b_{i}.$$ The inner product we have been
so far using in the Dirac notation sections is therefore the exact same
idea, but with a conjugate transpose of column vector kets rather than
just a transpose as the bras. That is,
$$\ip{\alpha}{\beta}=\sum_{i=1}^{n}a^{\ast}_{i}b_{i}$$ with components
$\setof{a_{i}}$ and $\setof{b_{i}}$ for $\ket{\alpha}$ and $\ket{\beta}$
respectively in an $n$-dimensional space.\
\
The problem we now face is that, while we wish to integrate kets in some
way to create a continuous inner product, we cannot do this currently as
kets are in no way related to any functions, which are our natural
inputs for integrals-- kets are abstract vectors. However we have seen
this problem of getting by an abstract ket: or, state vector, already!
All we need to generate a function which exists in a bijection with
state kets. We require this function to be continuous so we can
integrate it.\
\
The function which makes sense, then is the same component function we
worked with before $$\ket{\Psi}\to \psi(x).$$ This should be governed
by:

-   Input: Basis ket.

-   Output: Component corresponding to the input basis ket.

-   Domain: All kets in the basis.

-   Range: Complex numbers (the components).

which changes with the input position $x$ and gives as an output the
component corresponding to basis eigenket $\ket{x}$.\
\
Well, this is the wavefunction, we know, because we have done exactly
this already in the discrete case. Here, the argument $(x)$ represents
that we are inputting position values, so this is the position
wavefunction, which is only possible now because the position observable
exhibits a continuous spectrum. One problem we do have with this is
that, if we are trying to denote the value of the function evaluated at
position $0$, for example, the form becomes $$\psi(0)$$ where it is now
unclear whether or not it is a position wavefunction with position value
$0$ or momentum wavefunction with momentum value $0$ or so on.
Unfortunately, if we want to leave space for a subscript identifying
separate wavefunctions apart from each other, for example in
$$\ket{\Psi_{1}}\duac\psi_{1}(x),\stab \ket{\Psi_{2}}\duac \psi_{2}(x)$$
we have to sacrifice the ability to tell when the argument is absent
which basis a wavefunction is expressed in. The other side of the coin
is that first of all, context should always make it abundantly clear
which basis everything is expressed in anyway, and secondly, reserving
the same letter $\psi$ representing wavefunctions is more valuable than
alternative possibilities such as identifying different observable
wavefunctions with different letters, which would be just confusing.\
\
Now we can see easily that the position wavefunction is a continuous
function since,
$$\forall x_{0}, \stab \lim_{dx\to 0} \psi(x_{0}+dx)=\psi(x_{0}).$$ This
intuitively makes sense, since the component corresponding to the
position $x+dx$ should approach the component as we rotate to the
direction corresponding to position $x$. A final convincing of this
should be completed by the fact that the component relates the
probability of measuring a certain position, by the measurement
postulate: thus as we approach one position the component (probability)
of measuring positions approaching that specific position should become
progressively closer to the probability of measuring that specific
position. Note also that we could have $$\psi(p)$$ which changes
depending on input momentum-- assuming we are working in instances of
continuous momentum, which do exist-- to give the corresponding
component of the eigenket which is the eigenstate with that input
momentum. This would simply be used if we were working in momentum
space.\
\
Now, the components of a ket $\ket{\Psi}$ in a given basis
$\setof{\ket{x}}$, which we will use since it is most natural, are given
by $$\ip{x_{i}}{\Psi}=c_{i}.$$ Thus the position wavefunction is
$$\psi(x):=\ip{x}{\Psi}.$$ which is, the component of the ket
$\ket{\Psi}$ in the direction of the basis vector $\ket{x}$.\
\
Now, we pause, because the above definition in ket form is prone to
confusion, especially on passing glances, so it is important the next
clarification is understood thoroughly before we move on.\
\
The reason the function definition we have just reached looks so
absolutely wrong is because on the right hand side we have what appears
exactly as an inner product, which we instantly associate (rightly) with
a scalar constant, but on the left we have the position wavefunction we
have just learnt about as a continuous function. What is very important
here is that the inner label of the bra $\bra{x}$ in the inner product
is meant to represent a varying index, rather than just an inner tag on
a static bra obtained from a static ket. So we would have
$$\psi(0)=\ip{0}{\Psi}$$ which is, the component of the state
$\ket{\Psi}$ corresponding to position $0$ which is represented by the
ket $\ket{0}$ the corresponding bra of which is $\bra{0}$. We could also
have $$\psi(L)=\ip{L}{\Psi}$$ which is, the component according to
position $L$.\
\
It is not wrong for the reader to find the above somewhat unusual, since
a single inner product is always a scalar constant. It therefore might
seem like a bit of an abuse of notation to write $$\ip{x}{\Psi}$$ to be
a varying quantity, since before our inner labels were stationary orders
for kets and nothing more. Unfortunately, this is one point in quantum
mechanics which convention has not seen fit to bother with changing
notation to accommodate. The best way to deal with it is that in this
book I will always use $\ket{x}$ to represent a variable position ket,
$\ket{p}$ a variable momentum ket and $\ket{E}$ a variable energy ket.
Otherwise, for static single position kets I will use notation such as
$\ket{x_{0}}$ or $\ket{x_{1}}$ to denote these fixed points -- usually,
just $x_{0}$ if we only require one fixed point to compare to, as this
notation is quite common in quantum mechanics. Now we can fully
enunciate the action of this wavefunction is through the following
steps:

1.  Take the input observable value.

2.  Find the eigenket corresponding to that observable value, which is a
    pure eigenstate with probability 1 of obtaining that value.

3.  Find the inner product product of that eigenket with the state ket.

4.  Output that inner product value.

## Dirac Delta Function

That notational liberty of variable kets is aesthetically cumbersome, so
we should demand it to be at least useful to us. It is useful, in fact,
since we can finally define the integral for our abstract kets and bras:
$$\ip{\Psi_{1}}{\Psi_{2}}=\int_{-\infty}^{\infty}\psi_{1}^{\ast}(x)\psi_{2}(x)\,dx .$$
Finally, we have the continuous inner product! We indeed see that the
above is very much related to the discrete inner product, since instead
of discrete components we now have a continuous wavefunction storing the
components to deal with the fact there are infinitely many continuous
eigenkets, and finally we integrate just as an integral is a continuous
sum. The same varying input variable $x$ ensures that the coefficients
are matched up for both states $\ket{\Psi_{1}}$ and $\ket{\Psi_{2}}$
since each time the functions $\psi_{1}(x)$ and $\psi_{2}(x)$ give the
components corresponding to the eigenket representing the inputted
position, by their definition.\
\
The integral bounds can become definite, and often do, in physical
problems. An example of this fact might be if we are considering
position functions on a string-- in which case the variable $x$ might be
considered, and the bounds might be $0$ to $L$-- the other end of the
string of length $L$ from the end we defined to be position $0$. It is
clear that in this case it does not make sense to take an integral from
$0$ to $70000$km displaced from $0$, for example, if a string is say
$50$cm long, as we do not expect any particles we consider to be any
further than $50$cm (in the one dimension we are considering) from the
point on the other end which we defined to be position $0$. This is some
sort of way to saying that we can ignore the bounds of the integrals in
continuous quantum mechanics until a physical problem sets them for us.\
\
With this given, the orthogonal condition is the same: two kets
$\ket{x_{0}}$ and $\ket{x_{1}}$ (which, by the aforementioned convention
we are using, represent static kets corresponding to positions $x_{0}$
and $x_{1}$ respectively) are orthogonal if $$\ip{x_{0}}{x_{1}}=0.$$
However, the normalisation condition is different. To understand this,
consider the completeness relation, which we expect to be:
$$\infint \sop{x}\,dx=1$$ where we have continued the convention of $x$
without any subscripts representing a variable inner label. Left
multiplying by $\bra{x_{0}}$ and right multiplying by any non-basis ket
$\ket{\alpha}$ gives us
$$\infint dx\,\ip{x_{0}}{x}\ip{x}{\alpha}=\ip{x_{0}}{\alpha}$$ which is,
the component $\psi_{\alpha}(x_{0})$ of the ket $\ket{\alpha}$in the
direction of eigenket $\ket{x_{0}}$ corresponding to position value
$x_{0}$.\
\
Denote now the inner product between basis vectors $\ket{x}$ and
$\ket{x_{0}}$ as $$\ip{x}{x_{0}}:=
\delta(x-x_{0}).$$ The way of presenting the two arguments $x$ and
$x_{0}$, which are, the inputs, of the function should not throw one
off: it is convention, which has a not so significant but still very
much logical reason. We know that
$$\forall x\neq x_{0}, \btab \delta(x-x_{0})=0$$ since the position kets
are all orthogonal to each other as they are non-degenerate eigenkets of
a hermitian operator. Now, we can look at the above expression again:
$$\infint \ip{x_{0}}{x}\ip{x}{\alpha}\,dx=\ip{x_{0}}{\alpha}\implies \infint \delta(x_{0}-x)\psi_{\alpha}(x)\,dx=\psi_{\alpha}(x_{0})$$
The range over negative infinity to positive infinity seems expansive,
but in fact, an infinite part of it is redundant; this is because the
inner product $\delta(x-x_{0})$ is 0 for all $x\neq x_{0}$! Now it is
clear we need to continue to consider infinities since we are working
with continuous variables rather than discrete ones. Consider an
infinitely small region $[x_{0}-\Delta x,x_{0}+\Delta x]$ for an
infinitesimal difference $\Delta x$, which centres at $x_{0}$. In this
region we can consider the integral because it is only here where we can
consider $\delta(x-x_{0})$ to not definitively be $0$ since if $x$ is
infinitely close to $x_{0}$ we cannot just easily say $x\neq x_{0}$.
With these new bounds,
$$\int_{x_{0}-\Delta x}^{x_{0}+\Delta x}\delta(x-x_{0})\psi_{\alpha}(x)=\psi_{\alpha}(x_{0})$$
since this region is the only area where we cannot say the inner product
$\delta(x-x_{0})$ is $0$. As all values of $x$ in the integral lie in
this infinitesimal region, we can as we assume in the limit that the
components $\psi_{\alpha}(x)=\psi_{\alpha}(x_{0})$ since the input
direction $\ket{x}$ is infinitesimally different from the fixed
direction $\ket{x_{0}}$. This then is a specific value (not a function,
despite the notation), so we can pull it out as a constant:
$$\int_{x_{0}-\Delta x}^{x_{0}+\Delta x}\delta(x-x_{0})\psi_{\alpha}(x)\,dx=\psi_{\alpha}(x_{0})\int_{x_{0}-\Delta x}^{x_{0}+\Delta x}\delta(x-x_{0})\,dx=\psi_{\alpha}(x_{0}).$$
That is,
$$\int_{x_{0}-\Delta x}^{x_{0}+\Delta x}\delta(x-x_{0})\,dx_{0}=1.$$
What implications does this have for the inner product
$\delta(x-x_{0})$, which we call the (Dirac) delta function? The most
intuitive answer comes from using the conventional visualisation of an
integral as a way to measure the area under a smooth function. We know
the delta function $\delta(x-x_{0})$ is $0$ until it reaches an
infinitely small interval around the value $x_{0}$. Yet the integral of
the whole function with respect to $x$ is $1$. So if we draw a
horizontal axis for varying $x$ and a vertical axis for the value of
$\delta(x-x_{0})$ (with $x_{0}$ fixed), we will get a flat line for all
infinity until we get infinitely close to $x_{0}$. Yet, this as a whole
must have area $1$! So the infinitely small width interval close to $x$
is the only region which contributes any area to the integral, and this
whole area is $1$. So, in the picture we have created, the value
$\delta(x-x_{0})$ in this region is the height which contributes $1$ to
the area despite having an infinitely small width. The only explanation
therefore is that at the infinitesimally small region, the delta
function has infinite value. Otherwise, the infinitely small width
interval could not have any area which is not infinitely small! Then the
infinitesimally small domain for $x$ around $x_{0}$ can simply be
reduced to $x=x_{0}$, so $\delta(x_{0}-x_{0}):=\delta(0)$ is infinity!\
\
We summarise with the following: $$\delta(x-x_{0})=
\begin{cases}
0\stab\text{if}\stab x\neq x_{0}\\
\infty\stab\text{if}\stab x=x_{0}\\
\end{cases}$$ Of course, we do not like writing the infinity symbol as
if it is a value very often in mathematics, so this is better put $$$$
$$\delta(x-x_{0})=
0\stab\text{if}\stab x\neq x_{0}, \btab\btab
\int\delta(x-x_{0})\,dx=1$$ where the bounds of integration do not
matter since the function is $0$ anyway until we get infinitesimally
close to $x_{0}$. This will be commonplace any time we consider a
continuous basis. Another way to summarise this is also in the framework
of viewing the delta function as a *sampling function*, which means that
$$\int\delta(x-x_{0})f(x)\,dx=f(x_{0})$$ That is- because the range
where $x$ and $x_{0}$ are completely distinct vanishes, the integral
only selects the value of $f(x_{0})$, which changes over a continuously
varying $x_{0}$, which is the same as that at point $x$. Finally, it is
crucial to know that the delta function is real! This means that
$$\delta(x-x_{0})=\ip{x}{x_{0}}=\ip{x_{0}}{x}^{\ast}=\delta(x_{0}-x)^{\ast}$$
but as the delta function is real,
$$\dd{x_{0}}{x}^{\ast}=\dd{x_{0}}{x}$$ which altogether means that
$$\dd{x}{x_{0}}=\dd{x_{0}}{x}$$ -an important point, of course. It is
also very important to know that the minus sign in the function is meant
to be taken literally (technically, the Delta function is a function of
the difference between its two arguments, but this point is not
important at all). So we will often see expressions like
$$\delta(x)=\dd{x}{0}=\dd{0}{x}$$ or $$\delta(0)=\dd{x}{x}$$ and even
$$\delta(k)=\dd{x+k}{x}$$ in shorthand. A reader should not get confused
by this, and should also remember that $$\delta(k)=\delta(-k)$$ since
$\delta(x+k-x)=\delta(x-(x+k))$.\
\

## Position and Momentum

In order to understand the importance of orthonormalising to the Dirac
delta function as the continuous analogue of orthonormalising to the
Kronecker delta in the discrete case we have beforehand been working on,
we will undergo the necessary algebraic steps to work with the two
canonical quantum mechanical operators. Through this, one can practice
both the algebra and rationale of the Dirac delta function.

### Position and Momentum Operators

The first step we can take using the Dirac Delta function is to confirm
the action of the position operator-- the operator in quantum mechanics
which represents the physical variable of position-- in **position
space**, the space spanned by the continuous position eigenkets. Take
some function $f(x):=\ip{x}{f}$ represented by the ket $\ket{f}$ and
define $$\hat{X}\ket{f}:=\ket{F}$$ with $$F(x_{0}):=\ip{x_{0}}{F}.$$ Now
in the usual way we can determine the action of an operator on a ket by
left multiplying it by a basis bra:
$$\optrip{x_{0}}{X}{f}=\ip{x_{0}}{F}$$ We can then insert the continuous
completeness relation:
$$\int\sop{x}\,dx=I\implies\optrip{x_{0}}{X}{f}\equiv \int\optrip{x_{0}}{X}{x}\ip{x}{f}\,dx=\int x\ip{x_{0}}{x}\ip{x}{f}\,dx.$$
In Delta notation, this is
$$\int\optrip{x_{0}}{X}{x}\ip{x}{f}\,dx=\int x\dd{x}{x_{0}}f(x)\,dx.$$
As per usual, the delta function vanishes all the integrated terms
except for when $x=x_{0}$. Therefore we can assume the $x$ variable is
only relevant when $x=x_{0}$ and thus pull it out as $x_{0}$. To
finalise the result, we simply get the sampling property of the delta
function.
$$\int x\dd{x}{x_{0}}f(x)\,dx\equiv x_{0}\int\dd{x}{x_{0}}f(x)\,dx = x_{0}f(x_{0}).$$
So we have $$\optrip{x_{0}}{X}{f}=\ip{x_{0}}{F}
=F(x_{0})=x_{0}f(x_{0})$$ So $$\hat{X}f(x_{0})=F(x_{0})=x_{0}f(x_{0}).$$
Since this holds true for all $x_{0}$, we can generalise this for any
input of the position variable $x$ as simply: $$\hat{X}f(x)=xf(x)$$ in
the position basis; indeed, this is the position operator we are
familiar with. The matrix elements of $\hat{X}$ in the position basis
are trivial:
$$\optrip{x_{1}}{X}{x_{0}}=x_{0}\ip{x_{1}}{x_{0}}=x_{0}\dd{x_{1}}{x_{0}}.$$\
\
The position and momentum operators in any basis are related solely by
the commutation relation $$[\hat{X},\hat{P}]=i\hbar.$$ The choice one
makes for the momentum operator in position space is therefore
$$\hat{P}:=-i\hbar\nd{}{x}.$$ Solving its eigenvalue problem in the
continuous position space will prove a more challenging task, as it
contains a derivative. We start by considering its action on a function
in the position basis:
$$\optrip{x_{0}}{P}{f}\equiv -i\hbar\bip{x_{0}}{\nd{f}{x}}=-i\hbar f'(x)$$
where $f'(x)$ is the component in the $x$ direction of the derivative of
$f$ with respect to $x$. Expanding again with the completeness relation,
we also have the alternate equations
$$\optrip{x_{0}}{P}{f}=\int\optrip{x_{0}}{P}{x}\ip{x}{f}\,dx=\int\optrip{x_{0}}{P}{x}f(x)\,dx$$
So this means that
$$-i\hbar f'(x)=\optrip{x_{0}}{P}{f}=\int\optrip{x_{0}}{P}{x}f(x)\,dx.$$
The form we expect is that
$$\optrip{x_{0}}{P}{x}=-i\hbar\dd{x}{x_{0}}\nd{}{x}.$$ Indeed, this form
works with the delta function. We get:
$$\optrip{x_{0}}{P}{f}=\int-i\hbar\dd{x}{x_{0}}\nd{}{x}f(x)\,dx=-i\hbar\int\dd{x}{x_{0}}f'(x)\,dx$$
and this is, by the sampling property,
$$-i\hbar f'(x)\biggl\vert_{x=x_{0}}=-i\hbar f'(x_{0})$$ so we get
$$\optrip{x_{0}}{P}{f}=\hat{P}f(x_{0})=-i\hbar f'(x_{0})$$ as required.
So we have the matrix element
$$\optrip{x_{0}}{P}{x}=-i\hbar\dd{x}{x_{0}}\nd{}{x}.$$ Interestingly,
this is in fact $$\optrip{x_{0}}{P}{x}=-i\hbar\delta'(x-x_{0}),$$ that
is, $-i\hbar$ multiplied by the derivative of $\dd{x}{x_{0}}$ with
respect to its first argument (which here is $x$)! The rule for the
derivatives of Delta functions, which are too mysterious and challenging
to warrant their own proofs for now but which must be stated, is that
$$\frac{d^{(n)}\dd{x}{x_{0}}}{dx^{(n)}}=\delta'^{(n)}(x-x_{0})=\dd{x}{x_{0}}\frac{d^{(n)}}{dx^{(n)}}$$
where the exponent $n$ represents the order of the derivative. Do note
that the derivative is with respect to $x$ here because here $x$ is the
first argument of the delta function and the argument which is
variable.\
\
It is equally important to know that a very different definition for the
operators and their matrix elements occurs if we are in a different
basis- for example, the momentum space. Our original definition in
Postulate 6 was that the position operator was $\hat{X}=x$ and the
momentum operator was $\hat{P}=-i\hbar\nd{}{x}$, but this only holds
true in position space. Position space is generally the space used, as
aforementioned in chapter 5, as it is in physical reality, and it
usually is easier to express keep the potential $V(x)$, a function of
position, in the position basis than it is to find its form in momentum
space. Nevertheless, momentum space can also for example be considered.\
\
Now observe the way in which we derived the action of the position
operator in position space. It should be convincing to the reader that
if we were to replace the position operator with the momentum operator,
and multiply it by a momentum eigenbra, and use the completeness
relation but with momentum eigenkets, we will observe the exact same
result! Nothing at all is contributed by the fact that it was the
position operator we were discussing, other than that it was the
position operator whose eigenbasis was spanning the space above while we
were trying to express its action on constituent kets. Therefore, if we
consider any other continuous operator in a space spanned by its
orthonormal basis, we should obtain the exact same result-- but simply
expressed for a different physical variable!\
\
If one is convinced that we *derived* the action of the position
operator in its own space simply by using continuous relations and
manipulation with its own eigenkets, they should then be convinced that
in momentum space we have: $$\hat{P}f(p)=pf(p).$$ Its matrix elements in
this basis are easy as well:
$$\optrip{p'}{P}{p}=p\ip{p'}{p}=p\dd{p'}{p}.$$

### Position and Momentum eigenfunctions

Fruitful (but difficult) discussions come out of considering the
eigenfunctions of position and momentum. We will work in the position
space, as that is sufficient to provide the necessary discourse and is
the most common space to work in.\
\
One might assume that the eigenvalues of $\hat{X}$ in its own space are
natural. We can denote an eigenvector as $\xi(x)$ and the corresponding
eigenvalue as $x_{0}$. Then we have
$$\hat{X}\xi(x)=x\xi(x)=x_{0}\xi(x).$$ Consider this now carefully. We
have $$x\xi(x)=x_{0}\xi(x)$$ where $x$ is a continuous variable and
$x_{0}$ is a single constant eigenvalue! Clearly something is wrong. It
is impossible for a single eigenvalue to be multiple values of $x$ at
the same time; if it was a function instead, it would not be viable as
an eigenvalue and therefore $\xi(x)$ would also not be an eigenvector.\
\
It turns out this problem is fixed if we make the eigenvector $\xi(x)$ a
special type of function. Of course, by now one should anticipate this
is the Dirac delta function (we can see how useful it is), with
arguments $x_{0}$ and $x$. That way, if we have
$$\hat{X}\dd{x_{0}}{x}=x\dd{x_{0}}{x}=x_{0}\dd{x_{0}}{x}$$ we will see
that the function does the work for us! We get a crude $0=0$ for all the
values of continuous variable $x$ which are not $x_{0}$, and then for
$x=x_{0}$ clearly the eigenvalue and eigenvector conditions are
satisfied. We will rewrite this as
$$\hat{X}\dd{x}{x_{0}}=x_{0}\dd{x}{x_{0}}$$ as it is more conventional
to write $\dd{x}{x_{0}}$ than $\dd{x_{0}}{x}$, even though they are the
same thing.\
\
The momentum eigenvalue problem in position space is more important, and
difficult. The problem is
$$\hat{P}\phi(x)=-i\hbar\nd{}{x}\phi(x)=p\phi(x)$$ for an arbitrary
eigenvector $\phi(x)$ corresponding to eigenvalue $p$. We can tell that
immediately the problem we had with the position eigenvectors in
position space isn't going to be prominent here simply due to the form
of the operator; indeed, we will not need the delta function. Instead,
what one finds is that this is very simply a recognisable first order
differential equation. $$\begin{aligned}
p\phi(x)&=-i\hbar\nd{}{x}\phi(x)\\
\Rightarrow\stab\nd{\phi}{x}&=ip/\hbar\phi(x)
\end{aligned}$$ and this is an equation of the form $$\nd{y}{x}=ky$$
with general solution $y=Ae^{kx}$. So matching these two equations we
have the comparisons $y=\phi(x)$, $x=x$ and $k=ip/\hbar$. Therefore, the
solution to the eigenvector problem is $$\phi(x)=Ae^{ipx/\hbar}.$$ for
some arbitrary constant $A$. It should be noted that $i,\hbar$ are both
constants, and $p$ is the eigenvalue corresponding to the eigenvector,
which is not a single constant unless we are only concerned with a
single eigenvector. Therefore, $x$ is the only variable which changes
the value of the position space momentum eigenfunction as it is itself
varied, which is why we can call it a function of the position variable
$x$. Now, it might seem like our job is done in this section, but the
form of the momentum eigenvectors bring significant imperfections to the
Hilbert space we have so far seen as quite perfect for our job of
describing physical reality. We must deal with these in any valid
discussion of quantum mechanics.\
\
As mentioned in the section on infinities, an exponential function rises
exponentially to infinity as $x$ goes to infinity (when its exponent is
positive, as it is here). The reader should therefore realise that, no
matter what constant $A$ we try to multiply it with, we will never be
able to gain a finite integral over all space and therefore position
$x$. As there is no normalisation which produces a finite norm for a
momentum eigenstate, we can only do the next best thing, which is try to
normalise it in a way which encapsulates this infinite behaviour while
being still mainly serviceable for the needs of algebraic manipulations.
Of course, this can be best done through the Dirac delta function. We
have seen how useful it is, in that its derivatives are defined, it has
secondary properties like sampling which greatly simplify algebra with
it, and it is very commonly seen across what we have already done. Thus,
for such non-finite norm vectors we want to use the process of
*normalising to the Dirac delta function*, the continuous analogue of
normalising to unity!\
\
In the case of momentum eigenvectors, a constant $A$ is already set up
in the general solution. So we can try to find a constant $A$ which
normalises the momentum eigenvectors to the Dirac delta function. In
arbitrary terms, we have, still in the position basis,
$$\ip{p}{p'}=\int\ip{p}{x}\ip{x}{p'}\,dx$$ and we would like
$\ip{p}{p'}$ to be equal to $\dd{p}{p'}$ after we have modified
$\ket{p}$ (we can use the variable label $p$ since it should hold for
all eigenkets) by multiplying it by some constant. Currently the above
is $$\begin{aligned}
\ip{p}{p'}&=\int\ip{p}{x}\ip{x}{p'}\,dx =\int\ip{x}{p}^{\ast}\ip{x}{p'}\,dx\\
&=\int\psi_{p}^{\ast}(x)\psi_{p'}(x)\,dx = \int A^{\ast}e^{-ipx/\hbar}Ae^{ip'x/\hbar}\,dx\\
&=|A|^{2}\int e^{-ix(p-p')/\hbar}\,dx.
\end{aligned}$$ Unfortunately, at this point we cannot use any
mathematics we know or will be able to quickly learn to move forwards,
as the answer lies in a relationship given by Fourier transforms, which
are too advanced for this book. Therefore a relationship will just have
to be stated and taken as given. This is the relationship
$$\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-ik(x-x_{0})}\,dk=\delta(x-x_{0}).$$
It looks haphazard, but at the heart of it lies the connections between
complex numbers, exponentials and pi, of which an example is the Euler
formula. Any further explanation would be meaningless without the reader
understanding Fourier transforms (where from the relationship is
derived) in the first place, and that is hardly assumed knowledge here.\
\
This is reasonably closely related to our momentum eigenstate
normalisation question, with a bridge step. We had:
$$|A|^{2}\int e^{-ix(p-p')/\hbar}\,dx$$ for some normalisation constant
$A$ we are trying to find. We can rewrite this as
$$|A|^{2}\int e^{-i(\frac{p}{\hbar}-\frac{p'}{\hbar})x}\,dx,$$ which is
extremely close to the expression above. The only lemma we need to is
that $\delta(\frac{x}{a})=a\delta(x)$ for some constant $a$. Now we can
use the relations to get
$$|A|^{2}\int e^{-ix(p-p')/\hbar}\,dx=\frac{|A|^2}{2\pi}\delta\left(\frac{1}{\hbar}(p-p')\right)$$
and by the lemma this is $$\frac{|A|^2\hbar}{2\pi}\delta(p-p').$$
Finally, we can see what constant we want $A$ to be! Simply
$A=\frac{1}{\sqrt{2\pi\hbar}}$ will work, and, retracing our steps and
replacing $A$ with $(2\pi\hbar)^{-1/2}$ we will get
$$\ket{p}\duac\frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}\implies\ip{p}{p'}=\delta(p-p').$$
This has taken a lot of labour and a couple of steps we can only take
for granted without more advanced mathematical tools: but one should now
be able to fully understand that orthonormalising to the Dirac delta
function is the continuous analogue of orthonormalising to the Kronecker
delta in the discrete case, and that both are necessary, possible, and
useful.

## Probability Distribution Functions

The state problem was said at its introduction in this book to be a
problem of encapsulation and extraction. The question of extraction is
answered by observable operators and their eigenbases, and elaborated on
by the Compatibility Theorem and Heisenberg Uncertainty Principle, which
result from those observable and measurement postulates. The question of
encapsulation has been already largely answered by state vectors, but
both elegance and historical justice can be demonstrated with the
following formalisation, which will show that the continuous
wavefunction can be interpreted as a probability distribution function
which therefore encapsulates not only all the possible measurements, but
also their probabilities. This is naturally a direct mirror image of the
probability mass function we obtained for the discrete case
wavefunction. After that, the only difficulty-- though it will prove
itself to be much more diverse and challenging than any other-- would be
to solve for the state vector in some basis given the conditions of a
physical problem we are given.\
\
We know how to extract probabilities from our representation of a state:
$$P(\alpha_{i})=|(\alpha_{i},\Psi)|^{2}$$ if $\alpha_{i}$ is some
orthonormal eigenvector. It is important to remember that there are
bases of the state space which do not consist of eigenvectors of some
operator, but since we have already seen that we are exclusively
interested in observable eigenbases when we work in quantum mechanics,
we might often write eigenvector instead of vector with the implicit
assumption that the basis vector we are using would be an eigenbasis
vector. We also know that $$(\alpha_{i},\Psi)=c_{i},$$ the component of
the state vector in the orthonormal basis $\setof{\alpha_{i}}$.
Therefore the components of the state vector in some observable basis
are the links to probabilities in the state problem. We call them
**probability amplitudes**, and the modulus squared of these probability
amplitudes are called **probability densities**. If we work in discrete
cases, probability densities, called probability masses in the discrete
case, are simply synonymous with probabilities, as the postulate shows.
Very minor differences exist in the continuous case, which we now have
the correct definitions to tackle as well.\
\
The generalisation to continuous dimensions of probability mass
functions are well covered in mathematics already. The problem we have
is that continuity implies infinite eigenstates, and therefore, from the
perspective of probability, infinite events. If there are infinite
events, then all of them must have technically have $0$ probability
because we cannot pin a probability down to a single value when there is
a value which corresponds to shifting that value by an infinitely small
increment.\
\
Again, this is pure mathematics rather than quantum mechanics speaking.
It is convention to call the probability distribution functions
**probability density functions** in the continuous case. Since it is a
continuous function, we cannot take a certain value for a probability as
discussed, but we can integrate it between certain bounds!\
\
The integral $$\int_{x=a}^{x=b}|\psi(x)|^2\,dx$$ with a continuous
wavefunction, here the position wavefunction, is the probability that
the state is measured to be somewhere between the eigenstates $\ket{a}$
and $\ket{b}$ corresponding to position values $a$ and $b$. Thus we have
a way to find the probabilities we need now for the continuous case as
well, and see why wavefunctions are probability density functions with
respect to certain measurements of observables.\
\
The state problem, which we left as finished for the discrete case, is
now complete for the continuous case as well. The physical state
corresponds to the state vector, which can be transformed into
wavefunctions by eigenvector inner products. The resulting functions are
either probability mass functions, in the discrete case, or probability
distribution functions, in the continuous case. Finally, I am justified
in calling wavefunctions when I sounded strange beforehand. More
importantly, we are done with all the conceptual learning we will be
covering in this book!

## Exercises from Chapter 7

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 

{% endraw %}
