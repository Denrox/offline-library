# Why does path loss decrease as frequency decreases?

*Tags: antenna-theory, rf-power · score 5*

## Question

The Friis transmission equation can be given as:

```
Pr = Pt + Gt + Gr + 20 log10 (λ / 4πR)

```

Where the variables represent:

```
Pr: Power at the receiver
Pt: Power at the transmitter (in e.g. dBm)
Gt: gain of the transmission system (in decibels)
Gr: gain of the receiver
R: "radius" of signal, i.e. simply the distance between transmitter and receiver
λ: the wavelength of the signal

```

The λ term is very surprising, isn't it? It very conveniently makes the units work out, but why should the frequency of a signal affect how "rapidly" it dissipates?

I know that ionspheric and other terrestrial effects tend to make HF signals propagate farther than VHF and higher, but what accounts for this "increased range" of low frequency signals even in theoretical free space?!

## Answer (score 3, by natevw - AF7TB)

This is actually a side effect from the receiver/transmitter gain terms in the overall equation! In short, as communication frequency gets lower, the antennas must grow bigger to keep the same gain. A bigger antenna can capture more energy overall. Therefore, lower frequency signals will be "louder" at the receiver — **iff** its antenna is adjusted to compensate.

The Wikipedia article on Free-space path loss explains this frequency dependency in more detail.

In a sense, the equation has been simplified in a misleading way. More intuitively, instead of λ ending up part of the R term, the Gr term would be replaced with variables corresponding to the antenna aperture and that signal wavelength λ. In fact, one form of the Friis equation makes this clearer:

```
Pr = Pt * (At * Ar) / (r^2 * λ^2)

```

The "adding up gains" equation in the question basically re-groups this ratio (which is much more intuitively understood) into terms of decibels (which are much more practical to use).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6952/why-does-path-loss-decrease-as-frequency-decreases, by natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
