# Which HF bands are best during the day and which are better at night?

*Tags: hf, propagation · score 35*

## Question

I am rather new to HF operation and have recently purchased my first HF rig. I have read about bands being "open" and "closed" based on various conditions including time of day. As I have been listening, I have been bouncing around all the bands from 80 meters through 6 meters, but I am not sure which are better for me to try to make contacts on. I have heard that certain bands are more appropriate for daylight operation and others are better at night, but which are which?

## Accepted answer (score 39, by Phil Frost - W8II)

HF propagation over long distances is by skywave propagation, the reflection and refraction of radio waves between Earth's surface and the ionosphere. The ionosphere is a consequence of radiation from the sun ionizing Earth's atmosphere, so it changes significantly with time of day and sunspot activity.

Although time of day is just one of many variables, here is a simplified model of the ionosphere:

The F layer is mostly responsible for the refraction of radio waves back to Earth, preventing them from escaping to space. The other layers interact in other ways. During the day, the D layer forms, and the F layer splits into F1 and F2 layers.

The D layer is present during the day and is a good absorber of radio waves, increasing losses. Higher frequencies are absorbed less, so higher bands (20m to 10m or so) tend to perform better. Above the critical frequency, the ionosphere is unable to refract the signal back to Earth and it escapes to space. The critical frequency during the day is in the neighborhood of 6m: depending on the space weather, 6m way work for skywave, or it may not.

During the night we need not contend with D layer absorption, but the critical frequency is lower, so higher frequencies can not support skywave propagation. This can be observed on a map of critical frequency: see that the critical frequency is typically lowest around dawn, when the ionosphere has been in the dark the longest.

So, very rough rule of thumb:

- 20m, being in the middle, works to some extent day or night.
- Lower frequency bands work best at night.
- Higher frequency bands work best during the day.
- The farther from 20m you get in either direction, the more pronounced these effects are.

Of course, given that space weather is just as variable as Earth weather, there are exceptions to these rules every day.

## Answer (score 19, by PearsonArtPhoto)

In general, the shorter wavelength HF bands are better during the day, and the longer wavelength ones at night. Although that depends a bit on what you want to do, and like all things propagation, it's subject to change. Let me try and give a rough mode of operations. Also take a look at the chart from eham.

- 6m- Randomly opened, in random directions. I think this happens more in the day, but I'm not a 6m expert. Strictly speaking this is VHF, not HF, but it's often included on HF rigs.
- 10m- This is more consistently opened, especially in times of higher solar activity. Evening tends to be the best time, at least that's what I've found, but this is a daytime band.
- 12-17m- These are traditional daytime bands, usually opened. The longer the band in this window, the more reliable it is, and the more likely it is opened night or day.
- 20m- Can be opened day or night. This is the most reliable band for dx.
- 40m- Daytime is opened in a "local" area, give or take 500 km or more with a good set up. Night time opened worldwide.
- 80m- Similar to 40, but even more extreme.
- 160m- This one is only opened at night, and tends to be a more local area. Not unlike 6 meters, strictly speaking this is MF rather than HF, but it's often included on HF rigs.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1755/which-hf-bands-are-best-during-the-day-and-which-are-better-at-night, by ghendricks, Phil Frost - W8II, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
