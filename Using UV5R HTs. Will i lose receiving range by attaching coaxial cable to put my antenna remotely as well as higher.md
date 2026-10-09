# Using UV5R HTs. Will i lose receiving range by attaching coaxial cable to put my antenna remotely as well as higher?

*Tags: antenna, receiver, coaxial-cable · score 3*

## Question

Using beofeng UV5R HTs. Changed antennas to retevis whips. Will adding coaxial cable to HT & antenna for height reduce or increase reception. As i'm in a valley. I receive only. As i'm still studying for my licence. Gratitude in advance for any help. As i'm very new to this world.

## Accepted answer (score 6, by Deepstop)

The answer is that it depends, although in my experience increasing height will always improve range. Height matters a lot in most VHF propagation. For your UV5R HT, antenna height will generally trump any loss in the coaxial cable. A few dB makes very little difference. I recently raised my antenna from 24' to 50' and I've seen 20dB or more improvement from signals 20-50 miles away That's many times more improvement than you would lose from an extra 26' of coax.

## Answer (score 4, by natevw - AF7TB)

You have to be pretty high up in frequency (basically in GHz instead of MHz) where the coax loss becomes *more* of a factor than the gain you'll benefit from getting an antenna that much further away from the ground.

The further you get an antenna away from the ground, you get:

1. dramatically increased line-of-sight distance
2. somewhat less signal losses to the soil
3. possibly less local noise (?)

And especially when receiving, any coax loss really isn't a problem. See e.g. [https://ham.stackexchange.com/a/17922/1362](If%20receive%20performance%20doesn%27t%20depend%20on%20SWR%2C%20then%20how%20can%20I%20tune%20my%20manual%20HF%20antenna%20tuner%20by%20band%20noise.md) for more details, but basically:

for reception quality we're interested in signal-to-noise ratio

Your receiver can usually add the gain back it needs to compensate for any coax loss (which should attenuate both the signal *and* the noise ± equally anyway). So usually far better to give a good antenna a better "bird's eye view" — out of the valley, away from all the phone chargers and LED transformers and whatnot in your house with a little bit of coax loss, than to use a stubby antenna down by the ground.

All that said though, one important caveat! What I said is all good in **theory** but in **practice** sometimes especially the more cost-effective receivers end up doing *worse* with a better antenna: [Why do Baofeng radios have such poor reception reliability?](Why%20do%20Baofeng%20radios%20have%20such%20poor%20reception%20reliability.md)

With my Baofeng's I often find:

1. poor reception with stock antenna
2. **no** reception with a good antenna (!!!)
3. good reception with a good antenna *and* a filter to block 88–108 MHz which is the FM broadcast band here in the USA (quite strong signals from good towers for commercial music/news programs/advertisements)

Basically the receiver *could* amplify a weak signal however much it needs. But if there's *also* really strong out-of-band signals those throw a wrench in that idea, because in the real world the amplifier itself ends up *distorting* on the strong signals and making hash of *everything*, before it can get the weaker signals up to their proper level.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22037/using-uv5r-hts-will-i-lose-receiving-range-by-attaching-coaxial-cable-to-put-m, by Snowy, Deepstop, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
