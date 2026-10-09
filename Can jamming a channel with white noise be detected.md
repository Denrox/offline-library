# Can jamming a channel with white noise be detected?

*Tags: rfi · score 3*

## Question

If somebody were to setup a pirate radio signal that was broadcasting static would the people tuned in to that frequency be able to tell?

Assuming that there was nothing already on that frequency what kind of equipment would one need to be able to tell that this static was being broadcast and was distinct from the static that occurs in absence of any signal.

I’m assuming that if people tried to use that frequency and found that their signal was being jammed they would know and could triangulate.

Is there some measure of power that would come through or would the broadcast static be indistinguishable from no signal?

## Answer (score 8, by Glenn W9IQ)

The station would not really transmit static but rather white (or perhaps pink) noise. This would sound like static but as the observer tunes across the transmitter's frequency, the static would increase notably in volume (assuming amplitude modulation) and decrease again as the transmitting bandwidth is passed. Any signal strength indicator on the receiver, such as an S meter, would also indicate the received signal. These would be clear indicators to the observer that this is not simply atmospheric static or internally generated thermal noise.

The source of the signal is easily found using standard direction finding techniques since there is still an observable signal from the transmitter.

## Answer (score 3, by Marcus Müller)

It really depends. In wireless communications, it's often the case¹ that the majority noise is actually happening **in** the receiver – which is why you'd want a low noise figure on your receiver. So, there's usually no "broadcast static" – the majority of that noise power happens *in* your receiver, not *on the air*. Many receiver architectures will increase the sensitivity if there's no strong (intended) signal in the air, leading to amplified noise, too.

In these bands, the pure presence of an increased noise floor would give away the presence of a broadband interferer.

Now, things aren't quite that easy in general: Whilst a single "non-jammer" interferer usually isn't white in spectrum as what you describe as "static" would usually be, a sufficient number of summing interferers with random properties would both be white in spectrum and gaussian in amplitude distribution, making the detection of your jammer harder.

However, receivers with multiple receive paths cannot be deceived: Your transmitter would be detectable to transmit from a single direction, and thus, if you, for example, add up the signal from two antennas with just the right phase, you could isolate your transmitter well, because they constructively add with that phase, but cancel out with other phases. That technology, both in receive and transmit direction, is called *Beamforming*, and it works with any signal (note that the receiver noises in both receive paths are independent and never add up constructively, whereas the artificial jamming signal is correlated on both antennas). It's basically a form of triangulation. You can also do the same with distributed antenna systems that coordinate their observations in a central point, so that you can do *trilateration*.

On large scale, that belongs in the category of things that you'd typically do to do radio surveillance for signal intelligence, airspace security, or cellular infrastructure coordination. So, that's broadly employed wherever there's industrialized areas.

So, if you try that, especially with high TX power, prepare for a visit from your local regulating body, asking you *very* nasty questions. It might be a criminal offense, depending on which bands you interfered with and where you are.

¹ HF, if I remember correctly, being the most prominent exception

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10006/can-jamming-a-channel-with-white-noise-be-detected, by user2193122, Glenn W9IQ, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
