# dBi gain of random wire antennas

*Tags: united-states, hf, impedance-matching, wire-antenna, gain · score 4*

## Question

All antennas are a compromise. Are there any antennas that in free space perform strictly worse than an isotropic antenna would? Or a simple flat ground model?

This is what has been bugging me. I am a very new ham, especially with HF. I only have my technician license. I have a Xiegu G90 radio and was using a random wire antenna. I've seen all the articles about best lengths for random wire antennas. At some point, it occurred to me that while these may have a reasonable SWR that can be tuned on most bands, it doesn't necessarily mean they've got good gain.

I've tried finding data on this and it's hard. Either I get extremely basic results about half the half wavelength antenna is good or I fall into the black hole that is modelling software (and I don't want to try and figure out how to get that running on Mac/Linux, much less learn it for something simple). One thing I stumbled on though is that it is mostly the shape of the lines that changes. Sure, there may be more desirable shapes and less desirable ones, we don't want to point directional antennas straight down for example. But when you sum the gains in all directions, will it always be equivalent to an isotropic antenna?

I hope that makes sense. Basically I'm asking are there lengths or shapes of antennas that are actually doomed to be bad no matter how you use them. What are good lengths for random wire antennas if you want to get good gains? Or at least gains that aren't awful?

## Answer (score 2, by Ryuji AB1WX)

**Random Wire Antennas on HF Bands**

When delving into the world of **random wire antennas** (a really bad and misleading terminology!) for HF bands, it's easy to get frustrated by the lack of definitive engineering information (and overabundance of bad or wrong information... such is the norm of amateur radio literature).

As a technician, you might be focusing on bands like 10, 15, 40, and 80 meters. The key to understanding random wire antennas is defining your goal, as performance and optimal design can vary significantly based on what you aim to achieve.

**Defining Your Goal**

For those interested in **DX communications**, the focus should be on radiating power at lower elevation angles just above the horizon. This approach is crucial for bands like 10 and 15 meters, where only signals with shallow angles are bounced off ionospheric layers. Lower takeoff angles are important for DX on all bands, including 40 and 80m. In contrast, individuals more interested in local rag chewing and nets (NVIS: near vertical incidence skywave) often design their antennas to radiate at higher angles, closer to straight up. These antennas are only useful on lower bands like 80 or 40 meters, as NVIS does not happen on 20m and higher.

**Radiation Patterns and Elevation Angles**

Integrating the radiated power density over a sphere covering the antenna and comparing it to an isotropic antenna is a common approach in electromagnetic studies. However, in practical radio communication, you want to direct your power into specific directions, including elevation angles. Even if you deploy a random wire antenna strictly vertically, where the antenna is omnidirectional in the horizontal plane, the vertical plane radiation pattern becomes a major factor.

When discussing antenna gain, whether the unit id dBi or dBD (dipole reference), the *condition* is very important, and the measurement (or simulation) condition must align with your operational goal. If you are on 10/15m or chasing DX, the gain should be evaluated between 10 and 35 degrees of elevation. If you are interested in regional contacts on 40 and 80m, you might be evaluating the antenna at 45 to 60 degrees elevation.

**Optimal Radiator Lengths**

The best lengths for the radiating element depend heavily on the quality of your ground soil:

- **Sandy or Rocky Ground**: Optimal radiator lengths are around 0.6 wavelengths.
- **Saltwater Ground (e.g., fishing pier, ship)**: Optimal lengths are about 0.38 wavelengths or shorter.

For example, on the 10-meter band:

- On sandy or rocky ground, a radiating element of about 6.3 meters (0.6 wavelengths) is effective.
- On saltwater ground, a radiator length of around 3/8 of a wavelength (approximately 3.9 meters) works best.

Another limit is on the shorter end. You don't want to go much shorter than 1/4 WL, as the radiation efficiency drops. I personally don't like going below 1/8 wavelength, around which the performance drop is quite sharp.

**Multi-Band Operation**

Using a single radiator for multiple bands can be possible:

- A 10-meter band radiator (about 6.3 meters long) can also function effectively on the 15-meter band. (It also works well on 12, 17, 20, and 30m, but you need to upgrade your license.)
- For regional contacts on 80 meters and 40 meters, you can use a single inverted L on both bands with reasonable efficiency, as long as the length is longer than 1/4 WL on 80m and shorter than 5/8WL on 40m.

**Antenna Configurations**

Different configurations serve different purposes:

- **Vertical Deployment**: Ideal for DX communications. This is the only good option on higher bands like 15 meters or 10 meters. This configuration ensures that the power is radiated at lower elevation or takeoff angles.
- **Inverted L Configuration**: Suitable for regional rag chewing and nets on 80 meters and 40 meters.

**Ground Soil Quality**

The quality of your ground soil significantly impacts antenna's optimal design and its performance:

- **Elevated Radials**: Essential for improving performance, especially in dry or rocky ground conditions.
- **Seawater Ground**: Limits the radiator length to about 3/8 wavelengths due to high conductivity, but the whole antenna system performs much better (colloquially called "salt water amp.")

**Antenna Simulators**

While there is an antenna simulators available on macOS, it may not be well supported (not quite up-to-date). For random wire antennas used strictly in a vertical configuration with elevated radials, understanding performance from known examples can often suffice without custom simulations.

##### Personal note

I am primarily interested in DX, so vast majority of my antennas are optimized for 30m and higher and straight up vertical, with elevated radials. (I have a mast that supports a full size vertical on 40m.) When I do 40m/60m/80m while operating from mountain summits (SOTA), the operation is limited to mid-day anyway (when there is no DX propagation), I add a horizontal element at the top of my vertical to convert to inverted L. Either way, my vertical antennas make plenty of regional contacts with enough signal strength for rag chewing in CW, despite being optimized for DX. However, if I were focusing on the regional contacts, I would go straight to a horizontal or inverted L antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23490/dbi-gain-of-random-wire-antennas, by Captain Man, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
