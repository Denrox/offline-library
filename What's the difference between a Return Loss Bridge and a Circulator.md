# What's the difference between a Return Loss Bridge and a Circulator?

*Tags: electronics, swr-meter · score 3*

## Question

From my understanding a return loss bridge basically consists of three terminals: an RF input, a DUT output and a RF output which goes to say a spectrum analyzer; I understand that the RF input signal goes to the DUT output, and any reflected power from the DUT goes to the RF output (Spectrum analyzer).

Now consider a 3 terminal circulator: signal connected to terminal 1 is allowed to go to terminal 2 but not terminal 3, signal from terminal 2 is allowed to go to terminal 3 but not terminal 1, and so on. So if I connect an RF input to terminal 1 of the circulator, a DUT to terminal 2 and a spectrum analyzer to terminal 3, isnt that the same as a return loss bridge?

## Accepted answer (score 6, by Phil Frost - W8II)

For an ideal circulator, all the power entering one port exits the next port in the rotation and no other. So all the power in port 1 exits port 2, all into port 2 exits port 3, and all into port 3 exits port 1. This is expressed by the scattering matrix:

$$ S={\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}} $$

Or a 4 port circulator:

$$ S={\begin{pmatrix}0&0&0&1\\1&0&0&0\\0&1&0&0\\0&0&1&0\end{pmatrix}} $$

A return loss bridge might be more commonly known in the amateur radio hobby as an SWR bridge. These often employ some kind of directional coupler to measure the return loss. See [How does an SWR meter really work?](How%20does%20an%20SWR%20meter%20really%20work.md)

Like a circulator, a directional coupler can discriminate between forward and reverse power, but not in the same way. An ideal directional coupler's scattering matrix:

$$ S ={\begin{pmatrix}0&\tau &\kappa &0\\\tau &0&0&\kappa \\\kappa &0&0&\tau \\0&\kappa &\tau &0\end{pmatrix}} $$

Where:

- $\tau$ is the transmission coefficient, the ratio of voltage entering the input port which exits the output port. Typically this is a number close to 1, because usually it's desirable for the directional coupler to be transparent with regard to the input and output ports.
- $\kappa$ is the coupling coefficient, the fraction of voltage entering the input port which exits the coupled port. Typically this is a small number, since the objective is to "sample" the main signal while minimally disturbing it.

Naturally the law of conservation of energy requires $\tau^2 + \kappa^2 \le 1$.

A directional coupler is a reciprocal device, so the previous descriptions but with "input port" exchanged with "output port", and "coupled port" exchanged with "isolated port" apply equally. Electrically these ports are interchangeable: it's only the labels on the box, and possibly the connectors that distinguish them.

A circulator can be used as, or as part of a duplexer, allowing one port to be used simultaneously by a receiver and a transmitter. Or by terminating one port of the circulator in a dummy load it can function as an isolator, sending all reflected power to the dummy load. In this way the transmitter will always "see" a matched load, even if the antenna is not matched. Although, the dummy load may get very hot.

A directional coupler can not do these things. Because the coupling coefficient is small (and must be, if we want a high transmission coefficient), it does [not make a good duplexer](Are%20directional%20couplers%20ever%20used%20in%20duplex%20repeater%20systems.md). Nor can it be made to function as an isolator at all, because it's a reciprocal device: if it's going to pass one power in one direction, it must do so identically in the other direction.

## Answer (score 2, by Kevin Reid AG6YO)

(Disclaimer: I only just did some research on return loss bridges, not having heard of them before. Perhaps someone else will come along with a more knowledgeable answer.)

You are right that the two devices are similar in the abstract description of their function. The differences are:


They are differently *implemented.* A circulator uses a **permanent magnetic field** to influence propagating waves to produce its directional behavior. A return loss bridge, at least all the designs I have reviewed, uses conventional electronic components.


They have different *performance characteristics.* Most notably, a circulator generally has a **much narrower bandwidth**, which is undesirable in test equipment. Several sources say that return loss bridges have high insertion loss (compared to directional couplers, which are a third type of device) as a tradeoff with bandwidth, which acceptable for measurement but not for power applications.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10099/what-s-the-difference-between-a-return-loss-bridge-and-a-circulator, by S.s., Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
