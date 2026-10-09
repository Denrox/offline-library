# Antenna Patterns and Multipath Effect

*Tags: antenna, antenna-theory, radiation-pattern · score 3*

## Question

It's said that in order to decrease multi-path effects on receiving antennas that your antenna pattern should have a sharp slope near the horizon. Why?

for example this is article mentioned it.(Comparative Study of High-Performance GPS Receiving Antenna Designs Neus Padros, Juan I. Ortigosa, James Baker, Magdy F. Iskander, Fellow, IEEE, and Bryce Thornberg)

a very sharp slope is also desirable near the horizon directions to minimize the effect of the multipath signal.

## Answer (score 5, by Glenn W9IQ)

On HF (1.5 to 30 MHz) amateur radio operators use antennas with the major directive lobe close to the horizon in order to maximize the distance the signal will travel. At these frequencies the signals bounce off of the ionosphere - so by minimizing the incident angle, the distance of communications tends to be maximized. Multipath signals are rarely a problem on HF although they can happen. One of the most interesting means is "long path" where the signal takes the longest path around the earth. Under the right conditions this results in a strange echo effect due to the time delay of the long path compared to the short path.

On higher frequencies (VHF and higher), antennas with a major lobe to the horizon are generally preferred in order to maximize the gain for the line of sight conditions. Here multipath signals can readily occur due to signal reflections off of structures, for example. If multipath is a concern then an antenna with directivity in the azimuth can be deployed and the antenna is then turned in the direction of the most favored signal path.

[Edit]

In the citation that the OP added to the question as an example, the multipath issue is specific to receiving GPS satellite signals. In this case, it is desirable to only receive the signals directly from the overhead satellite constellation in order to achieve the desired GPS accuracy since the calculated position is based on the precise time delays between signals from multiple satellites. GPS signals are in the microwave region so they are very conducive to reflecting off of ground based structures, for example. Any satellite signals indirectly received as reflections off of ground based objects introduces timing (delay) errors due to the longer time of flight for the reflected signal.

The author is therefore making the point that, in the case of GPS signals, the antenna should have a *minimum* gain (also called a null) near the horizon so as to effectively attenuate any ground based signals due to reflections in favor of the desired signals directly from the satellites overhead. A typical antenna for GPS is a patch antenna that has a broad, major gain lobe (or multiple lobes) directly overhead but with very poor gain at the horizon. An alternative GPS antenna design is a quad helix (spiral) antenna that has similar pattern characteristics.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10241/antenna-patterns-and-multipath-effect, by mahyar p, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
