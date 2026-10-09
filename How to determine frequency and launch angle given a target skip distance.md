# How to determine frequency and launch angle given a target skip distance?

*Tags: hf, propagation · score 8*

## Question

I would like to communicate with someone 1000 miles (1600 km) away. I'm not sure how to target a specific distance.

(image source)

I assume it's an interrelation of the following factors:

1. Which frequency I'm using
2. Which ionospheric layer I'm reflecting from (and its height)
3. The launch angle of the antenna
4. The maximum usable frequency for these conditions
5. More stuff I don't know about yet

This distance is too far for groundwave or NVIS, but it seems awfully close for skywave communications.

How do you figure all of this out? Can you estimate where the skip zone (dead zone between skips) is? And can you change the effective skip zone distance by selecting an different band?

Specifically, I'm trying to reach from Portland, Oregon to Phoenix, Arizona (USA). Thank you for any insight you can give me.

## Accepted answer (score 12, by hobbs - KC2G)

The actual math here is annoying enough that you will hardly ever want to use it (it requires knowing the incidence angle of the signal on the ionosphere, which is dependent on the height of the F-layer and the distance between the stations *taking into account the curvature of the Earth*). Zolesi and Cander gives the formula for incidence angle as $\varphi_0 = \arctan \frac{\sin\frac{\theta}{2}}{1+\frac{h'}{R}-\cos\frac{\theta}{2}}$, where $\theta$ is the angular distance between the two points on the surface of the Earth, $h'$ is the virtual height of the F-layer, and $R$ is the radius of the Earth. Then the formula $MUF(D) = f_0 \sec \varphi_0 $ can be used to figure out the path MUF given the critical frequency at the midpoint of the path.

But that's pretty hard, so let's fudge it. First off, let's assume that $h' = 300 \,\mathrm{km}$, which is pretty reasonable, especially in the daytime. Then we can precompute some values of MUF(D) for different distances.

```
D (km) | MUF(D) / foF2 | MUF(D) / MUF(3000)
0      | 1             | 0.305
500    | 1.29          | 0.394
1000   | 1.85          | 0.565
1500   | 2.39          | 0.729
2000   | 2.81          | 0.858
2500   | 3.10          | 0.947
3000   | 3.28          | 1

```

So for a 1500km path, if you have a map of foF2, then your MUF should be around 2.4 times the foF2 at the midpoint of the path. If you have a map of MUF(3000), then your MUF should be around 73% of the MUF(3000) at the midpoint of the path. If you want to remember this as "MUF(1500) is about three-quarters of MUF(3000)", that would be perfectly acceptable. This is good enough that you could probably work 20 meters in mid-afternoon even under solar minimum conditions.

The "skip zone" is simply the areas which are too far away for line-of-sight or groundwave, but close enough that the effective MUF at that distance is lower than the chosen frequency. As such, it's completely dependent on the frequency you're using. For frequencies less than the "critical frequency" (foF2), there is no skip zone (these are the NVIS frequencies). As the frequency increases beyond the MUF for longer and longer distances, the skip zone grows, until no propagation is possible. Because the Earth is curved, the incidence angle can't be arbitrarily low — even a signal that leaves the Earth completely horizontal is going to reach the ionosphere at an angle of 15-20°, after travelling 1500 - 2000 km. For this reason, the longest possible single hop between points on the Earth is around 3000 - 4000 km in distance, and that's why we use MUF(3000) as a practical upper limit for skywave frequencies.

As for choosing a launch angle, very few people have any practical ability to fine tune their launch angle. If anything, they might be able to choose between a "DX antenna" which favors low-angle radiation over high-angle, or a "NVIS antenna" which favors high-angle over low-angle. A 1500km hop involves a launch angle in the neighborhood of 20° above the horizon, which is much more on the "DX" end of things.

## Answer (score 8, by hobbs - KC2G)

As an alternative to figuring all of this stuff by hand, you can use a tool like ITURHFPROP which does the math for you, based on statistical models of what the MUF and other variables will be for a given sunspot number, time of year, time of day, and location. I've chosen predtest.uk because it allows me to direct-link to results. After setting the TX location to Portland, the RX location to Phoenix, both antennas to "Dipole", power to 100W, and mode to SSB, the output should look something like

which shows the performance of different frequencies vs. UTC hour, for the month of February 2020. It indicates that your *best* prop is likely to be on 40 meters around sunrise, but also that 20 meters should work well from the morning until the late afternoon, 40 meters should be acceptable (if not great) at any time of day, and 80 meters may be usable at night.

## Answer (score 2, by Dr Marble)

There's a great online calculator for this here:

https://oh1tv.fi/toa-muf/MUF-calculator.html

You give it the distance between stations, and it gives you the MUF-multiplier as well as the MUF (based on "current conditions", although I'm not clear what it's using as a location for that).

It also lists the best take-off-angle and the best antenna height to hit that skip distance. Although, as hobbs said above, you rarely have the opportunity to fine tune the launch angle.

If you want to calculate these yourself, the formulae are:

$$A_m = \sin^{-1}\left(\frac{F_o}{F_b}\right)$$

where $A_m$ is the maximum angle, $F_o$ is the critical frequency in accordance with solar conditions and $F_b$ is the center frequency you are transmitting on.

The MUF can be calculated as:

$$F_m = \frac{F_o}{\sec(A_m)}$$

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16071/how-to-determine-frequency-and-launch-angle-given-a-target-skip-distance, by bitsmack, hobbs - KC2G, Dr Marble. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
