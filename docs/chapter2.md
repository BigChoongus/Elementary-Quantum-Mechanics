---
layout: default
title: Chapter 2
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


# The Stern Gerlach Experiment

In the Exoskeleton to this book, I presented the idea of modelling very
explicitly to the reader, because I think that a more authoritative
overview on the *procedure* of what we are trying to do is important and
often neglected by compendium-style textbooks full of algebra but not
much else. Considering this is a mathematics textbook, we have opened up
with a whole lot of words. However, this is, to my estimation, the best
way, and the result is that the reader should get a view of the subject
which will be a helpful guide throughout, before we open the algebra and
our horizons immediately become narrowed down for some time.\
\
To complete our view over quantum mechanics, then, we will now
investigate one of the radical experiments of the early 20's which
necessitated the birth of quantum mechanics to take the mantle from a
classical model which was suddenly proven woefully inadequate. I have
chosen the Stern Gerlach experiment, involving electron deflection in a
magnetic field. Other practical experiments, such as the Davisson-Germer
modification of Young's Double Slit or the Mach-Zehnder Inferometer, are
also often used as opening preludes to the quantum model, but the Stern
Gerlach experiment is amongst these the easiest-accessible exhibition of
the phenomena we will be trying to mathematically model, without much
additional Physics knowledge required. What we herein are trying to
understand is what exactly the demands-- from physical reality-- quantum
mechanics had to meet were. It is a model, and models are valuable only
based on how well they meet the demands of the predictions they need to
be capable of making. With these extraordinary experimental results,
quantum mechanics very much was given a deeply challenging and novel set
of demands, so its rules -- the Postulates -- can be said to be directly
motivated by them.\
\
Thus, understanding these motivations provides a stabilising force of
unification between the otherwise unexplainable haphazard mathematical
abstractions which will follow. The author strongly suggests
understanding Planck's (discretised) solution to the blackbody radiation
problem, Bohr's new atom model, Young's double slit experiment, De
Broglie's matter waves, and Born's radical idea of before beginning to
read this book. These need not be learned out of textbooks or with any
length or depth of study at all-- only the most superficial familiarity
with the concepts is needed-- but are very useful to have a basic grasp
of in order to understand what new issues quantum mechanics had to
address when it was conceived. We cannot cover all the above physics
experiments in any true detail, because doing so not only violates the
mathematical focus of this book-- dissipating the reader's attention
with phenomenological distractions-- but also requires far more complex
physics than can fit into this textbook.\
\
Now, then, if the reader feels introduced to the ideas of inherent
probability and superposition, we will press on with a very concrete
example to see these principles in real world practice.

## The Stern-Gerlach experiment

The idea of inherent probability has been introduced and is well covered
even by non-mathematical media on quantum mechanics. If the reader has
familiarised themselves with these background ideas of inherent
probability, we can investigate this further, and the consequences it
has on the quantum state, by turning to the Stern-Gerlach experiment.
The reason this experiment is so useful is because it allows us to focus
on a particular *observable*-- that is, something we measure in an
experiment-- which can only take two possible values. This allows
greater lucidity in how we organise a systematic investigation into the
strange quantum mechanical phenomena of probabilities.\
\
The setup deals with the magnetic properties of silver (Ag) electrons.
Specifically, we consider what happens when we pass them through a
magnetic field. What we expect is for deflection to occur; this is due
to a property of electrons, called spin, which is directly influenced by
the magnetic moment exerted on the electrons by the magnetic field. A
problem with spin is that it has no classical analogue- that is, we have
not seen any such quality with our own eyes in our macroscopic world;
indeed, the physicist Pauli describes spin as something . Nevertheless,
all the reader needs to know is that this quality determines the
different ways an electron is deflected by the magnetic field, and that
it is a measurable quality. We can reduce each electron to be considered
as a single point particle with a particular spin, by performing some
net cancellations. So we will make that assumption that the particles we
are working with in the experiment are single point particles with some
spin values.\
\
Now, after electrons are deflected by this magnetic field, they are
detected by an electron detector on the other side, which we can
visualise as a simple screen which shows where the electrons land. The
expectation classically is that there is a large patch of electrons
formed on the detector screen, bounded by the furthest deflections
achieved (and possible) during the experiment. This is because we expect
that spin is some continuous value which may differ from electron to
electron, resulting in slightly different respective deflections by the
magnetic field: thus forming in this patch on the detector screen.\
\
However, the results which are achieved are rather different. There are
only two positions at which electrons are detected after deflection on
the screen. If we proffer that this quality of spin is the only facet
which changes the deflection-- other than the magnetic field, which is
the same for every electron passing through it and constant throughout--
then this necessarily means we have observed the *quantisation* of spin:
the property of an observable having a finite set of discrete values--
here, two. There are two possible deflections, and therefore there must
be two possible spins given that nothing else is changing.\
\
In the above we could have made a subtle semantic adjustment and said: .
We will show that, while this might seem sensible to classical
intuition, it is in fact impossible for us to say this because it is
impossible for an electron to have a specific value of spin before
passing through the magnetic field! This is a dramatic statement,
because under classical intuition every object we study must have some
value for any observable at all times. We can change the momentum of a
baseball by striking it, but that doesn't mean it did not have a
momentum before we struck it and measured the result. Somehow, quantum
mechanics tells us that with spin, the electron can exhibit a certain
spin value after it passes through the magnetic field, but does not
necessarily have one before it does so. This is a prime example of
purely quantum behaviour, and was indeed why the Stern Gerlach
experiment, which strongly suggests this fact, was so seminal as one of
the experiments which necessitated the birth of quantum mechanics.\
\
To understand how the results of the experiment show us this strange
behaviour must exist, we will engage in some sort of proof by
contradiction. We will assume the opposite is true: that the electron
must have a spin value at all times, and show that the results of the
experiment lead to a contradiction if this assumption is true. By doing
this, we will thereby prove our assumption is incompatible with the
results of experiment, and that therefore the electron cannot in fact
have a spin value at all times.\
\
In our work, we will focus on the two-dimensional Stern-Gerlach
experiment. The primary dimension we focus on will be the
$y$-dimension-- or, as we will think of it, the direction. Here, the two
possible spins in our experiment are , and . More interesting things
come when we consider a second dimension, so we will use the
$x$-dimension as our secondary dimension, where the two spins are , and
. Corresponding to these dimensions there are the $y$-dimension magnetic
fields and $x$-dimension magnetic fields, which deflect electrons in
those dimensions alone.\
\
Let us now take our classical assumption on until we reach a
contradiction: we will assume that the electron must already have some
value of spin before passing through the magnetic field. Thus begins our
proof by contradiction.\
\
Let us first consider the purposes of the magnetic fields. It might seem
like they are performing a physical action on the electrons- which they
are: they are deflecting them. However, the real purpose of the magnetic
fields in this experiment is to *reveal* the spin value of electrons
which we assume they possess. By passing a single electron through the
$y$-dimension magnetic field it is either deflected down, if it had down
spin, or it is deflected up, if it had up spin. In this way, the action
is of passing an Ag electron through the magnetic field is the action of
measuring the spin it has.\
\
The second quality of the magnetic field is that it separates a group of
electrons into two new groups corresponding to the two possible spins in
its dimension. Note that it can do both of these functions at the same
time: it deflects down spin electrons down and up spin electrons up,
which both splits them into distinguishable groups, and measures
(reveals) their spin. After passing a random beam of electrons through
the magnetic field, we will get these two resulting groups split by
their initial spin: surely, a useful thing to have.\
\
If this is the case, then we expect successive $y$-dimension magnetic
fields to yield a clear result when applied to a group of electrons. The
first $y$-dimension magnet separates the group of electrons into
electrons with up spin and electrons with down spin. If we allow for
enough distance to distinguish the two separate deflections of up and
down, and place two new magnetic fields in the up deflection position
resulting for up spin electrons and the down deflection position
resulting for down spin electrons, then we therefore expect the second
line of magnetic fields to perform its measurement function.
Specifically, the second $y$-dimension magnetic field in the
up-deflected position should measure all its electrons to have up spin,
and the second $y$-dimension magnet in the down-deflection position
should measure all its electrons to have down spin. This is of course
because they have already been separated into two distinct groups and
measuring the spin of all the electrons in those distinct will only
yield one result. We did not know the spin value of the electrons before
we passed them through the first magnetic field, but after we do all our
revelations are done.\
\
This is indeed what we achieve when we do actually perform the
experiment. The first $y$-dimension magnet splits a group of electrons
into two groups corresponding to each spin, and an infinite succession
of $y$-dimension magnetic fields on each of these deflected trajectories
will continue to measure the same spin by continuing to deflect them in
the same direction. The same holds for successive $x$-dimension magnetic
fields: the first separates the electrons into two groups with left and
right spin respectively, and the subsequent magnetic fields will
continue to measure the same spins if applied successively along the two
initial trajectories obtained by the first magnet.\
\
Of course, physicists were more inspired than just applying the same
magnetic field over and over again on the same electrons. We might
wonder what would happen if we applied some sequence of $y$ and $x$
magnetic fields. Let us note that electrons passing through a magnetic
field in a certain dimension are not deflected in anyway in any other
dimension. We implicitly see this in the fact that electrons passing
through the $y$ magnetic field follow a straight trajectory with respect
to the $x$-dimension and therefore still all hit the detector screen a
certain $x$ distance away from the field.\
\
Our assumption is that an electron at all times holds a value for its
spin. We therefore also posit that an electron may at one time hold two
simultaneous properties of $x$ spin and $y$ spin, which are independent
of each other: just like a ball may have momentum and acceleration
values at the same time. We test the relationship between the $x$ and
$y$ spins of an electron: is an up spin electron more likely to be a
right spin electron, for example? Understandings like this are
physically relevant, of course- if a electron passing through magnetic
fields was more likely to be deflected right and up or left and down
then this would surely have physical implications.\
\
Suppose we isolate a certain $y$-spin and only consider electrons with
that $y$-spin: say, up spin. To do this experimentally is simple-- pass
a group of electrons through a $y$-magnetic field, give sufficient
distance for the deflected trajectories to diverge, and block the
down-deflected path so that none of those electrons can keep moving
forwards and the only ones moving forwards are the up spin electrons.
Let us suppose we did this. Then, we can investigate what happens when
we place an $x$-magnetic field in the path of the up-deflected
electrons. The point of blocking out the down-deflected electrons in
this way is to assure us we will past this point never have to deal with
down spin electrons during our considerations.\
\
The $x$-magnetic field on any ensemble of electrons will not show
considerable bias towards any spin, in fact. We obtain two new deflected
trajectories, therefore: up-left and up-right. Again, this all seems
good, until we add another $y$ magnetic field, after which a bizarre
phenomenon occurs.\
\
If we add another $y$ magnetic field to the trajectory of the up spin
electrons which we have just deflected left or right with the $x$
magnetic field, we would expect all the electrons to be deflected
upwards, since these are after all electrons with up spin. We know that
we have blocked out all the down spin electrons far back, so they cannot
escape to intervene with the results of our current experiment.\
\
Such is not the case. What we get instead is that both the up-left and
up-right ensembles of electrons have subgroups of electrons which are
deflected downwards by the new $y$ magnet! This by all means should
absolutely be impossible, given we have filtered out all the down spin
electrons already. Clearly, something is wrong.\
\
To keep track of everything following this revelation, we will use a new
notation: $\uspin$, $\dspin$, $\lspin$, $\rspin$ for different spins, as
well as two-fold notations such as $\urspin$ to record when an electron
has had its $y$ spin and $x$ spin measured. We will call this state
notation, as we are attempting to label its state-- by considering its
spin properties. The reason this is so useful is, among other things,
simply that it saves us a lot of time by avoiding having to write all
the time.\
\
This state denotation model is just some arbitrary and meaningless
labelling, so one should not carried away with its importance other than
for making things more concise. Nevertheless, let's take this state
denotation one final step further by adding scalars to the mix.
Specifically, we will use scalars to show how many electrons are in each
state for a given set. For example, we could have
$$1000\elec=500\uspin + 500\dspin.$$ That is: we have some 1000
electrons, 500 of which are up spin and 500 of which are down spin.
Similarly, we could say $$500\uspin = 250\ulspin + 250\urspin$$ or even,
$$500\uspin \implies 250\ulspin + 250\urspin + 0\dlspin + 0\drspin.$$
That is, out of some sample of 500 up spin electrons, we have measured
250 to have up left spin and 250 to have up right spin. We can use the
$\implies$ arrow to show that there is a change after we place the
electrons in a magnetic field. With this interlude we can now clearly
express what is strange about our above result again-- given our
original classical assumption-- by tracking what information was
revealed [after]{.underline} each step:

1.  Pass the electron beam through a $y$-magnetic field:
    $$1000\elec \implies 500\uspin+500\dspin$$ assuming we start with
    1000 electrons and the sample is indeed random.

2.  Block out the down-deflected channel:
    $$500\elec \implies 500\uspin+0\dspin$$ reflecting that we now have
    500 electrons since 500 down spin electrons have all been blocked
    out from the experiment.

3.  Pass the electron beam through an $x$-magnetic field:
    $$500\elec \implies500\uspin+0\dspin=250\ulspin+250\ulspin+0\dspin$$
    assuming again an equal distribution which is experimentally
    realistic.

4.  Block the left spin channel.
    $$250\elec\implies0\ulspin+ 250\urspin + 0\dspin$$

5.  Finally, pass the electron beam through a $y$-magnetic field.
    $$250\urspin\implies125\uspin+125\dspin$$

The scalars themselves are really not important at all: one needn't
think about numbers of electrons, as they are irrelevant in these
scenarios. What is relevant is what happens if we track what happens to
the $\dspin$ count between these above steps.

1.  $500\dspin$

2.  $0\dspin$

3.  $0\dspin$

4.  $0\dspin$

5.  $125\dspin$

We have followed one single trajectory! So we should not be counting
500, 0, 0, 0, 125 unless down spin electrons have materialised out of
thin air (this is impossible, rest assured). We might therefore guess
that some of the $0$ counts are false. We can consider this:

-   In step 2, we have just blocked out all the down-spin electrons. The
    0 count surely therefore must be accurate.

-   In step 3, we have just passed the electron beam through an
    $x$-magnetic field. We might offer 1 possible guess: that the
    $x$-magnetic field actually influences the $y$-spin and that it is
    here therefore that the subsequent 0 count was wrong.

-   In step 4, we blocked out all the left-spin electrons. If the 0
    count here is false, that means that either blocking out left-spin
    electrons switched the $y$-spin of some of the electrons, or that
    there already were down spin electrons by this point before we
    blocked out the left-spin electrons. If there were down spin
    electrons before step 4 was implemented then this necessarily means
    again that after step 3 the 0 count was already wrong.

So everything points to the only reasonable explanation being that the 0
count after step 3 of the $x$-magnetic field was false: and this would
only occur if the $x$-magnetic field actually flipped the $y$-spin of
some electrons. We first remember that the counter detector has only
actually measured the number of left spins and right spins after step 3,
since an $x$-magnetic field does not make any discernible
$y$-deflections. So it is certainly true that if the $x$-magnetic field
did flip some of the electron $y$-spins we would not have detected this
since it would not have manifested in a deflection.\
\
To test this one lifeline for our assumption, there is a cunning
modification to the apparatus. We recall that what we did originally was
place successive magnetic fields a relatively large distance away from
each other such that different deflected trajectories could be given
sufficient distances over which to diverge from each other and therefore
be discernibly different according to the measurements of detectors.
This makes sense if we simply consider the fact that we are considering
magnetic deflections of electrons, which are obviously not significant
at all in scale.\
\
On the other hand, we can also well imagine that we can let both
deflected paths pass through the same magnetic field, since the angle of
deflection is small. If we try this, we continue to add to the list of
complications. We can use our step by step denotation to track things
again:

1.  Pass the electron beam through a $y$-magnetic field:
    $$1000\elec \implies500\uspin+500\dspin$$ assuming we start with
    1000 electrons and the sample is indeed random.

2.  Block out the down-deflected channel:
    $$500\elec \implies500\uspin+0\dspin$$ reflecting that we now have
    500 electrons since 500 down spin electrons have all been blocked
    out from the experiment.

3.  Pass the electron beam through an $x$-magnetic field:
    $$500\elec=500\uspin+0\dspin\implies250\ulspin+250\urspin$$ assuming
    again an equal distribution which is experimentally realistic.

4.  Pass both the up right and up left electrons through a new $y$
    magnetic field.
    $$500\elec=250\ulspin+ 250\urspin\implies 500\uspin$$

So if we compare the results of adding a new $y$ magnetic field to the
experiment (step 5 in the previous experiment and step 4 here):

-   If we remove one of the right or left channels of $x$-deflected
    electrons, then both up and down channels emerge from the
    $y$-magnetic field applied to the remaining beam.

-   If we keep both of the right and left channels, then only one $y$
    deflection emerges from the $y$-magnetic field applied to the
    remaining beam.

The above effectively cancels out any idea that the $x$-magnetic field
is flipping the $y$ spin of some of the electrons. We had guessed that
in the first experiment that the reason why down spin electrons were
appearing seemingly out of nowhere (having been blocked out, we thought,
earlier) was because the $x$-magnetic field was flipping these
electrons. If this was the case, then adding left spin electrons would
not change anything, since the spin of one electron most definitely does
not effect the spin of another. Therefore, if the $x$ field really did
flip electrons when the left spin electrons were still absent, adding
them would simply mean we still have down spin electrons (perhaps more,
since presumably some left spin electrons would be flipped too if right
spin electrons are). Yet adding these left spin electrons eliminates
rather than augments the number of down spin electrons. Since the spin
of one electron does not affect the spin of another electron, we thereby
infer our hypothesis that an $x$-magnetic field can flip a $y$ spin is
false.\
\
This now undoubtedly therefore suggests a problem with our original
assumption that an electron has pre-determined spin values, within which
there can be no explanation for certain empirically observed phenomena.
Therefore, the assumption that electrons have a spin value at all times
leads to a contradiction with empirical results and must be false.

## Remodelling the Stern Gerlach Experiment

Within the next two chapters from this one, the exact reason for our
bizarre results will become quite clear. However, the gist is already
apparent: it seems like it is impossible for an electron to have
pre-determined spin values at every point in the experiment: and that
they only have pre-determined values at some very specific points in the
experiment. We need to ensure this could be consistent with experimental
data, so let us do this.\
\
One clue comes when we repeat the exact same experiment, but with $x$,
$y$, $x$ magnetic fields rather than $y$, $x$, $y$ fields. The exact
same set of phenomena occurs, but simply with the sequence of spin
dimensions switched around to reflect the new sequence of magnetic
fields. The explanation we now proffer-- which is finally the correct
explanation-- is that we cannot know the $x$ and $y$ spins of the
electrons simultaneously. This is obviously not a classical explanation,
and is our first experience of a quantum phenomenon in action- that
there can be observables which cannot simultaneously both hold values
for a given state was certainly shocking to physicists of that time and
should be equally shocking to us.\
\
This does however, become consistent with all the phenomena we have been
getting in the experiments explained. When we have both left and right
channels going into the same magnet, out from the magnet emerges one
single channel (in our case, up). This is because, when both channels
enter the same magnetic field we can't tell which of them have left and
which of them have right spin-- and therefore we can tell afterwards
what their $y$ spin is. However, if we pass only one $x$-deflected
channel through the magnet, then we can tell what the $x$ spin of the
input electrons are by what channel we have chosen, and therefore some
are deflected down and some are deflected up-- we can no longer tell
what their $y$ spin is.\
\
The facts above, however, are presented to imply another question which
someone trying to cling onto classical common sense would reasonably
ask. It may be true that if we stand above the apparatus and only look
at detector readings we cannot tell which electrons have which spin when
we are passing all of them into the same magnetic field. However, if we
were to focus in on electrons one by one, tracking which electrons have
which spin, surely we could for example track the $x$ spins of each of
the electrons passing into the $y$ field and then each of the $y$ spins
when they come out of it: and thereby know the $x$ and $y$ spins
simultaneously?\
\
Investigating this leads us to try and repeat the experiment with as few
electrons as possible. The first thing we realise, when doing so, is
that 10 electrons and $10^8$ electrons exhibit the same types of
phenomena when we study them, though naturally the groups of electrons
are different in quantity for the two scenarios. In other words--
intensity (a measure of the number of electrons per unit area in the
beam) does not affect the experiment. Well this is good news, since that
means we can reduce to single electrons in our electron gun and once and
for all understand the phenomenon!\
\
All seems well. The first $y$ magnetic field, let's say, gives the
electron to have up spin. The second $x$ magnetic field, might give a
right spin. So we know both of the $x$ and $y$ spins simultaneously, we
think: seemingly invalidating our quantum hypothesis that we could not
do this. To confirm, we put a new $y$ magnetic field to our up-right
spin electron. And finally, we get a nasty shock, because that electron
which we measured to have up and then right spin suddenly exhibits a
downwards deflection, showing down spin.\
\
This is the probabilistic state. We have already proved that the
magnetic fields cannot flip any spins, and only reveal the spin in the
relevant dimension where the magnet is set to. Yet this electron has
exhibited up and down spin in successive measurements. This leads us to
the only possible conclusion. Our overarching point: that an electron
cannot have a spin value at all times, must be true. This would be in
line with our other quantum hypothesis that we cannot know
simultaneously the $x$ and $y$ spins. The electron *cannot* have a spin
value at all times, and this means that there are times it does not have
a fixed spin value, and in particular we now know that these times where
the spin value cannot be known at least include all the times when the
spin value in another dimension is known.\
\
Why do electrons still get deflected, if they do not have spin values?
The logical explanation is the correct one this time: an electron might
not *have* a spin value, but it can *take* a spin value. It turns out
that it takes a spin value with specific probabilities, which we will
soon learn how to calculate. So what we achieved in the first two
measurements on this single electron: an up and right spin, is simply a
result of the electron taking some measurement with some probability.
That probability (which turns out to be $\frac{1}{2}$ in our case) is
simply flipped into a new outcome when we try to measure the $y$ spin
again, and therefore we never did know the two spins simultaneously!\
\
A few things are maintained in this world of chaos, fortunately. We
recall that applying the same magnet to an electron beam over and over
again gives the same spin every time. This would not be true if for each
magnet we were simply experiencing a probability of $\frac{1}{2}$ that
it exhibits up spin and $\frac{1}{2}$ of down spin, since an infinite
sequence of magnetic fields would eventually of course invoke that
$\frac{1}{2}$ probability of the other spin to the one we are measuring
every time. This therefore proves that if we measure the spin of an
electron it *takes* a state- here, with probability $\frac{1}{2}$ of
taking an up spin state and $\frac{1}{2}$ of taking a down spin state-
and stays in this state until we force it out of that measured state
with some type of action. The example we have seen for one type of
action which takes an electron out of the original state it has taken,
shockingly, is trying to measure its $x$ spin. By measuring its $x$ spin
we force it into either a left or right state (it turns out, also with
probabilities $\frac{1}{2}$), but also revert it into an unmeasured
state with respect to its $y$ spin.\
\
This term is a clumsy denomination. Quantum physicists came up instead
with the term **superposition** of states-- literally, the idea of
different possible states being added onto each other to make a new
state. Here, the superposition is of two states (up and down in the $y$
spin, or left and right in the $x$ spin). However, if we were
considering different observables with more than two possibilities- such
as position, which has infinite possibilities- then we could have a
superposition of infinite possible states. Of course, some of these
states in the superposition might have a greater probability of being
measured than others: which is why the idea of superpositions and
inherent probability are inextricably linked when we are considering the
states of quantum systems. Through our long proof by contradiction, we
have thus established that:

-   A system may exist in a superposition of states.

-   A measurement on a system in a superposition forces it into one of
    the possible states in that superposition.

-   There is some probability associated with forcing that superposition
    into one of the constituent states.

-   There are certain observables, like $x$ and $y$ spin, which get in
    each other's ways when one tries to force a system out of the
    respective superpositions.

By the end of the next three chapters, the reason for these things will
all be clear.

## Conclusion

This chapter is actually more of a pedagogical exercise than a strict
reportage of phenomena. That is why we kept offering false hypotheses
instead of the correct answer from the start. The point is that the
reader should get a feeling of classical mechanics and their own
intuition starting to fail, and the logical links we must make to try
and offer explanations for these strange quantum phenomena. The contents
of this chapter will, for the most part, be swept under the rug, but the
ideas it has introduced to the reader will on the other hand be central.
The most important two ideas, which the reader must remember, especially
for the next chapter? Superposition of states, and inherent
probabilities.\
\
These will provide good motivation for the mathematical innovations we
see in the next chapter, which will begin our journey of quantum
mechanics formally.

{% endraw %}

{% endraw %}
