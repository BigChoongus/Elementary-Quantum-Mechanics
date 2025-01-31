---
layout: default
title: Chapter 4
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


# State Space Operators and the Quantum Observables Problem

The previous chapter introduced the concept of Hilbert space vectors,
called state vectors, representing physical states. The state space,
like any infinite-dimensional vector space, has infinite bases, and this
was claimed to be a motivating factor for the Hilbert space formulation
in the first place: because it allows for the state represented by the
state vector to be looked at from the perspective of different
observables like momentum and position. To complete our understanding of
how the state problem is approached in quantum mechanics we need to
understand exactly how observables are incorporated into this linear
algebraic vector space system, through very specific bases. This
question will be answered by an investigation into **linear operators**.

## Hilbert Space Operators

An operator is a function, but it is the lexicon used to describe a sort
of function which acts on functions or vectors as inputs-- here, in the
state space, on state vectors. For a new student of quantum mechanics it
is paramount to understand that the distinction between an operator and
a function does not exist. The only reason the term operator is used in
conjunction with vector spaces is to avoid exhausting the term function,
since operators act on state vectors which are themselves linked already
to wavefunctions. Since it is a term one is not likely to have seen
anywhere other than quantum mechanics before, there is a harmful
tendency to give a mystic image to operators, but this must not be done.
An operator, just like a function, takes an input and maps it to an
output, and that is the extent of it. One operator the reader will have
seen already is the differential operator: $$\frac{d}{dx}f(x)=f'(x).$$
This takes some input function $f(x)$, and maps it to an output function
$f'(x)$. In that sense, it is a function because it has an input and
output, but it is an operator because it acts on functions. If the input
was $f(x)=x^2$ then the output of the differential operator would be
$2x$; if it were $e^x$ then its output would also be $e^x$. A scalar can
also be an input of the operator: since an operator is a function of
functions, we could just define the input function to be $f(x):=k$ for
that scalar $k$, and of course this would still be a function whilst
sharing no differences to the scalar. Here, if such a scalar was an
input of the differential operator, than the output would be the null
function: or, 0, but for other operators, this may be different.\
\
If this is understood, the technical requirement for an operator which
is linear, here donated by $\Omega$, is that they are linear maps:
$$\Omega: \mathscr{H} \mapsto \mathscr{H},\:\:\:\: \Omega(\Psi_{1}+\Psi_{2})\equiv \Omega\Psi_{1}+\Omega\Psi_{2}.$$
There do exist non-linear operators, but in this book, and much of
quantum mechanics, we will only ever encounter linear operators, and so
we can take the latter linear distributive property to be a given for
our work. We also have:

-   Associativity of scalar multiplication:
    $$(c\Omega)\Psi=c(\Omega\Psi).$$

-   Distributivity:
    $$(\Omega_{1}+\Omega_{2})\Psi=\Omega_{1}\Psi + \Omega_{2}\Psi.$$

-   Associativity in operators:
    $$\Omega_{1}(\Omega_{2}\Psi)=\Omega_{1}\Omega_{2}\Psi$$

We do not, however have commutativity:
$$\Omega_{1}\Omega_{2}\Psi\neq\Omega_{2}\Omega_{1}\Psi$$ for most pairs
of operators $\Omega_{1}$ and $\Omega_{2}$ (some do commute by chance
rather than definition). Moreover, the order of the operators often
specifies completely unrelated results, unlike with inner products,
where one order is the complex conjugate of the other. The rest of the
operator facts again should, like the rules of vector spaces, come
mostly naturally. A useful point to remember is that for any operator we
work with in quantum mechanics, it maps from the state space
$\mathscr{H}$ to the state space $\mathscr{H}$: in other words,
performing that operator on any input state space vector will directly
create a new state space vector! Thus $$\Omega\Psi$$ is a new state
space vector, and so is
$$\Omega_{1}\Omega_{2}\Psi=\Omega_{1}(\Omega_{2}\Psi)$$ which is, the
action of $\Omega_{1}$ on the state space vector $\Omega_{2}\Psi$
obtained after operating with $\Omega_{2}$ on an original state vector
$\Psi$. We have a tendency, which is natural, to be suspicious when some
arbitrary function acts on an immensely complex input vector. However,
in the rules of quantum mechanics where linear operators dominate, we do
not need this suspicion. Fluency should soon dictate that we see
$\Omega\Psi$ as just another state space vector.\
\
Now, the much more important qualities of operators in quantum mechanics
are that they possess quantities called eigenvalues and eigenvectors,
which is where the quantum mechanical formalism will really start to
come together.

### Eigenvalues and Eigenvectors

We have just studied operators, which are fundamentally crucial to all
quantum mechanics, but of the moment seem to have fuzzy physical
interpretations. The other side of the same coin is **eigenvalues**.
Flip to the middle chapter of any quantum mechanics text and you might
find a large mixture of words with the prefix "eigen-\": eigenvector,
eigenfunction, eigenvalue, eigenvector, eigenenergy, eigenstate,
eigenmomentum- et cetera. After understanding eigenvalues this becomes
either natural or self-consciously amusing; before this, however, it is
horrifying. The study of eigenvalues must be treated with utmost
respect, but after we are done we are in a very good place indeed.\
\
Consider a three dimensional example first. We will pick a random
vector, which in this case can be a column vector, $$V=\begin{pmatrix}
\frac{47}{10}\\
\pi\\
5.06\\
\end{pmatrix}$$ and a random operator, $$\Omega \begin{pmatrix}
x_{1}\\
x_{2}\\
x_{3}\\
\end{pmatrix}=\frac{1}{2}\begin{pmatrix}
x_{2}\\
x_{3}\\
x_{1}\\
\end{pmatrix}$$ Upon applying this operator to the vector $V$, we are
likely not going to get an output vector which is anything like the
original vector in terms of how corresponding components are related.\
\
We are however given the grace from mathematics of sets of functions,
belonging to specific operators, which behave much more stably. To each
operator $\Omega$ there exists a set of vectors, called
**eigenvectors**, such that: $$\Omega\omega = \lambda\omega$$ for some
constant $\lambda$ and vector $\omega$. In the above equation, which we
call an eigenvalue equation, $\omega$ is an eigenvector of $\Omega$, and
$\lambda$ is the corresponding eigenvalue: a complex constant. This
equation corresponds to the operator $\Omega$ scaling the eigenvector
$\omega$ by a scale factor $\lambda$: a relatively very trivial
transformation compared to the nontrivial possibilities, as
aforementioned, which occur far more easily for large-dimension spaces
with nontrivial operators $\Omega$. In the above example we just saw,
for example, no such simple scaling exists at all even though the
components have not been dramatically altered and only switched around!\
\
Let us consider a basic operator and try to solve for all possible
eigenvectors and eigenvalues. We could use the identity operator, which
is extremely trivial: $$I\epsilon = \epsilon$$ means that any vector
$\epsilon$ is an eigenvector of the identity operator, with
corresponding eigenvalue $1$. It is a rather uninteresting result, which
pertains to a uniquely simple vector. This eigenvalue equation was not
particularly difficult, but for more complicated operators, it is still
clear that this case analysis inspection might not be such an easy and
useful method of solving the eigenvalue problem every time. The more
advanced methods of solving eigenvalue problems will come later in this
book; for now, only the theory is important.\
\
A final note on the above: the prefix eigen-, which is derived from
German and means (hence, each operator has its set of eigenvectors), is
always used in mathematics when we are dealing with the above cases. We
therefore have eigenvalues, eigenvectors, eigenfunctions: but also,
later on, eigenenergies, eigenmomenta, and so on, when the eigenvalues
are energy and momentum values respectively. The context and this
explicit note should demystify such eigen- words in the future.

### Hermitian Operators

The next important definition central to quantum mechanics is of
**Hermitian** operators. Operators are Hermitian if they possess the
property: $$\oip{\alpha}{\Omega\beta}=\oip{\Omega\alpha}{\beta}.$$ for
any vectors $\alpha,\beta$. There are some consequent facts for
hermitian operators following this definition.

1.  Hermitian operators must have real eigenvalues.\
    \
    [Proof:]{.underline}\
    \
    For a hermitian operator the eigenvalue condition is the same
    $$\Omega \omega= \lambda \omega.$$ We have, in taking the inner
    product with the eigenvector $\omega$:
    $$\oip{\omega}{\Omega\omega}=\oip{\Omega\omega}{\omega}$$ by the
    definition of Hermiticity, so $$\begin{aligned}
        \oip{\omega}{\lambda\omega}=\oip{\lambda\omega}{\omega} &\Rightarrow\:\: \lambda\oip{\omega}{\omega} = \lambda^{\ast}\oip{\omega}{\omega}\\
        \Rightarrow\:\: \lambda = \lambda^{\ast} &\Rightarrow \:\: \lambda \in \mathbb{R} \btab \square
        \end{aligned}$$

2.  Eigenvectors $\omega_{1}$ and $\omega_{2}$ of the same hermitian
    operator corresponding to different eigenvalues are orthogonal to
    each other.\
    \
    [Proof:]{.underline}\
    \
    To prove that $\omega_{1}$ and $\omega_{2}$ are orthogonal we need
    to prove that $\oip{\omega_{1}}{\omega_{2}}=0$. We can do this by
    manipulating the hermitian property of the operator, here denoted
    $\Omega$. $$\begin{aligned}
        \oip{\omega_{1}}{\Omega\omega_{2}}&=\oip{\Omega\omega_{1}}{\omega_{2}}\\
        \Rightarrow\:\: \oip{\omega_{1}}{\lambda_{2}\omega_{2}}&=\oip{\lambda_{1}\omega_{1}}{\omega_{2}}\\
        \Rightarrow\:\: \lambda_{2}\oip{\omega_{1}}{\omega_{2}}&=\lambda_{1}^{\ast}\oip{\omega_{1}}{\omega_{2}}\\
        \end{aligned}$$ but $\lambda_{1}$ is an eigenvalue of a
    hermitian operator so it is real: i.e,
    $\lambda_{1}^{\ast}=\lambda_{1}$. So above we had $$\begin{aligned}
        \lambda_{2}\oip{\omega_{1}}{\omega_{2}}&=\lambda_{1}^{\ast}\oip{\omega_{1}}{\omega_{2}}\\
        \end{aligned}$$ which is,
    $$\lambda_{2}\oip{\omega_{1}}{\omega_{2}}=\lambda_{1}\oip{\omega_{1}}{\omega_{2}}.\\
    $$ Therefore, if the eigenvectors do not have the same eigenvalue
    then $\lambda_{2}\neq\lambda_{1}$ so the above implies that
    $\oip{\omega_{1}}{\omega_{2}}=0$ and so these eigenvectors must be
    orthogonal. $\btab\btab\square$\
    \
    There is a note for the above proof, however. The proof works on the
    assumption that for different eigenvectors their eigenvalues are
    also different. This is not always a correct assumption. Consider
    the identity operator $I$. It is clearly hermitian:
    $$\oip{\Psi_{1}}{I\Psi_{2}}=\oip{\Psi_{1}}{\Psi_{2}}=\oip{I\Psi_{1}}{\Psi_{2}}.$$
    However, it has infinite different eigenvectors but they all have
    the same eigenvalue: 1. Thus the proof above cannot apply to the
    identity operator. In this case, the collapse of the point should be
    obvious anyway-- all vectors are eigenvectors of the identity
    operator, but certainly not all vectors are orthogonal to each
    other. In general, an operator where different eigenvectors can
    share the same eigenvalue is said to be **degenerate**. In
    particular, we say particular eigenvalues are degenerate if they can
    correspond to multiple different eigenvectors-- but we do not say
    eigenvectors are degenerate because an eigenvector can never
    correspond to multiple different eigenvalues.\
    \
    There are a few proofs of theorems in this book which involve the
    assumption that we are working with non-degenerate operators. These
    proofs, when we incorporate degeneracy, are usually different -- and
    unfortunately, more difficult. For every step where we assume
    non-degeneracy, it would still be within the reaches of this book to
    prove an alternative proof in the case of degeneracy, but at the
    same time these would take labour and space. Therefore, I will not
    include them in this book because they will not alter anything in
    the fundamental understanding of a reader. Should the reader want to
    find such proofs, they may turn to a more advanced textbook which
    has the space and desire to cover this technicality. It should not
    make a massive difference either way whether the reader is aware of
    the degenerate case proof, so long as they understand when
    degeneracy makes a difference to actual consequent theorem or result
    (and indeed when it does not, which is quite common here). I will
    highlight these cases at when they occur.

3.  For an operator $\Omega$ with real eigenvalues $\lambda_{i}$ and
    eigenvectors $\alpha_{i}$, if the eigenvectors constitute an
    orthonormal basis in the Hilbert space then the operator is
    hermitian.\
    \
    [Proof:]{.underline}\
    \
    Take the component expressions for the two arbitrary vectors
    $\Psi_{1}$ and $\Psi_{2}$. We know they can be both expressed as a
    linear combination of the eigenvectors $\alpha_{i}$ since the set
    $\{\alpha_{i}\}$ is stated in the conditions to be an orthonormal
    basis. So we have:
    $$\Psi_{1}=\sum_{\{i\}}c_{i}\alpha_{i},\:\:\Psi_{2}=\sum_{\{j\}}\gamma_{j}\alpha_{j}$$
    where the components $c_{i}$ and $\gamma_{j}$ are found by
    $(\alpha_{i},\Psi_{1})$ and $\oip{\alpha_{j}}{\Psi_{2}}$
    respectively. Then $$\begin{aligned}
        (\Omega\Psi_{1},\Psi_{2})&=\left(\Omega\sum_{\{i\}}c_{i}\alpha_{i},\sum_{\{j\}}\gamma_{j}\alpha_{j}\right)\\
        &=\left(\sum_{\{i\}}c_{i}\Omega\alpha_{i},\sum_{\{j\}}\gamma_{j}\alpha_{j}\right)
        \end{aligned}$$ where the operator can be incorporated into the
    sum term as it is a linear operator. Then this becomes
    $$\begin{aligned}
        (\Omega\Psi_{1},\Psi_{2}) &= \left(\sum_{\{i\}}c_{i}\lambda_{i}\alpha_{i},\sum_{\{j\}}\gamma_{j}\alpha_{j}\right)\\
        &=\sum_{i,j}c^{\ast}_{i}\lambda_{i}^{\ast}\gamma_{j}(\alpha_{i},\alpha_{j})
        \end{aligned}$$ but $\{\alpha_{i}\}$ is an orthonormal basis so
    $(\alpha_{i},\alpha_{j})=\delta_{ij}$. The above then becomes $0$
    except for when the two basis vectors are the same, so we are left
    with:
    $$(\Omega\Psi_{1},\Psi_{2})=\sum_{i}c^{\ast}_{i}\lambda^{\ast}_{i}\gamma_{i}.$$
    Now, considering $(\Psi_{1},\Omega\Psi_{2})$, we have very
    similarly: $$\begin{aligned}
        (\Psi_{1},\Omega\Psi_{2})&=\left(\sum_{\{i\}}c_{i}\alpha_{i},\Omega\sum_{\{j\}}\gamma_{j}\alpha_{j}\right)\\
        &=\left(\sum_{\{i\}}c_{i}\alpha_{i},\sum_{\{j\}}\gamma_{j}\Omega\alpha_{j}\right)\\
        &= \left(\sum_{\{i\}}c_{i}\alpha_{i},\sum_{\{j\}}\gamma_{j}\lambda_{j}\alpha_{j}\right)\\
        &=\sum_{i,j}c_{i}^{\ast}\lambda_{j}\gamma_{j}(\alpha_{i},\alpha_{j})=\sum_{i,j}c_{i}^{\ast}\lambda_{j}\gamma_{j}\delta_{ij}\\
        &=\sum_{i}c_{i}^{\ast}\lambda_{i}\gamma_{i}.
        \end{aligned}$$ so we have
    $$(\Omega\Psi_{1},\Psi_{2})=\sum_{i}c^{\ast}_{i}\lambda^{\ast}_{i}\gamma_{i},\:\:\:\:(\Psi_{1},\Omega\Psi_{2})=\sum_{i}c_{i}^{\ast}\lambda_{i}\gamma_{i}$$
    but we have conditioned that the eigenvalues $\lambda_{i}$ are real
    so we therefore see that $\lambda_{i}=\lambda_{i}^{\ast}$ and so
    $$(\Psi_{1},\Omega\Psi_{2})=(\Omega\Psi_{1},\Psi_{2})$$ which is the
    definition of a Hermitian operator. This holds true for any
    arbitrary $\Psi_{1}$ and $\Psi_{2}$ so long as they are in the space
    spanned by the orthonormal basis and can subsequently be expressed
    as a linear combination of the orthonormal constituent vectors;
    therefore, any operator with real eigenvalues whose eigenvectors can
    form an orthonormal basis set is Hermitian. $\square$\
    \
    This proof in fact goes both ways: more significantly, any Hermitian
    operator possesses a set of eigenvectors which are an orthonormal
    basis set of the state space! The proof is rather technical, so it
    will be ignored-- but the profound consequences are clear. If an
    operator in the state space is Hermitian it has a basis consisting
    eigenvectors, called its **eigenbasis**, spanning the space; if we
    take any basis of the state space we can take its inner product over
    all the basis eigenvectors with any state vector to produce a
    wavefunction. These representations will prove massively helpful.

4.  The action of all Hermitian operators whose eigenvectors form an
    orthonormal basis can be specified by their eigenvalues and
    eigenvectors.\
    \
    [Proof:]{.underline}\
    \
    For a Hermitian operator $\Omega$ with eigenvalues $\lambda_{i}$ and
    eigenvectors $\alpha_{i}$, any vector can be expressed in the
    orthonormal basis: $$\psi=\sum_{i}(\alpha_{i},\psi)\alpha_{i}$$ so
    $$\Omega\psi=\Omega\sum_{i}(\alpha_{i},\psi)\alpha_{i}=\sum_{i}(\alpha_{i},\psi)\Omega\alpha_{i}=\sum_{i}(\alpha_{i},\psi)\lambda_{i}\alpha_{i}.$$
    This clearly requires no external knowledge other than understanding
    the sets $\{\lambda_{i}\}$ and $\{\alpha_{i}\}$. Conversely: if we
    completely understand these sets then we can completely specify the
    operator given an input vector $\psi$ the operator is acting on.

With all this knowledge about operators in vector spaces, and clear
signs that their eigenbases will be very useful, we now come to the
Second Postulate of quantum mechanics.

## Observables in Quantum Mechanics

The state problem is a question of information. The most relevant
information to a physicist about a state is the value of its
*observables*. The problem, we have seen, is that unlike with the
classical state, the quantum state cannot just be said to possess a
value for any observable, as it is instead a superposition of many
different possible states and it is thus far unclear which state will
emerge upon measurement. This problem was dealt with by placing states
in correspondence with vectors in a vector space which meant that all
possible states could be summed together in a superposition to create a
new state without forming something out of the space of possible states,
and we learnt how to create more wavefunctions from those state vectors.
However, we still do not know why wavefunctions are so tangible. The
genius of the formalism comes when we incorporate operators and their
orthogonal eigenbases into the picture, where wavefunctions in
eigenbases will answer our problem. [**Postulate 2:
Observables**]{.underline}\
\
To each physical observable there exists a corresponding hermitian
operator. There exists an orthonormal eigenbasis of this operator which
spans the state space: that is, for some observable operator $\hat{A}$
with eigenvalues $\{A_{i}\}$ corresponding to eigenvectors
$\{\alpha_{i}\}$, $$\forall\:\Psi, \:\: \Psi=\sum_{i}c_{i}\alpha_{i}$$
for some components $\setof{c_{i}}$. The only possible values for the
observable whose operator is $\hat{A}$ which can be measured are the
eigenvalues $\setof{A_{i}}$ and these correspond to the eigenstates
$\setof{\alpha_{i}}$. If there comes a condition
$$\hat{A}\Psi=A_{i}\alpha_{i}$$ then we say that the eigenvalue $A_{i}$
is the measured value of the physical observable and the new state
vector is the eigenvector $\alpha_{i}$. The most essential outcome to us
here is that we want real values for the results of physical
measurements, as imaginary position or imaginary energy for example
would be nonsense; since the set of eigenvalues $\setof{A_{i}}$ are the
only possible results of measurements, we therefore require real
eigenvalues. By the postulate, we have Hermitian operators representing
observables, which therefore must have real eigenvalues. The postulate
is that these eigenvalues are the only possible measurable results for
that observable for any states, so that they are real is critical. It is
from the fact we need the operator to have real eigenvalues if these are
to be the measured values for a physical operator, combined with the
fact it is postulated to have an orthonormal eigenbasis spanning the
state space, which guarantees the operators representing observables
must be Hermitian. That is precisely, we recall,
$$\oip{\hat{A}\Psi_{1}}{\Psi_{2}}=\oip{\Psi_{1}}{\hat{A}\Psi_{2}}.$$ We
start a fuller discussion by noting the assertions of the postulate in
short-form:

1.  All physical observables are represented by hermitian operators
    whose eigenvectors form an eigenbasis which spans the state space.
    For brevity it is customary to call these operators which represent
    physical operators throughout the course of this book.

2.  Each measurement of a physical observable must yield one of the real
    eigenvalues of the observable operator.

3.  As it is possible for an operator to have a finite/and or discrete
    number of eigenvalues, so can a physical observable have a finite
    number of possible results after being measured if their operator
    has a finite number of eigenvalues. Such a situation is rarer than
    one would assume in quantum mechanics, considering we are working in
    an infinite dimensional vector space where it is relatively unlikely
    there are not infinite eigenvectors and eigenvalues to an arbitrary
    operator, but it is far from a non-existent possibility. The
    physical phenomenon resulting from discretely distributed
    eigenvalues is called quantization; its implications, most famously
    perhaps in the discrete energy levels of electrons, are important
    and may well have been already known to the reader.

Now we must consider the importance of time. Crucial is that operators
corresponding to physical observables never change with time, and there
is only one operator corresponding to each physical observable. That
does not mean that the measured values of the observable will remain
constant across any time period. That is because clearly the measured
value of the observable depends on the state vector $\Psi$ representing
the state of the system which is the input vector we the observable
operator is operating on; we have already stated this state vector can
evolve with time. The precise nature of all these temporal
considerations will be covered in due course, but that observable
operators do not evolve with time is surely a great relief, especially
if we need to think about their eigenbases and eigenvalues and do not
want to have to continually solve what are not trivial eigenvalue
equations.\
\
The second part of the postulate gives us an interesting and significant
link between the state vectors which represent states, the state space
operators representing physical observables, and the eigenvalues of
those observables representing possible results after measurement.\
\
To start off, note that we expect that most state space vectors will be
linear combinations of the eigenvectors of any observable operator,
since the set of (infinite) eigenvectors of a hermitian operator
constitutes an orthonormal basis of its space. We do not expect all
possible states to be pure scalar multiples of single eigenvectors since
there can be infinite linear combinations of the eigenvectors which are
not pure scalar multiples of single eigenvectors. The postulate now
states that the condition $$\hat{A}\Psi=A_{i}\alpha_{i}$$ means that
$A_{i}$ is the measured value of the physical observable represented by
the operator $\hat{A}$. However, this condition is clearly very singular
if we are working with a wavefunction which is a linear combination of
the infinite eigenvectors of an observable operator-- since the state
$\Psi$ does not naturally coincide with the eigenvector $\alpha_{i}$
alone. What should be abundantly clear, however, is that,
post-measurement, $\Psi$ has changed from a linear combination of
eigenvectors to a multiple of only one of them, the eigenvalue
corresponding to which is the measured value of the observable. So the
act of measurement is clearly very important; indeed, it forms one of
the central pillars of quantum mechanics and especially the mathematics
which formulates it. We have seen this, already, in the Stern Gerlach
experiment! There, measuring the $x$ spin led to irrevocable changes in
the $y$ spin even without physically affecting it in that dimension.
This measurement problem is the final component of the quantum
mechanical solution to the state problem, and pulls everything together
in an understandable way. Thus to complement Postulate 2 on observables,
we have Postulate 3, on Measurements.

### Measurements

[**Postulate 3: Measurements**]{.underline}\
\
After a measurement of a physical observable, the state vector is forced
into a specific eigenvector corresponding to the eigenvalue measured for
that observable. The probability that the (normalised) state vector is
forced into a state represented by a state vector $\alpha_{i}$, which is
called an eigenstate, is given by
$$P(\alpha_{i})=|\oip{\alpha_{i}}{\Psi}|^2,$$ which is therefore also
the probability of measuring the eigenvalue $A_{i}$ as the final result
of the measurement for the observable. This Postulate now provides great
meaning to the discourse immediately preceding this section. By
*forcing* a state vector into specific eigenvector of an observable
operator after a measurement of that specific observable, we guarantee
several things:

-   We do not restrict the state vector to being a pure scalar multiple
    of one single eigenvector prior to measurement. This is important as
    by Postulate 1, all state space vectors represent physical states,
    and there certainly should be infinite Hilbert space vectors which
    are linear combinations of any orthonormal basis vectors which span
    it: including when that orthonormal basis is the eigenbasis of an
    observable operator. This is the superposition of different possible
    states which exists before a measurement.

-   We guarantee that after measurement, Postulate 2 has meaning: since
    the measurement forces the wavefunction into a specific eigenstate,
    we will indeed achieve after measurement
    $$\hat{A}\Psi\to \hat{A}\alpha_{i}=A_{i}\alpha_{i}$$ and therefore
    we guarantee that a measurement will always yield one single value--
    the eigenvalue $A_{i}$: regardless of what superposition of states
    it was in previously.

This is all well and good, but what gives order to the chaos is the
probabilistic link of the postulate. Without it, we would be wondering
what to do in any arbitrary superposition in states, since intuition
tells us that just because we have a superposition it does not mean that
all the measurements must have equal probabilities. Fortunately, we have
the postulate: $$P(\alpha_{i})=|\oip{\alpha_{i}}{\Psi}|^2$$ where
$P(\alpha_{i})$ is the probability of measuring the state vector to be
in the state $\alpha_{i}$. Here we make a clarification of similar type
as that regarding the distinction between state and wavefunction: the
reader must understand that the state vector being in an eigenstate
$\alpha_{i}$ is not so interesting itself as is the fact that when it is
in that eigenstate we know $A_{i}$ is the eigenvalue is the measured
result for the observable. Thus when we say the state is measured to be
the eigenstate $\alpha_{i}$ we really allude to the fact that a
measurement will yield $A_{i}$ as the value. The reason we do not write
$P(A_{i})$, the probability of measuring $A_{i}$, is due to the fact
that in the face of degeneracy (say, eigenvalue $A_{1}$ corresponding to
two different eigenstates $\alpha_{1}$ and $\alpha_{2}$), we have the
following problem:
$$P(A_{1})\neq\oip{\alpha_{1}}{\Psi}\neq\oip{\alpha_{2}}{\Psi}$$ in
fact, here it would be
$$P(A_{1})=\oip{\alpha_{1}}{\Psi}+\oip{\alpha_{2}}{\Psi}.$$ So we see
that defining the probability of a wavefunction being in an eigenstate
is slightly easier and more consistent. Next, consider the state
$$\Psi=\alpha_{n}.$$ In this state a measurement will yield value
$A_{n}$ with probability
$$P(A_{n}):=|\oip{\alpha_{n}}{\Psi}|^2=|\oip{\alpha_{n}}{\alpha_{n}}|^2=1$$
since the eigenvectors $\alpha_{n}$ are assumed to be normalised. So if
the state vector is a pure eigenstate then the eigenvalue corresponding
to the eigenstate it is in will be measured with probability 1. When do
pure eigenstates occur for state vectors? They may occur organically for
some arbitrary physical state which happens to be a pure eigenstate of a
physical observable, though we expect this to be comparatively rare.
More importantly: they also occur after measurements, since by the first
part of the postulate a measurement will force a state vector into an
eigenvector -- a pure eigenstate -- of the observable operator. This now
explains why instantaneous successive measurements must yield the same
answer: the first measurement forces the state vector into a pure
eigenstate $\alpha_{n}$ corresponding to the eigenvalue $A_{n}$
measured, and then the second measurement will give the same eigenvalue
$A_{n}$ with probability $$P(A_{n})=|\oip{\alpha_{n}}{\alpha_{n}}|^2=1$$
since the state vector is now the pure eigenstate $\alpha_{n}$ after
being forced into this eigenstate by the first measurement. We saw this
intuitive consequence in the Stern Gerlach experiment, where successive
magnetic fields in the same axis yielded the same spin results each
time!\
\
The disturbance to classical intuition comes when we make the same
observation we have already made. By Postulate 1, all state space
vectors represent physical states, and there are infinite state space
vectors which are linear combinations of any orthonormal basis vectors
which span it. Thus if the orthonormal basis is the eigenbasis of a
physical observable operator, there are infinite state vectors which are
not pure eigenvectors of the observable operator, but rather linear
combinations of the corresponding eigenvectors. Then,
$$\Psi=\sum_{i}\oip{\alpha_{i}}{\Psi}\alpha_{i},$$ by the expansion of
Hilbert Space vectors in an orthonormal basis. But then, for any $A_{n}$
in a non-degenerate state (similar reasoning holds for degenerate
states), $$\begin{aligned}
P(A_{n}):=|\oip{\alpha_{n}}{\Psi}|^2=|\oip{\alpha_{n}}{\sum_{i}\oip{\alpha_{i}}{\Psi}\alpha_{i}}|^2
\end{aligned}$$ so if this probability was zero then that would imply
the component $\oip{\alpha_{i}}{\Psi}=0$. In a nontrivial linear
combination of eigenvectors, there will exist more than one eigenvector
$\alpha_{i}$ for which this is not true, and therefore more than one
eigenvalue $A_{i}$ which can be measured with nonzero probability.\
\
This is the famous probabilistic nature of quantum mechanics
encapsulated through our postulates. Do there exist such state vectors
which are linear combinations of multiple eigenvectors of an observable
operator? Certainly yes, by Postulate 1. Yet in such cases multiple
eigenvalues can be measured with nonzero probability: that is, multiple
values can be obtained for the same measurement. Thus the wording of the
postulate-- the state vector is forced into a specific eigenvector-- is
relevant: the state vector in these cases does not possess a single
fixed value for an observable which must be revealed upon measurement so
it cannot be said, technically, to have a position or momentum or any
other observable value. We can only say that an eigenvalue is the
measured value of this specific measurement: or, the eigenvector the
state vector has been forced into was not necessarily the state vector
before at all; in another scenario, with defined probability, the state
vector may well have been forced into a different eigenstate and then
yielded a different value for an observable.\
\
We end this section with a summary on quantum states and inherent
probability:

-   In a pure state with respect to a physical observable the state
    vector is made up solely of one eigenvector of the observable
    operator. A measurement will therefore yield the eigenvalue
    corresponding to that eigenvector with probability 1. In such cases
    (a rarity) a deterministic prediction can be made about the results
    of a measurement.

-   After measurement a state vector is forced into a pure eigenstate
    $\alpha_{i}$ with probability $|\oip{\alpha_{i}}{\Psi}|^2$. Thereon
    the above determinism of a pure state applies for successive
    measurements unless the system experiences external perturbation
    which once again moves it out of the pure eigenstate.

-   A state vector is in a mixed state with respect to a physical
    observable if the state vector is a non-trivial linear combination
    of more than one eigenvector of the observable operator. In those
    cases the strongest predictive statement about the result of a
    measurement is that a specific eigenstate $\alpha_{i}$ has
    probability $|\oip{\alpha_{i}}{\Psi}|^2$ of being measured. We
    cannot make any deterministic predictions at all, and we do not
    really think of a mixed state as having a value for that specific
    observable. Most naturally occurring states in quantum mechanics are
    indeed mixed states.

Another question still remains. We know that state vectors represent
states-- and that is, physical states. If we think to use our classical
intuition, we know a physical state can be thought about from the
perspective of one observable (such as when we consider the momentum of
two colliding objects). However, that does not mean it does not possess
any values for all other physical observables, as it still has energy,
angular momentum, and so on: only that we are not currently considering
the other observables. Similarly, we would not be particularly pleased
if the physical states pertaining to a certain measurement of one
specific observable-- these so called pure states-- suddenly contained
absolutely no information on any other observables. This is a question
of information encapsulation: how does an energy pure state store
extractable information about momentum, for example? To understand this
question, which is far more complicated than the classical one of , we
treat the two seminal theorems on the matter. Along the way, we will
also be able to practise the mathematical operations we have introduced
at a level and intensity we have not had the occasion to do so far.

## Simultaneous states

The question of deals with the segue from the previous section onto this
one. We want to investigate which states (state vectors) can contain
information on multiple observables at a time, and which observables
these are. We have seen in the Stern Gerlach experiment that for example
$x$ and $y$ spin simultaneous states are impossible, so this is a
relevant, fully quantum in nature, problem.\
\
It turns out that the ability for different observables to have
information represented in the same state vectors depends strongly on
the relationship between their observable operators, as these in turn
relate their orthonormal eigenvectors. To see this, there is one
sweeping but simple theorem on operators for observables which can be
measured simultaneously, and one dramatically anticlassical one for
observables which cannot.

### The Compatibility Theorem

Consider an unperturbed system, two physical observables, and three
measurements ordered chronologically. The first and third measurements
are for the first physical observable, but the second measurement is for
the second observable. We know from the Measurement Postulate that:

-   The first measurement forces the wavefunction into a pure eigenstate
    of the first physical observable operator.

-   The second measurement forces the wavefunction into a pure
    eigenstate of the second physical observable operator.

-   If the second measurement of the different observable did not exist,
    then we would have successive measurements of the same state (which
    is, the operator acting on the same eigenstate the starting state
    vector was forced into following the first measurement) and we would
    expect the same measurement for the observable as we originally
    obtained.

The question is therefore whether or not this second measurement changes
the result of the third. This is a profound question, because if it
does, then we would conclude the simple act of measuring the second
observable has moved the state vector out of the pure eigenstate it was
in after the first measurement; that would then imply the second
measurement is in itself a perturbation to the system: a confusing
result. Indeed-- the reader will recognise that this is exactly the
class of behaviour which appeared so shockingly in the Stern Gerlach
experiment.\
\
We shall see that the determining factor is what the relationship
between the two observable operators is. To start off, we will use the
notations $\mathcal{A}$ and $\mathcal{B}$ as shorthand to distinguish
between the two observables, so we do not have to name them. We define
$\mathcal{A}$ and $\mathcal{B}$ to be **compatible observables** if the
first and third measurements yield the same value regardless of the
starting state and the value of the second observable measured in the
second measurement. If we call the values measured $\mathcal{A}^{(1)}$,
$\mathcal{B}^{(1)}$, $\mathcal{A}^{(2)}$, then observable $\mathcal{A}$
and $\mathcal{B}$ are compatible iff
$$\forall\:\Psi,\:\mathcal{B}^{(1)},\:\:\mathcal{A}^{(1)}=\mathcal{A}^{(2)}.$$
**Compatibility Theorem**: Two observables $\mathcal{A}$ and
$\mathcal{B}$ are defined compatible if they possess a common eigenbasis
or their operators commute. These three conditions in fact all imply
each other. [Proof:]{.underline}\
\
First we prove that $\hat{A}$ commutes with $\hat{B}$ iff they possess a
common eigenbasis. Consider two observable operators which commute, and
define their eigenbases to be $\{\alpha_{i}\}$ and $\{\beta_{i}\}$. Now
take an arbitrary eigenvector $\alpha_{i}$ of $\hat{A}$ with eigenvalue
$A_{i}$. We have $$\hat{A}\hat{B}=\hat{B}\hat{A}$$ so we get
$$\hat{A}\hat{B}\alpha_{i}=\hat{B}\hat{A}\alpha_{i}=\hat{B}A_{i}\alpha_{i}.$$
However, we can now pull the constant eigenvalue out:
$$\hat{A}(\hat{B}\alpha_{i})=A_{i}(\hat{B}\alpha_{i})$$ so clearly
$\hat{B}\alpha_{i}$ is an eigenvector of $\hat{A}$ corresponding to
eigenvalue $A_{i}$. Assuming that the eigenvalues are nondegenerate this
implies that $\hat{B}(\alpha_{i})$ coincides with $\alpha_{i}$ as the
eigenvalue $A_{i}$ has only one distinguishable eigenvector. The fact
that $$\hat{B}\alpha_{i}\equiv\alpha_{i}$$ means we must have
$$\hat{B}\alpha_{i}=c\alpha_{i}$$ for some scalar multiple $c$. This
means that $\alpha_{i}$ is an eigenvector of $\hat{B}$ corresponding to
eigenvalue $c$. So we can say that $\forall\:i, \alpha_{i}$ is an
eigenvector of $\hat{A}$ and $\hat{B}$: which means that they have the
same eigenbasis. This isn't of course, to say, the eigenvalues are the
same for $\hat{B}$ and $\hat{A}$ even though it may correspond to the
same eigenvector (above, they are not the same unless $A_{i}=c$), since
we expect the operators to be formulated differently so there will still
be different values measured for each observable. Yet at the same time
this is clearly helpful: if we know two physical observable operators
commute and we have the eigenbasis of one then we automatically have the
eigenbasis of the other.\
\
Now, we prove it the other way around. Assume $\hat{A}$ and $\hat{B}$
both possess the eigenbasis $\{\gamma_{i}\}$. We want to prove they
commute. As they possess the same eigenbasis with eigenvalues
$\{A_{i}\}$ and $\{B_{i}\}$ respectively, we can write
$$\hat{A}\hat{B}\gamma_{i}=\hat{A}B_{i}\gamma_{i}=B_{i}\hat{A}\gamma_{i}=B_{i}A_{i}\gamma_{i}$$
and the exact same applies for $\hat{B}\hat{A}\gamma_{i}$:
$$\hat{B}\hat{A}\gamma_{i}=\hat{B}A_{i}\gamma_{i}=A_{i}\hat{B}\gamma_{i}=A_{i}B_{i}\gamma_{i}.$$
Clearly, as $A_{i}$ and $B_{i}$ are constant eigenvalues,
$$A_{i}B_{i}\equiv B_{i}A_{i}.$$ So this easily proves that two
observable operators possessing the same eigenbasis must commute. Thus
the implication works both ways and therefore two observable operators
commute iff they share a common eigenbasis.\
\
Now to look at the practical definition: we are probably more interested
in the concept of compatibility, as it concerns whether or not a
measurement of a second observable in between measurements of a first
observable will alter the measured results from the first measurement,
effectively forcing the state vector out of the pure eigenstate it was
forced into. Let's first prove that two observables having common
operator eigenbases is necessary and sufficient for the above defined
definition of compatibility to hold.\
\
Start by considering two observables $\mathcal{A}$ and $\mathcal{B}$
represented by operators $\hat{A}$ and $\hat{B}$ respectively. Define
the measurements to be $\mathcal{A}^{(1)},\mathcal{B}^{(1)}$,
$\mathcal{A}^{(2)}$. For the observables to be compatible we need
$\mathcal{A}^{(1)}$ to be the same as $\mathcal{A}^{(2)}$ regardless of
the starting state and $\mathcal{B}^{(2)}$. Assume to begin with that
the two operators $\hat{A}$ and $\hat{B}$ have the common eigenbasis
$\{\gamma_{i}\}$. By definition the first measurement of $\mathcal{A}$
must force the state vector into a single eigenvector in the eigenbasis
of the operator $\hat{A}$: that is, some $\gamma_{i}$ such that the
measured value is for observable $\mathcal{A}$ the eigenvalue $A_{i}$.
Next, measurement ${{B}}^{(1)}$ is the action of the operator $\hat{B}$
on the eigenvector $\gamma_{i}$. But by the Measurement Postulate of
quantum mechanics, $$P(\alpha_{i})=|\oip{\alpha_{i}}{\Psi}|^2$$ That is,
the probability that the arbitrary operator $\hat{A}$ forces the state
vector into an arbitrary eigenvector $\alpha_{i}$ from its eigenbasis.
Here, then, since the state vector has been forced into the eigenstate
$\gamma_{i}$ by the first measurement, the probability the second
measurement of the other observable $\mathcal{B}$ forces the state
vector into the same eigenstate is:
$$P(\gamma_{i})=|\oip{\gamma_{i}}{\gamma_{i}}|^2=1$$ where we assume as
per usual that the eigenvectors $\gamma_{i}$ have been normalised. So we
can say that measurement B will not alter the eigenstate the state
vector is in and therefore the third measurement will follow the same
logic to yield the exact same value, the eigenvalue $A_{i}$
corresponding to $\gamma_{i}$. Thus, if two observable operators possess
the same eigenbasis, they are compatible observables.\
\
If the observables are compatible then this implies their operators have
the same eigenbasis. The proof for this is simple. If the observables
$\mathcal{A}$ and $\mathcal{B}$ are compatible then for the successive
measurements $\mathcal{A}^{(1)},\mathcal{B}^{(1)},\mathcal{A}^{(2)}$ the
measured values for $\mathcal{A}^{(1)}$ and $\mathcal{A}^{(2)}$ must be
the same. The measurement $\mathcal{A}^{(1)}$ must have forced the
wavefunction into an eigenvector of $\hat{A}$, some arbitrary
$\alpha_{i}$. Then, the measurement $\mathcal{B}^{(1)}$ must force the
wavefunction into some arbitrary eigenvector $\beta_{i}$ of the operator
$\hat{B}$. However, the final measurement must yield the same result as
the first if the observables are compatible, which is, the same
eigenvalue corresponding to the same eigenvector $\alpha_{i}$ of
operator $\hat{A}$ as it originally was in. The probability that the
measurement forces the wavefunction, currently in the eigenstate
$\beta_{i}$ of $\hat{B}$ as the measurement $\mathcal{B}^{(1)}$ has just
been performed, into the same eigenstate $\alpha_{i}$ as originally
measured is: $$P(\alpha_{i})=|\oip{\alpha_{i}}{\beta_{i}}|^2.$$ However,
if these observables are to be compatible, the final measurement must
with certainty yield the eigenvalue $A_{i}$ again and therefore the
above probability of measurement $\mathcal{A}^{(2)}$ forcing it back
into the original eigenstate must be 1. So
$$|\oip{\alpha_{i}}{\beta_{i}}|^2=1 \Rightarrow\:\: \alpha_{i}\equiv\beta_{i}$$
and therefore their eigenbases must be the same as the above holds true
for any arbitrary $\alpha_{i}$ and corresponding $\beta_{i}$ from the
measurements.\
\
The Compatibility Theorem is now complete. We have shown that:

-   Two operators commuting is necessary and sufficient for them to
    possess a common eigenbasis.

-   Two operators possessing a common eigenbasis is necessary and
    sufficient for the two observables they represent to be compatible.

-   Therefore, two observable operators commuting is also necessary and
    sufficient for them to represent compatible observables.

The logical implications of these facts all run three ways.\
\
While we have now seen facts about compatible observables, an example of
incompatible observables sticks in our mind-- that of the Stern Gerlach
experiment. We saw exactly that $x$ and $y$ spins were incompatible,
because measuring the $x$ spin in between two $y$ measurements stopped
the second $y$ measurement from being the same as the first with
certainty-- which is to say, we now know, that the measurement of $x$
spin forced it out of the eigenstate of $y$ spin it had been previously
forced into. All the questions about the quantum state raised by the
Stern Gerlach experiment will finally come to an end with this section.
We would like to formalise our understanding of how incompatibility
affected the experiment. To explain it all, we witness-- and prove
ourselves!-- one of Physics' most groundbreaking and shocking theorems.

## The Heisenberg Uncertainty Principle

The idea of commuting observable operators being necessary and
sufficient for the two observables they represent to be compatible is a
very important one for the question of simultaneous states, and has been
shown above. Now we must surely consider when two observable operators
do not commute: in other words, when they represent **incompatible**
observables. One of the most important and dramatic results of all
quantum mechanics, the Heisenberg Uncertainty Principle, results when we
carry out some elegant mathematics to investigate this problem. Before
we begin the statement and proof, let us define the commutator between
two operators to be $$[\hat{A},\hat{B}]:=\hat{A}\hat{B}-\hat{B}\hat{A}$$
so that if we have two commuting operators $\hat{A}$ and $\hat{B}$, then
$$[\hat{A},\hat{B}]=\hat{A}\hat{B}-\hat{B}\hat{A}=0$$ since
$\hat{A}\hat{B}=\hat{B}\hat{A}$ iff they commute. For operators which do
not commute, their commutator may take a wide variety of forms: which is
why it is useful under universal convention to have this shorthand.

::: tcolorbox
**[Heisenberg Uncertainty Principle]{.underline}**\
\
For any state $\Psi_{t}$,
$$\Delta A_{t}\Delta B_{t}\geq\frac{1}{2}|\oip{\Psi_{t}}{[\hat{A},\hat{B}]\Psi_{t}}|$$
where $\Delta A_{t}$ is the standard deviation of measurable values of
observable $\mathcal{A}$ at time $t$: which is therefore a measure of
uncertainty for these variables.
:::

[**Proof:**]{.underline}\
\
We will continue to refer to arbitrary observables $\mathcal{A}$ and
$\mathcal{B}$ for the proof; all the proof is relevant at any instant of
time and so time subscripts will be eschewed. The notation $\Delta A$
refers to the standard deviation of the measurements of observable
$\mathcal{A}$; this standard deviation is no different from the
statistical definition:
$$\Delta A=\sqrt{\langle \hat{A}^2\rangle-\langle \hat{A}\rangle^2}$$
where the symbol $\langle X\rangle$ is the expected value of the
variable $X$, as seen in the probability preliminary. First we note that
this principle is valid for compatible observables: as compatible
observables, their operators must commute. Thus
$$[\hat{A},\hat{B}]=0 \Rightarrow\:\: \Delta A_{t}\Delta B_{t}\geq\frac{1}{2}|\oip{\Psi_{t}}{[\hat{A},\hat{B}]\Psi_{t}}| = \frac{1}{2}|\oip{\Psi_{t}}{0} |=0.$$
So for compatible observables, $$\Delta A_{t}\Delta B_{t}\geq 0$$ which
is neither interesting nor invalid at all since the standard deviation
of any measurement can never be negative. Now, we will prove this for
all physical operators, regardless of whether they commute.\
\
[**Lemma 1:**]{.underline}\
Any operator $\hat{X}':=\hat{X}-\qexp{\hat{X}}$ where $\hat{X}$ is a
Hermitian physical operator is also Hermitian.\
\
[**Proof:**]{.underline}\
\
Recall that the definition for an expected value of a variable is the
sum of its possible values multiplied by the probabilities of the
variable taking those values. Therefore, we can say that, over the
eigenbasis $\{\xi_{i}\}$ of $\hat{X}$ with eigenvalues $\{X_{i}\}$,
$$\qexp{\hat{X}}=\sum_{\{i\}}P(\xi_{i})X_{i},$$ but by our knowledge of
the previous postulates we can describe the probability more precisely:
the measurement postulate defines this to be
$$\qexp{\hat{X}}=\sum_{\{i\}}X_{i}|\oip{\xi_{i}}{\Psi}|^2.$$ Our job is
to prove that the operator $\hat{X}':=\hat{X}-\qexp{\hat{X}}$ is
hermitian if $\hat{X}$ is hermitian for all quantum operators. That is,
we need to prove that:
$$\oip{\Psi_{1}}{\hat{X}'\Psi_{2}}=\oip{\hat{X}'\Psi_{1}}{\Psi_{2}}$$
for all Hilbert space functions $\Psi_{1}$ and $\Psi_{2}$. The operator
$\hat{X}$ must be hermitian as $\hat{X}$ is defined to be a quantum
operator corresponding to a physical observable. Meanwhile, the
expectation value
$$\qexp{\hat{X}}=\sum_{\{i\}}X_{i}|\oip{\xi_{i}}{\Psi}|^2.$$ is clearly
a real scalar, as the probabilities, which are square moduli, will all
be real numbers and so will each eigenvalue of the hermitian operators.
Therefore,
$$\oip{\hat{X}\Psi_{1}}{\Psi_{2}}\equiv\oip{\Psi_{1}}{\hat{X}\Psi_{2}}$$
and
$$\oip{\qexp{\hat{X}}\Psi_{1}}{\Psi_{2}}\equiv\oip{\Psi_{1}}{\langle\hat{X}\rangle\Psi_{2}}\equiv\qexp{\hat{X}}\oip{\Psi_{1}}{\Psi_{2}}$$
so for any physical operator $\hat{X}$ the defined operator $\hat{X}'$
is the sum of two hermitian operators. So $$\begin{aligned}
\oip{\hat{X}'\Psi_{1}}{\Psi_{2}}&=\oip{[\hat{X}-\langle\hat{X}\rangle]\Psi_{1}}{\Psi_{2}}=\oip{\hat{X}\Psi_{1}}{\Psi_{2}}-\oip{\langle\hat{X}\rangle\Psi_{1}}{\Psi_{2}}\\
&=\oip{\Psi_{1}}{\hat{X}\Psi_{2}}-\oip{\Psi_{1}}{\langle\hat{X}\rangle\Psi_{2}}\\
&=\oip{\Psi_{1}}{\hat{X}'\Psi_{2}}
\end{aligned}$$ using the linear properties of the inner product. Thus,
the operator $\hat{X}'$ is Hermitian for any physical operator.
Therefore, defining $\hat{A'}:=\hat{A}-\qexp{\hat{A}}$ and
$\hat{B}':=\hat{B}-\qexp{\hat{B}}$ for the purpose of the problem also
gives us two hermitian operators. $\square$\
\
The commutator in the generalised principle might give pause with
regards to the development of these new operators, but, importantly,
$$[\hat{A}',\hat{B}']=[\hat{A},\hat{B}].$$ This fact can be proved quite
simply: $$\begin{aligned}
[\hat{A}',\hat{B}']&= \hat{A}'\hat{B}'- \hat{A}'\hat{B}'\\
&= (\hat{A}-\qexp{\hat{A}})(\hat{B}-\qexp{\hat{B}})-(\hat{B}-\qexp{\hat{B}}) (\hat{A}-\qexp{\hat{A}})\\
&=(\hat{A}\hat{B}-\hat{A}\qexp{\hat{B}}-\qexp{\hat{A}}\hat{B}-\qexp{\hat{A}}\qexp{\hat{B}})-(\hat{B}\hat{A}-\hat{B}\qexp{\hat{A}}-\qexp{\hat{B}}\hat{A}-\qexp{\hat{B}}\qexp{\hat{A}})
\end{aligned}$$ but as the expectation values $\qexp{\hat{A}}$ and
$\qexp{\hat{B}}$ are real scalars it is clear that
$\qexp{\hat{A}}\qexp{\hat{B}}=\qexp{\hat{B}}\qexp{\hat{A}}$, and
$\qexp{\hat{A}}\hat{B}=\hat{B}\qexp{\hat{A}}$ and vice versa swapping
the $A$ and $B$ around. So the terms cancel out and we are left with
$$[\hat{A}',\hat{B}']=\hat{A}\hat{B}-\hat{B}\hat{A}:=[\hat{A},\hat{B}]. \:\:\square$$
Now, one last important lemma:\
\
[**Lemma 2:**]{.underline}\
$$\oip{\hat{A}'\Psi}{\hat{A}'\Psi}=(\Delta\hat{A})^2$$\
\
[**Proof:**]{.underline}\
By the Hermiticity of $\hat{A}'$,
$$\oip{\hat{A}'\Psi}{\hat{A}'\Psi}=\oip{\Psi}{([\hat{A}']^2\Psi}.$$
Expanding the definition, $$\begin{aligned}
\oip{\hat{A}'\Psi}{\hat{A}'\Psi}&=\oip{\Psi}{\hat{A}'^2\Psi}\\
&=\oip{\Psi}{[\hat{A}-\qexp{\hat{A}}][\hat{A}-\qexp{\hat{A}}]\Psi}\\
&=\oip{\Psi}{[\hat{A}^{2}]\Psi-2\qexp{\hat{A}}\hat{A}\Psi+\qexp{\hat{A}}^2\Psi}\\
&=\oip{\Psi}{[\hat{A}^{2}]\Psi}-2\qexp{\hat{A}}\oip{\Psi}{\hat{A}\Psi}+\qexp{\hat{A}}^2\oip{\Psi}{\Psi}\\
&=\langle\hat{A}^2\rangle\oip{\Psi}{\Psi}-2\qexp{\hat{A}}\qexp{\hat{A}}\oip{\Psi}{\Psi}+\qexp{\hat{A}}^2\oip{\Psi}{\Psi}\\
&= \langle\hat{A}^2\rangle-2\qexp{\hat{A}}\qexp{\hat{A}}+\qexp{\hat{A}}^2\\
&=\langle\hat{A}^2\rangle-\qexp{\hat{A}}^2\\
&=(\Delta\hat{A})^2 \:\:\:\:\:\:\square
\end{aligned}$$ Now we can use these lemmas to prove the problem. We
want to prove that
$$\Delta{A}\Delta{B}\geq\frac{1}{2}|\oip{\Psi}{[\hat{A},\hat{B}]\Psi}|$$
at all times $t$. We start by replacing $[\hat{A},\hat{B}]$ with
$[\hat{A}',\hat{B}']$. Then, we have,
$$\oip{\Psi}{[\hat{A},\hat{B}]\Psi}=\oip{\Psi}{[\hat{A}',\hat{B}']\Psi}=\oip{\Psi}{[\hat{A}'\hat{B}'-\hat{B}'\hat{A}']\Psi}.$$
This is,
$$\oip{\Psi}{[\hat{A},\hat{B}]\Psi}=\oip{\Psi}{\hat{A}'\hat{B}'\Psi}-\oip{\Psi}{\hat{B}'\hat{A}'\Psi}
.$$ We can rearrange this by the hermiticity of $\hat{A}'$ and
$\hat{B}'$:
$$\oip{\Psi}{[\hat{A},\hat{B}]\Psi}=\oip{\hat{A}'\Psi}{\hat{B}'\Psi}-\oip{\hat{B}'\Psi}{\hat{A}'\Psi}=\oip{\hat{A}'\Psi}{\hat{B}'\Psi}-\oip{\hat{A}'\Psi}{\hat{B}'\Psi}^{\ast}$$
so this is
$$\oip{\Psi}{[\hat{A},\hat{B}]\Psi}=2i\text{Im}\left(\oip{\hat{A}'\Psi}{\hat{B}'\Psi}\right)$$
according to rudimentary arithmetic of complex numbers. Then, the
expression we need is
$$\frac{1}{2}|\oip{\Psi}{[\hat{A},\hat{B}]\Psi}|\leq\frac{1}{2}\times2|\oip{\hat{A}'\Psi}{\hat{B}'\Psi}|=|\oip{\hat{A}'\Psi}{\hat{B}'\Psi}|.$$
This is because of the above expression for
$\oip{\Psi}{[\hat{A},\hat{B}]\Psi}$ and the fact that the modulus of the
imaginary part of a scalar cannot be greater than the modulus of the
scalar (Exercise 1.3.2a). Then, by Lemma 2
$$\oip{\hat{A}'\Psi}{\hat{A}'\Psi}=(\Delta\hat{A})^2\Rightarrow\:\:\Delta\hat{A}=\sqrt{\oip{\hat{A}'\Psi}{\hat{A}'\Psi}}.$$
So
$$\Delta\hat{A}\Delta\hat{B}=\sqrt{\oip{\hat{A}'\Psi}{\hat{A}'\Psi}}\sqrt{\oip{\hat{B}'\Psi}{\hat{B}'\Psi}}.$$
By Cauchy-Schwartz,
$$\sqrt{\oip{\hat{A}'\Psi}{\hat{A}'\Psi}}\sqrt{\oip{\hat{B}'\Psi}{\hat{B}'\Psi}}\geq|\oip{\hat{A}'\Psi}{\hat{B}'\Psi}|$$
and so, conclusively,
$$\Delta\hat{A}\Delta\hat{B}=\sqrt{(\hat{A}'\Psi,\hat{A}'\Psi)}\sqrt{(\hat{B}'\Psi,\hat{B}'\Psi)}\geq|\oip{\hat{A}'\Psi}{\hat{B}'\Psi}|\geq\frac{1}{2}|\oip{\Psi}{[\hat{A},\hat{B}]\Psi}|$$
so
$$\Delta\hat{A}\Delta\hat{B}\geq\frac{1}{2}|\oip{\Psi}{[\hat{A},\hat{B}]\Psi}|.$$
This proves Heisenberg's Uncertainty Principle. $\square$\
\
This general form we have above is still difficult to interpret, but if
we consider a few examples we will realise this is a very important
result. One of the most famous iterations comes with considering simply
the two central operators of quantum mechanics: the position and
momentum operators, which we have not yet introduced but will for now
just use for calculation purposes. We can calculate the commutator:
$$\begin{aligned}
&[\hat{X},\hat{P}]=\hat{X}\hat{P}-\hat{P}\hat{X}\\
\Rightarrow\:\:&[\hat{X},\hat{P}]\Psi(x)=-xi\hbar\frac{\partial}{\partial x}\Psi(x)--i\hbar\frac{\partial}{\partial x}\biggl(x\Psi(x)\biggr)\\
\Rightarrow\:\:&[\hat{X},\hat{P}]\Psi(x)=-i\hbar x\frac{\partial \Psi}{\partial x}--i\hbar\biggl[\frac{dx}{dx}\Psi(x)+x\frac{\partial\Psi}{\partial x}\biggr]\\
\Rightarrow\:\:&[\hat{X},\hat{P}]\Psi(x)=-i\hbar\biggl[x\frac{\partial\Psi}{\partial x}-\Psi(x)-x\frac{\partial\Psi}{\partial x}\biggr]\\
\Rightarrow\:\:&[\hat{X},\hat{P}]\Psi(x)=i\hbar\Psi(x)\\
\Rightarrow\:\:&[\hat{X},\hat{P}]\equiv i\hbar.
\end{aligned}$$ After this, if we plug this into the Generalised
Uncertainty principle and assume that the wavefunction is normalised,
$$\Delta{\hat{X}}\Delta{\hat{P}}\geq\frac{1}{2}|\oip{\Psi}{i\hbar\Psi}| \Rightarrow \Delta{\hat{X}}\Delta{\hat{P}}\geq\frac{1}{2}|i\hbar\oip{\Psi}{\Psi}|=\frac{1}{2}|i\hbar|=\frac{1}{2}\sqrt{-i\hbar\times i\hbar}=\frac{\hbar}{2}.$$
The key end result is that
$$\Delta{\hat{X}}\Delta{\hat{P}}\geq\frac{\hbar}{2}.$$ This is the most
well known form of the Uncertainty Principle, but we can see that the
Generalised Uncertainty Principle can be applied more broadly than just
to the two observables of position and momentum.\
\
Returning to our considerations of the physical results of trying to
measure two incompatible observables, it is clear how bizarre this
result is. Consider if we have just made a measurement for the position
of a particle. Then we have forced its wavefunction into a position
eigenstate and therefore we can say that the uncertainty in the position
is now $0$: we know the successive measurement must yield the same
position value with probability 1. However, if we plug in
$\Delta{\hat{X}}$ into the Uncertainty Principle we get
$$0\times\Delta\hat{P}\geq\frac{\hbar}{2}$$ which implies somehow that
the uncertainty in momentum must be infinite! So if we know the value of
the position with certainty we are completely unable to distinguish
between infinite possibilities for the momentum. The relationship works
both ways so the same applies for the momentum: if we know the momentum
of a particle then we necessarily have infinite uncertainty in the
position of the particle and we have not a clue where it is. This is
undoubtedly one of the most anti-classical results in quantum mechanics,
and yet it results beautifully from the mathematics we have defined (and
has never been experimentally refuted). If nothing else, it should now
be clear that the mathematical manipulations of quantum mechanics are
rich and impactful.\
\
The same is manifested, of course, in the Stern-Gerlach experiment. By
knowing $x$ spin, we had infinite uncertainty in $y$ spin- with
absolutely no way to tell if an electron would be up or down spin. By
knowing the $y$ spin, we had infinite uncertainty in the $x$ spin. This
is one example of an experimental verification of the Heisenberg
Uncertainty Principle.

## Probability Mass Functions

We conclude this section on measurements, and indeed conclude the state
problem, with a formalisation of how discrete wavefunctions encapsulate
probabilities as probability mass functions.\
\
We have already stated that the discrete wavefunction, which we denoted
${\psi}_{\alpha}(x)$ with a domain of orthonormal eigenvectors, is
exactly the function which stores the components corresponding to the
eigenvectors we input. We therefore call it a **probability mass
function**. This is a formal name for a very simple idea: it stores
probabilities of discrete events- here, the event is the state vector
being forced into a certain eigenstate by a measurement-- and can be
extracted as an output of the probability mass function when we input
the event (eigenstate). We know that these components are probabilities,
because of the measurement postulate and the common expansion we have
already proved!\
\
If the discrete wavefunction is a probability mass function, then
necessarily the modulus squared of its outputs must sum to exactly $1$.
This is naturally because the modulus squared of its outputs are the
modulus squared of the probability amplitudes, which are probability
densities and must sum to $1$, therefore. There is an important
clarification to make to prove that our formalism works.\
\
*Claim: The modulus squared components of a normalised state vector must
sum to 1 in a discrete basis.*\
\
The importance of this claim is clear, since it is equivalent to the
statement that the sums of the different probabilities for all the
possible measurements of an observable must sum to $1$, which must be
true if they are to be considered probabilities in the first place.\
\
**[Proof:]{.underline}**\
\
For some state vector $$\Psi:=\sum_{\{i\}}c_{i}\alpha_{i}$$ in some
orthonormal basis $\setof{\alpha_{i}}$, we need to prove that
$$\sum_{\{i\}}|(\alpha_{i},\Psi)|^2=1$$ given that the state vector is
normalised. Well we know that $$(\Psi,\Psi)=1$$ so we know that
$$\biggl(\sum_{\{i\}}c_{i}\alpha_{i},\sum_{\{i\}}c_{i}\alpha_{i}\biggr)=1.$$
Then, by the rudimentary expansion this is
$$\biggl(\sum_{\{i\}}(\alpha_{i},\Psi)\alpha_{i},\sum_{\{j\}}(\alpha_{j},\Psi)\alpha_{j}\biggr)=1.$$
Due to linear distributivity this means that we get sum terms of the
form
$$\oip{\alpha_{i}}{\Psi}^{\ast}\oip{\alpha_{j}}{\Psi}\oip{\alpha_{i}}{\alpha_{j}}$$
for some $i,j$. However, due to the orthonormality of the basis, all
terms when $i\neq j$ disappear, so we have
$$\biggl(\sum_{\{i\}}(\alpha_{i},\Psi)\alpha_{i},\sum_{\{j\}}(\alpha_{j},\Psi)\alpha_{j}\biggr)=\sum_{\{i\}}\oip{\alpha_{i}}{\alpha_{i}}^{\ast}\oip{\alpha_{i}}{\alpha_{i}}=1.$$
But then this is simply $$\sum_{\{i\}}|\oip{\alpha_{i}}{\Psi}|^2=1.$$
and our proof is complete.\
\
Thus indeed, we have the result that the square modulus components of
the discrete state vector, which is, the square modulus of the outputs
of its discrete wavefunctions, are valid probabilities in themselves of
measurements. In this way, the encapsulation component of the state
problem is much better understood: a state vector represents a physical
state, we can then transform that state vector into wavefunctions in
another bijection to the state and state vector, and in the discrete
case the modulus squared of the outputs of these wavefunctions are the
probabilities we need if we want to make predictions about
measurements.\
\
Now, we are ready to move onto time evolution.

## Exercises from Chapter 4$\ast$

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

