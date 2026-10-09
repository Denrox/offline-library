# Do MRI machines use the ISM band, and do they generate audible CW signals?

*Tags: cw, uhf · score 4*

## Question

I've recently had an MRI, and after studying chapter two and three of the ARRL manual, I've got a better understanding of how my MRI machine might have worked.

Now, I am curious to know what would happen if I brought a transceiver within range of an MRI machine and tuned it to the frequency. Assuming it was CW, would I hear the same rise and fall of the pitch the way mentioned in this article. There was a guy by the name of Stephen Charlie, or something like that who recorded these phenomena, and in fact is another reason I want to experiment with radio.

## Accepted answer (score 6, by tomnexus)

Medical MRI looks for the nuclear magnetic resonance of hydrogen, at around 1 or 2 Tesla, at about 100 MHz. NMR is a phenomenon of the nucleus, not the atom, it is different to anything involving ions or electrons moving in a magnetic field, like aurora and the ionosphere.

Here is a table of NMR frequencies for somewhat higher magnetic field strengths.

MRI machines operate in shielded rooms, because they generate strong RF signals, perhaps 100 Watts, and they need to detect very weak signals.

Think of it as a kind of through-meat radar, but using magnetic field gradients and different frequencies to probe different parts of you, not time delay and direction.

From outside the room you might hear a pulsed RF signal, scanning over a frequency range of 10% or so as the machine probes different regions of the magnetic field.

Finally, because of the large magnets, you wouldn't be allowed to take a transceiver, phone or even a belt buckle into the room.

## Answer (score 3, by imabug)

An MRI unit used for clinical imaging will be a 1.5T or 3T magnet. Because of abundance, the receiving coils of most clinical magnets will be designed to pick up the induced RF signals from hydrogen, which has a Larmor frequency of about 42.6 MHz/T. For a 1.5T magnet, it's listening around 63.87 MHz or so. For a 3T magnet, it will be listening around 127.7 MHz.

RF shielding for MRI rooms is primarily to keep out external RF that would create artifacts in the images.

While you wouldn't be able to bring a receiver into the MRI room, outside the room would be doable. Depending on the pulse sequence being used you might hear a pattern of chirps. If anything was heard though, first thing I'd do is question the integrity of the room's RF shielding.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12673/do-mri-machines-use-the-ism-band-and-do-they-generate-audible-cw-signals, by The Harmonic Rainbow, tomnexus, imabug. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
