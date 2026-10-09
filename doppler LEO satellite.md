# doppler LEO satellite

*Tags: satellites, doppler · score 6*

## Question

I am trying to model Doppler shift of LEO satellite, From my research so far I have come across the following formula:

\begin{equation} \frac{f_r}{f_s}=\frac{1-\frac{u}{c}cos\theta}{\sqrt{1-\frac{u^2}{c^2}}} \end{equation}

that in my understanding would model the doppler shift.However the doppler curve (https://georgeri.smugmug.com/My-First-Gallery/i-m8tmT5V/A) can not be extrapolated by it,since they follow a sinwave shape (as seen in the picture) not a cosine that the formula would plot.

Am I heading in the right direction?Can someone please provide some references on how to replicate the doppler curve? Shall I dig in more to special relativity or is a simpler way to model doppler shift?

## Answer (score 4, by Glenn W9IQ)

The general equation for the change in frequency due to Doppler shift is:

where c is the speed of light, fO is the frequency of operation, and Δv is the relative velocity.

When applying this formula to the ground observation of a satellite, Δv is better described as range velocity (rate of change of distance from the satellite to observer). Because many LEO satellites are in an elliptical orbit, the math to obtain Δv as a function of time or position is not solved through simple angular calculations and therefore becomes very tedious to execute even when applying matrix math for some of the calculations.

I would like to suggest, however, that there is little value in recreating all of the calculations except for academic interest. Instead, I prefer to use a well engineered software library called PyEphem that does nearly every type of ephemeral calculation one could need (I even use this library in my home automation system to calculate the on/off times of my exterior lights to obtain automatic seasonal adjustment). This is a completely free Python library that is easily run on nearly any operating system and platform including the ubiquitous Raspberry Pi.

Applying the library for amateur radio satellites is quite simple. First, acquire the TLE (two line elements) for the desired satellite. These are available from the TLE Info site. A typical set of TLE data contains all the necessary ephemeral variables and looks like this:

```
OSCAR 7
1  7530U 74089B   17170.24378275 -.00000031 +00000-0 +84707-4 0  9992
2  7530 101.6303 138.8875 0011838 320.4872 153.4129 12.53627377948883

```

This information is used with the PyEmphem library in the following fashion. First establish the observer location on earth (I will use Chicago, IL, USA as an example):

```
my_loc = ephem.Observer()
my_loc.lon = '87.6298'
my_loc.lat = '41.8781'
my_loc.elevation = 181

```

Then apply the TLE data to create a my_sat body object:

my_sat = ephem.readtle(name, line1, line2);

The library can now calculate a variety of data related to the next pass of my_sat at my_loc:

info=my_loc.next_pass(my_sat)

So for example, we can print the rise and set times, maximum altitude, and the time of the maximum altitude for the next pass:

print("AOS: %s LOS: %s Maximum Altitude: %s Maximum Altitude Time: %s" % (info[0], info[4], info[3], info[2]))

Note that the maximum Doppler shift will occur at AOS and LOS and that the maximum altitude time is when the Doppler shift will be at zero because the range velocity (Δv) will drop to zero.

We can also inquire as to the range velocity at any time during the pass. For example, at the start of the pass:

```
my_sat.compute(info[0])
print("Range velocity: %s " % (my_sat.range_velocity))

```

By applying this technique to obtain the range velocity throughout the pass, we can easily calculate the Δf of a specific pass as viewed from a specific location on earth. And all of that for only a few dozen lines of code!

You can learn more about the expansive PyEphem library here.

If you wish to explore more of the raw math behind LEO satellite calculations, the following links may be helpful:

Orbit Calculation and Doppler Correction

Adaptive Doppler Correction

Satellite Orbit Basics

## Answer (score 2, by SandPiper)

The Doppler curve IS the Doppler shift. That graph you have is exactly what you will see at your receiver station. Especially for LEO satellites, you don't need to extrapolate further because the satellite is obscured by the Earth.

You mention you are concerned about the cosine function in the equation... remember that cosine is the same thing as sine but shifted 90 degrees. You don't need to worry about that.

This formula is easier to think about if you take the curvature of the Earth out of the equation. If you imagine for a moment that you are on a flat surface and you have an object coming towards you (but slightly offset from you), the frequency you receive is higher than the source it is transmitting. As it gets closer, there will be less and less velocity in your line of sight. Then, when it reaches the closest point of approach to you, your received frequency will be exactly equal to the transmitted frequency because the velocity in your line of sight to the object is exactly zero. As it continues away, your received frequency will decrease until it is far enough away that the velocity component in your line of sight is essentially equal to the object's total velocity.

Therefore, the picture in the link is showing you a lot of information. If you know the transmitted frequency, then when you measure the difference between max or min frequency and that reference, you are able to determine how fast the object is traveling. If you don't know the base frequency, then you can take the average of the max and min to calculate it. Finally, you know that when the satellite crossed zero in that graph it was at it's closest point of approach to you.

To summize, you are on the right track. You just have to remember that u in that equation is a relative speed in receiver's line of sight, not the speed of the satellite.

This is the exact same principle used in sonar tracking and signal processing as well. If you can't find more on satellites, you can look there too.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7763/doppler-leo-satellite, by Rizias, Glenn W9IQ, SandPiper. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
