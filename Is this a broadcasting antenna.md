# Is this a broadcasting antenna?

*Tags: antenna · score 8*

## Question

We bought an old house and found an antenna inside the attic of the house. I don't know much about antennas or radio but searching in Google I found a similarly shaped one and it describes it as a broadcasting one. Is that what this antenna is? If so, can it be used to receive my local TV signal instead? If not, does an antenna like this have any value?

## Answer (score 13, by Glenn W9IQ)

It appears to be a "vertical" CB ground plane antenna that had been mounted or stored in a horizontal orientation. It is not suitable for effective TV or FM reception.

It is also noteworthy that one of its three ground plane elements is missing in the picture. It likely that it had to be removed to place the antenna into that location.

## Answer (score 9, by Kevin Reid AG6YO)

#### What you've got

First, a small point of terminology: the question you want to ask is whether it is a *transmitting* antenna, not *broadcasting.* Broadcasting has a formal definition which (in the US) is "Transmissions intended for reception by the general public". We like to be precise about this because we are *not allowed to broadcast.*

That does look like it might be a radio amateur's antenna. In fact, it looks like an antenna that was intended to be installed vertically that was hung sideways from the rafters instead (note the three-way symmetry of the metal plate but with one rod missing).

It's not likely to be *particularly good* for TV reception, because it is too large. An antenna that is much larger than the wavelength of the signal it is being used to receive will

- have a very unpredictable pattern — which directions it is good or bad at at receiving signals from, and
- pick up more irrelevant signals on lower frequencies (longer wavelengths). The receiver can ignore them, but there's always a limit.

There will also be an *impedance mismatch* due to the antenna not being intended for TV bands and being designed for a different impedance. But impedance mismatches don't matter too much for receiving — at worst it doesn't work.

#### Course of action

If your primary goal is to get good TV reception, then your best course of action is to install a completely separate TV antenna in your attic — or even better, on top of your roof — and possibly reuse the *path* of the existing coax to run a standard 75 Ω TV coax line.

If you think it'll be a fun project to try to use the antenna for your TV and don't mind spending a two-digit amount of money on the experiment, then it's worth hooking it up to see what happens. (Your TV, or your FM radio, or shortwave (international) radio if you are interested in that.)

Even a bad antenna that's on top of the house may be better than a good one installed lower down. In general cases, you're not going to hurt a receiver by trying out an antenna with it.

#### Hooking it up

Broadly, all you need to do is follow the coaxial cable down to wherever it ends, and hook it up.

However, you will most likely need an adapter, because the connector on the end of the cable will not be a TV-coax "F" connector. Most likely, it will be a "UHF"/"PL-259" connector, or an "N" connector. You can find an adapter from either of those, or any other common RF connector, to a "F" type connector which is the kind used for TV antennas and cable TV; it will cost a few dollars.

(The reason I say that it won't be an "F" connector is because amateurs *most often* don't use "F" connectors, and because the coax is too thick for a standard "F" connector — besides eyeballing the size, I also faintly see it is marked "RG 8/U" on the part running across the top of the photo.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11688/is-this-a-broadcasting-antenna, by Wilreyca, Glenn W9IQ, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
