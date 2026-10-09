# How does Wi-Fi antenna work?

*Tags: antenna-theory, wifi · score 8*

## Question

Since I'm working with wireless communications, I decided it would be good to educate myself a little and at least get a basic understanding how does a Wi-Fi antenna work.

My first question is about the most basic 2.4Ghz antenna that is usually attached to every cheap Wi-Fi router you can find on the market. I stumbled upon this link, which happily explains that the such antenna is a half wave dipole and has a picture of it removed from plastic cover, which is copied below. Everything's fine so far, except it's hard to not see that the length of one half of the dipole on the picture is ~25mm, but 1/4 wavelength of 2.4Ghz wave is ~30mm. Does anyone know where does that difference come from?

Next question is about high gain Wi-Fi antennas. I found a video showing internals of such antenna, and it turns out that the only difference is that one half of the dipole is longer and contains a coil. The author of the video says that it is a loading coil, and if I understand correctly they are used to shorten physical antenna length. But here the standard half-wave dipole was made longer. To summarize: How does making the antenna longer increases its gain? And why in this case only one half of the dipole was made longer?

Thanks in advance for explanation!

## Answer (score 4, by Phil Frost - W8II)

Between lengths of infinitesimal and one wavelength, the lobes in the radiation pattern become narrower. Here's a picture from antenna-theory.com:

Notice how for the 1-wavelength antenna, the lobes are skinnier than the 0.25-wavelength antenna. A 0.5-wavelength antenna is somewhere between the two. These patterns can be calculated from the current distribution on the dipole. The math isn't simple so refer to antenna-theory.com if you want the math.

Assuming antennas with negligible losses (which these are), it's a fact that as the antenna pattern becomes narrower, gain in the peak direction increases. Gain can't increase in all directions because that would violate the law of conservation of energy.

As the dipole becomes longer than 1 wavelength, the pattern starts growing extra lobes which aren't pointing in any useful direction. The maximum gain peaks around 1.25 wavelengths (see [5/8 wavelength monopoles](What%20makes%20a%205%208%20wavelength%20vertical%20desirable.md)). Beyond that the lobes continue to get narrower, but also more numerous so peak gain does not increase.

So that explains why the higher gain antenna is longer, but why the coil? When a dipole is (approximately) a half-wavelength long, it's resonant and has a feedpoint impedance in the neighborhood of 75 ohms. This is a good match for most transceivers, so the antenna can be connected directly to the radio.

At different lengths, the dipole itself is no longer resonant and the feedpoint impedance will be something else. As such, some additional impedance matching will be required to efficiently couple the antenna to the radio, and that's what the coil does.

## Answer (score 4, by abcd567)

The antenna in photo below is the 1st antenna of the question.

It is supposed to be 1/2λ long (radiator+sleeve). However its length is 2x25 mm instead of 2x30 mm. The antenna will still work even if its length is different from 1/2λ. However the impedance/swr of antenna changes as the length changes. When dipole's length is exactly 1/2λ, its impedance is 75 ohms.

Please see sketch below which shows Gain & Radiation pattern for dipoles of lengths from 0.12λ to 1.25λ (total of both limbs):

***CLICK ON IMAGES BELOW TO SEE LARGER SIZE***

Dipole SWR vs Length (0.1λ ~ 2.1λ)  
Dipole Gain vs Length (0.1λ ~ 2.1λ)  
Dipole Impedance vs Length (0.1λ ~ 2.1λ)

## Answer (score 4, by abcd567)

This is the 2nd antenna of the question (screenshot from video linked in the question).

Below are simulation results of an antenna similar to the one above. Although simulated antenna is not for WiFi 2.4 GHz (it is for ADS-B, 1.090 GHz), this simulation gives a general idea of characteristics of this type of antennas.

The simulated antenna has two vertical sections, a coil and decoupling sleeve. Upper vertical wire is slightly longer than 5/8 λ. while lower vertical is slightly longer than 1/8 λ. The coil between two vertical section is used for phase-shifting the currents, as well as impedance matching. The decoupling sleeve is 1/4 λ in length.

***CLICK ON IMAGES BELOW TO SEE FULL SIZE***  
.  
.  
**Image 1 of 2 - Gain, SWR, Radiation Pattern**  
.  
.  
.  
**Image 2 of 2 - Current Distribution**

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7200/how-does-wi-fi-antenna-work, by xba, Phil Frost - W8II, abcd567. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
