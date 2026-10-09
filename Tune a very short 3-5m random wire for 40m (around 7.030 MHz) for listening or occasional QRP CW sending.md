# Tune a very short 3-5m random wire for 40m (around 7.030 MHz) for listening or occasional QRP CW sending

*Tags: antenna-construction, wire-antenna, qrp · score 4*

## Question

I would like to use a small trx first for listening CW on 7030 kHz and then for transmitting, locally, among friends.

My conditions are "prohibitive" as for antennas: a block of flats, 4th floor in 8 floor building. Among other blocks of flats. Administration will not allow antennas - i.e.I need to go 'clandestine' or operate from a bench in a park so as not to attract attention.

I live in a capital city where there are plenty of CW addicts, I dream about being able to first listen to them on CW and then respond. No need to go DX; I would be happy to communicate locally.

I was thinking of a random wire matched with a capacitor and a coil but I am not an engineer. What would you recommend? I need only to have it tuned around 7.030 Mhz qrp calling freq and fit my pocket for bench operation or in a window for swl.

## Accepted answer (score 1, by Glenn W9IQ)

Very short antennas have very close to the same directivity as a full size 1/2 wave antenna but their efficiency, and as a result gain, can suffer. The gain of an antenna is given as:

$$Gain = Directivity * Efficiency \tag 1$$

The efficiency is the result of losses in the wire and, in your case, in the matching network that is needed to make the antenna work with your transmitter. So will you want to use the largest gauge wire possible for your situation and make very good solder joints at all connections.

Using EZNEC, I modeled a 6 meter (2 pieces, 3 meters each) center fed dipole in a vertical orientation for this example. The bottom end of the antenna was 7 meters above ground. I did not adjust for building proximity. At 7.030 MHz, the antenna impedance will be 5.4 -j1826 ohms. As a shortened antenna, the 1826 ohms of capacitive reactance is not unexpected. The 5.4 ohms of resistance is low but a manageable number.

A matching network such as this can be used to adjust to impedance to 50 ohms:

I designed this simple L matching network using http://leleivre.com/rf_lcmatch.html. The transmitter side of the matching network is 50 ohms so a convenient length of RG8X coax could be connected to this point and run to the transmitter. The coil should be made of fairly large diameter wire or even 1/4 inch soft copper tubing from the hardware store.

For the inductor shown, a construction example would be 0.25 inch soft tubing wound 10 inches in diameter, 7 inches long, and with 14 turns. The circuit can be adjusted by slightly expanding or compressing the coil. Keep in mind that this is a very big coil that must be placed at the center of dipole to optimize the efficiency but you may be able to cleverly use it to support the antenna. Many other coil geometries are possible. You can calculate alternate coil details using a site such as http://www.daycounter.com/Calculators/Air-Core-Inductor-Calculator.phtml.

This may not be the exact antenna you envisioned but it gives you an idea how to go about designing a compromise antenna. At your building height, you should give thought to using a vertical or horizontal, shortened dipole antenna. It may serve you well if you pay attention to construction details that can affect efficiency and thus gain.

## Answer (score 2, by Duston)

Clandestine can be very effective. A thin wire hanging out of your window is hard to see, especially if you only have it outside while operating. Commercially built tuners aren't expensive either.

Another option to consider is MCW (modulated CW) where you send the Morse tones over audio via VHF/UHF FM. If you have enough CW fans there you may be able to get enough interest. Or for that matter, VHF or UHF CW. It's far less common, but not unheard of.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10305/tune-a-very-short-3-5m-random-wire-for-40m-around-7-030-mhz-for-listening-or-o, by Jacek Kotowski, Glenn W9IQ, Duston. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
