# Why are the lower HF frequencies not working during winter day time?

*Tags: hf, propagation, icom · score 5*

## Question

Currently my location is Nepal. We use the ICOM f-7000 radios without the antenna tuner. We use the frequencies round about 5-9 MHz, for communication over distances between 150 and 400 km.

During the summer time during the day the radio works fine in all frequencies. But during the winter time there is hardly any communication possible on any frequency. The best chance is the lowest frequency within the range. What could be the problem?

## Answer (score 4, by Phil Frost - W8II)

At distances of 150 to 400 kilometers, you will largely be relying on reflection of your signal by the ionosphere. In the winter the atmosphere receives less solar radiation and the ionosphere's index of refraction is less. This increases the critical frequency in the winter, putting the receiving station in the skip zone unless you use a lower frequency.

To gain an intuitive understanding of how this works, look at a glass of water. Looking through the side of the glass at a shallow angle it appears reflective like a mirror. But at a steeper angle it becomes transparent like a window:

The ionosphere interacts with radio waves in much the same way: different layers have different indices of refraction, and at some angles this can result in the radio waves being reflected back towards earth. For the purposes of terrestrial radio communication, we need the ionosphere to be like a mirror, not a window.

This is what creates the skip zone. For short distances, the angle to the ionosphere is too steep, and thus the ionosphere looks like a window. In this example, communication with anything closer than 1000 km is not possible by ionospheric reflection, because the signal instead escapes to space:

This refractive behavior is frequency dependent. A prism works because the index of refraction of glass is different for the different frequencies of visible light. It is the same for the ionosphere. As the radio frequency decreases, the waves are bent more. At some point, even waves straight up are reflected back towards earth, and the skip zone disappears:

The frequency at which this occurs is called the critical frequency.

The critical frequency also changes with the seasons, time of day, and solar conditions. Generally, more solar radiation increases the critical frequency. So the critical frequency is higher during the day than the night, higher in summer than winter (because the days are longer), and higher when the solar cycle is at its maximum.

So what's happening to you in the winter is the critical frequency is lower due to the shorter days and less radiation of the atmosphere, and so at higher frequencies the receiving station is too close because it's in the skip zone. If you get just the right frequency you might even find you can communicate with farther stations, but not closer ones. So, you must decrease frequency to get below the critical frequency where your signal will be reflected at nearly vertical angles.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12317/why-are-the-lower-hf-frequencies-not-working-during-winter-day-time, by Angry Hooman, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
