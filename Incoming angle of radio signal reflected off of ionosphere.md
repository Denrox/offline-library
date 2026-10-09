# Incoming angle of radio signal reflected off of ionosphere

*Tags: propagation, ionosphere · score 5*

## Question

I am about 870 miles and 16 degrees due west of WWVB at Ft. Collins, CO. WWVB transmits at a frequency of 60 KHz. At this distance I should be getting the signal reflected from the ionosphere. If I assume the ionosphere layer I'm getting the bounce off of is sixty-two miles high and it's a straight line between here and WWVB, using Tangent = Opposite÷Adjacent (T=62÷435), I get an incoming angle of 8.1°. Since I'm 16° away, I'm tilted 8° away from the midpoint between here and WWVB, which gives me an incoming angle of only 0.1°. This seems counterintuitive.  
  
The reason I ask this is because I have a so-called atomic clock on my kitchen counter that does not get a signal unless I move it away from the solid patio cover next to the kitchen, but since the signal is at such a low angle, the patio cover shouldn't matter. I only need to move it a few feet for it to get a signal.  
  
So is my math right, or am I missing something?  
  
**Edit:** I'm not sure where I got the 62-mile figure, but a Wikipedia article I found and a PDF state the altitude of the F Layer starts at 93 miles. With that figure plugged into the formula, it gives me an incoming angle of slightly more than 4°, which is probably just enough (can't measure it precisely) for the patio cover to come into play.

## Accepted answer (score 2, by Hamsterdave)

Calculating the angle of an incoming signal traveling via skywave is not nearly so straight forward as you might presume, and there are two primary reasons.

The ionosphere is highly variable, and also exists not as a single impermeable layer, but rather a diffuse region several hundred kilometers thick. At any given moment, two signals of significantly different frequency will likely appear to 'bounce' from two very different altitudes depending on ionospheric conditions, transmitter antenna characteristics, and frequency of the waves. The height at which the signal appears to reflect is referred to as the "virtual height".

In reality, the signal is refracting over a relatively large physical distance, gradually bending back toward earth as it moves through the ionosphere. The distance over which the refraction takes place is dependent primarily on frequency, with higher frequency requiring a longer path. This means that if you have a 10MHz and a 20MHz transmitter with identical antennas, the 20MHz signal will have a longer single hop range, so long as the maximum usable frequency at the point where your signal meets the ionosphere is greater than 20MHz.

Things are further complicated by the highly variable nature of the ionosphere. Depending on time of day, solar conditions, and the state of the earth's magnetic field, the varying layers of the ionosphere can not only change altitude by more than 50% over the course of a single day, but they can even merge with other layers, or almost disappear completely. The F1 and F2 layers merge during local night to form a single layer, and the D and E layers are dramatically weaker or almost absent, for example. The F1 layer might begin at 150km at 10am today, but it could start somewhere above 200km at 10am tomorrow.

The exact range of a single hop also depends on takeoff angle from the transmitting station, as a wave with a frequency of 5MHz for example, is likely to return to the earth even if radiated nearly straight up, just as it would if it were radiated at 4 degrees above the horizon. Waves can also make multiple trips between the surface and the ionsphere, and there are times when two short hops can result in good reception, while a single longer hop may not.

In your case, you are well within range of ground wave propagation (nearly the entire continental US is for at least part of the day). At 60KHz, and a whopping 70kW ERP, the night time ground wave range is >1,000 miles.

Skywave propagation on VLF is finicky stuff. The ionosphere and the surface of the earth can form a waveguide that a VLF signal propagates along quite well, but this can vary depending on time of day and ionospheric conditions, as sometimes the altitude of the layers is not optimal for a particular frequency.

Lastly, if this were indeed a case of skywave 'shadowing' from a porch awning or other object in your home, the size of the shadow would depend on the electrical size of the object that's creating it to the wave that it's blocking. In the case of a 60kHz wave, an object would have to be absolutely **enormous** to create appreciable attenuation, as the wavelength is almost exactly 3 miles long. That means significant shadowing might require an object to be several hundred feet along at least one axis.

By comparison, the low end of AM broadcast at 500kHz is about 1 mile, and FM radio at 100MHz is just 3 meters.

Moving the object just a foot or two and seeing marked improvement, as you describe in the comments above, all but rules out skywave shadowing on this frequency. It is far more likely that you've got an issue with local radiated or coupled interference that's rendering your WWVB receiver deaf.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5760/incoming-angle-of-radio-signal-reflected-off-of-ionosphere, by BillDOe, Hamsterdave. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
