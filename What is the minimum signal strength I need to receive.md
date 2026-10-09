# What is the minimum signal strength I need to receive?

*Tags: transceiver, baofeng, 2m-band, transmission-line, path-loss · score 6*

## Question

Let's say a transmitting station is using a 8W radio with a J pole antenna. The cable connecting the radio to the antenna is RG-58A/U and is 25ft long.

At 144.075MHz, the attenuation of the cable is 1.5dB. At 8W, the power from the radio is 9.03dB. Assuming no losses other than cable losses, the antenna is getting 7.53dB, or 5.66W.

Let's now say the receiving station, 4 miles away, has the same setup (8W radio, J pole, and RG-58A/U). Assuming the gain of the two J pole antennas is 2.15dBi, and using the Friis transmission equation, the receiving antenna is receiving 1.733e-8W.

With the cable losses of the receiving station being 1.5dB (1.41W), and the antenna receiving 1.733e-8W, it appears the received signal will never make it to the receiving station's radio.

Me and my buddy have this setup with Baofeng BF-F8HP radios. If we are both using J pole antennas, we cannot communicate with each other. If one of us is using a J pole and the other is using the stock rubber ducky, the rubber ducky user can **receive** the J pole user's transmissions. I'm assuming the reason we cannot communicate with each other if we are both using J poles is because of the cable losses.

Is this correct? If so, is there a way around this?

## Accepted answer (score 1, by KM4NTK)

I ended up switching from a **25ft** RG-58A/U cable with **F connectors** on each end to an **18ft** RG-58A/U cable with **PL-259** connectors on each end. I can now receive, using my J-pole, my buddy's signal when he is transmitting with his J-pole. However, there is **a lot** of noise. This fixed the reception issue, but I'm still experimenting to figure out what the minimum signal strength is required at the RF input of my radio.

Here is the answer to "What is the minimum signal strength I need to receive?"

Baofeng Sensitivity

## Answer (score 5, by Phil Frost - W8II)

At 8W, the power from the radio is 9.03dB.

With the cable losses of the receiving station being 1.5dB (1.41W), and the antenna receiving 1.733e-8W, it appears the received signal will never make it to the receiving station's radio.

This seems to be the crux of your misunderstanding. You can't convert watts into decibels, or decibels into watts. A decibel expresses a ratio of two things.

In the case of losses at the receiver, it expresses the ratio of the received power (before losses) to the output power (after losses).

In the case of dBi, it expresses the ratio of the radiant intensity of a given antenna in its direction of maximum gain to the same of a hypothetical antenna which radiates equally in all directions.

In the case of dBm, it expresses the ratio of some power to 1mW.

So if your transmitter is 8W (that is, 8000mW), we can convert that into dBm:

$$ \require{cancel} \frac{8\:\mathrm W}{1\:\mathrm{mW}} = \frac{8000\:\cancel{\mathrm{mW}}}{1\:\cancel{\mathrm{mW}}} = 10 \cdot \log_{10}(8000)\:\mathrm{dBm} = 39\:\mathrm{dBm} $$

Notice how this is a ratio, and it is a unitless number because the unit (mW) cancelled in the second step. We add the "m" to "dB" to remember that the denominator is 1 mW.

We can convert 39 dB back into a ratio:

$$ 10^\frac{39}{10} = 7943 $$

This ratio is telling us that something is 7943 times bigger than something else.

The "m" at the end of "dBm" reminds us that this is the proportion of some quantity *in relation to 1 mW*, so to get back to the original quantity we must multiply by 1 mW:

$$ 7943 \cdot 1\:\mathrm{mW} = 7941\:\mathrm{mW} \approx 8\:\mathrm W $$

The discrepancy is just rounding error. Really 8 W is closer to 39.03089986991944 dBm.

If your receiver losses are 1.5 dB, then we can calculate the corresponding ratio (and I'll use *negative* 1.5 dB, because it's a *loss*):

$$ 10^{-1.5 \over 10} = 0.71 $$

Remember that's a ratio: to get to some quantity we have to multiply it by something. In this case we are comparing the power delivered to the receiver to the power received by the antenna. So if the antenna was receiving 0.01 mW, then we'd do this:

$$ 0.71 \cdot 0.01\:\mathrm{mW} = 0.0071\:\mathrm{mW} $$

With this in mind, try your calculations again, and I think you will get a more sensical answer.

## Answer (score 3, by Craig K)

From the symptoms you state of not being able to hear transmissions from identical setups only 4 miles from each other, and then being able to have one person receive with the rubber duck antenna, it tells me your J-Pole antennas are not behaving ideally on the frequency you choose.

Consider that an antenna like a J-Pole has about a 10MHz bandwidth in the 70cm Ham band. The rubber duck antenna has a broader bandwidth. Prove this to yourself by comparing reception of your NOAA weather broadcast station using first the J-pole and then the rubber duck. I'll bet you can receive it with the rubber duck. The NOAA broadcast is about 162.5MHz which is far above the 2M Ham band yet the rubber duck will work and very likely the J-pole tuned for the Ham band will not work.

Consider that the two antennas may have their band sweetspot tuned to some frequency 20MHz away from your transmitting frequency as an example. The antenna itself may contribute a lot of loss. You begin by looking at your feedline loss but maybe at the transmit frequency you have a very high SWR meaning that most of the power is reflected back from the antenna at your chosen frequency.

Invest in an SWR meter and measure the SWR of your J-pole at your desired frequency. Compare the two J-Poles. You should be able to see an SWR between 1.0 and 1.5 and if you see some crazy high SWR >5 then you can blame the J-pole instead of the feedline. You may be able to "hunt" for a frequency that your J-pole likes by using your SWR meter, meaning a frequency that the J-pole is tuned to work.

Also consider that any obstructions like trees and houses and especially hills between you and your friend will contribute most of the loss you see. Fighting this problem by desiring more output wattage can be a losing battle. If you have reasonable line of sight between the two radios then likely the rubber duck antennas will work for you with only 1 Watt. You can prove this to yourself by driving to hills that are within line of sight and see how well it works.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5445/what-is-the-minimum-signal-strength-i-need-to-receive, by KM4NTK, Phil Frost - W8II, Craig K. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
