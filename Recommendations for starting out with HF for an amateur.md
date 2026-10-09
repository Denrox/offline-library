# Recommendations for starting out with HF for an amateur

*Tags: antenna-construction, hf, india · score 4*

## Question

I'm a beginner who's nearly half a year from receiving my ham license in India. I want to start with HF radio and wish to build my own rig. Currently I have looked and multiple designs using the ad9860 module. Also I live in a city and know very little about antenna design. Can someone guide me to the next level? Thanks.

EDIT: About myself.  
*Currently Second Year Computer Engineering Student  
*Fairly competent with practical electronics having built a Morse code oscillator with an arduino.  
***NOT** looking to buy a rig, but **WANT** to build one.

## Answer (score 2, by N8JEA)

I strongly suggest that you begin with a one-band radio kit. There are several manufacturers and the cost is likely to be quite reasonable even with shipping. The main reasons are:


to get on the air as quickly as possible.


Even a little experience with real-world operations will likely change your view on what you want from a radio.


The main obstacle to successful operating is likely to be antenna design and location. Time spent in this area will yield much more performance improvement than reworking radio designs. Local issues, especially QRM/QRN may lead you to change your thinking about HF entirely.

A 20 m or 15 m CW-only transceiver would be my recommendation for an in-city location. Antenna length and noise levels both increase at longer wavelengths.

A local college may have a ham club with useful equipment and assistance. A good SWR meter or even an antenna analyzer could be really useful. Being able to test your new radio with an existing, low-SWR antenna would give you confidence that the radio works and some experience with tuning.

## Answer (score 2, by Brian K1LI)

Welcome to ham radio!

Discussion of some of the simplest and most common forms of ham radio antennas (aerials) begins on page 72 of the Study Manual for the Restricted Grade Indian amateur radio licence. The half-wave dipole may be the single most common amateur antenna at HF because it is simple and inexpensive to build, easy to erect and almost 100% assured of working the first time if the wire is cut to the correct length.

Sadly, the Study Manual doesn't give the formula for the length of the half-wave dipole antenna, which is: $$l=\frac{0.95*c}{2f}$$ where is is the speed of light (3x10$^8$-m/sec) and $f$ is the operating frequency in Hz. The factor of 0.95 in the numerator is the *velocity factor*; it reflects the fact that the wave propagating along the antenna wire is slightly slower than the speed of light. The factor of 2 in the denominator reflects the fact that the antenna is a half-wavelength.

Using the 20-meter ham band as an example: $$l=\frac{0.95 * 3x10^8-m/sec}{2 * 14.1x10^6-Hz}=10.1-m$$ This makes sense, since this value is about 1/2 of the wavelength in the "20-meter" ham band.

I'm sure your university library will contain numerous books on antenna theory and design. Hopefully their collection will include some publications from ARRL, RSGB or other noteworthy sources, or you may be able to borrow a book from a local ham or club.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2268/recommendations-for-starting-out-with-hf-for-an-amateur, by Parth Sane, N8JEA, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
