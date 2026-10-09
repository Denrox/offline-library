# Suggestions for mounting a mini-whip as high as possible

*Tags: hf, antenna-construction, rfi · score 4*

## Question

I've ordered two mini whip antennas from Ebay (Russia) for HF and MW. As power lines cross my city property in a L shape - the only way to get away from them is to go up. So I'm hoping that going 5-20 feet above my roof line will reduce the extreme RFI that is on the power lines.

What is the best option for mounting a mini whip high above the roof?

I'm considering using 10 ft emt. Is it safe to go any higher (say 20 feet) or do I need cables or a tower to do so?

I want to mount two of them so I can phase them. I'm considering using the sewer pipe (which already has a diamond discone), chimney, or gutter/side of the roof.

## Accepted answer (score 2, by Glenn W9IQ)

First and foremost consider the safety aspects of your intended installation. You should ensure that if the antenna and its supports were to fall, it should not contact the power lines. The same consideration should be given for the installation process to ensure that under no circumstances should the antenna, mast, or cabling nor any equipment used for the installation be able come into accidental contact with the power lines.

Secondly, elevating the antenna by 10 to 20 feet may have a minimal effect on the amount of RFI received from local sources. If the noise source is in the near field of the antenna, then the results can be unpredictable. If the noise source is in the far field of the antenna, then it will basically follow the inverse square law. For example, if the far field noise source is 100 feet away when the antenna is on the ground and you now elevate the antenna by 10 feet, the noise will decrease by less than 1% - an imperceptible amount. Elevating the antenna may help with increasing the amount of desired signal, however, and this would have a positive effect on the Signal to Noise Ratio (SNR).

The question of the mast construction depends on several factors - the yield strength of the mast, the inner and outer diameters of the mast, the height of the mast, and the wind load of the load at the top of the mast (your active antenna system). These factors can be used to calculate if the mast will bend under specified wind conditions and the amount of stress the mounting system for the mast (bending moment at the base of the mast) needs to endure to support the mast under the calculated conditions.

The calculations are rather laborious. I have an Excel spreadsheet that I use in an attempt to reduce the number of errors. For example, I show that with a 1 inch OD mast, 0.1 inch wall thickness, 35 kpsi yield strength, with a 1 square foot of cylindrical wind load at the 8 foot position, the maximum wind speed it can survive is 67 mph (108 km/h). This will have a total moment of > 3,620 in-pounds (> 410 nm). This is the equivalent moment of an average adult pushing as hard as they can on a pipe 1 meter from the mounting point.

If you are interested in the detailed formulas, post back in the comments and I will add them to this answer. Alternatively, you can find the formulas and a spreadsheet here: http://thebont.com/spreadsheets/AnalysisOfAntennaMastStrength.htm

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9676/suggestions-for-mounting-a-mini-whip-as-high-as-possible, by Noroti, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
