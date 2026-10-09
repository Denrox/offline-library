# Is it ok to use a length of wire as an RX only antenna to test my new radio?

*Tags: antenna, wire-antenna · score 7*

## Question

I have almost finished building my first shortwave transceiver kit (mcHF). Remarkably it's fired up and not gone up in a puff of smoke. The kit still needs some finishing off and I need to decide on an antenna solution, but in the mean time I'd like to start hearing some sounds on it.

Is it ok to part strip a short length of Coax and tape it to my window for some RX testing? Is the whole antenna tuning exercise just needed for transmitting ?

## Accepted answer (score 10, by Zeiss Ikon)

You are generally correct.

Antenna tuning is primarily about maximizing radiation for the transmission frequency, which is important because power emitted by the final transmitter amplifier stage that isn't radiated or consumed by ohmic resistance will reflect back into the amplifier, causing (potentially catastrophic) heating of the components.

This only matters, however, when significant power is being emitted -- and when receiving only, the transceiver shouldn't emit any power (or only a tiny fraction of a milliwatt), at least for a well designed set.

Therefore, antenna tuning matters almost not at all in receive mode; all you care about is that the antenna produces an RF voltage at the receiver terminals for the receiver to amplify, tune, detect, decode, etc. to eventually produce sounds of either Morse or voice. While impedance matching the antenna (which is what you're really doing when you "tune" to a given frequency) will improve the received signal strength (at best, maybe double it), with most modern receiver designs it's unnecessary. It might be helpful for things like a crystal set, or extreme DX, but the presumption here is that you just want to be sure the receive section of your freshly built radio works as it should.

From my personal experience, my Heathkit SB-102 receives fine with an FM antenna from an old stereo, on bands from 80 m up to 10 m (providing there is signal present), just as my old Hallicrafters S-120 multi-band receiver does. It wouldn't be a good idea to key up 100 W output to that antenna on 80 m, however; I'd be likely to damage one of my 6146 tubes or other components connected to them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20305/is-it-ok-to-use-a-length-of-wire-as-an-rx-only-antenna-to-test-my-new-radio, by rcx935, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
