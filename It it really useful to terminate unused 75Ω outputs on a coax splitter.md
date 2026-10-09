# It it really useful to terminate unused 75Ω outputs on a coax splitter?

*Tags: uhf, coaxial-cable · score 8*

## Question

When discussing improvements to my home HDTV Antenna/distribution system a colleague brought up the need to terminate all coax, even unused splitter ports.

My understanding of the way terminator works is that they prevent wave reflection, which can cause ghosting in analog signals and in my case - digital HDTV - noise. However for the reflection to introduce noise I assume you need some cable length, so that the reflected signal is actually offset from the main one.

In the case of a splitter the length is very short - limited to the splitter's own wiring. Would that still be enough to cause noise? If not, could it even have the inverse effect of preventing an in-phase reflection from actually boosting the signal's strength to used ports?

## Accepted answer (score 11, by Phil Frost - W8II)

Terminating unused ports will never make things worse, and indeed is necessary to provide "ideal" behavior. Is ideal behavior really necessary? It depends on the application. Is your setup working now? If so, terminators aren't necessary :-)

A typical splitter has these properties:

- It has an input port and two output ports, which we'll call A and B.
- It has high *isolation*, meaning power going into one output port doesn't show up at the other output port.
- It is *matched*, meaning the impedance looking in to any port is the same (usually one of 75 or 50 ohms).
- It is *reciprocal*, meaning it works in either direction: it can also be used as a *combiner*.

This sounds like nothing could go wrong: since the outputs are isolated then leaving one of them unterminated couldn't cause problems with the other output.

However, when the port is left open, it reflects *all* the power, and then you have to consider how that affects the other components. Even though the ports may be labeled "output", they are still inputs because the splitter is reciprocal. Power reflected from an output port is an input that must be considered.

For example, say 1 W enters the input port. One output is connected to a TV, which we assume is properly terminated internally. The other port is left open. (In practice the power is orders of magnitude less: I want to keep the numbers simple.)

What happens:

1. 1 W enters the input.
2. The splitter divides that power evenly between the outputs. So 0.5 W comes out of each output.
3. On port A, that power is converted to heat in the TV and we don't need to worry about it anymore.
4. On port B, there's nowhere for the power to go so it's reflected. Now it's an input on "output B". Although it's called an "output", because the splitter is a *reciprocal* device, it works an an input, too.
5. Half of the reflected power is lost as heat in the splitter.
6. The other half is sent out the "input" port.
7. Depends on what's attached to the input port!

If the input port is also 75 ohms, the reflected power is absorbed there, and we don't ever see it again. This reflected power means the source does not "see" 75 ohms, however that's unlikely to be an issue in practice for a TV system.

But if the input port isn't 75 ohms, the reflected power gets re-reflected and is sent another time into the input port. Now you have the opportunity for ghosting.

However in most cases, a number of factors combine to make this not that big of a deal.

1. The source may not be 75 ohms, but it's not usually that far off. So the source does end up absorbing a significant fraction of the reflected power.
2. The real world is already full of reflections. If the source is an antenna, it already contains time-shifted "ghosts" from the signal finding its way to you by multiple paths of differing length. An HDTV receiver employs *channel equalization* to compensate for this to some extent.

## Answer (score 5, by Kevin Reid AG6YO)

Lack of termination is a particular case of impedance mismatch. An impedance mismatch on one port of a power divider ("coax splitter") means that the common port of the divider itself will not present the the intended impedance to the incoming signal.

(From a circuit analysis perspective, this is the same thing as a lumped-component network of some sort that has the wrong impedance on its ports for the pair of transmission lines attached to it. No lengths of unterminated line are necessary.)

This mismatch will cause reflections which propagate backwards along the line. What happens after that depends on the electrical characteristics of the next thing-that-is-not-a-transmission-line the reflection hits, but a simple case is if there is another similar mismatch in the line, which will produce the second (forward) reflection called ghosting, the time between reflection depending on the length of line between those two defects.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12023/it-it-really-useful-to-terminate-unused-75o-outputs-on-a-coax-splitter, by Thomas Guyot-Sionnest, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
