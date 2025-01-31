---
layout: default
title: Chapter 5
mathjax: true
render_with_liquid: false
---

{% raw %}

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

# Time Evolution and Problem Solving Techniques

We will complete our study of the postulates of quantum mechanics in
this chapter, which will be more pragmatic than the precedent two
chapters where we had to deal with abstract mathematical theory in
vector spaces and operators. The time-evolution problem, which we will
study in this chapter, will prove to be a double-edged challenge. On one
hand, the time evolution postulate is completely trivial conceptually,
especially compared to the state vector, observable and measurement
postulates, so the reader can breathe a sigh of relief and know they
won't have to deal with learning a new field of mathematics just to
tackle this problem. All it will include is learning one equation: the
all-famous Schrödinger Equation postulated by Erwin Schrödinger, and
this equation will not be difficult to understand. On the other hand,
the time evolution problem has by far the most potential to be complex,
and in some advanced cases, impossible to solve without new intensely
demanding mathematical techniques for manipulation and indeed often
(though still very accurate) approximation. This should not be
disheartening, however. The fact that it is very difficult for the
reader to produce numerical predictions for a very complex
multi-particle system in a constantly varying electrical field simply
with nothing but an A4 sheet and their algebraic knowledge is nothing
other than to be expected. Feynman, Dirac, Heisenberg, Pauli were not
immortalised for only reaching the depth of an introductory book like
this one. The Schrödinger Equation is still always valid, even when it
is difficult for us to practically solve the actual complete solutions
of it.\
\
Before we start on that, however, there are two pragmatic clarifications
to be made, both of which are related to the explicit forms of operators
and how we use them in problem solving. These are, observable spaces and
formulation of the observable operators.

## More on Observable Operators

### Observable Spaces

When we refer to an , we do not mean a space we can observe. We mean the
state space when it is spanned by a physical observable. Precisely, that
means working with the state space where the underlying basis is an
eigenbasis of some observable operator.\
\
A large component of problem solving in quantum mechanics consists of
being able to apply two concepts related to bases:

1.  Staying flexible without committing to a specific base and
    considering the state vector without a basis first.

2.  Switching into a basis which is useful for our specific needs and
    algebraic manipulations.

It is clear, even from the very early section on orthonormality, that
not a bases are created equal. Some are simply better selected because
algebraic manipulation becomes a lot easier when a problem is considered
in those bases. Out of such bases, the eigenbases of physical
observables are the most significant. Thus we reach this definition of ,
which sounds strange but is simply translated to , , when we actually do
have a physical observable in mind. We understand that all these
observable spaces are not actually new vector spaces: they are all this
same state space we have been studying, but simply with different
eigenbases spanning the space and therefore where the same vectors will
take different expansions. Nevertheless, these terms of position space
and momentum space and so on are completely essential technical terms
when we refer to these ideas.\
\
All quantum mechanics problems are solved in the end in one of these
spaces. Rarely, we might solve one part of a problem in one observable
space and then switch bases (more in Chapter 6), after taking what we
have learnt from that part, to solve the rest of the problem. Most of
the time -- especially overwhelmingly in this book -- we work in
position space where possible. This is not only because it makes sense
to work with time and position as the two most important variables, as
in our physical reality, but also because there are important variables
to consider in the time evolution problem -- in particular the potential
$V(x)$, a function of position-- which are easier to express in the
position basis than any other. Momentum space is by far the other main
counterpart in quantum mechanics, and usually we might work in momentum
space in problems where the conditions or potential are easily expressed
in terms of the momentum. Only rarely will we see energy space in
action, and any other observable space will essentially be inferior to
position and momentum space because the observables of position and
momentum are far more important than any other.\
\
Now, there is an important conceptual detail to understand. Recall back
to when we first were introduced to hermitian operators; we proved that
each operator's action can be uniquely specified in its own eigenbasis
if we have its eigenvalues. Consider some vector $\Psi$ in a the state
space spanned by the eigenbasis $\setof{\omega_{i}}$ with eigenvalues
$\setof{\lambda_{i}}$ of an operator $\Omega$. We have, by the common
inner product expansion:
$$\Psi=\sum_{i=1}^{n}\oip{\omega_{i}}{\Psi}\omega_{i}.$$ Then the action
of the operator $\Omega$ is
$$\Omega \Psi = \Omega\sum_{i=1}^{n}\oip{\omega_{i}}{\Psi}\omega_{i}$$
which, as it is a linear operator,
$$\Omega\Psi=\sum_{i=1}^{n}\oip{\omega_{i}}{\Psi}\Omega\omega_{i}$$
which is, $$\sum_{i=1}^{n}\oip{\omega_{i}}{\Psi}\lambda_{i}\omega_{i}.$$
So quite simply, we get
$$\Omega \Psi = \sum_{i=1}^{n}\oip{\omega_{i}}{\Psi}\lambda_{i}\omega_{i}.$$
Of course, it is very clear that these eigenvalues $\lambda_{i}$ are not
obtained if we are not working in the space spanned by the eigenbasis of
$\Omega$. This in turn shows us the very important fact: that the action
of the operator-- not just the forms of the state vectors-- is different
if we are working in different spaces! It is important to know this
idea, that the formulation of observable operators we are to see in the
following section is based specifically in one space -- here, in the
common position space. The operator formulations would not look the same
were we in other observable spaces, such as momentum or energy space.

### Formulation of Observable Operators

We've studied the observable operators, their hermiticity and eigenbases
in good detail, but this has all been done theoretically. Of course,
there would be no point knowing about operators and eigenvalue equations
if we didn't actually know what action the operators performed
(remember, operators are functions with state vectors as inputs and
state vectors as outputs), because there would be nothing to solve and
no measurable eigenvalues to find. The next step in our work is
therefore to actually give form to the physical form operators we want
to work with. It turns out there is a very simple rule, presented in the
next postulate, that we can use to correctly define any operator we
need. We are certainly glad we do not have to run a massive set of
definitions again to answer this question, and so the section is duly
and appreciatedly short.

#### Formation of Observable Operators

**[Postulate 4: The Formation of Observable Operators]{.underline}**\
\
The two canonical operators in quantum mechanics, expressed in position
space, are the position operator: $$\hat{X}\Psi=x\Psi$$ and the momentum
operator: $$\hat{P}\Psi=-i\hbar\frac{\partial}{\partial x}\Psi.$$ which
can be both shown to be Hermitian. To form any other physical observable
operator, express the classical observable in terms of the classical
variables of $x$ (position) and $p$ (momentum), and replace the $x$
terms with the operator $\hat{X}$ and the $p$ terms with the operator
$\hat{P}$. Note that the position operator and momentum operator are
here one dimensional: if instead we were considering position and
momentum in three directions then all we would do would be to replace
the $x$ with the $y$ and $z$ variables for the $y$ and $z$ directional
operators instead. Generalising up physical dimensions (as in, position
dimensions) is only marginally more complicated because we have more
terms to consider, and otherwise this rationale stays the same and
everything is straightforward. Let us, to punch this in, consider the
kinetic energy operator, which will become very useful. Note again that
everything is happening in position space, or things would look quite
different in another space with a different eigenbasis.

#### Kinetic Energy Operator

The classical formula for kinetic energy is of course
$$KE=\frac{1}{2}mv^2.$$ We want this in terms of position and momentum.
It is important that mass is treated as a constant so does not interfere
in this as a separate observable. The kinetic energy formula expressed
in momentum and position is
$$KE=\frac{1}{2}mv^2=\biggl(\frac{m}{2m}\biggr)mv^2=\frac{m^2v^2}{2m}$$
which is, $$KE=\frac{p^2}{2m}$$ where position does not appear in this
particular observable expression, which is completely fine. Then, by the
postulate, all we need to do is to replace the classical variable $p$
with the momentum operator:
$$KE=\frac{p^2}{2m}\duac \hat{KE}=\frac{\hat{P}^2}{2m}.$$ The notation
$\hat{KE}$ looks foolish and so convention uses $\hat{T}$ instead. The
expression $\hat{P}^2$, we know, means applying the same momentum
operator twice.\
\
Therefore, in position space, where the momentum operator is
$$\hat{P}\Psi=-i\hbar\frac{\partial}{\partial x}\Psi,$$ we get
$$\hat{T}\Psi=\frac{\hat{P}^2}{2m}\Psi=-\frac{i\hbar}{2m}\biggl(\frac{\partial}{\partial x}\biggl(-i\hbar\frac{\partial\Psi}{\partial x}\biggr)\biggr)$$
which is,
$$\hat{T}{\Psi}=\frac{(i\hbar)^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}=-\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2}.$$
Thus we are done, and have the position space form of the kinetic
operator:
$$\hat{T}\Psi=-\frac{\hbar^2}{2m}\frac{\partial \Psi}{\partial x^2}.$$
There is a final note to make, on mass and time. Both of these are not
treated as observables in quantum mechanics. This makes intuitive sense
for time: in experiments we would measure the duration of an event, but
this is first of all not something which pertains to the state problem
but more importantly not something we expect to involve probability. The
time at which we are measuring the time obviously should not be
probabilistic; it is therefore treated more like an underlying variable
just like the space of the universe.\
\
With mass, the answer is not so clear. The best way to think about mass
operators at this stage-- and indeed the way that quantum mechanics
generally thinks of mass operators-- is to not think about mass
operators at all. They do not exist, for whatever reason, in
non-relativistic quantum mechanics, which always treats the mass of a
particle as constant until more mass is added by external sources to the
system. So we treat mass as a constant, and time as some universal
external parameter; neither time nor mass have an operator attached to
them.\
\
Finally, now that we have completed our survey into observable operators
fully, we can move onto the Time Evolution Problem and Schrödinger' s
Equation

## Time Evolution and Schrödinger's Equation

Now that we have established the stationary properties of quantum
states, observables and measurements, we are done with the quantum
mechanical state problem. The second paramount question of Physics is
the question of time evolution. One might be relieved to find that,
theoretically speaking, the time evolution problem is much simpler and
will not require us to do so much complex postulating as the state
problem did. In fact, we only need one more postulate to introduce time
evolution; this is the famous Schrödinger Equation (which is a
postulate, not a derivation!), which will be important to quantum
mechanics much similar to the way $F=ma$ is ubiquitous in classical
mechanics.

::: tcolorbox
[**Postulate 5: Schrödinger Equation and the Hamiltonian**]{.underline}\
\
In quantum mechanics, there exists the Hamiltonian operator, written
$\hat{H}$, which corresponds to the total energy of the system. It is
also hermitian, and it plays an integral role in the time-evolution
equation in quantum mechanics, the Schödinger Equation:
$$i\hbar\frac{\partial \Psi(t)}{\partial t}=\hat{H}\Psi(t)$$ which
determines how the wavefunction will evolve in time provided there are
no perturbations to the system.
:::

Note that we have moved from $\Psi_{t}$ to $\Psi(t)$ which is a better
shorthand notation now that we are not discussing stationary states.
This function notation doesn't clash with the fact that the state vector
is a state vector: it just means that the input is a time value and the
output is the state vector corresponding to the state at that time.\
\
Now, we once more start by listing the assertions of this postulate for
clarity.

1.  There is a total energy, regardless of the specific qualities of the
    potential, which is integral to quantum mechanics. Clearly it is a
    physical observable since it is represented by a hermitian operator,
    the Hamiltonian.

2.  The Hamiltonian operator is the operator form of the classical
    Hamiltonian- that is, the quantum mechanical version of
    $$H(x,p)=\frac{p^2}{2m}+V(x).$$ This, of course, contains the
    kinetic energy operator we have just found in 5.1.2; the other part
    of the Hamiltonian, the more tricky potential, will be dealt with
    subsequently as it does not change much of the conceptual discussion
    right now.

3.  Since we say that this Hamiltonian operator exists, there must be
    eigenvalues (also called eigenenergies for obvious reasons) which
    are the possible measured values of energy and corresponding
    eigenvectors of the Hamiltonian- or, energy eigenstates. In fact we
    often get that the eigenvalues are discretely distributed for the
    Hamiltonian operator: which means energy is quantised. Bohr's famous
    electron model results from this energy quantisation.

4.  Given a state vector at time $0$ it evolves in a completely
    deterministic way. This is surely a great relief. The state may not
    be deterministic-- in which case it is a mixed state for which the
    strongest predictive statements which can be made are those detailed
    in Postulate 3. However, it will evolve into a new state vector in a
    predictable way. That is not to say at all that after the evolution
    it will not still be in a mixed state, as the new state it has
    evolved over time into may well still be a superposition of
    eigenstates. It is just to say that we can determine future state
    vectors (not necessarily measurements) well given the starting one
    and the Hamiltonian for the given system.

For all quantum mechanics problems, solving the Schrödinger equation is
the most difficult part of the problem. The reason for this is that the
Hamiltonian operator is the only major operator which will change
depending on the conditions of the problem. The position operator,
momentum operator, spin operators all remain the same, but the
Hamiltonian is subject to great variation and even variation over time
if the potential of the system is varying over time. This means that for
different physical problems we always have to go through the
considerable difficulty of finding the form of the Hamiltonian given the
different conditions, and then solving the eigenvalue equation for that
Hamiltonian, which is rarely not incredibly difficult. With all that
said, this next section details why such painstaking effort is worth it:
with the energy eigenvalue, or Hamiltonian eigenvalue, equation solved,
Schrödinger's Equation is also immediately solved.

### Solving with Energy Eigenstates

This section will require a difficult mixing of the rules we have thus
far learnt and to be able to follow the developments we make will be
tantamount to truly consolidating our grasps on the postulates and
mathematics up to this point. It also gives many procedural insights
into how one should approach problems (not just subproblems, but full
problems) in quantum mechanics, by giving the most elementary way to
solve the Schrödinger equation. This method is through considering
**energy eigenstates**: that is, the eigenstates of the Hamiltonian
operator and the state vectors in the orthonormal basis they form which
spans the Hilbert space.\
\
To start recall that for any state vector in the state space and
orthonormal basis $\{\alpha_{i}\}$ the state vector can be expressed in
terms of how it acts on those eigenvectors:
$$\Psi_{t}=\sum_{i=1}^{k}\oip{\alpha_{i}}{\Psi_{t}}\alpha_{i}.$$ where
$k$ is the dimensionality of the space: in the state space, we would sum
to infinity. There are infinite orthornormal bases which can we can
choose to span the state space, but we have already seen that, for the
action of an operator on the state vector, considering that state vector
as a combination in the form above but with eigenvectors from the
eigenbasis of that operator is natural and fruitful because we get
simplifications involving eigenvalues, which also have clearer physical
meaning. Now the Schrödinger Equation clearly puts the Hamiltonian to
the forefront of our focus, and therefore we might like to consider the
state vector $\Psi$ when it is expressed in the energy eigenbasis. The
Schrödinger Equation states that
$$i\hbar\frac{\partial \Psi(t)}{\partial t}=\hat{H}\Psi(t).$$ If we take
the eigenbasis of the Hamiltonian to be $\{\varepsilon_{n}\}$ and the
corresponding energy eigenvalues to be $\{E_{n}\}$ then the state vector
can be expressed as
$$\Psi_{t}(x)=\sum_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\varepsilon_{n}$$
and the Schrödinger Equation now takes the form
$$i\hbar\frac{\partial}{\partial t}\sum_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\varepsilon_{n}=\hat{H}\sum_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\varepsilon_{n}.$$
Continue by using the linear distributivity of Hermitian operators (fact
H4). This tells us that the right hand side can be written
$$\hat{H}\sum_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\varepsilon_{n}=\sum_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\hat{H}\varepsilon_{n}=\sum_{n}E_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\varepsilon_{n}.$$
Then consider the time derivative of the quantities
$\oip{\varepsilon_{n}}{\Psi_{t}}$. The eigenvectors of the Hamiltonian
in the state space must be independent of time, presuming the
Hamiltonian itself isn't varying over time (cases with time-varying
Hamiltonians are far trickier to solve and thus will not be considered
in this book). Therefore, they have 0 time derivative, which means we
have
$$\frac{\partial}{\partial t}\oip{\varepsilon_{n}}{\Psi_{t}}=\oip{\varepsilon_{n}}{\frac{\partial}{\partial t}\Psi_{t}}.$$
One can be assured of this fact by explicitly writing out the summation
form of the inner product. Next, by rearrangement of Schrödinger's
Equation,
$$\frac{\partial}{\partial t}\Psi_{t}=-\frac{i}{\hbar}\hat{H}\Psi_{t}$$
so we can substitute this into the above expression:
$$\frac{\partial}{\partial t}\oip{\varepsilon_{n}}{\Psi_{t}}=\oip{\varepsilon_{n}}{-\frac{i}{\hbar}\hat{H}\Psi_{t}}=-\frac{i}{\hbar}\oip{\varepsilon_{n}}{\hat{H}\Psi_{t}}.$$
Then, substituting the energy eigenbasis expression of $\Psi_{t}$,
$$\begin{aligned}
\frac{\partial}{\partial t}\oip{\varepsilon_{n}}{\Psi_{t}}&=-\frac{i}{\hbar}\oip{\varepsilon_{n}}{\hat{H}\sum_{m}\oip{\varepsilon_{m}}{\Psi_{t}}\varepsilon_{m}} =-\frac{i}{\hbar}\oip{\hat{H}\varepsilon_{n}}{\sum_{m}\oip{\varepsilon_{m}}{\Psi_{t}}\varepsilon_{m}}\\
&=-\frac{i}{\hbar}\oip{E_{n}\varepsilon_{n}}{\sum_{m}\oip{\varepsilon_{m}}{\Psi_{t}}\varepsilon_{m}}
=-\frac{i}{\hbar}E^{\ast}_{n}\oip{\varepsilon_{n}}{\sum_{m}\oip{\varepsilon_{m}}{\Psi_{t}}\varepsilon_{m}}\\
&=-\frac{i}{\hbar}E_{n}\oip{\varepsilon_{n}}{\sum_{m}\oip{\varepsilon_{m}}{\Psi_{t}}\varepsilon_{m}}
\end{aligned}$$ where the fact that $\hat{H}$ is hermitian is used in
the algebraic manipulations. Then, as the inner product is linearly
distributive across the sum term, this becomes
$$\frac{\partial}{\partial t}\oip{\varepsilon_{n}}{\Psi_{t}}=-\frac{i}{\hbar}E_{n}\sum_{m}\oipbig{\varepsilon_{n}}{\oip{\varepsilon_{m}}{\Psi_{t}}\varepsilon_{m}}$$
and as the inner product $\oip{\varepsilon_{m}}{\Psi_{t}}$ is some
constant for fixed $m$ and t, we can pull it out to write the expression
as
$$\frac{\partial}{\partial t}\oip{\varepsilon_{n}}{\Psi_{t}}=-\frac{i}{\hbar}E_{n}\sum_{m}\oip{\varepsilon_{m}}{\Psi_{t}}\oip{\varepsilon_{n}}{\varepsilon_{m}}=-\frac{i}{\hbar}E_{n}\sum_{m}\oip{\varepsilon_{m}}{\Psi_{t}}\delta_{nm},$$
which is,
$$\frac{\partial}{\partial t}\oip{\varepsilon_{n}}{\Psi_{t}}=-\frac{i}{\hbar}E_{n}\oip{\varepsilon_{n}}{\Psi_{t}}$$
as the Kronecker delta resulting from the orthogonality of the
eigenvectors cancels out all other sum terms except for when the index
$m$ matches up with $n$. This is clearly equivalent to the differential
equation $$\frac{\partial y}{\partial t}=ky$$ which has general solution
$x=Ce^{kt}$ for some constant of integration $C$. One might consider
that the inner product is a constant and therefore not a traditional
function one might find in differential equations of this form, but we
recall that constants can be seen us functions of the form $f(x)=c$.
Substituting $x:=\oip{\varepsilon_{n}}{\Psi_{t}}$ and
$k:=-\frac{i}{\hbar}E_{n}$ analogously leaves us with the solution
$$\oip{\varepsilon_{n}}{\Psi_{t}}=Ce^{-\frac{iE_{n}t}{\hbar}}.$$ The
final step is to realise the constant $C$ is not random: at $t=0$ we
should have $\oip{\varepsilon_{n}}{\Psi_{0}}=C$, which implies that the
constant is $C=\oip{\varepsilon_{n}}{\Psi_{0}}$. Thus we conclude that
the rule for time-evolution is
$$\oip{\varepsilon_{n}}{\Psi_{t}}=\oip{\varepsilon_{n}}{\Psi_{0}}e^{-\frac{iE_{n}t}{\hbar}} \:\:\:\:\square$$\
Many consequences for the solution of Schrödinger's Equation derive
themselves promptly. We list them in the taxonomical format again.\

1.  We first note what the fact above actually means. By the rule S8,
    the term $\oip{\varepsilon_{n}}{\Psi_{t}}$ is the component of
    $\Psi_{t}$ in the eigenbasis $\{\varepsilon_{i}\}$ corresponding to
    eigenvector $\varepsilon_{n}$:
    $$\Psi_{t}=\sum_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\varepsilon_{n}.$$
    The eigenvector $\varepsilon_{n}$ itself does not evolve with time.
    Therefore, by determining how the component
    $\oip{\varepsilon_{n}}{\Psi_{t}}$ evolves with time, we get:
    $$\Psi_{t}=\sum_{n}\oip{\varepsilon_{n}}{\Psi_{t}}\varepsilon_{n}=\sum_{n}\oip{\varepsilon_{n}}{\Psi_{0}}e^{-\frac{iE_{n}t}{\hbar}}\varepsilon_{n}.$$
    We cannot fall for the common deception of thinking we can pull out
    the term $e^{-{iE_{n}t}/{\hbar}}$ from the sum, since the
    eigenvalues $\setof{E_{n}}$ corresponding to the eigenvectors
    $\setof{\varepsilon_{n}}$ change for each $n$ so it is not a
    constant. However, we do know now that, if we can determine the
    eigenvectors of the Hamiltonian for a given system, and the
    corresponding eigenvalues, and know the initial state (and therefore
    the components $\oip{\varepsilon_{n}}{\Psi_{0}}$ of the initial
    state vector) then we have a fully defined state $\Psi_{t}$ for any
    $t$ as we can track how each of its components evolve very easily.
    This amounts, of course, to solving the Schrödinger Equation: or,
    more satisfyingly put, solving the problem of time evolution and
    solving both the central problems of quantum mechanics.

2.  An important clarification which has been alluded to but not
    explicitly stated thus far must now be emphasised. There is no
    physical operator which changes form over time. Most operators, like
    the position and momentum operators, do not change even if there is
    a perturbation to the system. However, the Hamiltonian is not the
    same for all systems. Like all other observables operators, its
    formulation does not change- but, unlike most other operators, this
    formulation consists of something which can vary through
    perturbations. Specifically, the Hamiltonian is expressed as
    $$\hat{H}=\frac{\hbar^{2}}{2m}\frac{\partial^2}{\partial x^2}+V(x)$$
    where $x$ here is the position variable and the function $V(x)$ is
    the potential of the system. It is the potential which changes the
    form of the operator, as different systems have different
    potentials; moreover, these potentials can shift over time so in
    that way the form of the Hamiltonian changes over time. Note the
    difference: the formula to construct the Hamiltonian doesn't change,
    but the Hamiltonian itself does-- when $V(x)$ changes.\
    \
    The role of energy eigenbases as the easiest way to solve the
    Schrödinger Equation is now however fully clear to us. For a given
    system, if we can formulate the Hamiltonian accurately, then we can
    find its eigenvalues and corresponding eigenvectors using the
    characteristic equation, and then by HE1 we can theoretically
    determine the answer to the time evolution problem for the state
    with that Hamiltonian. This is why almost invariably, for problems
    which are not immensely complicated, **the goal of the Physicist is
    to formulate the Hamiltonian**.

3.  Since we have established that formulating the Hamiltonian is
    crucial to the solution of all non-advanced quantum mechanical
    problems, we see that the secondary result is that the potential
    energy is often what makes (or, for advanced problems of truly
    complex systems, breaks) this energy eigenstate method of solving
    Schrödinger's Equation. As the potential almost invariably is far
    more complicated than the kinetic energy operator which forms the
    other term in the sum which makes the Hamiltonian, we will see a
    host of illustrative problems where the potential is bounded by
    constraints (eg, the infinite potential well or the free particle
    question) in all introductory textbooks. The underlying idea, which
    we now understand despite the fact that often textbooks do not
    enunciate it, is that in these problems the potential is simple and
    therefore the Hamiltonian is simple, making a solution possible
    without advanced measures like perturbation theory and methods of
    approximation, which have to be used for complex or time-evolving
    potentials. Once we have the formulation of the Hamiltonian, our
    work is to solve its eigenvalue equation so we can obtain the
    eigenvectors: $$\hat{H}\varepsilon_{n}=E_{n}\varepsilon_{n},$$ and
    after that we have a solution as shown above. The energy eigenvalue
    equation is often in literature referred to, misleadingly, as the
    time-independent Schrödinger Equation, because it consists of time
    independent eigenvectors. One should never be confused by this term,
    however, as it is nothing more than the energy eigenvalue problem;
    certainly, it is nothing of a postulate that such an equation would
    exist given any operator, including the Hamiltonian.

4.  Back to the mathematics, we note that there are other observables
    whose operators have the same eigenbasis as the eigenbasis of the
    Hamiltonian-- by the Compatibility Theorem, this occurs when the two
    observable operators commute. In those cases we should convince
    themselves that we have this analogous time-evolution rule for the
    components of the state vector in the eigenbasis of that observable
    compatible to the Hamiltonian energy observable. This is because the
    above is really an exercise in understanding how the energy
    eigenvectors evolve in time, and compatible operators have the same
    eigenvectors.

5.  By Postulate 3, the value $|\oip{\varepsilon_{n}}{\Psi_{t}}|^2$ is
    the probability energy value $E_{n}$ is measured to be the value of
    energy for the system at time $t$. In computing this amplitude we
    achieve very interesting results: $$\begin{aligned}
        |\oip{\varepsilon_{n}}{\Psi_{t}}|^2 &=  |\oip{\varepsilon_{n}}{\Psi_{0}}e^{-\frac{iE_{n}t}{\hbar}}|^2\\
        &=|\oip{\varepsilon_{n}}{\Psi_{0}}|^2e^{-\frac{iE_{n}t}{\hbar}}e^{\frac{iE_{n}t}{\hbar}}\\
        &=|\oip{\varepsilon_{n}}{\Psi_{0}}|^2\times 1\\
        &=|\oip{\varepsilon_{n}}{\Psi_{0}}|^2
        \end{aligned}$$ In other words, the probability of measuring the
    energy $E_{n}$ at time $t$, represented by
    $|\oip{\varepsilon_{n}}{\Psi_{t}}|^2$, is the exact same as the
    probability of measuring that energy at time 0, which is
    $|\oip{\varepsilon_{n}}{\Psi_{0}}|^2$. In another sense this means
    that, unless there is some perturbation to our system, there is no
    change in the probability of a certain energy value being measured;
    this rule of time evolution essentially amounts to the energy
    conservation law for a closed unperturbed system as whatever energy
    we measure it to have at time 0 stays the same for all time $t$.\
    \
    This is not the last of this important result! We once more see that
    the above holds for any observables with the eigenbasis
    $\{\varepsilon_{i}\}$ which is the same as the energy eigenbasis, as
    the energy values themselves cancel out, leaving the component
    amplitudes purely in terms of the eigenvectors. This in fact means
    that for other observables compatible with the energy- for other
    observables whose operators commute with the Hamiltonian-- the
    probability of making a measurement of the eigenvalue corresponding
    to a certain eigenvector is also constant over time. This is
    significant, as we have just proven the quantum mechanical
    requirement for some observable to be a **constant of motion**.

6.  Consider the case when the state vector is in a pure energy
    eigenstate- when $$\Psi_{t}=\varepsilon_{k}$$ for some $k$. Then the
    probabilities of measuring the eigenvalues $E_{n}$ are
    $$|\oip{\varepsilon_{n}}{\Psi_{t}}|^{2}=|\oip{\varepsilon_{n}}{\varepsilon_{k}}|^{2}=\delta_{nk},$$
    which means that the probability of measuring the energy $E_{k}$ is
    1 and the probability of measuring all other energies $E_{n\neq k}$
    is 0. This is the deterministic energy pure state, whose relevance
    is clear due to the heavy discussion following Postulate 3 on
    measurement and quantum states. Yet there is more to be said:
    $$\oip{\varepsilon_{n}}{\Psi_{t}}=\oip{\varepsilon_{n}}{\Psi_{0}}e^{-{iE_{n}t}/{\hbar}}$$
    so the state vector would be
    $$\Psi_{t}=\sum_{n}\oip{\varepsilon_{n}}{\varepsilon_{k}}e^{-{iE_{n}t}/{\hbar}}\varepsilon_{n}=\sum_{n}\delta_{nk}e^{-{iE_{n}t}/{\hbar}}\varepsilon_{n}=e^{-{iE_{k}t}/{\hbar}}\varepsilon_{k}.$$
    However, this is the same as the system at time $0$ because the
    exponential has modulus 1 and therefore does not change the
    eigenvector in the Hilbert space from the ray $\varepsilon_{k}$
    which represents the initial state. Thus the whole system does not
    change at all if it starts in a pure energy eigenstate; therefore,
    all observables remain constant under time evolution so long as the
    Hamiltonian remains the same.\
    \
    The consequence of this is that we can define the vectors:
    $$\forall n\in\mathbb{Z}^+,\:\:\:\:\Psi_{t}^{(n)}:=e^{-iE_{n}t/\hbar}\varepsilon_{n}.$$
    and these vectors $\Psi_{t}^{(n)}$ are the deterministic forms of
    the state vector if at initial state for $t=0$ the state vector is
    coincident with the eigenvector $\varepsilon_{n}$. We call these
    **stationary states**, which belong to the specific system, as their
    value is contingent on the eigenbasis of the Hamiltonian which
    describes the system. Now, if at time 0 the system is in a pure
    energy eigenstate $\varepsilon_{n}$, then:
    $$\Psi_{t}=\Psi_{t}^{(n)}.$$ Otherwise, if it is in a mixed state at
    time 0, then
    $$\Psi_{t}(x)=\sum_{n}e^{-iE_{n}t/\hbar}\oip{\varepsilon_{n}}{\Psi_{0}}\varepsilon_{n}$$
    by HE1, which can then be written as
    $$\Psi_{t}=\sum_{n}\oip{\varepsilon_{n}}{\Psi_{0}}\Psi_{t}^{(n)}$$
    since $\Psi_{0}^{(n)}$ (the stationary state at time $0$) is the
    initial pure state corresponding to stationary state $n$, which is
    the eigenvector $\varepsilon_{n}$. This gives us a physically
    meaningful method of describing the solution to the Schrödinger
    Equation: finding its stationary states along with knowledge of the
    initial state is sufficient to solve the Schrödinger Equation.\
    \
    Note that the solution now does not give us a deterministic state if
    the initial state was not a pure state; we get a mixed state in
    terms of the stationary states. Thus we might be confused as to how
    it amounts to a solution: but we recall that a fully defined mixed
    state is most of the time tantamount to achieving the highest level
    of understanding physically possible, by the measurement
    postulates-- so it does count as a solution since it represents the
    precise superposition of possible states we get in reality. Finally,
    the solution of finding the stationary states is absolutely the same
    as the solution detailed in HE2 and HE3-- we've just labelled
    vectors to be stationary states, but the underlying procedure is
    still simple. This is:

    1.  Formulate the Hamiltonian for the system

    2.  Solve the time-independent Schrödinger, or energy eigenvalue
        equation.

    3.  Formulate the state vector as a function of time and the initial
        state as shown above.

### Free Particle

The first problem we can easily solve is the solution of the time
evolution of a free particle. A free particle is a particle in a zero
potential: so $V(x)=0$. We begin by listing out our procedure:

1.  List the boundary conditions.

2.  Formulate the Hamiltonian and solve its eigenvalue equation.

3.  Use the eigenvectors and their eigenvalues to formulate the
    stationary states and therefore the state vector.

An important thing to note is that this procedure only applies for
systems where the Hamiltonian remains constant. This occurs if and only
if the potential of the system does not vary with time-- we recall that
the Hamiltonian consists of the kinetic energy operator and therefore is
not affected by the kinetic energy of the particle changing! The energy
of the state will be affected, but the operator representing all
possible energy states will not because the kinetic energy operator is
constant. For the questions in these chapters, as well as for most
introductory quantum mechanical problems, time-varying potentials will
not be considered, as they are extremely complex and do not have any
place in the rudimentary foundations of quantum mechanics.\
\
Let us now solve this simplest problem in quantum mechanics with this
procedure.

#### List the Boundary Conditions {#list-the-boundary-conditions .unnumbered}

The of a problem are simply all the conditions the problem sets up for a
solution. Listing them at this stage can be very useful because there
are many times, for example when evaluating integrals or probabilities,
that the boundary conditions can provide insights to shortcuts where
there seem like there are too many obstacles to a solution. For now,
though, this as a separate step will not be vindicated considering there
is one boundary condition specified here only.

1.  The potential energy is $0$.

#### Formulate the Hamiltonian {#formulate-the-hamiltonian .unnumbered}

This is also quite easy, as we do not have to consider the potential.
$$\hat{H}:=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x), \stab V(x)=0 \Rightarrow \hat{H}=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}$$
Solving the eigenvalue equation will take more work since this is the
first time we have done it for such a complicated problem. We want to
find eigenstates and eigenvalues which satisfy the eigenvalue equation
$$\hat{H}\varepsilon_{n}=E_{n}\varepsilon_{n}$$ for real $E_{n}$. This
equation is, as aforementioned, also known as the time-independent
Schrödinger Equation in literature. We can solve it for the free
particle relatively easily. The Hamiltonian is
$$\hat{H}\Psi(x)=\frac{\hat{P}^2}{2m}\Psi(x)$$ and so the eigenvalue
equation (time-independent Schrödinger) is to find eigenvectors
$\setof{\varepsilon_{n}}$ which satisfy:
$$\frac{\hat{P}^2}{2m}\varepsilon_{n}=E_{n}\varepsilon_{n}$$ for some
real constant eigenvalues $E_{n}$. The crucial insight for this
eigenvalue equation is that the Hamiltonian operator of the system
commutes with the momentum operator! This is intuitively obvious, since
the Hamiltonian operator is the momentum operator squared divided by a
constant, and the momentum operator is just the momentum operator, so
the commutator $$\left[\frac{\hat{P}^2}{2m},\hat{P}\right]$$ consists of
only the operator $\hat{P}$, somewhat modified on one side. Constants
clearly do not affect commutators and operators commute with themselves,
so we would expect the commutator to be $0$. It can be verified by the
reader as well, if we put in $\hat{P}=-i\hbar\nd{}{x}$, but this is not
greatly necessary.\
\
From our vigilance, however, in checking the commutation relation
between the Hamiltonian and momentum operators (over time, one gains an
intuitive feeling for this vigilance) we achieve something much greater.
As their operators commute, energy and position are compatible
observables. And as they are compatible observables, they must possess a
common eigenbasis! Therefore, to any energy eigenvector
$\varepsilon_{n}$ there also exists a momentum eigenvector $\phi_{n}$
which is the same function! Let us therefore try to put that in instead,
with this information. For all energy eigenvectors $\varepsilon_{n}$
such that
$$\hat{H}\varepsilon_{n}=\frac{\hat{P}^2}{2m}\varepsilon_{n}=E_{n}\varepsilon_{n},$$
there must exist a momentum eigenvector such that
$$\phi_{n}\equiv\varepsilon_{n}\implies \frac{\hat{P}^2}{2m}\phi_{n}=E_{n}\phi_{n}.$$
Now, if the eigenvalue of momentum corresponding to the eigenvector
$\phi_{n}$ is $P_{n}$, then the eigenvalue corresponding to $\hat{P}^2$
on $\phi_{n}$ is $P_{n}^{2}$. So the above can be written
$$\begin{aligned}
\frac{\hat{P}^2}{2m}\phi_{n}=E_{n}\phi_{n}\iff\frac{P_{n}^{2}}{2m}\phi_{n}=E_{n}\phi_{n}.
\end{aligned}$$ The eigenfunction $\phi_{n}$ is clearly not the null
vector, and therefore the above implies that the $n$'th eigenmomenta and
eigenenergies are related by:
$$\frac{P_{n}^{2}}{2m}=E_{n}\implies P_{n}=\pm\sqrt{2mE}.$$ We can now
try to find the free particle wavefunction. Replacing the momentum
operator with its algebraic formulation (in position space, as we have
been working thus far), we have
$$-{\frac{\hbar^2}{2m}}\frac{d^2\Psi}{dx^2} = E\Psi \Rightarrow\:\: \frac{d^2\Psi}{dx^2} =-{\frac{2mE}{h^2}}\Psi.$$
We could also express this as
$$\frac{d^2\Psi}{dx^2} =-{\frac{p^2}{h^2}}\Psi$$ since we know that for
the free particle $E=p^2/2m$ as just shown. We have already seen that
momentum has extra importance in the free particle problem as it is
compatible with energy (though that is not to say this is the only such
question where this may be true); therefore, the momentum eigenstates
are also the energy eigenstates, which we know are very important due to
their intimate relationship with time evolution. It is also very clear
that the free particle problem is a fundamental conceptual problem. De
Broglie therefore defined a relationship
$$k=p/\hbar \implies p = \hbar k$$ (where the latter form is far more
commonly seen) for a constant $k$ which we will now plug into the
equation we have above:
$$\frac{d^2\Psi}{dx^2} =-{\frac{p^2}{h^2}}\Psi, \stab p=\hbar k \implies \frac{d^2\Psi}{dx^2} =-k^2\Psi.$$
The physical meaning of the constant $k$ is somewhat tangential for this
discussion, though it must be remarked that the De Broglie relations
concern all the important aspects of a classical wave and are not simply
random definitions. Nevertheless, for our purposes working with $k$
instead of $p/\hbar$ will be cleaner for the algebra to follow. A reader
should clearly see that the equation we have just reached is perfectly
analogous to the rudimentary differential equation
$$\frac{d^2y}{dx^2}=-k^2y.$$ Which has the general solution
$$y=Ae^{-ikx}+Be^{ikx}:=\Psi.$$ This is therefore the general solution
to the free particle wavefunction where constants $A$ and $B$ are to be
determined based on further boundary conditions of the physical problem!
It looks generic, but when we do set bounds: whether these be positional
bounds or any other bounds, we will see that we can suddenly get quite
interesting and specific forms for the wavefunction. Such is for example
shown in part 8.2, where we see the free particle confined to an ellipse
and get a very clear reult.

## A Holistic Summary

The meaning of these last three chapters has always been to provide a
robust defence against the many conceptual pitfalls which one can fall
into if they try to educate themselves on quantum mechanics purely
mathematically without grasping the underlying ideas fully. Certainly,
the rest of the book will be far more dense mathematically- though
effort will still be made to be extremely clear with that discourse. It
is therefore paramount, given that I have offered such a verbose
discourse on the relationship between quantum mechanics and physical
reality, to summarise everything we have learnt in a concise way; by
revising this section, the reader should be able to answer all the
physical questions they have about quantum mechanics.\
\
The problem of a physical model consists of two components, the state
problem and the time-evolution problem. The state problem consists of
two main problems: the first, how we represent physical information; the
second, how we extract physical information.\
\
**[The representation of physical information]{.underline}**

-   The representation of physical information is carried out by the
    state vector and its wavefunctions in quantum mechanics. It is
    represented by a normed Hilbert space vector; all scalar multiples
    are the same ray so represent the same state.

-   In the book we have referred to the state vector at times as , which
    is somewhat of a shorthand and can be confusing. What really is true
    is that the state vector is given meaning by the relation
    $$P(\alpha_{i})=|\oip{\alpha_{i}}{\Psi}|^{2}$$ for any arbitrary
    eigenstate $\alpha_{i}$, which means we can convert it to
    wavefunctions which are probability distribution functions.
    Subsequently, the wavefunction does store information because it is
    defined by its components, which must correspond to specific
    eigenvectors and therefore are probability amplitudes. As every
    arbitrary state vector must have a unique expansion in every basis
    spanning the space, every state vector therefore inherently can be
    converted to its expression in any space, and therefore every state
    vector possesses components in observable eigenspaces- which are,
    probability amplitudes of measurements with respect to those
    physical observables whose eigenspace it is in. That is how a state
    vector encapsulates information.

-   Physical observables are represented by hermitian operators, which
    do not change over time. The distinct eigenvectors of these
    observable operators and the corresponding eigenvalues are also
    therefore unchanging over time. The Hamiltonian is an exception, but
    not because its formulation changes over time, but because its form
    changes over time as the potential $V(x)$ may change over time.

-   The vector space expressed as being spanned by an observable's
    eigenbasis is called its eigenspace. It is especially useful when
    considering measurements of that observable, since the components of
    the state vector in that eigenbasis are the probability amplitudes
    corresponding to measurements of the observable.

## Exercises from Chapter 5$\ast$

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
