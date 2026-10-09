# 50Ohm Coax presents 50 Ohms of impedance on which frequency?

*Tags: coaxial-cable, impedance · score 6*

## Question

Either there's a simple answer that I'm not finding in a spec sheet somewhere, or, I'm asking the wrong question!

## Accepted answer (score 10, by Phil Frost - W8II)

For practical purposes, all frequencies.

If you cut a transmission line into infinitesimal segments, each segment can be modeled as:

($G$ is conductance, the inverse of resistance)

The characteristic impedance is:

$$ Z_0 = \sqrt{ R + j\omega L \over G+j\omega C } $$

($\omega$ is the angular frequency, two pi times the ordinary frequency in hertz)

Wikipedia has the full derivation, if you're interested.

For a lossless transmission line, the resistance and conductance are zero. So the equation simplifies:

$$ \require{cancel} \begin{align} Z_0 &= \sqrt{ 0+j\omega L \over 0+j\omega C } \\ &= \sqrt{ \cancel{j\omega} L \over \cancel{j\omega} C } \\ &= \sqrt{ L \over C } \end{align} $$

and there is no longer any frequency term.

Real transmission lines of course have some loss, but if the transmission line is any good the loss will be low, and have negligible effect on the characteristic impedance.

## Answer (score 5, by tomnexus)

The characteristic impedance of a line does change with frequency.

At high frequencies the loss components are effectively zero and $Z_0$ depends only on $L$ and $C$ (per unit length).

But at low frequencies, $R$ (and $G$) cannot be ignored and contribute significantly to the line impedance. There is a "corner frequency" where one regime takes over from the other.

Belden publishes a graph on their blog which I reproduce here:  
The site PRC68 (Archived) has a detailed derivation of the equations, which I won't transcribe here, but the summary of the examples includes these surprising figures:

- **$600\Omega$ Open Wire Lines** as seen on telephone poles, the corner frequency is 194 Hz.
- **CAT5 cable**, with two AWG24 wires twisted together, has a nominal impedance at high frequencies of about $110\Omega$. Below 100 kHz though, its impedance rises to $750\angle{-46}^\circ \Omega$ (yes, a complex $Z_0$)
- **RG-58** has a corner frequency of 36 kHz, below this its impedance rises.

See also this excellent PDF by Audio Systems Group, which shows the impedance of a $75\Omega$ coaxial cable rising to $1000\Omega$ at 1 kHz, and almost $10k\Omega$ at 1 Hz.

None of this really matters for hams! You can see the impedance of the coaxial cable is stable down to 100 kHz. It matters (used to matter) to telephone companies, running many kilometres of cable, and carrying frequencies down to 300 Hz.

**Upper frequency limit**: At even higher frequencies, the coaxial cable starts to support higher order waveguide modes, when its impedance (and loss) changes dramatically. This occurs when the cable diameter is more than $\lambda/2$, approximately.  
This effect could possibly be a problem for hams.  
On cellular phone towers, before the radios were moved to the mast top, the long run of coax introduced a significant loss. Large diameter cables are used to keep this loss as small as possible, but the cable can't go bigger than about 2 1/4" because the cut-off frequency then gets below 2 GHz, where the cable is used. High power VHF transmitters for example use much larger cable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17039/50ohm-coax-presents-50-ohms-of-impedance-on-which-frequency, by Adam Palmer, Phil Frost - W8II, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
