# SWR of 1.5 -- use internal antenna tuner or not?

*Tags: impedance-matching, antenna-tuner, icom-ic-7300 · score 3*

## Question

My IC-7300 has an internal antenna tuner that can handle a SWR of up to 3:1.

The other day I noticed that a frequency I was transmitting on (the 40m FT8 frequency FWIW) has an SWR of 1.5 (was my first time running FT8 on 40 meters). I expected that because the antenna itself is tuned for best 40m SWR in the phone region, which I use more often.

If I turn on the IC-7300's antenna tuner it can, unsurprisingly, knock that back to 1:1. But should I bother doing that? From what I've read, a SWR of 1.5 isn't that bad. What are the cons of using the internal tuner when I "don't have to"? And is 1.5 a "don't have to" or is that far enough from 1:1 that it's a good idea?

## Accepted answer (score 2, by Andrew)

For transmit, compared to a perfect SWR of 1:1, an SWR of 1.5:1 will give about 4 % loss of power radiated by the antenna due to reflections at the antenna / feed line junction.

All other things equal, this will result in about 0.2 dB drop in signal strength for a remote station receiving your transmissions.

Similarly, for your receive , compared to a perfect SWR of 1:1, an SWR of 1.5:1 will give about 0.2 dB loss of received signal, noting that 1 S point is equal to 6 dB of change in signal.

These losses for an SWR of 1.5:1 would normally be considered negligible and would not be noticeable.

The radio may heat up a bit more during transmit with a 1.5:1 SWR, however i imagine that all Icom radios are designed to easily handle the slight increase in temperature without problems.

In general a SWR of 1.5:1 is perfectly acceptable, and considering as already mentioned in another answer that you have to wait for the radio to re-tune every time you change frequency with the antenna tuner enabled, i would leave it off because the negligible difference it would make in this case is not worth the effort.

## Answer (score 2, by user10489)

If it is convenient to reduce the swr by fixing the antenna, that would be a more effective solution. But, as you say, 1.5 is not that bad, and likely you would like to continue using the antenna in the phone region anyway.

So is it better to run it at 1.5 or engage the tuner? It is probably easier on the radio to use the tuner. The disadvantage of the tuner it that it decreases efficiency slightly. But with the swr fixed by the tuner, the radio may be able to put out a higher power without overheating, which should more than make up for the efficiency loss.

The antenna likely will not radiate as well with the tuner as it would without the tuner if it had 1:1 swr, but it is better to have the tuner heat up than the radio's finals, so I would run with the tuner. The only real disadvantage is that you have to wait for the tuner to match to the antenna (a one time thing each time you tune), and you are less certain how much of your power is going into the antenna. (If you know you have a 1.5 swr, you know how much is not going into the antenna. The tuner covers up the loss without removing it.)

It's really a toss up if the swr is less than 1.5.

## Answer (score 2, by Scott Earle)

If you do not use the tuner, you are getting some power (another answer here says around 4%) reflected back into the final stage of the power amplifier (PA) of the radio. This will cause the final transistor(s) to heat up, and the cooling fan will be used to remove the heat.

If you do use the tuner, you move the mismatch from the PA to the tuner circuitry, and instead of heating up the PA transistor(s) you will be heating up the tuner components. The cooling fan will be used to remove the heat.

There is a small insertion loss when using the tuner, but its components are much less sensitive to heat. If you operate in a hot environment, you want to keep as much heat away from the PA as possible, and the insertion loss is a small price to pay for that. If you operate in a cool environment, if makes little difference, as the cooling fan can remove the heat very easily.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19908/swr-of-1-5-use-internal-antenna-tuner-or-not, by QuantumMechanic, Andrew, user10489, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
