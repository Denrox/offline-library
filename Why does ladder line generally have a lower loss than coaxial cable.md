# Why does ladder line generally have a lower loss than coaxial cable?

*Tags: coaxial-cable, feed-line, transmission-line · score 9*

## Question

It is well understood in the amateur radio community that ladder line, window line, etc. have lower losses per foot than say RG-213 or LMR400, particularly on HF frequencies. It is also understood that this loss is a function of the RF resistance of the conductors.

When you examine the size (surface area) of the conductors in LMR400, they are much larger than say the conductors in 450 ohm window line. This includes the LMR400 center conductor and certainly the shield is quite a bit larger. This would seem to suggest that the RF resistance of LMR400 would be lower than that of the 450 ohm ladder line.

As an example, place 50+j0 ohm loads on 100 feet of LMR400 and 100 feet of 450 ohm window line and measure the losses on 20 meters. The 450 ohm window line will have lower losses even though the 450 ohm window line has a 9:1 SWR while the LMR400 has a 1:1 SWR. So even with the additional losses due to SWR, the 450 ohm window line has lower losses.

What then accounts for the typically lower losses on HF frequencies of parallel transmission lines compared to coaxial transmission lines?

## Accepted answer (score 6, by Cecil - W5DXP)

When the SWR is 1:1, the matched line loss of ordinary ladder line is lower than the matched line loss of ordinary coax because at HF, most of the loss is $I^2R$ loss, and the current magnitude is inversely proportional to the characteristic impedance of the feedline. Of course, a high SWR results in higher standing wave currents and thus increases the $I^2R$ losses on a 1/2 wavelength (or longer) feedline.

Ladder line is not always at a lower loss than coax. For instance, if the frequency is 10 MHz, the load is 20 ohms, and the length of the feedline is 100 feet, the loss in RG-213 is 1.524 dB according to TLDetails, while the loss in Wireman #551 ladder line is 2.236 dB. The SWR for the RG-213 is 2.5:1 while the SWR for the ladder line is about 22:1.

## Answer (score 4, by Phil Frost - W8II)

It is well understood in the amateur radio community that ladder line, window line, etc. have lower losses per foot than say RG-213 or LMR400, particularly on HF frequencies.

Is it though? I'd say only sometimes.

From the LMR-400 datasheet:

From DX Engineering's 300 ohm ladder line datasheet:

Compare the loss at say, 30 MHz: 0.7 versus 0.668 dB/100 ft. For practical purposes, the same. If the ladder line is wet, or running in proximity to other things, the loss is much higher.

Of course, not all ladder line is equal: there are examples both better and worse than this one. But the unqualified assumption that ladder line has lower loss is not true.

OK then, but why is ladder line, at least in this example, able to deliver about the same loss, with less copper?

It's the same reason power lines run at high voltages for long-distance distribution: higher impedance means for a given power less current and more voltage. Less current means less resistive loss.

Power $P$ is the product of current $I$ and voltage $E$:

$$ P = I E $$

So, 50 volts and 1 amp delivers the same power as 1 volt and 50 amps. The ratio of volts to amperes is the line impedance, which we get from Ohm's law:

$$ R = {E \over I} $$

Resistive losses are the square of current, times resistance $R$:

$$ P = I^2 R $$

So a higher impedance means more volts per amp, which means more power per amp, which means less amps are necessary for a given power, which means less resistive loss. Or we can just use less copper, thus increasing $R$ but decreasing cost while keeping losses the same.

As an example, place 50+j0 ohm loads on 100 feet of LMR400 and 100 feet of 450 ohm window line and measure the losses on 20 meters. The 450 ohm window line will have lower losses even though the 450 ohm window line has a 9:1 SWR while the LMR400 has a 1:1 SWR. So even with the additional losses due to SWR, the 450 ohm window line has lower losses.

That may be, however this one situation can not be generalized to conclude 450 ohm window line will have lower losses at other load impedances, feedline lengths, and frequencies.

The issue is the standing waves set up alternating nodes of high current, and high voltage. They are spaced a 1/4 wavelength apart, repeating every 1/2 wavelength. As explained above, a higher voltage is associated with lower loss, and conversely higher current with higher loss.

At 20 meters, 100 feet is approximately 1.25 wavelengths, or enough for 5 nodes. If the load impedance is selected such that there are 3 high current nodes and 2 high voltage nodes, the loss will be greater than if there are 2 high current nodes and 3 high voltage nodes.

The trouble is, "ladder line has low loss" is usually mentioned in an antenna proposal such as this: put a tuner in the shack, run "low-loss" ladder line up to a dipole of whatever length, *et voila:* low-loss multiband antenna, easy to build, and cheap too! Right?

But in this proposal, the feedline's physical length is dictated by the site, its electrical length varies with frequency, and the load impedance varies by frequency too. At any particular frequency, the standing waves may fall in a way that reduces loss or increases it, but what's the average case?

That can be calculated by [assuming the line has uniform loss throughout](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md). Let's do that for the example provided.

The LMR-400 datasheet doesn't go to 14 MHz, but the Times Microwave calculator puts the matched loss at 0.5 dB for 100 feet at 14 MHz. No adjustment for SWR is required because the SWR is 1:1.

Very little ladder-line comes with a datasheet, but some independent tests put the matched loss for The Wireman type 553 at .25 dB / 100 ft.

As you say, the SWR is now 9:1; We first calculate the magnitude of the reflection coefficient:

$$ |\Gamma| = {9-1 \over 9+1} = 0.8 $$

And convert that 0.25 dB to a linear ratio:

$$ L = 10^{-0.25/10} = 0.944 $$

Now we can calculate the feedline loss:

$$ -10 \log \left(L { 1 - |\Gamma|^2 \over 1-L^2 \: |\Gamma|^2 }\right) = 1.02\:\mathrm{dB} $$

Even assuming no tuner losses, this 450 ohm ladder line has 1 dB more loss than LMR-400. So indeed, in the particular example given, the ladder line does have lower loss than LMR-400, even without matching the load to the line. However it was due to luck, not an inherent advantage of ladder line: in fact more often than not, LMR-400 will outperform this 450 ohm ladder line if used to feed a 50 ohm load without a matching device.

## Conclusion

Ladder line can be applied to good effect, but the often repeated, unqualified statement that it has lower loss than coax is demonstrably wrong in enough situations that I would not say it's "generally true".

Not all kinds of ladder line have lower loss than coax. Just like coax, ladder line loss varies. Look for specifications. Usually a datasheet is not available, and you have to find independent tests.

If ladder line is used to feed a mismatched load, SWR losses can be substantial. Calculate it for the particular length and load impedance, if possible. If not, [use an estimation](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md). Using ladder line to drive a load that's better matched to coax can often be a losing proposition.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13030/why-does-ladder-line-generally-have-a-lower-loss-than-coaxial-cable, by Glenn W9IQ, Cecil - W5DXP, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
