# Were there any 6m handhelds produced ever?

*Tags: ht · score 9*

## Question

Just of curiosity...

Outside of kits/ham produced prototypes, Do you know about any commercially produced 6m handhelds?

Should be technically feasible despite the fact that it would be more cumbersome than VHF / UHF radios, But I recall that CB operators have 27 Mhz handhelds.

Do you know the historical/technical/marketing other reason for them not to exist?

Or maybe they do exist and I cannot find any positive info about them...

## Answer (score 12, by tomnexus)

The Yaesu VX-5R had/has 50-54 MHz FM, 5 watts. Nice compact little radio!  
The VX-7 and VX-8 can also transmit 5 watts FM on 6 m, *and* 1 watt AM. None of the 3 will transmit SSB.

It had a little extension of the rubber duck to make it work at 50 MHz, though I doubt it was very efficient.

Antenna calculation:  
The whip is about 25 cm long, so I'll consider a 0.5 m dipole. Radiation resistance the dipole is 1.4 $\Omega$. Reactance is about -1500 ohms, resonating this with a coil will introduce the rest of the 50 $\Omega$ resistance, probably giving a reasonable match. Efficiency is thus about -15 dB.

Further thoughts:  
When talking to someone with a full-size dipole, like a repeater, the gain of the 6 m antenna will be partially compensated for by the reduced path loss. The path loss is 6 dB smaller at 6 m, compared to 2 m. Assuming the gain at 2 m is -3 dBi, and the gain at 6 m is -15 dBi, at 6 m the handheld will deliver only 6 dB less signal to the repeater.

## Answer (score 4, by Mark Shreves)

Wouxun KG-UV7 is available in

- 2M/70cm (UHF 420-450 MHz)
- 2M/1.25M (220 MHz) and
- 2M/6M (50-54 MHz) frequency ranges.

## Answer (score 3, by Phil)

Also the Cherokee AH-50, which is the 6m big brother to the AH-27 (CB variant). They were produced from about 1995 to the early/mid 2000s. FM-only and able to use with repeaters. Very basic radio but back then, choices were limited to this radio for a 6m ht/handheld.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11750/were-there-any-6m-handhelds-produced-ever, by rodv92, tomnexus, Mark Shreves, Phil. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
