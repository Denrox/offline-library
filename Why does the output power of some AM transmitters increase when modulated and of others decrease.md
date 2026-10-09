# Why does the output power of some AM transmitters increase when modulated and of others decrease?

*Tags: rf-power, am · score 3*

## Question

I didn't fully understand all the finer details of AM, so I'd like an explanation for the following behavior:

I have 3 radios. In AM mode, one of the radios, when modulated, increases output power on my PEP-reading meter. On the two other radios, the output power decreases, as I provide modulating signal. Same also happens in the average mode as well.

What is happening here?

## Answer (score 3, by Glenn W9IQ)

First a bit of background on AM modulation and power levels. If we start with a 100 watt carrier and no modulation, we would measure 100 watts peak and average power. They are the same due to lack of modulation.

When 100% amplitude modulating a 100 watt carrier, the PEP (Peak Envelope Power) is 400 watts. The carrier average power will be 2/3 of the 100% of the modulated average power. The other 1/3 of the modulated average power goes into the upper and lower sidebands so each sideband has 1/6 of the modulated average power.

Most modern solid state transceivers have a 100 watt maximum output. Their output is controlled through an ALC (Automatic Level Control) circuit that monitors the *peak* power of the output and adjusts the drive levels accordingly so at to not exceed this peak.

Now when we use one of these solid state rigs to generate AM, we set the carrier output to 25 watts knowing that the peak power will then be 100 watts at 100% modulation. But the ALC is watching the output and during 100% modulation, it cuts the *peak* power back to 25 watts. This puts the carrier output in the 7.5 watt range. When no modulation is present, the carrier output goes back up to 25 watts! Not all radios have this odd ALC characteristic. If I recall correctly, the Yaesu FT-1000D is an example of one that properly handled the ALC action during AM.

The solution for the radios that cut back carrier power at 100% modulation is to inject an adjustable negative voltage into the ALC control circuit connection on the back of the radio. A 9 volt block battery with its positive lead connected to the radio's ground and a 100k $\Omega$ potentiometer will do the trick:

With the radio's power control wide open, slowly adjust the negative ALC voltage using the pot until the carrier output power is 25 or so watts. Then adjust the mike level control to achieve 100 watts PEP at 100% amplitude modulation. Don't forget to disconnect this ALC injection circuit when operating in other modes if you wish to have full power output.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10012/why-does-the-output-power-of-some-am-transmitters-increase-when-modulated-and-, by AndrejaKo, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
