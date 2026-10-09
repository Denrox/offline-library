# Effect of night on VHF/UHF propagation

*Tags: propagation, vhf, uhf · score 6*

## Question

I have had some conflicting experiences relating to the effect of night time (ionosphere, temperature, etc.) on propagation. Perhaps it is related to the frequency of what I was working with.

Several years ago I troubleshot a Wi-Fi network in the desert. Every night at a variable time (but early on in the night, say 10PM) the network would go down. I fixed this problem by using directional antennas. This was a ~2.45 GHz system. So it seems the received power, or at least SNR, decreased with night. One person I asked about it thought that it was due to increased noise (due to reflection of many other signals off the ionosphere at night).

Last night I looked at a broadcast FM station. The power was pretty high. I just checked it out again during the day and the receive power was at least 5 dB less. This was ~85 MHz.

So there are conflicting results. One signal propagates better at night, another worse.

**Question:** What things affect VHF/UHF signal propagation at night?

## Accepted answer (score 4, by billy)

When we have a large temperature spread here (day/night) I start looking for new repeaters on vhf/uhf. The gradient will usually form a temperature inversion that is pretty efficient at scattering radio signals, sometimes in very pronounced ways. Before digital tv it wasn't uncommon to be watching a station and have another 100's of miles away completely take over the channel (with digital tv you just get a blank screen). It's called tropospheric ducting, and could have been your culprit seeing as how temperatures differ quite a bit in an environment like the desert. In your case it could have brought in noise from other distant wifi transmitters that blocked the signals you were trying to receive, and then disappeared when the inversions went away.

Moisture can also affect (attenuate) frequencies in the GHz so that may have been an issue between sites. When you installed directional antennas you boosted the SNR by focusing all of your RF towards the desired receiver.

Ionospheric propagation at night doesn't typically work for any freq over about 10mhz so that is most likely not your issue. It's fascinating stuff to learn about!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2337/effect-of-night-on-vhf-uhf-propagation, by Ken - Enough about Monica, billy. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
