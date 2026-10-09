# Stacking Two UHF Yagi Antennas

*Tags: antenna-theory, uhf, yagi · score 4*

## Question

Aloha!

I have two HYS TC-YG05 Yagi antennas that were gifted to me and I would like to stack them side by side ( Collinear), in the vertical orientation for some local weather balloon telemetry data gathering.

I have attempted to use my Google-Fu as the best that I can in the attempt to search in understanding the stacking of yagi antennas; it seems the boom spacing is not very critical so to speak when not utilizing long yagi antennas. I believe I can get away with the spacing @ 432mhz using .6λ @3dB which equates to a spacing of ~1.4 feet

So after researching a bit more, appears there is a formula that can be used if you know the E/H Beamwidth information of the antenna;

https://atlcllc.com/simple-formula-for-the-stacking-of-yagi-antennas/

So stacking on the Stacking distance E plane in inches, looks like my distance between the Yagi antennas would be roughly 3 feet, center to center. Using the DL6WU calculator, it came out to be be 3.3 feet; however, from my understanding, the DL6WU calculator should be used for long yagi antennas.

Any thoughts if I am correct in my research?

Thanks!

## Answer (score 2, by user10489)

The ARRL Antenna book has an article on stacked yagis that covers this.

It states that colinear yagis have the *elements* end to end, not the booms. This could be horizontally polarized antennas horizontally stacked or vertically polarized antennas vertically stacked. Alternately, they can be stacked side by side, with horizontally polarized yagis being vertically stacked or vertically polarized antennas horontally stacked, with the elements in parallel. Which arrangement you use depends on the easiest way to mount them. For EME yagi arrays, a grid of antennas may be used, stacking them both horizontally and vertically.

The antenna book article also states there are several reasons to do this, increased gain being only one of them. Other reasons include broadening the radiation pattern, reducing noise, and reducing fading. I have also seen applications where a variable phasing harness was used to do beam steering, to adjust the elevation angle of the primary lobe.

The stacking distance depends greatly on which of these effects is your goal. Spacing between 0.5 and 1.0 wavelengths are commonly used. The antenna book article discusses not merely maximizing gain, but actually shaping multiple lobes of the radiation pattern for specific varieties of uses. Also, different yagis with different numbers of elements and boom lengths have different ideal stacking distances.

It is clear from reading this article that there is no simple formula for stacking distance. To determine ideal stacking distance, you need to consider what goal you have for stacking them and the exact type of yagi you are using, and then model the system, optimizing the shape of the various lobes resulting in stacking them. Basically, at best, there would be a different formula for each antenna model and usage goal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18268/stacking-two-uhf-yagi-antennas, by RF101, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
