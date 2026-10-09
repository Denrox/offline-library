# What would propagation look like on Mars?

*Tags: hf, propagation · score 11*

## Question

If we could get a few HF stations on Mars, what would the propagation look like? Thought shamelessly copied from this blog.

## Answer (score 8, by user)

According to NASA TP 2000 209756, particularly section 2.5, it shouldn't be *too* different from similar propagation on Earth *during daytime,* except we'd need significantly lower frequencies than we are used to for similar results. According to that report,

The Martian dayside ionosphere at solar maximum has a peak density similar to that of the Earth nightside ionosphere at solar minimum. (...) Even though the Martian ionospheric peak density and TEC [total vertical electron content] are lower than in the Earth’s ionosphere, we can still use them for ionospheric communication.

According to table 2-2, *Usable Critical Frequency and Hop Distance for Various Launch Angles*, and assuming I'm reading the data correctly, around 4 MHz would be about the upper bound for near-range communications (NVIS to almost-NVIS), and by the time you get a take-off angle of 60° this climbs to a whopping 8 MHz and a single hop distance of 400-450 km. (The table says 433 km.)

If you want to penetrate the ionosphere, section 2.6 *Summary and Recommendations* says to use a frequency above 450 MHz. Nighttime communications beyond those offered by line of sight are tricky:

[T]he nightside ionosphere has some limitations for global communication because of its low usable frequency and very unstable conditions.

The report specifies a critical frequency of 0.6 MHz during solar minimum night time. That isn't impossible to work with (it was at one time considered "high frequency") but it takes a lot more than a "rubber duck" antenna on a handheld radio to produce useful results and bandwidth is highly limited, so nighttime ionospheric communications on Mars would be extremely limited at best. (You'd probably buffer up data for transmission after sunrise and focus your efforts on a higher frequency, near the boundary between what we consider MF and HF around 2-4 MHz in order to achieve reasonable antenna sizes as well as reliable communications even during solar minima.)

If you can manage a take-off angle in the 75° range, the maximum usable frequency climbs to a whopping 15.5 MHz, says table 2-2. At those frequencies, it should be possible to pack quite a bit of data into a transmission.

## Answer (score 2, by Paul)

I just read the ionospheric sounding data obtained from MARSIS and it looks like Top Band (160 meters) would work great. Moreover: zero atmospheric noise (no thunderstorms).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/421/what-would-propagation-look-like-on-mars, by PearsonArtPhoto, user, Paul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
