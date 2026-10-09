# What is the appropriate length of an antenna for a handheld on 2 meters?

*Tags: antenna, baofeng, ht · score 10*

## Question

I want to upgrade the stock antenna on my Baofeng uv-5r for which I mostly use the 2 meter band. The quarter wavelength for this band is about 19.2 inches, but when I look for antennas, they are typically 15.6 or 7.5, or some other seemingly random number of inches. Not to mention for 70cm, which they advertise they work for, the length is way off. Would these non-19.2 inch antennas work correctly since they are not a resonant length? Could they cause damage when transmitting?

## Accepted answer (score 14, by Andrew)

These antennas don't always contain a simple straight length of conductor, but rather usually have coils of wire inside, so the actual physical length doesn't mean that much. They are designed so that the antenna is wound into a coil normally to make the antenna shorter which is more practical for a hand held radio.

That's why you don't see a whip that is exactly the 1/4 wave in length you expect.

There are many different types of whip antennas and they all probably look similar on the outside but are very different inside.

For example some are designed for a single band made from one long helically wound coil, while others might be multi band with a few coils in series or even multiple separate antennas all contained within the one whip.

Also keep in mind that some handheld antennas may be specific to the model radio they were designed to work with, and might use a custom matching network that won't work on other radios.

So to answer your questions, most antennas will work for receive to some extent on just about any band, but for optimum performance you need to choose the correct antenna for the bands you are using, and you must use the correct antenna for transmitting otherwise you risk damaging the radio if the antenna is not resonant on the bands you are transmitting on.

Hope that helps !

## Answer (score 5, by user10489)

70cm is not quite but almost a third harmonic of 2m. What this means is that a 2m antenna that has sufficient bandwidth will also be a good match for 70cm. Sometimes the radiation pattern is not good, but it will still radiate with a good SWR.

Also, it is possible to add inline loading coils to antennas to make them work on multiple bands without being harmonically related.

And a good antenna is not necessarily an actual physical 1/4 wavelength due to stray inductance and capacitance of surrounding parts. For example, adding dielectric insulation can have a very small effect that would change the ideal length a bit. Adding a knob on the tip (so it is less sharp and also to prevent arcing) acts as a capacitive hat.

And 1/4 wavelength isn't the only "ideal" length. Antennas that are 3/8, 5/8, and even 1/2 wavelength can be found. (A 1/2 wavelength antenna usually has a huge loading coil on the bottom.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18019/what-is-the-appropriate-length-of-an-antenna-for-a-handheld-on-2-meters, by Ryan J., Andrew, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
