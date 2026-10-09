# Why a thousand miles long antenna is not needed to receive LW and MW?

*Tags: antenna · score 8*

## Question

From what I've learnt so far, the longer the wave frequency on which you want to transmit or receive, the longer the antenna needed to do so. However my portable receiver other than SW can also receive LW and MW, and is receiving those using its internal (very short!) antenna.

How is that?

How is that even possible that the short internal antenna does its work better than the much longer telescopic antenna that the radio uses for SW? (my radio automatically switches to the internal when on LW MW...)

## Answer (score 5, by Phil Frost - W8II)

A ferrite stick antenna is a kind of small loop antenna, "small" here meaning small retaliative to wavelength. These kinds of antennas can most easily be understood by electromagnetic induction:

- The loop acts as a "net" for magnetic flux.
- As the magnetic flux changes, an electromotive force (EMF) is induced in the loop.
- This force pushes the electric charges in the loop around, making a current through the loop and a voltage across the feedpoint which the receiver can detect.

This is the same operating principle behind an electric generator. However, in the case of a loop antenna the changing magnetic field comes not from a nearby moving magnet, but instead from a distant radio transmitter.

Electromagnetic induction is formally described by Faraday's law of induction. It says EMF ($\mathcal{E}$) is proportional to the rate of change of magnetic flux ($\Phi_B$).

$$ \mathcal{E} = -{{\mathrm d\Phi_B} \over \mathrm dt} $$

There are several ways we might increase the magnetic flux through the antenna, thus increasing the EMF and making it easier to build an efficient antenna.

We could make the magnetic field strength higher, by increasing the power of the transmitter or getting closer to it.

Or, we can make the loop bigger. A bigger loop captures more flux, like a bigger net.

We can also add more turns around the loop. It doesn't matter that both turns are capturing the same area of space. The EMF in each turn adds together, so an antenna with two turns captures twice the magnetic flux as an antenna with one turn of equal diameter. A ferrite stick antenna might have 60 turns, so it captures 60 times the magnetic flux as one turn would.

The last thing we can do is to stick a ferrite rod in the loop. The ferrite rod has some interesting magnetic properties that make it work.

All ordinary matter has some magnetic properties. For example, every electron is like a tiny bar magnet, or a magnetic dipole. In most matter, these magnetic dipoles are arranged in random directions, and so at macroscopic scales there are no interesting magnetic properties.

In ferromagnetic materials some of these magnetic dipoles can be reoriented. For example, if a piece of iron is placed in a strong magnetic field, then its magnetic dipoles tend to align with that field, just like a compass aligns with the Earth's magnetic field. The ability of the magnetic dipoles to align is called permeability.

When the external field is removed, some of the magnetic dipoles tend to "stick" in their orientation, and you are left with a permanent magnet. This tendency for the magnetic dipoles to stick is called coercivity.

The interesting property of the ferrite material used in a ferrite antenna is that it has low coercivity and high permeability. So their magnetic dipoles are good at aligning with an external field, but they tend not to get stuck, like a compass needle.

So when you stick a ferrite rod in the loop, whichever way the magnetic field from the transmitter is going (remember it's oscillating with the transmitter's frequency), the magnetic dipoles in the ferrite are aligned in the same direction. The fields of the magnetic dipoles add to the external field, and the result is that the magnetic flux through the loop is stronger.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5920/why-a-thousand-miles-long-antenna-is-not-needed-to-receive-lw-and-mw, by red-o-alf, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
