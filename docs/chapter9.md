---
layout: default
title: Chapter 9
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

{% raw %}

# A Mathematical Toolbox

This book is designed so that even high schoolers can access quantum
mechanics. As such, this section is a reference section, which
acknowledges the fact that high school curricula might teach different
topics in slightly different orders and detail, and also that some of
the prerequisite mathematics assumed here might be just a small reach
beyond high school syllabus. The reference section contains some
instruction, but it should not be used for anyone learning these topics
for the first time, as I have been quite brief so as not to distract
from the main topic of this book. For those who are unfamiliar with
using any of the mathematical rules referenced as assumed knowledge,
they should turn to any textbook which covers these topics and complete
a thorough run through some exercises before reading any other part of
this book. For many other students, they can simply look at the
exercises in these sections, and if they do not see anything unfamiliar,
they can simply skip this reference chapter.\
\

## Mathematical Syntax

There are multiple symbols used as figures of proof in this book, which
represent common phrases one might turn to were they reciting a proof
out loud. As these are ubiquitous symbols, being fluent reading them
will be necessary, as otherwise they can be especially easy to confuse
with each other.\
\

      **Symbol**                **Meaning**
  ------------------ ----------------------------------
         $:=$        
      $\forall$      
      $\exists$      
        $\in$                   (for a set)
      $\implies$     
        $\iff$       
                     
   $\sum_{i\neq j}$  
    $\sum_{\{i\}}$   
      $\square$                    Q.E.D
       $f'(x)$           First Derivative of $f(x)$
       $f''(x)$         Second Derivative of $f(x)$
   $\setof{x_{i}}$   
       $x\to y$      
     $\mathbb{Z}$         the set of all integers
     $\mathbb{R}$       the set of all real numbers
   $\mathbb{Z}^{+}$   the set of all positive integers
       $\equiv$      

\
\
Fluency with basic summation and product notation is assumed. There is
also interval notation commonly used for inequalities:

-   $x\in[a,b)\iff a\leq x < b$

-   $x\in(a,b]\iff a< x \leq b$

-   $x\in(a,b) \iff a< x< b$

-   $x\in [a,b] \iff a \leq x \leq b$

and round brackets are always used for any side of the inequality
bounded by $\pm \infty$.

## Probability$\ast$

In this book, as correct and conventional, probabilities are numbers
between $0$ and $1$, sometimes represented by fractions.

For a random $X$ variable which can take multiple values $x_{i}$

## Complex Numbers$\ast$

Define the imaginary unit, $i$, to be equal to the square root of $-1$.
We then have:

-   $i^2= (\sqrt{-1})^2=-1$

-   $\forall\stab k \in \mathbb{R}, \mtab \frac{k}{i}=\frac{ik}{i^2}=\frac{ik}{-1}=-ik$

-   $\forall\stab k \in \mathbb{R}^+, \mtab \sqrt{-k}\equiv\sqrt{-1} \times \sqrt{k}=i\sqrt{k}$

-   $\forall\stab a,b \in \mathbb{R}, \mtab ai \pm bi = a\sqrt{-1}\pm b\sqrt{-1}= (a\pm b)\sqrt{-1}=(a\pm b)i$

Complex numbers are numbers usually represented in the form $$z:=a+bi$$
for some $a,b\in\mathbb{R}$. Then there are two functions commonly
referred too:

-   $\text{Re}(z)$ is called the of the imaginary number $z$, which is,
    the real number $a$ if $z:=a+bi$.

-   $\text{Im}(z)$ is called the of the imaginary number $z$, which is,
    the real number $b$ if $z:=a+bi$. Note that $\text{Im}(z)=b$ and not
    $\text{Im}(z)=bi$.

It is then clear that a real number is also a complex number, but with
imaginary part $0$. Conversely, if a complex number has imaginary part
$0$, then all that remains is its real part and so it must be a real
number. Therefore,

-   $z \in \mathbb{R} \iff \text{Im}(z)=0$.

We may represent any complex number on a real-valued two dimensional
plane called an Argand diagram (figure). From this figure we can create
a few more useful definitions:

-   The modulus of a complex number $z$ is denoted $|z|$ and defined to
    be $|z|:=\sqrt{\text{Re}(z)^2+\text{Im}(z)^2}$. This is the
    application of Pythagoras' Theorem to find the distance from any
    point $z$ represented on the Argand diagram to the origin.

-   For all complex numbers $z:=a+bi$, we denote with $z^{\ast}$ the
    complex conjugate of the complex number, defined by $z^{\ast}=a-bi$
    (in other words, reversing the sign of the imaginary part).

-   For all complex numbers $z$, we define the modulus squared (or
    square modulus) of that complex number to be $|z|^{2}:=zz^{\ast}$.
    This modulus squared is always real.

    #### Exercises on Complex Numbers\*

    1.  Express as a single complex number with distinct real and
        imaginary parts:

        1.  $(4i)^3$\

        2.  $(5-7i)(6-8i)$\

        3.  $\frac{3+5i}{2-4i}$\

        4.  $(-4-7i)^{\ast}$\

        5.  $|2+3i|^2$\

    2.  Show, with proof, whether each of the following statements are
        true

        1.  $|z|>|\text{Re}(z)|$ and $|z|\geq|\text{Im}(z)|$\

        2.  $\forall\stab z\in\mathbb{C}, \mtab |z|^2\in\mathbb{R}$\

    3.  Show that $|r\cos\theta+ir\sin\theta|=r$\

    4.  

## Matrices\*

A matrix is an array of values. They are placed into rectangular
arrangements in rows and columns, and are an extremely important way of
mathematically listing values. We shall see that the structure of a
matrix allows for powerful computations to be done. For now, there are
many definitions to cover.\
\
A matrix with $m$ rows and $n$ columns is said to be an $m\times n$
matrix. A $n\times n$ matrix is called a square matrix, a $n\times 1$
matrix is usually called a column vector, and a $1\times n$ matrix is
usually called a row vector.\
\
The values of a matrix are usually called the element of that matrix.
For a matrix denoted by any symbol, for example $M$, the notation
$M_{ij}$ usually represents the element in the $i$'th row and $j$'th
column of the matrix. Therefore, we can show the four usual types of
matrices we might often see:

1.  An arbitrary $m\times n$ matrix: $$\begin{bmatrix}
            \text{M}_{11} & \text{M}_{12} & \dots &\dots & \text{M}_{1n} \\
            \text{M}_{21} & \ddots & \dots &\dots & \vdots \\
            \vdots & \dots & \ddots & \dots & \vdots \\
            \text{M}_{m1} & \dots & \dots & \dots & \text{M}_{mn} \\
        \end{bmatrix}$$

2.  A $n\times n$ square matrix: $$\begin{bmatrix}
            \text{M}_{11} & \text{M}_{12} & \dots & \text{M}_{1n} \\
            \text{M}_{21} & \ddots & \dots & \vdots \\
            \vdots & \dots & \ddots  & \vdots \\
            \text{M}_{n1} & \dots & \dots & \text{M}_{nn} \\
        \end{bmatrix}$$

3.  A $n\times 1$ column vector: $$\begin{bmatrix}
            \text{M}_{11} \\
            \text{M}_{21} \\
            \vdots \\
            \vdots \\ 
            \text{M}_{n1} \\
        \end{bmatrix}$$

4.  A $1\times n$ row vector: $$\begin{bmatrix}
            \text{M}_{11} &
            \text{M}_{12} &
            \dots &
            \dots &
            \text{M}_{1n} 
        \end{bmatrix}$$

As shown in the examples, a variety of dots are used often to show the
idea that we can have a large number of unlisted elements between
elements explicitly written. This should not be a great worry, since the
arrangements of elements in a matrix are always in ordered rows and
columns anyway. We now move onto defining the operations:

1.  Scalar multiplication of a matrix $M$ by a scalar $a$ results in a
    new matrix $aM$ with each previous element $M_{ij}$ replaced with a
    new element $aM_{ij}$. So for example, $$-1\times\begin{bmatrix}
            5 & 4 & -9 \\
            0 & -1 & 6 \\ 
        \end{bmatrix}
        =
        \begin{bmatrix}
            -5 & -4 & 9 \\
            0 & 1 & -6 \\ 
        \end{bmatrix}$$

2.  Two matrices can be summed iff they are of the same dimensions. If
    they are of the same dimensions, the sum of two matrices $M$ and $N$
    are obtained by creating a new matrix $S:=M+N$, of the same
    dimensions, where each new element of the resultant matrix $S_{ij}$
    is the result of summing corresponding position elements in $M$: in
    other words, $\forall\stab i,j,S:=M+N, \mtab S_{ij}=M_{ij}+N_{ij}$.
    So for example, $$\begin{bmatrix}
            3 & 2 \\
            -1 & 8 \\
            0 & 5
        \end{bmatrix} + 
        \begin{bmatrix}
            7 & -3 \\
            -1 & 0 \\
            0 & 2 
        \end{bmatrix} = 
         \begin{bmatrix}
            3+7 & 2-3 \\
            -1-1 & 8+0 \\
            0+0 & 5+2 
        \end{bmatrix}= \begin{bmatrix}
            10 & -1 \\
            -2 & 8 \\
            0 & 7
        \end{bmatrix}$$

3.  A matrix multiplying another matrix is more complicated. First of
    all, for two matrices $M$ and $N$ the matrix products $M\times N$
    and $N\times M$ are rarely the same: whichever matrix is on the left
    of the product changes the result. We say that matrix multiplication
    is non-commutative. The terms left-multiply and right-multiply
    emerge naturally from this non-commutativity, where left-multiplying
    a matrix $M$ by a matrix $N$ means performing a matrix
    multiplication with that matrix $N$ on the left of the
    multiplication, and vice versa.\
    \
    Next, matrix multiplication can only be performed if the number of
    columns of the matrix on the left are the same as the number of rows
    of the matrix on the right. If we have an $a\times b$ matrix $M$ and
    a $c\times d$ matrix $N$, then the product $M\times N$ is only
    possible if $b=c$. The result can be best memorised by the crude
    representation: $$b=c\implies
        (a\times b) \times (c \times d) = (a\times \cancel{b}) \times (\cancel{b} \times d) = a\times d.$$
    Here, we get the idea that the values when we list the dimensions of
    the two matrices being multiplied together in the correct order must
    match up and then are discarded, leaving the number of rows of the
    left matrix and the number of columns of the right matrix as the
    dimensions of the resulting matrix after multiplication.\
    \

## Calculus\*

## Misc.\*
