# Help understanding transmission loss of trivial circuit

*Tags: diy, uhf, filter · score 3*

## Question

I was trying to DIY a VHF/UHF diplexer, and got some weird readings from the VNA.  
By debugging I reached this trivial circuit:  
Which has the following frequency response:  
I'm trying to figure out where the parasitic elements come from and why they are of such magnitude that I get -9dB in UHF. Any help or pointers would be awesome.

EDIT: To be more precise, I've calculated the stray inductance at around 60nH and capacitance at less than 1pF for this specific scenario (wire above ground plane). What makes me uncomfortable is that the simulated cutoff is earlier and less aggressive than what I measure.

## Accepted answer (score 3, by tomnexus)

Your measurement looks about right. I think your circuit looks like a loop antenna, of about 20 cm in circumference, so it will start to radiate well when the wavelength gets below ~ 80 cm, about 400 MHz.

The loss you see is radiation - the circuit/antenna is radiating the signal into space, not absorbing it.

Stray inductance calculations don't work when the circuit is a good fraction of a wavelength, but if you like, 60 nH is 170 $\Omega$ at 450 MHz, which is a lot more than 50 $\Omega$.

For a circuit to work at UHF, keep the wire lengths shorter than 1 or 2 cm, or better, use 50 ohm track on the circuit board. For starters, solder the SMA connectors directly to the board. You could place them on edge, or better, use a single sided board, and solder them flat on to the copper side, with their pins sticking through, ready for inventing your circuit on the clean side.

Here's a picture of a good looking DIY UHF construction method (from here)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15317/help-understanding-transmission-loss-of-trivial-circuit, by Rimio, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
