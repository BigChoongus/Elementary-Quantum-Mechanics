---
layout: default
title: Chapter 1
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


# Exoskeleton

## Preface

The sudden, explosive rise of quantum physics is probably both one of
the most significant events in human intellectual history. Born in the
ashes of a Newtonian model believed for two centuries to have been so
unquestionable it almost held its own divinity, and forged by a cohort
of Physicists who lopsidedly dominate the historical halls of fame in
both number and scope of achievement, quantum physics has never been
uncontentious, never obvious and never immediately complete. Yet in just
50 years, it ascended to full prominence, and its ideas, practices and
results took to centre stage. It was nothing short of a revolution.\
\
This revolution, speaking for a second from an academic point of view
past just electron spins and fundamental particles, was radical for two
main reasons. The first was that physics had to fully accept that
validity was derived from result and result alone. No matter how
offensive the theories of quantum mechanics were to human intuition, the
truth, if it lay beyond human imagination, simply lay beyond human
imagination. Common sense was discarded for practical correctness, and
the priority was achieving the results corroborated empirically even
when everything seemed wrong. This mindset is critical to any quantum
mechanics student, especially when they are starting off and unable to
grasp the nuances of quantum mechanics well enough to even fathom
debating the philosophical side of things. Indeed, it is the approach I
take in this book. When a theory can make predictions accurate to the
nearest ten billionth, as seen in quantum electrodynamics, and is not
invalidated in any obvious way, it must be at least relevant. Studying
quantum mechanics is central to science, and it will be still for quite
some time. That should and will suffice for us.\
\
Secondly, quantum mechanics was a revolution in the history of applied
mathematics. When the earliest serious formulations of quantum mechanics
came in the mid 1920's, what belied them was mathematics: and not only
mathematics, but fringe, new and diverse mathematics being unified to a
single purpose: to create a theory which could explain the unexplainable
results Physicists were obtaining at the time. The genius of Dirac,
Heisenberg, Born and other founders was that they could draw from a
purely abstract discipline and stamp it onto the real, physical world.
Mathematics running physics has always been a well-understood fact, but
the level we are are working at will be wholly new to the reader. Even a
surface incursion into quantum mechanics will start reaching towards the
deepest vestiges of mathematics in all corners.\
\
This will all present a stiff challenge to the reader, if this is the
first time they have handled any theory of this level of complexity. In
this sea of randomly drawn abstractions and deeply anti-human results,
confusion becomes a very serious threat to the learner. It is
extraordinarily easy in quantum mechanics to read 400 pages of textbook
and still have absolutely no clue what a state vector/ wavefunction --
the first central mathematical object in quantum mechanics -- really is.
Quantum mechanics is a famous sinkhole for people trying to be more
intelligent than they are capable of understanding, but even that cannot
be chalked up solely to outsiders who have never studied the subject
before. Assuming one can learn quantum mechanics as one might learn
differential equations -- crunching problems and becoming an expert
through practising the mathematics -- is naive. There are rules to
learn, and concepts to understand; and therefore rules and concepts to
fail to understand regardless of how well one might feel they follow the
proofs.\
\
Thus the aim of this book is to avoid confusion at all costs, and to be
pragmatic. Most, if not all, of quantum mechanics textbooks work on the
basis that students reading those textbooks are propped up by a rigorous
undergraduate trimester and experienced professors explaining the
nuances in lectures and seminars and even practical experiments while
working with the same textbook. Self-learning quantum mechanics from
such books is dangerous, because they are far too brief on explanation
in their bid to prioritise swathes of algebra and computations, assuming
experienced professors will do the rest for their usual readers. It is
by no means impossible, especially for those trained in undergraduate
mathematics, but it is likely ill-advised for the rest of self-learners
to jump straight into quantum mechanics via books like those.
Conversely, to those for which all the mathematics here comes in the
blink of an eye, or who have finished studying a quantum mechanics
textbook or course already, this book will comparatively less useful,
because it involves very detailed and explicit proofs and explanations
which are optimised for those learning quantum mechanics completely from
the book, rather then those looking for a reference textbook.\
\
In the end, this book is but a stepping stone. A stepping stone which I
believe is critical for a new student, to set principles in order before
entering the true deep end, but also a stepping stone which is written
to be a stepping stone. This book won't give you everything, but, simply
by painstakingly avoiding a whole lot of bad, I hope it can give a
self-learning student new to quantum mechanics a whole lot of good.\
\
You of course, shall be the judge of that.\
\
Han-Sen Choong

## A Physical Model

One of the most difficult things in starting to learn quantum mechanics
is that it can be very difficult to tell between concrete rules (of
reality), chosen assumptions and mathematical logic. It is my belief
that a new student of quantum mechanics must be able to distinguish
between these as early as possible, because otherwise there are dangers
of confusions where one questions assumptions as if they are concrete
logical consequences when in the very first place they cannot be subject
to such inspection. Thus, I think, it is useful to understand quantum
mechanics as a discipline before delving into its details so that there
is at all times in our learning of quantum mechanics this awareness of
why exactly its components are arranged as they are. So let us begin
with a question. What is the difference between quantum mechanics and
quantum physics?\
\
The question may have been in the mind of the reader with the loose
treatment of both terms in the Preface, and indeed if they have heard
both terms elsewhere without knowing their distinction. In fact, the
term is will soon become extinct in the rest of this book, because the
book is a quantum mechanics textbook-- not a quantum physics textbook.
The difference is uncontentious; every classification would put quantum
mechanics as *the rules* and quantum physics as *the application*. The
latter is more advanced and difficult, but it is also wholly predicated
on the former.\
\
Quantum mechanics, easiest thought of then as the pure mathematical
component to the study of quantum phenomena (sans experimentation), is
what we call a **model**. Specifically, quantum mechanics is a model of
physical reality, and thus we might refer to it as a physical model.
However, it is the rationale of modelling which is a key characteristic
of quantum mechanics as an academic discipline. In modelling, we take a
situation where we have some computation or prediction we want to make,
and we take the tools we have available to us from mathematics to create
a system which is to make such predictions without any additional
predictions which conflict with our desired subject. We choose the rules
of our model based on what makes sense -- one would never model the
probability of a train arriving $x$ minutes late with an exponential,
for example, because the probability of a train arriving 100 minutes
late should not be exponentially greater than it arriving 10 minutes
late. How perfect are our rules? That would depend on the purpose of the
prediction we are trying to make. In the situation of a train's arrival
time, knowing the train has a probability 0.498263 of arriving at a
specific time is no more useful than knowing it has 50% probability,
rounded to the nearest percentage point. In quantum mechanics, on such
microscopic scales, we would like to be as accurate as possible, but yet
our greater priority is making sure there are no glaring discrepancies
between predictions made by the quantum model and physical experimental
results. This latter condition of being true to real world experimental
results is clearly prerequisite for any physical model, and the reason
why quantum mechanics needed to be created in the first place was
because the previously widespread model of Newtonian classical mechanics
was proven incompatible with the results of new and radical quantum
experiments.\
\
Now we can understand our task in this book as engaging with the model
of quantum mechanics. Such consists of working with and understanding
the rules the original Physicists creating the quantum model set out.
These rules are called the **postulates** of quantum mechanics. This
word is critical -- as it means that these rules are *assumed*, just
like any mathematical model would assume rules and be tested on how well
the resultant model fit its requirements. Thus the postulates of quantum
mechanics are fundamentally different to other the reader might have
come across in earlier mathematical studies. Those rules -- like the
Pythagoras theorem -- are hard and concrete, and arise *logically* from
the definitions of a right-angled triangle, and side length. These
rules, the quantum mechanical postulates, are *assumed* rules by which
we choose to abide! The difference is of course critical. Pythagoras'
Theorem is not an assumption: it drops out of a construction we hold to
be true. These quantum mechanical rules, however, don't drop out of
logic. They were chosen, by the founders of quantum mechanics, to
predict reality, and they were kept mainly because they worked.\
\
Now we return to the ideas of the Preface. In all modelling, the rules
we assume are simply validated by the results of the predictions of the
model compared to the results obtained in that which we are modelling.
If the model is accurate and performs its functions well, we can then
trust its rules are at least reasonably sound, and that studying that
model is useful and relevant. This is the story of quantum mechanics,
which is indeed the most successful mathematical model ever created. The
Postulates we will be learning, in this book about quantum mechanics,
are what define this quantum model we will be working with.\
\
Now, it is useful to undergo an understanding of what physical
modelling-- in many ways, essentially no different to theoretical
physics-- really aims to do, because most students will not have learnt
this explicitly before. Physical modelling (physics) has two aims--
problems to answer:

1.  The State Problem

2.  The Time-Evolution Problem

If a physical model can fully answer both these problems, then it is
considered complete.

### The State Problem {#the-state-problem .unnumbered}

The state problem concerns our ability to describe any state at any
given time. It is therefore a problem of description, encapsulation and
extraction.\
\
Description is the most obvious criterion in the solution of the state
problem. It pertains to our ability to observe a state and be able to
put it down into description-- usually, mathematical description. It is
only after this that we can bring anything successful to practical
experiment, as there is no point trying to find data on states if there
is no standard system whereby states can be distinguished and results
can be recorded down.\
\
Linked with that description component problem, then, is the extraction
problem, which is another key component of the state problem. If we have
some state we have observed, and we have recorded its information down
as some solution to the problem of description, we have gone from an
observation to an abstract representation. However, we also want to be
able to take an abstract representation and be able to at least imagine
or compute the characteristics of the physical state it represents.
Consider a situation, for example, where we can isolate air molecules
and work out their speed in a simulation, and we decide to colour any
air molecule with velocity above 550m/s red in our simulation, all air
molecules with measured velocity 525-550m/s yellow, and all below 525m/s
blue. That would be an attempt to tackle the description component of
the state problem. However, it would also clearly be incomplete as a
model of reality. The reason for that is simple: given a physical state
(specifically, an air molecule having a certain velocity), we can
certainly describe it using our colouring system. However, given a
certain colour, we cannot at all work out anything about its velocity,
other than how its value relates in magnitude to the value of 550m/s. In
this case, it is clear that we can describe states better than we can
extract information from a description, and it is clear this loss in
reversability of information is a problem.\
\
That example, and the final component of the state problem in
encapsulation of information, will become more important very soon. For
now, it should be very clear that the state problem is quite relevant,
not always straightforward (especially after the groundbreaking results
of the Stern Gerlach experiment we are about to study) and deserving of
a place as one of the two most important problems in Physics.

### Time Evolution and Observables {#time-evolution-and-observables .unnumbered}

The definition of the time-evolution problem is luckily much easier.
Given a particular state, we want to be able to calculate how that state
will evolve in a certain period of time into a new state (subject
perhaps to time-evolving external conditions). This is the physics
problem all readers will be familiar with: whether it be through
acceleration-time graphs or via other common time-based experiments.\
\
Such time-evolution is usually governed by an equation. In quantum
mechanics, this is, as we will discover in Chapter 5, the widely famous
Schrödinger Equation. Equally, we note that a time-evolution equation
clearly creates a greater onus on the results of the state problem in
our model to be mathematical objects, so that these can actually be run
through the equations we have.

We here have built an understanding of the central aims our physical
model needs to meet, and in framing this beforehad, such discussions
should no longer seem to come out of nowhere when we reach them by
Chapter 3.

## A Structure

If the reader is a student who feels high--school mathematics is
trivially within their grasp, as indeed most students who dare start
learning quantum mechanics are, you may start reading this section
immediately. If you are a high--school student and do not think you have
learnt every corner of the syllabus yet, do not worry-- move swiftly
onto Chapter 1, where a list of prerequisite mathematics is found in
reasonable detail. As described there, you should by no means deprive
yourself of a chance to get an early foothold into this significant
subject even if out of just interest, but you should also open up some
simultaneous study of those areas listed using textbooks written to
present those areas, rather than trusting 20 bullet-pointed pages of a
quantum mechanics textbook to teach you those crucial foundational
concepts.\
\
Now, this section will present an insight into how this book will set
about accomplishing its task of providing a pragmatic entry into quantum
mechanics which avoids chronic confusions, building off the Preface.\
\
The first thing to make clear is that this is a mathematics textbook.
Certainly, it is a lot more verbose than a traditional mathematics
textbook, because I prioritise, as I have already stated, an
understanding of the principles over the cleanliness of logical
arguments. However, none of the mathematics here is watered-down,
inaccurate or simplified. By the time we move to Chapter 3, this will
become rapidly clear, and by the time we reach Chapter 6, the
prerequisite knowledge of Chapter 1 will be all but a fond memory of the
good and easy times.\
\
The second thing to note is that there will be a notation switch in
Chapter 6. This structure is rare in quantum mechanics books: most of
the time, an author chooses one notation and sticks to it. The reason I
have chosen to set up this book with a notation switch is because I
believe the conventional quantum mechanical notation is too good to not
be learnt, but at the same time too novel and therefore distracting to
focus on right at the beginning. The reader should bear in mind that no
area in this book is wrong, and the notation shift will only introduce
new algebraic manipulations, rather than replacing or correcting ideas
covered in preceding chapters. I simply prefer that the reader struggles
a bit with some extra reformulation there than struggles with notation,
mathematics and conceptual understanding all at the same time, and in
any case the demand of that switch is as much aesthetic as anything
else, which should be acceptable.\
\
The book can be split into two constituent parts, therefore: before and
after Chapter 6. Chapter 2 starts by providing motivation for the
developments of quantum mechanics with the exemplifying Stern Gerlach
experiment, and will be critical in laying out the new physical results
which had to be accounted for. Chapter 3, 4 and 5 (quantum states,
quantum observables and time-evolution respectively) lay out the quantum
mechanical model and its rules with detailed study of subsequent
implications both physically and algebraically.\
\
The second part of this book can be characterised by the remaining
chapters, which treat the mathematics more seriously and vigorously than
the first part of the book. It will take the model we built in Chapters
3, 4 and 5, and recodify it in a way which allows us to understand the
algebraic manipulations accessible to us in a more lucid and detailed
manner. Finally, after doing all these things, the reader will be ready
to move onto physical problems for the first time, and with some
practice, will meet the end of the content of this book in Chapters 8
and 9. The closing problem will be the solution of the hydrogen atom,
and we will witness a number -- and a perfectly accurate number at that
-- drop out of the quantum mechanical model for the energy levels of
hydrogen, which, astonishingly, is corroborated by empirical evidence.
That should provide a satisfying conclusion to the journey of starting
off with quantum mechanics, before the final chapter, Ad Infinitum, has
been included as a conclusion to the book which I believe best sets a
student on a path moving onwards from this text to learn more advanced
quantum mechanics. Hopefully the reader will be in very robust shape
after all is said and done to press onto more advanced textbooks when
their mathematics allows it, and then I will have successfully completed
my task in writing this pragmatic exposition.



