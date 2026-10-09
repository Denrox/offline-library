# What is a general procedure for aligning directional antennas?

*Tags: antenna, software-defined-radio, microwave · score 5*

## Question

I want to establish a microwave link (1.2GHz) between two stations using antennas with a directional radiation pattern. The stations have a clear line of sight to each other. Each antenna is attached to a half-duplex transceiver operating at relatively low power.

If the antennas are too far apart to align "by eye", what's a good procedure to use that is applicable in general for aligning this type of antenna system? I want to align the antennas for best reception (maximum signal intensity, low error rate) at each station when the other transmits.

Assume there is a licensed operator present at each station who can manually operate the transceivers, and that the operators can communicate with each other in real time (with cell phones). Additionally, the transceivers are software-defined radio devices, so it is very easy to get FFT/waterfall displays from them, as well as test with non-standard signals. However, a procedure that uses a common modulation scheme to align (e.g. narrowband FM voice) would be preferred.

## Accepted answer (score 5, by user)

**Use a map and a compass.**

Really. It doesn't have to be more involved than that. As long as we are talking about line of sight propagation, that should be close enough to get you well within the ballpark unless this is about *hugely* directional antennas (as in, beam widths of perhaps 10° or narrower in the horizontal plane), and even if that's the case, it gets you a start.

Pull out a map (it can be digital or paper-based), mark the two antenna locations, and determine the magnetic bearing between them. For what can be reliably achieved on UHF, I'd probably just use a straight ruler and not worry about things like great circle propagation. Then, bring a compass to each location and aim the antennas in roughly the correct direction: as good as you can, but not fretting over half a degree. Make a test transmission, note the signal strength, adjust one of the antennas by some reasonable fraction of the beam width in either direction, try it again, rinse and repeat until you hit peak signal strength. Mark the exact antenna direction somehow in case someone bumps it, go back in and have a cup of your hot beverage of choice.

If you want to save time and the remote station can transmit continuously, after doing the coarse general-direction aiming you can even simply have the remote station transmit (using a fixed-power fixed-frequency mode; I would suggest a continuous carrier in CW mode, technically N0N) then gradually aim for the strongest received signal. When you are done, switch roles such that the receiving station becomes the transmitting station, and perform the process all over again. All you would need for that is a reliable means of measuring the received signal strength to sufficient precision.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2181/what-is-a-general-procedure-for-aligning-directional-antennas, by mtrberzi, user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
