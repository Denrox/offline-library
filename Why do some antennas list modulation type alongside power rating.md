# Why do some antennas list modulation type alongside power rating?

*Tags: antenna, modes, rf-power, transmission · score 6*

## Question

Looking at HF antennas I've noticed that occasionally I'll see power ratings similar to "200W (SSB)".

Why would the modulation matter for an antenna's power output rating, and in the absence of other information how does one properly derate such an antenna for other modes?

## Accepted answer (score 7, by user)

**It's about transmission duty cycles.**

For example, FM has a very high duty cycle during transmission: the transmitter's output power is constantly at 100% regardless of the amount of modulation. AM varies between 50% (carrier only) and 100% (full modulation). SSB varies with modulation between 0% and 100%. CW is like FM, 100% power output during transmission, but the actual periods of transmission are shorter for an overall much lower duty cycle than FM. PSK31 is somewhere in between FM and CW, with a high transmit power and moderate length transmissions. And so on.

What the manufacturer is telling you is mostly **how much sustained power the antenna can tolerate.** This is a matter more of heat buildup than e.g. the risk of arcing across components.

What this means is of course also that without a specified duty cycle, the "SSB" figure is largely meaningless. If you have weak modulation, you can run the transmitter at a much higher power output setting than the 200W indicated because you really aren't pushing very much power to the antenna. Conversely, if you have a very strong modulation, it's possible that the antenna can't take the power even though you have tuned the transmitter to a lower power output, because the *actual* power being fed to the antenna is higher than the manufacturer intended.

If you know what duty cycle (in percent) the manufacturer's specifications assumes, then you can work backwards to a safe continuous power. For example, if the maximum is 200W at 60% duty cycle, then the maximum safe continuous power is in the neighborhood of 60% * 200W = 120W. If the antenna is sold for amateur radio use we should also assume that the transmitter is not active 100% of the time, giving the antenna time to cool off. For a *truly continuous transmission*, you'd probably want to reduce the number to about one tenth, to simulate a 10% transmit 90% receive cycle. *Once you know the safe continuous power, you can easily work your way backwards to any transmission mode.*

**The other side of the coin** is the maximum instantaneous power that the antenna can handle. This is easier, since we can fairly safely assume that the manufacturer wouldn't say 200 W *anything* unless the antenna is capable of handling an instantaneous 200 W of RF. This is where issues such as arcing across coil windings, power handling capability at the feedpoint, etc., come in.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/944/why-do-some-antennas-list-modulation-type-alongside-power-rating, by Adam Davis, user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
