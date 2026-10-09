# How effectively do modern transmitters protect against high SWR?

*Tags: impedance-matching, amplifier, equipment-protection · score 10*

## Question

The following are fairly common knowledge:

1. Transmitting at full power with too much of an impedance mismatch can damage your finals.
2. If we do so inadvertently, modern radios drop the power significantly for self-protection.

Yet, it's still very common to hear people suggesting that high SWR risks damaging your transmitter. How much of an issue is this with modern radios? Do we really still need to be concerned about damaging our finals, or is it outdated advice that refuses to die?

In the extreme case, can we freely transmit at (attempted) full-power into an empty jack without shortening the lifetime of the finals?

## Accepted answer (score 2, by webmarc)

I believe the answer currently is: yes it matters less, but it still matters.

Variables include 1) the mode of operation and 2) the speed of the foldback circuit in the radio that provides the trigger for power reduction on a bad match.

While modern transceivers all seem to have a foldback circuit to limit potential damage (for ex, see ic7300 operator manual page 13-4, "The transceiver has a 2 step protection function to protect the final power amplifiers in case the antenna SWR becomes high."), they depend on measuring the reflected power which means it's already inside the radio by the time the circuit can respond.

If operating SSB, that may not be much of a problem since the modulated signal is likely not at full power (probably MUCH less) and doesn't give much opportunity to build-up heat before the foldback kicks in.

If operating CW/digital/any instantaneously full-duty cycle mode, then there is more opportunity for maximized power reflection back into the PA before foldback kicks in... depending on component tolerances, radios from the same manufacturer may even have different foldback activation speed. At least SOME power will make it back to the PA, which are running at full power already... this is not ideal.

So a scenario that I could envision is running a digital mode at high power on a band that the PAs are matched to, heating them up already, then moving to another band with high SWR. Now I've got pre-heated PAs, running at full duty, plus need to dissipate whatever large reflected power is... could be a life-shortener if not a blowout event.

So in short, while not NEARLY as critical as back in the day, it's still important.

I also recognize that this answer is VERY light on referenced material, and ENCOURAGE others to augment this answer (or provide a more robust additional) as they see fit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17661/how-effectively-do-modern-transmitters-protect-against-high-swr, by Dominick Pastore, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
