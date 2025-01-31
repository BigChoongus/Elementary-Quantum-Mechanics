---
layout: default
title: Chapter 6
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


# Dirac Notation and Matrix Mechanics

The second part of this book, starting now, will be far more
mathematically demanding. It seeks to complete the original aim of this
pragmatic book: to allow a reader to segue onto mathematically advanced
quantum mechanics texts without chronic confusions of what the
mathematics *means*. Particularly, we will now tackle the challenging
case of extending our quantum mechanics to cover continuously
distributed observables.\
\
We have covered now all of the quantum mechanical postulates we need to
cover. On the other hand, our problem solving skills, which are very
different in quantum mechanics to just standard algebra, are still very
limited in the wider scope of things. There are many manipulative
techniques we have not covered which are fundamental, but far from
trivial. Furthermore, learning these techniques will require a
reformulation of almost everything we have done so far into a new
notation. This switch will be strange and unwelcome at first, but sooner
than later the reader will find that the new notation is far more useful
than confusing, and at that point they will be on a very good path
indeed.\
\
The benefit of this somewhat counterintuitive approach of learning one
way and then reformulating into a new notation is not only that we don't
have several factors affecting our understanding at once and causing
trouble, but that the reader gets training to an undoubtedly
undergraduate level without wrecking their ability to appreciate nuances
as they grapple with difficult problems. Without a wider context of
measurements and probabilities and state evolution within which to frame
the mathematics in this book, it would seem like an endless barrage of
symbols for which we have no use and no appreciation. On the other hand,
after reading the previous chapters, we are capable of understanding why
components are important-- they are probability amplitudes; how the
state vector is both a label and can be used as a substitute for a
physical state; how operators are central to the measurements we achieve
for different operators. With all this conceptual learning done, in many
ways our task from hereon is relatively simple-- change notation and
crunch algebra without any other concerns any more! Remember what
started things off. That $\uspin$ notation, which was designed to show
how unimportant symbols themselves are, was where our discussion
started, and we now come full circle to this idea that notation is far
from sacred and must be evaluated simply based on pragmatic convenience.
This new Dirac notation we are switching too will certainly make things
more convenient, even though the state vector is still a state vector
and the wavefunctions are still wavefunctions and the operators are
still operators. Subsequently, looking in greater detail at the
mathematical processes of quantum mechanics will become easier with our
increased ability to engage in more efficient algebra. Nothing has
changed. We are just switching from more intuitive symbols to the proper
quantum mechanical convention of Dirac notation, which one might not
have seen before but which needn't be mystified.\
\
In addition, it is simply necessary to cover the conventional notation,
called Dirac notation for its founder, and the pertinent techniques
which follow it, because there does not exist a textbook whose level is
a step up from this one and which does not use such conventions and even
in many cases assume it is prior mastered. We will also see that it
would have been difficult to understand what it means outright before we
understood what a state vector is, for example, but on the other hand
now that we do understand what the state vector is, it will make problem
solving more powerful without any danger of confusions.\
\
In this chapter, we will set forwards some new limitations so we can
focus on the algebraic content (given that we understand the concepts of
the postulates quite well now). The primary limitation will be the one
maintained in previous chapters: that we are working in discrete cases.
The next chapter will be all dealing with continuity, which contains
some extremely difficult mathematics resulting from the mathematics in
this chapter, so this limitation will be soon loosened. We will also be
avoiding any thoughts about the wavefunctions being the primary
representations of abstract state vectors, because we will see that with
Dirac's notation comes another natural and powerful idea of matrix
representations! We can also feel free to ignore measurements and
related probabilities so that we can focus on developing algebraic
techniques which will make problem solving more efficient and workable,
because we already understand the postulates we need to therein. So for
now, the job is mainly to forget the wavefunction, and focus on the more
explicitly state vector (and matrix) focused approach we will start
below. We appreciate throughout that wavefunctions (and therefore
measurement probabilities) are still obtainable, by taking the inner
product of a state vector with the relevant input basis vectors in that
component function transformation we have seen, so its absence is far
from its demise.

## Dirac Bra-Ket Notation

Our new notation begins here. Like any new notation, our job will be
changing the way we label the objects we want to consider. The starting
point will be the state vector, and its notation. We will not change any
properties of the state vector! Things may look different because the
notation looks nothing like we have ever seen before, but that does not
mean at all that the characteristics are different.\
\
The state vector will now be written as $\ket{\Psi}$. This called
**ket** psi. We simply call it a ket instead of vector because Dirac
notation is so ubiquitous in quantum mechanics that its authority over
the discourse of quantum mechanics has turned the word ket into a common
noun in itself. The ket and the state vector are one and the same! The
only difference is that we now use the notation $\ket{\Psi}$ instead of
the notation $\Psi$.\
\
The space of possible physical states will now be called the ket space
instead of the state space. Obviously, since kets are the same as state
vectors, kets are still in bijection with physical states. The vectors
which span the ket space are also kets themselves. Therefore, an
arbitrary ket can be expressed with components $\setof{c_{i}}$ as
$$\ket{X}:=\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}$$ for a basis set
$\setof{\ket{\alpha_{i}}}$. We can define scalar multiplication exactly
as we have before:
$$k\times\ket{X}=k\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}=\sum_{i=1}^{n}(kc_{i})\ket{\alpha_{i}}$$
where the scalar multiplies each component of the vector to give it new
components. Addition is defined by summing corresponding components as
well:
$$\ket{X}:=\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}, \ket{Y}:=\sum_{i=1}^{n}c'_{i}\ket{\alpha_{i}}\implies \ket{X}+\ket{Y}=\sum_{i=1}^{n}(c+c'_{i})\ket{\alpha_{i}}$$\
\
An extremely important point, again, is that the ket is an abstract
object. Recall that the state vector could not be given a form until we
chose a specific basis. Since the ket is the same, we will here need to
chose a basis for the ket to take a form. The key novelty of our new way
of approaching the same ideas is that, in our bid to make our state
vector, now ket, more , we will this time try to divorce the ket from
the idea of a wavefunction representation and replace this with yet
another representation in bijection to the state vector-- a matrix
representation! This is because ideas of matrices will be very useful to
us in our work and manipulation. To do this, recall that in any basis a
constituent of any vector space has unique components in that basis,
most often referred to as its unique expansion in that basis. This
allows us to create a unique matrix expression of any ket: for any
$$\ket{X}:=\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}$$ in the basis
$\setof{\ket{\alpha_{i}}}$, we can express it as a column vector of its
components $$\ket{X}=\begin{bmatrix}
c_{1}\\
c_{2}\\
\vdots\\
c_{n}\\
\end{bmatrix}$$ and this is a unique way to express the ket in that
basis. As all kets have the same dimensions in this matrix expression
(since the dimension of the ket space is the same so the number of
components specifying them are the same), we can form any linear
combinations of them since we are just summing matrices of the same
dimensions, which is acceptable, and this matrix expression will not be
meaningless.\
\
Another important point is for the inner labelling of kets: i.e-
$$\ket{\textbf{Inner Label}}.$$ The inner label of a ket never has any
mathematical meaning. We can label kets
$$\ket{1}, \ket{2}, ... \ket{5}$$ if we want to. They are absolutely
nothing to do with the numbers $1$ to $5$. Instead, the inner label
serves to **organise** different kets: above, we have ordered ket $1$,
ket $2$, ket $3$, and so on in some arbitrary way which is meaningful to
us. We could also label them
$$\ket{\text{Dirac}}, \ket{\text{Heisenberg}}, \ket{\text{Feynman}}$$
except this provides no logical order for us and is long to write.
Sometimes one will see some long-winded labels, such as
$$\ket{P=\sqrt{{2mE}/{\hbar}}\:}$$ which is an example taken from
Chapter 8, where we needed to label a ket by its momentum value
$\sqrt{{2mE}/{\hbar}}$ to distinguish it from another ket with another
momentum value (but otherwise identical characteristics). One should not
be confused if there are numerical numbers as inner labels of kets: they
are part of a taxonomy we have chosen ourselves. For example, in this
book and ubiquitously in all books, convention is to denote eigenkets by
the eigenvalue they represent. This is not to say that the label is
physically meaningful-- we could easily label each eigenket by the
square of its eigenvalue, for example- but it is useful to remember and
use because it makes things clear for us when we have several lines of
algebra simultaneously. Next, we need to complete the new notation for
the inner product.

### Bra space and Inner Products

One operation we cannot perform with a ket alone is the all-crucial
inner product. To define this, we first define a new vector space. This
vector space is the bra space, and is made by a simple transformation:
for every ket $\ket{X}$, the corresponding bra is written $\bra{X}$ and
is defined by $$\bra{X}=\ket{X}^{\dagger}.$$ The notation means the
**Hermitian adjoint** of the ket $\ket{X}$. This is the formal way to
refer to the transpose conjugate of any matrix (see the matrix
preliminary) -- that is, complex conjugate all the matrix element values
and then transpose the matrix. For the column vector kets, this
therefore turns them to row vectors with the complex conjugate entries:
$$\ket{X}=\begin{bmatrix}
c_{1}\\
c_{2}\\
\vdots\\
c_{n}\\
\end{bmatrix}\Rightarrow\stab\bra{X}=\begin{bmatrix}
c^{\ast}_{1}\stab c^{\ast}_{2} \dots c^{\ast}_{n}.
\end{bmatrix}$$ One sees that the relationship exhibited between the two
vector spaces of the ket space of kets and the bra space of bras is
bijection. This is because every ket is unique as a column vector-- due
to its unique expansion in any basis set-- and therefore taking the
Hermitian adjoint will give us one single unique bra. For every element
of the ket space there is therefore a single element in the bra space,
and vice versa. This exists precisely because of the way we have defined
the bra space.\
\
Why define such a bra space? Bras never represent physical states
directly- even though they are in bijection with the state vectors
(kets) which are in bijection with physical states so each bra is in
bijection with physical states. The answer is simple-- because we need
the inner product to be a real scalar given two input states: as we have
already seen for the last few chapters. We cannot simply multiply two
kets because we cannot multiply two column vectors by the rules of
matrix multiplication! Therefore, we define the bra, which is a row
vector with the complex conjugate entries, and now if we multiply them:
$$\bra{X} \times \ket{X}$$ we should get a $1\times n$ row vector
multiplying an $n\times 1$ column vector, and therefore a $1\times 1$
result: eg, a scalar, as desired.\
\
We should be convinced that this new inner product is exactly the same
as the old inner product. Take any two state vectors
$$\forall\stab\ket{\beta}:=\sum_{i=1}^{n}b_{i}\ket{\alpha_{i}}, \:\: \ket{\gamma}:=\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}},$$
By the rules of matrix multiplication, the $i$'th column component of
the row vector multiplies the $i$'th row component of the column vector.
Thus we have
$$\bra{\beta}\times\ket{\gamma}:=\ip{\beta}{\gamma}=\sum_{i=1}^{n}b^{\ast}_{i}c_{i}.$$
as the components of the ket column vector, here $\ket{\beta}$ are
replaced by their complex conjugates in the bra row vector. There is
absolutely no difference to the inner product operation: only, we
consider it from a new perspective due to the matrix representations we
have introduced.\
\
Several properties we have established previously can now be written in
the new notation:

-   $\ip{X}{Y}=\ip{Y}{X}^{\ast}$

-   $\ip{X}{X}\geq0$

-   A normalised ket $\ket{\Tilde{\alpha}}$ is such that
    $\ip{\Tilde{\alpha}}{{\Tilde{\alpha}}}=1$.

-   Two kets $\ket{\alpha}$ and $\ket{\beta}$ are orthogonal if
    $\ip{\alpha}{\beta}=0$.

To further the bijection between the ket space and bra space, as bras
will prove more useful than only to appear in inner products, we have,
using the conventional $\leftrightarrow$ symbol to mean :
$$\begin{aligned}
\ket{X}&\duac\bra{X}\\
c\ket{X}&\duac c^{\ast}\bra{X}\\
\ket{X}+\ket{Y}&\duac \bra{X}+\bra{Y}.\\
\end{aligned}$$ The way we obtain this is an important algebraic point:
by performing the operation on any linear combination of kets, we
immediately create a new set of bras in bijection with linear
combinations of kets of that type, in much of a similar argument to the
one we used originally to show the bra space is in bijection to the ket
space.\
\
The expansion of bras in their basis should be clear following the above
facts. For $$\ket{X}:=\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}$$ we have
$$\bra{X}=\sum_{i=1}^{n}c_{i}^{\ast}\bra{\alpha_{i}}.$$ Thus completes
our investigation of the bra space, and now we can continue to
reformulate old ideas in this new notation to familiarise ourselves with
it.\
\
Further with inner label conventions: in general, for scalars we write
$\ket{aX}$ to mean $a\ket{X}$, and $\bra{aX}$ to mean $a^{\ast}\bra{X}$.
It is up to the reader to distinguish which are the scalars and which
the placeholder letters for kets and bras in question, though the
context should never make this in any real doubt if one follows the
steps through. Similarly, we want to ensure brevity with this notation
as one (but not the only) of the benefits of employing bra ket notation,
so we also often write $\ket{aX+bY}$ instead of $\ket{aX}+\ket{bY}$ or
$a\ket{X}+b\ket{Y}$. Using the ket $\ket{aX+bY}:=\ket{aX}+\ket{bY}$ is
somewhat easier than for example defining $$\ket{Z}:=\ket{aX}+\ket{bY}$$
every time we sum two kets, where a new letter in the inner label would
just be confusing.\
\
The inner product short-form facts are always helpful; indeed, we have
*linearity in ket*:
$$\ip{V}{aX+bY}\equiv\bra{V}\times(\ket{aX}+\ket{bY})\equiv\ip{V}{aX}+\ip{V}{bY}\equiv a\ip{V}{X}+b\ip{V}{Y}.$$
This fact is one we have seen already (fact S7 in Chapter 3) for inner
products, but expressed in Dirac notation. The comparable idea exists in
bra:
$$\ip{aX+bY}{V}=(\bra{aX}+\bra{bY})\times\ket{X}=\ip{aX}{V}+\ip{bY}{V}=a^{\ast}\ip{X}{V}+b^{\ast}\ip{Y}{V}.$$\
Next, we can also recall the ubiquitous expansion. Take an arbitrary ket
$\ket{X}$ in the orthonormal basis $\setof{\ket{\tilde{\alpha}_{i}}}$
and the following will always hold: $$\begin{aligned}
\ket{X}&:=\sum_{i=1}^{n}c_{i}\ket{\tilde{\alpha}_{i}} \implies \forall j, \stab \ip{\tilde{\alpha}_{j}}{X}=\bra{\tilde{\alpha}_{j}}\times\sum_{i=1}^{n}c_{i}\ket{\tilde{\alpha}_{i}}.
&
\end{aligned}$$ By linearity in ket, the outside bra is absorbed into
the sum notation so we get
$$\ip{\tilde{\alpha}_{j}}{X}=\sum_{i=1}^{n}c_{i}\ip{\tilde{\alpha}_{j}}{\tilde{\alpha}_{i}}=\sum_{i=1}^{n}c_{i}\delta_{ij}$$
by the orthonormality of the basis. Then, this is simply
$$\ip{\tilde{\alpha}_{j}}{X}=c_{j},$$ which should certainly be familiar
now, though perhaps not before in Dirac notation. It tells us that,
given a basis, if we orthonormalise it (with the Gram-Schmidt process),
the expansion coefficients of any ket are not random: they are the inner
products of the ket being expanded with the corresponding basis kets. So
for any ket $\ket{X}$,
$$\ket{X}=\sum_{i=1}^{n}\ket{\tilde{\alpha}_{i}}\ip{\tilde{\alpha}_{i}}{X}.$$
It is important to represent it explicitly here because the above will
be used universally for problems to follow, and without explicitly
stating that this is the expansion we already know it could otherwise be
confusing. The reader should find it simple to produce a bra expansion
in an orthonormal bra basis, though this is seldom as useful or commonly
used.

### Operators and Eigenkets

The action of an operator $\Omega$ on a ket $\ket{X}$ is written
$\Omega\ket{X}$. This is perhaps why we incorporate scalars into the ket
inner label, as noted above-- so that there is no mixup between scalar
multiplication and the action of an operator on a ket. The action of an
operator on a bra is conversely written $\bra{X}\Omega$.\
\
We always focus on linear operators which map one ket onto another ket
in the vector space. This makes sense: the application of observable
operators for example we do not expect to make an impossible state, and
any possible state is represented by some superposition of the state
vectors which constitute the ket space. It is good to keep in mind very
explicitly the notion that an operator acting on a ket always produces a
new ket. More properties of linear operators can be expressed in bra-ket
notation:

-   $a\Omega\ket{X}=\Omega a\ket{X}$

-   $\bra{X}a\Omega=\bra{X}\Omega a$

-   $\Omega_{1}\ket{X}=\Omega_{2}\ket{X} \forall\ket{X}\implies\Omega_{1}=\Omega_{2}$

-   $\Omega\{a\ket{X}+b\ket{Y}\}=a\Omega\ket{X}+b\Omega\ket{Y}$

-   $\Omega\{a\bra{X}+b\bra{Y}\}=a\bra{X}\Omega+b\bra{Y}\Omega$

The product of two operators means to apply the operator to the ket or
bra respectively and then apply the second, operator to the resulting
ket or bra. We already know from our study of compatibility in
particular that the assumption that two given operators will commute is
false. The commutator is denoted the same way:
$$[\Omega, \Lambda]:=\Omega\Lambda-\Lambda\Omega$$ and so is the
anticommutator: $$\{\Omega, \Lambda\}:=\Omega\Lambda+\Lambda\Omega.$$
The eigenvectors of the operators will now often be called eigenkets,
for obvious reasons, and the name eigenbras follows for bras in
bijection with eigenkets.\
\
We must now introduce the unique way to specify an operator as a matrix.
This will allow us to perform some important operations in the future.\
\
We start by noting that the action of an operator on the basis vectors
of a ket space (any basis, not just its own eigenbasis!) is sufficient
knowledge to specify its actions on all kets in that basis:
$$\Omega\ket{\alpha_{i}}=\ket{\alpha'_{i}}\imp\:\: \forall \stab\ket{X}:=\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}, \mtab \Omega\ket{X}=\Omega\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}$$
and by the linearity of the operator, this is just
$$\Omega\ket{X}=\sum_{i=1}^{n}\Omega c_{i}\ket{\alpha_{i}}=\sum_{i=1}^{n} c_{i}\Omega\ket{\alpha_{i}}=\sum_{i=1}^{n}c_{i}\ket{\alpha'_{i}}.$$
However, things are not over from the perspective of a matrix
formulation. Not only does this specification not give any clue as to
how to express the operator as a matrix, but the resulting ket after the
transformation is made is also not in any way representable as a column
vector. This is because we must remember that a linear transformation on
the basis vectors of a space by no means produces another basis which
still spans the space at all (in which case a vector of components makes
no sense anymore). The best example of this, of course, would be if
$\Omega=\Omega_{0}$, the null operator, in which case all
$\ket{\alpha'_{i}}$ would be null kets and certainly span no space at
all.\
\
So the above informs us that to complete the task we need to return all
the above to the original basis, which we know is serviceable for matrix
representations. We thus start by expressing the components of the
transformed kets $\setof{\ket{\alpha'_{i}}}$ in the original basis. If
$$\ket{\alpha'_{j}}:=\sum_{i=1}^{n}c^{(j)}_{i}\ket{\alpha_{i}}$$ and we
assume the starting basis $\setof{\ket{\alpha_{i}}}$ is orthonormal,
since otherwise it could be orthonormalised, then we clearly know the
components $c_{i}^{(j)}$ are simply the inner products
$\ip{\alpha_{i}}{\alpha'_{j}}$. This component is the component of the
$j$'th transformed ket corresponding to the $i$'th basis ket. We can
then define the entities
$$\Omega_{ij}:=\ip{\alpha_{i}}{\alpha'_{j}}=\bra{\alpha_{i}}{\Omega}\ket{\alpha_{j}}$$
and these are the components of the transformed kets in the original
basis before they were transformed. The original question can be
reposed. If we define
$$\Omega\ket{X}:=\ket{x_{0}}:=\sum_{i=1}^{n}c'_{i}\ket{\alpha_{i}}$$ for
some components $c'_{i}$, then these components are
$$c'_{i}=\ip{\alpha_{i}}{x_{0}}=\bra{\alpha_{i}}\Omega\ket{X}=\bra{\alpha_{i}}\Omega\biggl(\sum_{i=1}^{n}c_{i}\ket{\alpha_{i}}\biggr).$$
By the linearity of the operator, this becomes
$$c'_{i}=\bra{\alpha_{i}}\times\biggl(\sum_{j=1}^{n}c_{j}\Omega\ket{\alpha_{j}}\biggr),$$
and then by linearity in ket this becomes
$$c'_{i}=\sum_{j=1}^{n}c_{j}\bra{\alpha_{i}}{\Omega}\ket{\alpha_{j}}.$$
Thus using the same notations defined above this is simply
$$c'_{i}=\sum_{i=1}^{n}c_{i}\Omega_{ij}.$$ The notation $\Omega_{ij}$ is
clearly meant to hint that these can be placed in some matrix where each
value $\Omega_{ij}$ (note these are inner products, so they are indeed a
scalar values) is the entry in the $i$'th row and $j$'th column of the
matrix. And as each $\Omega_{ij}$ is the component of the $j$'th
transformed ket corresponding to the $i$'th basis ket, we say that the
upper limit of $i$ and $j$ are both $n$ since there are $n$ original
basis kets, and therefore $n$ transformed kets as well. Thus we can
create an $n\times n$ matrix for all the entries $\Omega_{ij}$. The
relationship we get is that $$\begin{bmatrix} 
c'_{1} \\ 
c'_{2} \\
\vdots \\ 
c'_{n} \\ 
\end{bmatrix}
=
\begin{bmatrix}
\langle{\alpha_{1}}|\Omega|{\alpha}_{1}\rangle & \langle{\alpha_{1}}|\Omega|{\alpha}_{2}\rangle &
\dots & \langle{\alpha_{1}}|\Omega|{\alpha}_{n}\rangle\\ 
\langle{\alpha_{2}}|\Omega|{\alpha}_{1}\rangle & \ddots &
\:\dots\: & \vdots \\
\vdots & \vdots & \ddots & \vdots\\ 
\langle{\alpha_{n}}|\Omega|{\alpha}_{1}\rangle & \dots & \dots & \langle{\alpha_{n}}|\Omega|{\alpha}_{n}\rangle
\end{bmatrix}
\begin{bmatrix} 
c_{1} \\ 
c_{2} \\
\vdots \\ 
c_{n} \\
\end{bmatrix}$$ as a way to relate the components of the transformed
vector $\Omega\ket{X}:=\ket{x_{0}}$ to the original components of
$\ket{X}$ before it was transformed. We see that the left hand side is
the matrix representation of $\ket{x_{0}}$ in the basis we have been
using, since it specifies the components of $\ket{x_{0}}$ as a column
vector. Meanwhile, the right column vector clearly does the same for the
original $\ket{X}$. And therefore this whole matrix equation is clearly
the matrix form of the definition $\ket{x_{0}}=\Omega\ket{X}$, which
then means that the $n\times n$ matrix in the middle is the matrix
representation of $\Omega$. So to conclude this discussion we restate
the fact that $$\begin{bmatrix}
\langle{\alpha_{1}}|\Omega|{\alpha}_{1}\rangle & \langle{\alpha_{1}}|\Omega|{\alpha}_{2}\rangle &
\dots & \langle{\alpha_{1}}|\Omega|{\alpha}_{n}\rangle\\ 
\langle{\alpha_{2}}|\Omega|{\alpha}_{1}\rangle & \ddots &
\:\dots\: & \vdots \\
\vdots & \vdots & \ddots & \vdots\\ 
\langle{\alpha_{n}}|\Omega|{\alpha}_{1}\rangle & \dots & \dots & \langle{\alpha_{n}}|\Omega|{\alpha}_{n}\rangle
\end{bmatrix}$$ is the way to represent the operator $\Omega$ in the
$n$-dimensional ket space spanned by the orthonormal basis vectors
$\setof{\ket{\alpha_{i}}}$.

## A Rudimentary Manipulation Toolbox

The introduction of Dirac notation is surprisingly powerful because its
unorthodox aesthetic form allows for the formulation of some identities
and operators which under normal circumstances would look like a long
amalgamation of random algebraic entities, but look simple and orderly
(and therefore easy to memorise and use) in Dirac notation. This section
will introduce essential identities and axioms which will be used
without second thought for advanced problem solving, and in doing so, I
hope the reader can also continue the process of becoming fluent in Bra
Ket.

### General Solution of the Eigenvalue Problem

The first tool we will see is a general solution of the eigenvalue
problem, for which we have been waiting. The eigenvalue condition is
always $$\Omega\ket{\omega} = \lambda\ket{\omega}.$$ for some eigenvalue
$\lambda$ and eigenvector $\ket{\omega}$ We know that all operators in
the space can be represented by an $n\times n$ matrix (where $n$ is the
dimensionality of the space). Just to convert the eigenvalue $\lambda$
into matrix form as well, we will multiply both sides by the $n\times n$
identity operator $I$: $$\begin{aligned}
\Omega\ket{\omega} &= \lambda I\ket{\omega}\\
\Rightarrow\:\: (\Omega-\lambda I)\ket{\omega} &= 0
\end{aligned}$$ where 0 is the null matrix. Considering the whole in
matrix form, we write: $$\begin{bmatrix}
\Omega_{1,1}-\lambda & \Omega_{1,2} & \dots  & \Omega_{1,n} \\ 
\vdots  &   \Omega_{2,2}-\lambda & \vdots & \vdots \\ 
\vdots &  \dots & \ddots & \vdots \\
\Omega_{n,1} & \dots & \dots & \Omega_{n,n}-\lambda\\ 
\end{bmatrix}
\begin{bmatrix}
c_{1} \\ 
c_{2} \\ 
\vdots \\ 
c_{n} \\ 
\end{bmatrix}
= 
\begin{bmatrix}
0 \\
0 \\
\vdots \\ 
0 \\
\end{bmatrix}.$$ Looking at the matrix representation of the equation
above, we can deduce that
$$\forall i, \:\: \sum_{j}c_{j}(\Omega_{ij}-\lambda\delta_{ij})=0$$ by
the rules of matrix multiplication. This is a linear system of
equations, with coefficients $\Omega_{ij}-\lambda\delta_{ij}$ and
unknowns $c_{i}$. Therefore the logic behind Cramer's Rules apply: and
since the $c_{i}$ are the components of $\ket{\omega}$ in the basis they
are not all zero since $\ket{\omega} \neq 0$, and thus we need
nontrivial solutions and therefore the determinant of the leftmost term
must be zero. In other words, $$\det(\Omega-\lambda I) = 0 \iff
\forall i, \:\: \sum_{j}c_{j}(\Omega_{ij}-\lambda\delta_{ij})=0$$ This
is practically helpful, especially in problems with fewer dimensional
spaces, and as a theoretical concept which shows us we can always solve
the eigenvalue problem. There will be other methods to solve eigenvalue
equations too, but these often rely somewhat more on inspection and then
proof that one has all the solutions by inspection; these inspection
methods only arise as shortcuts based on specific conditions we get.

### The Associative Axiom

Dirac introduced in his paper on Dirac notation a critical axiom called
the Associative Axiom. This axiom will save a huge amount of confusion
for those unfamiliar with Bra-Ket notation, and is possibly the most
powerful idea of them all. This axiom states that all (legal) operations
in Dirac notation are always associative.\
\
Put in scalar terms, this word associative is usually seen as
$$(a\times b)\times c = a \times (b\times c).$$ In other words, so long
as the order of the terms $a,b,c$ are kept (here, $a$ before $b$ before
$c$), the two multiplication operations can be performed in either
order. With numbers this is completely natural (as also is additive
associativity, but not subtractive or divisive associativity), but with
Dirac notation this is much less trivial and also much more powerful.\
\
The first example we have seen but not explained explicitly is the inner
product $$\bra{X}{\Omega}\ket{Y}.$$ This is an inner product since it is
the product of a bra, $\bra{X}$ with a ket $\Omega\ket{Y}$ (which is
another ket in the ket space the operator $\Omega$ has mapped the
original ket $\ket{Y}$ to). However, it can also be seen as a bra,
$\bra{X}\Omega$, multiplied by a ket $\ket{Y}$. This is the associative
axiom: in fact it does not matter which way the multiplication goes and
only because of this can we write the concise $\bra{X}{\Omega}\ket{Y}$.\
\
The ramifications of this fact are profound, as beginners with Dirac
notation often get confused about which products are and must be
performed first, leading to a great state of bewilderment when a term
might have several bras, operators and kets next to each other. The
answer is very simply that, so long as operations are being performed
left to right, the order does not matter and the reader may read the
multiplications in any way they like. It also immediately leads to
theorems for entities in Dirac notation, by defining them through the
perspective of other known products. The first example of this we will
see is the following completeness relation.\
\
**[The Outer Product]{.underline}**\
\
We discussed above how the associative axiom holds for all legal
multiplications between bras, kets and operators. What constitutes an
illegal multiplication? Well, to start we can give the example of the
orthonormal expansion of any ket $\ket{X}$,
$$\ket{X}=\sum_{i=1}^{n}\ket{\talpha_{i}}\ip{\talpha_{i}}{X}.$$ Contrast
this to the naive expansion
$$\ket{X}=\sum_{i=1}^{n}c_{i}\ket{\talpha_{i}}$$ which we might use if
we were not sure the basis was orthonormal, for example. We see that the
position of the component shifted from the leftmost sum term to the
rightmost sum term when $c_{i}$ was replaced with $\ip{\talpha_{i}}{X}$.
One might ask why this is. The best answer for this is simply the
associative axiom: if we had written
$$\ket{X}=\sum_{i=1}^{n}\ip{\talpha_{i}}{X}\ket{\talpha_{i}},$$ then we
might think this is okay as we have a scalar $\ip{\talpha_{i}}{X}$
multiplying a ket $\ket{\talpha_{i}}$. However, by the associative axiom
we also expect the above to be equally well expressed as
$$\ket{X}=\sum_{i=1}^{n} \bra{\talpha_{i}}\times\biggl(\ket{X}\times\ket{\talpha_{i}}\biggr).$$
This is where our problem is-- two kets cannot be multiplied together,
as they are both $n\times 1$ matrices! Similarly, two bras cannot be
multiplied together as they are both $1\times n$ matrices. So this is
why we cannot write
$$\ket{X}=\sum_{i=1}^{n}\ip{\talpha_{i}}{X}\ket{\talpha_{i}}.$$ This
however implies that for the expansion
$$\ket{X}=\sum_{i=1}^{n}\ket{\talpha_{i}}\ip{\talpha_{i}}{X}$$ it is
correct and therefore not only is the operation
$\ket{\talpha_{i}}\times\ip{\talpha_{i}}{X}$ legal (it is a scalar
multiplying a ket, so it should be)- but also that the operation
$$\left(\op{\talpha_{i}}{\talpha_{i}}\right)\times \ket{X}$$ should be
possible. This product $\op{\talpha_{i}}{\talpha_{i}}$ is called the
outer product between the bra $\bra{\talpha_{i}}$ and ket
$\ket{\talpha_{i}}$. We can verify it should be possible, as it is an
$n\times 1$ matrix multiplied by a $1\times n$ matrix, which should give
an $n\times n$ matrix. As it produces an $n\times n$ matrix it clearly
does not result in a scalar like the inner product; rather, we might
posit that it is an operator, as operators are represented by
$n\times n$ matrices. This is in fact a true assumption: an outer
product is fundamentally meant to be treated as an operator. However,
before we discuss that we should establish and prove a fundamental
theorem in quantum mechanics which will be surprisingly useful for
manipulation. This is the completeness relation, which results from the
associative axiom, and deserves its own section for its importance even
though the proof requires no considerable thought if we have the
associative axiom in mind.\
\
**[The Completeness Relation]{.underline}**\
\
We have seen that the representation
$$\ket{X}=\northexp{X}{\talpha_{i}}$$ is allowed because the sum term
$\sop{\talpha_{i}}\times \ket{X}$ is just the action of the outer
product on the ket ${X}$. However, by the rule of linear operators that
$$(\Omega_{1}+\Omega_{2})\ket{X}=\Omega_{1}\ket{X}+\Omega_{2}\ket{X}$$
and the fact that the outer products are operators, we can use the same
principle to write
$$\ket{X}=\biggl(\sum_{i=1}^{n}\sop{\talpha_{i}}\biggr)\ket{X}.$$ And
this is very revealing, of course, because this is true for any
arbitrary ket $\ket{X}$, and therefore we come to the conclusion that
$$\sum_{i=1}^{n}\sop{\talpha_{i}}=1.$$ This is the most commonly written
form of the completeness relation, but one should be aware that the 1
here represents the identity operator, rather than a scalar-- since the
sum of $n\times n$ matrices will give us an $n\times n$ matrix rather
than a scalar.\
\
On the other hand, the more we foray into problem solving the more we
will see of this seemingly completely useless relation. One example can
be in the proof that the sum of the modulus squared components of a
normalised ket is also equal to $1$:
$$\sip{X}=\bra{X}\times\ket{X}=\bra{X}\times (1\ket{X})=\bra{X}\times \sum_{i=1}^{n}\sop{\talpha_{i}}\times\ket{X}$$
where the number $1$ is the identity operator again and the kets
$\setof{\talpha_{i}}$ are the orthonormal basis vectors. Then, by
linearity in ket, we can write this as
$$\sip{X}=\sum_{i=1}^{n}\bra{X}\times\sop{\talpha_{i}}\times\ket{X}$$
and by the associative axiom this is just
$$\sip{X}=\sum_{i=1}^{n}\ip{X}{\talpha_{i}}\ip{\talpha_{i}}{X}=\sum_{i=1}^{n}\ip{\talpha_{i}}{X}\times(\ip{\talpha_{i}}{X})^{\ast}=\sum_{i=1}^{n}|\ip{\talpha_{i}}{X}|^{2}.$$
However, as the inner products $\ip{\talpha_{i}}{X}$ are the components
of $\ket{X}$ in the basis $\setof{\talpha_{i}}$, if the ket $X$ is
normalised then the left side is $1$ so we get
$$1=\sum_{i=1}^{n}|c_{i}|^2.$$ So the modulus squared of the components
of a normalised ket in a basis sum to $1$. We know these modulus squared
components are probabilities if we are working in an observable space by
the measurement postulate! So what we have just proved, in a flick of
the pen when working with Dirac notation, is that the reason we like
working with discrete wavefunctions is because their components in this
way perfectly represent probabilities summing in total to $1$! We have
already proved this fact, at the end of Chapter 4 on normalised discrete
wavefunctions being interpreted as probability mass functions, but, if
one takes a quite glance at that, the proof is neither so short, nor so
elegant: it is positively clunky in comparision. The purpose of showing
this is to exhibit that, just like in normal algebra, the world of Dirac
notation can belie some extremely unusual and ingenious manipulations
which without the notation would not be so easy to express, but with the
fluency in the notations, can be done in just a few lines or seen in a
matter of seconds.

## Change of Basis

One of the most important concepts in matrix mechanics is that of
diagonal matrices. A square matrix is diagonal if all its elements are
$0$ except those in the major diagonal: that is, elements $M_{ii}$,
which can be anything. One example of a diagonal matrix is the identity
matrix, which has all zero entries except the major diagonal, which is
filled with $1$'s.\
\
**Theorem: Every Hermitian operator has at least one orthonormal**\
**eigenbasis in which its matrix representation is diagonal. The**\
**diagonal entries are the eigenvalues of the operator.**\
\
This proof is quite tough and not particularly illustrative for our
current needs, and therefore will not be shown for now. However, we will
find that the implications of this theorem are hugely powerful, because
it means that if we can diagonalise the operator matrix then we
immediately solve the eigenvalue problem as the diagonal matrix values
give us the eigenvalues from which deriving the eigenvectors should be
easy: clearly, a great problem-solving step.\
\
So we want to diagonalise the operator. By the theorem, this means we
want to take one matrix in any basis to the eigenbasis which
diagonalises the operator. Thus we will often be interested in a
**change of basis**.\
\
A change of basis is performed by applying an operator to the original
basis kets and mapping them onto the new kets. Such is a common idea in
quantum mechanics: to transform one ket to another we also try to see if
there is a way we can formulate it as an operator equation. Here, we
certainly can; such operators are usually denoted $U$. So we guess that
for some original basis $\setof{\ket{\alpha_{i}}}$ and operator $\Omega$
with eigenvalues $\setof{\beta_{i}}$ and eigenvectors
$\setof{\ket{\beta_{i}}}$,
$$\forall i, \stab U\ket{\alpha_{i}}=\ket{\beta_{i}}.$$ Assuming without
loss of generality that these basis sets are both orthonormal, the
operator which works is $$U:=\sum_{j}\op{\beta_{j}}{\alpha_{j}}.$$ We
can prove this. For any original basis ket $\ket{\alpha_{i}}$,
$$\biggl(\sum_{j}\op{\beta_{j}}{\alpha_{j}}\biggr)\ket{\alpha_{i}}=\sum_{j}\ket{\beta_{j}}\ip{\alpha_{j}}{\alpha_{i}}=\sum_{j}\ket{\beta_{j}}\delta_{ij}=\ket{\beta_{i}}$$
and this holds for any $i$ since we have orthonormal sets. What is much
more important, however, is that the operator $U$ satisfies a very
interesting condition. Consider, for the operator defined, the product
$$U^\dagger U=\biggl(\sum_{k}\op{\alpha_{k}}{\beta_{k}}\biggr)\times\biggl(\sum_{j}\op{\beta_{j}}{\alpha_{j}}\biggr)$$
As the basis sets are orthonormal, we see that all the terms disappear
on account of the inner product $\ip{\beta_{k}}{\beta_{j}}$, except when
$k=j$. In those cases, we get $$\sum_{k}\sop{\alpha_{k}}=1.$$ So for
this , we have $U^{\dagger}U=1$. Similarly, $U U^{\dagger}=1$. Such an
operator is called **unitary**. Now consider some arbitrary operator
which is unitary and its action on a state ket which is normalised. We
know that for the ket $\ket{\Psi
}$

## Exercises from Chapter 6$\ast$

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
