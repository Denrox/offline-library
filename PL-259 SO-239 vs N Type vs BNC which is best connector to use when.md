# PL-259/SO-239 vs N Type vs BNC which is best connector to use when?

*Tags: connectors, pl259-so239-connector · score 5*

## Question

I understand that the:

- **PL-259/SO-239** connector (so-called "UHF connector") isn't great for UHF frequencies, but is very common
- **N type** connector is water-proof; and the
- **BNC** connector is quick to connect and disconnect

From James Eagleson's YouTube video I can see that the PL-259/SO-239 (so-called UHF-connector) performs the worst over VHF, BNC is significantly better, with the N-type performance being comparable to the BNC.

However I, as a ham-in-training building his own SWL rig, haven't been able to figure out when to use which as my primary coupling for antennas and switches as the cabling comes down to my rig.

I, personally, plan on creating antennas for a wide array of bands. My first antenna is for the 2m band, and I plan on creating some UHF antennas, but most of them will be for HF frequencies.

When do I use which is best connector to use when?

## Accepted answer (score 14, by Marcus Müller)

For shortwave listening, it doesn't really matter – all these connectors are suitable for 30 MHz, and for reception you don't need to work with significant power.

## PL-259

### 2m-band

If you, however, plan to work in the 2m band (2m being the wavelength, so frequency is, $f=\frac c\lambda=\frac{3\cdot10^8\,\frac{\text m}{\text s}}{2\,\text{m}}=150\,\text{MHz}$), then PL-259 definitely reaches its limits. That connector was designed before going "so high" in frequency was expected to be common for civil/low-cost radio equipment, and thus, the shape creates impedance changes over frequency. And that gets worse with increasing frequency.

### UHF

Just to cite Amphenol RF, which probably are the most important industrial player in RF connectors: They do offer PL-259 connectors, but even they say "Impedance: Non-Constant" on their product specifications, for example: https://www.amphenolrf.com/083-1sp-15rfx.html

That's not really an option, to be honest, when handling power. Your amplifier will not like seeing its power getting reflected back at him. You will not like getting less power at your antenna than your amplifier generates.

Oh, and even they only say the connector works up to 0.3 GHz. UHF actually is defined to be 0.3 to 3 GHz, so nope:

It's called UHF-connector, but it's not good for what we call UHF, at all.

## BNC

The go-to connector for anything that is high-frequency, but not outright microwave, at least in labs. It can be manufactured to a high degree of precision, which allows frequencies above 1 GHz to be transported well. If you spend more money, you can even get connectors that work up to ~ 4.5 GHz. These expensive connectors don't make sense unless both sides of a connection have the same precision. And you don't want to go up that far in frequency, anyway, probably

BNC is pretty nice for the lower UHF band, i.e. below ca 1.8 GHz. It's cheap, easy to buy from multiple reliable manufacturers (I wouldn't go for "sale boxes" on connectors – if you save 1€ on a connector to 50€ on cabling, but end up with something flaky, or lossy, you'll be sad). Also, they are typically able to withstand 1 kV of voltage – enough for high-power transmitters.

Cables that work with these connectors are cheap, and there's adaptors available to basically anything you want, from SMA over N-Type to Gardena garden hose.

You have to pay a bit of attention: BNC systems and connectors exist in 75Ω and in 50Ω variants – you need to pick what is identical to your system! (50Ω is kind of standard in RF measurement and lower- to medium-power systems, but 75Ω has typically lower losses and thus is preferrable if you have long cables delivering much power – but the 75Ω cables and connectors typically don't work for frequencies as high as their optically nearly identical 50Ω counterparts, soooo... it depends on what you have, anyway, but don't buy BNC stuff that doesn't say whether it's 75 or 50 Ω.)

BNC is also pretty nice as it's quick to connect and disconnect. It's, on the other hand, not as sturdy, and not outdoor-compatible.

## N-Type

Kind of what you see the most in medium-power professional RF equipment's antenna connectors. Works up easily to 10 GHz (again, depends on the price, in the end), handles significant power, is sturdy, has low loss and excellent impedance match.

It's a bit more expensive than BNC stuff.

More of a hassle to connect, and disconnect, but very reliable once tightened (don't over-tighten!), and can be wrapped in self-vulcanizing tape to make a connection weatherproof.

N-type is used in most sensitive RF measurement equipment when BNC doesn't go high enough in frequency – exactly because you can tighten it precisely enough to give a very reliable low-attenuation connection, which isn't easily degraded.

## Conclusion

You're not starting with a 1 kW transmitter. You'll probably be happiest with using no connectors outside, and BNC inside.

When aiming for higher frequencies as interconnects between low-power devices, SMA might be a better, because smaller, alternative to N-type. For high power, N-Type is pretty much your go-to choice.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13061/pl-259-so-239-vs-n-type-vs-bnc-which-is-best-connector-to-use-when, by Amin Shah Gilani, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
