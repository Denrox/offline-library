# What kind of antenna is this?

*Tags: antenna · score 7*

## Question

This was found among some old ham stuff and is believed to have been used on 2 meters.

The vertical elements are 17 1/2" long and the connector on the bottom is a standard SO-239.

Antenna (left) and Connector (right)

(See test results below pics.)

Edited to add Test Results: I mounted the antenna to a small mounting bracket; just basically something to hold it but provided no ground plane. Then a ~20' length of RG-58 to an SWR meter and a 3' pigtail to my HT.

I got an SWR of 1.5:1 on 146.52Mhz and 1.2:1 on 446.000Mhz.

I also got a good, clear signal report on a repeater on 443.525Mhz that's about 11 miles away. The antenna was inside, leaning against my couch.

Edited again to add: There was a comment about impedance matching being done in the mount. There is not. Here is the mount disassembled.

This is the inner assembly with the outer shell removed:

## Accepted answer (score 5, by tomnexus)

I'm sure it's a simple monopole for 2 metres. Mount it through a hole in a large metal sheet.

17.5" plus the distance from the bend to the groundplane, is almost exactly 1/4 wave on 2 metres.

Why two whips? I've never seen this before, but it will make it slightly broader band than a single whip. The effective radius of a pair of wires is (from memory) $r_{eff}= ({r_{wire}}^2+(spacing/2)^2)^{0.5}$. The wind resistance of the two wires might be lower than that of a single thicker conductor.

A quick note about 70 cm: often a 2 m antenna will also resonate at 70 cm. Being about three times the frequency, the monopole is 0.75 wavelengths long at 435 MHz. Unfortunately, the radiation pattern of a 0.75 wavelength monopole, or a 1.5 wavelength dipole, is far from ideal - it has a null at the horizon. So although the SWR is good, the effectiveness is poor. The longest you can make a monopole is about 5/8 wavelengths, which needs a coil at the base to add some inductance. With care you can make this coil work for both bands, but that's a new antenna design entirely.

In both cases the antenna depends on a reasonable ground plane, at least 18“ square, or a vehicle roof, etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7392/what-kind-of-antenna-is-this, by Lance, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
