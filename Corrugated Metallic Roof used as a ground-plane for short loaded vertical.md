# Corrugated Metallic Roof used as a ground-plane for short loaded vertical?

*Tags: vertical-antenna, short-antenna · score 3*

## Question

My house has a corrugated metallic roof. 2500 sq. ft.

The roof is grounded via couple cables.

What's your comment on using the roof as the ground for a short center-loaded vertical 80M antenna?

Thanks David Hart VE6AQF, V21C

## Answer (score 3, by Marcus Müller)

basically: large metal plates work great as ground plane, even if not connected to earth (if large enough).

Now "large" in "large metal plate" depends on the wavelength – and from the geometry of the problem stems the fact that a ground plane should be at least about one quarter of the wavelength in radius.

In your case, that's 80/4 m = 20m radius, or 40m across. 2500 ft² is, best case, 50 ft × 50 ft, and that's smaller.

Now, not all is lost, because of course you still have the actual ground as ground plane, but modeling that gets much harder. For example, you'll often find that in Northern Germany, radio broadcast antennas are preferrably placed on slightly moist ground – because that increases the conductivity.

Luckily, field density is highest close to the antenna, so your roof will have a strong positive effect. I'm afraid that's all I can say, lacking explicit experience with such antenna systems.

Regarding corrugation: Shouldn't matter, structure size is much much smaller than wavelength, but the altered path the currents in the metal take might make for an interesting delay – might electrically look a bit as if the roof was curved downwards orthogonal to the corrugation, but ever so slightly.

It's probably much more interesting how well the connections/overlap between the sheet metal elements of your roof are electrically connected.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7823/corrugated-metallic-roof-used-as-a-ground-plane-for-short-loaded-vertical, by David Hart, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
