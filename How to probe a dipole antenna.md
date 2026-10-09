# How to probe a dipole antenna?

*Tags: wire-antenna, measurement · score 3*

## Question

I want to start experimenting and tinkering with antennas, starting with ½ wave dipoles. I will be measuring the AC voltages on both the transmitter and the reciever antennas simultaneously. And by changing the distance between them, I will observe the phase angle and delay time (of the EM waves) between them.

As I started planning with no practical experience, I stumbled at each step.

I found this calibrated signal generator (https://www.rf-consultant.com/calibrated-signal-generator/) and Rigol DS1102E so that I will be able to work with 100 MHz. I know the scope is rated for 100 MHz but after reading this thread (https://hackaday.io/project/4327-stretching-the-limits-of-a-rigol-ds-1102e-scope), I was convinced that it could work well even at higher frequencies (only if we are measuring with one channel).

First problem is how to connect the transmitter antenna to the signal generator. I will use a 50 ohm coax cable of small length. Since the waveform and directivity is not critical, could I get away without adding a balun? Or would there be a risk of damaging the signal generator with signal reflections (it has 50 ohms and +10 dBm (0.01 Watts) output) ?

If no baluns is ok, I will simply split the coax inner wire and braid apart into a dipole antenna. Soldering would maybe introduce abrupt impedance changes.

Second and biggest problem is how to probe the antennas to see the voltage waveforms? Could I attach the probe directly on the transmitting antenna center? While measuring on the reciever antenna, could I attach the probe on the other end of the coax cable (because the probe cables could fall short of the distance between the antennas while making simultaneous measurements) ?

If I attach the probe to the inner wire of the coax, should I attach the ground clip to the braid? Or at 100MHz should I completely remove the ground clip to eliminate the inductive coupling of the “ground clip-antenna-probe” loop (see under the title “Beware using ground clips...” in http://www.radio-electronics.com/info/t_and_m/oscilloscope/using-oscilloscope-scope.php)? Or should I probe like this (http://www.gorferay.com/pic/Mifare_4k_1_49.jpg)?

## Accepted answer (score 5, by Kevin Reid AG6YO)

First problem is how to connect the transmitter antenna to the signal generator. I will use a 50 ohm coax cable of small length. Since the waveform and directivity is not critical, could I get away without adding a balun? Or would there be a risk of damaging the signal generator with signal reflections (it has 50 ohms and +10 dBm (0.01 Watts) output) ?

A good signal generator should tolerate any impedance at all at its output (including a short circuit).

But you should still use a balun in your antenna design, because if you construct a dipole without a balun, then the feed line will act as an antenna element (along with all of the grounded chassis metal of your signal generator, and so on). This means that you will not be measuring the antenna design you think you are.

A balun for a dipole prevents this unwanted RF current, so that the antenna's behavior is independent of how it is connected (though the path of the part of the feed line near to the antenna still matters — just as does any nearby object). The same thing applies in reverse to a receiving antenna; both need baluns to be predictable.

Also note that the feed point impedance of a dipole is not (usually) 50 Ω, so you will have some reflections from the transmit antenna no matter what unless you use a suitable matching network at the feed point (which would usually be combined with the balun).

Second and biggest problem is how to probe the antennas to see the voltage waveforms? Could I attach the probe directly on the transmitting antenna center?

If you do this you must do it on the unbalanced (coax, not antenna) side of the balun, otherwise the probe cable ground will upset the balance and radiate as I mentioned above.

While measuring on the reciever antenna, could I attach the probe on the other end of the coax cable (because the probe cables could fall short of the distance between the antennas while making simultaneous measurements) ?

Yes, you can. The normal sort of operation would be to connect the feed line coax to the oscilloscope input, without using an oscilloscope probe. You must include a 50 Ω load (‘terminator’) *at the oscilloscope's end of the cable,* either:

- a BNC tee and a terminator (which looks like a BNC male connector with a metal cap instead of a cable attached),
- a feed-through terminator (typically more expensive; has a BNC male and female connector), or
- an internal 50 Ω load provided by your oscilloscope (not a feature of your Rigol DS1102E).

This will ensure there are no reflections, and you are making a realistic measurement. (Remember that ideally the antenna should also be matched to the cable's 50 Ω. If it is not, there will still not be reflections, but the received signal will not be as strong as in the matched condition — in exactly the same way as any receiver's antenna input of the same impedance.)

Alternatively, you could use the probe and a regular resistor as the load at the antenna's feed point; that would be awkward in general compared to using proper coax parts but might be easier to get started with the components you have on hand to set up an experiment.

If I attach the probe to the inner wire of the coax, should I attach the ground clip to the braid? Or at 100MHz should I completely remove the ground clip to eliminate the inductive coupling of the “ground clip-antenna-probe” loop?

If you are using an oscilloscope probe for RF, you *must* have a ground connection (removing it is the worst case), and the connection should be as *short and parallel* as you can manage (least loop area).

As I mentioned above, the best option is to skip the probe and use a matched load. This is what you should do for your receiving antenna.

For your transmit antenna, if your balun has conveniently exposed wires you can hook onto them, but consider using a shorter ground lead to minimize the loop area — a custom bent piece of solid wire, coiled to fit snugly onto the shield around the *tip* of the probe rather than the ring farther back up the shaft where a regular ground lead attaches.

Another option is to obtain an oscilloscope-probe-to-BNC adapter (note that there are several sizes depending on your probe tip diameter) and use it together with a tee connector to tap off the signal.

Also, since you want to compare phase, don't forget to consider the length of the cables to your oscilloscope. If you use cables of the same length and the same type of coax, then you know they have the same delay; in any other case you must account for the difference.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7781/how-to-probe-a-dipole-antenna, by Xynon, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
