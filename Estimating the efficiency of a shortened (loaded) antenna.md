# Estimating the efficiency of a shortened (loaded) antenna

*Tags: antenna-theory, dipole, efficiency · score 9*

## Question

Recently I've build a trap dipole for 20/40/80m bands. I followed an article by John DeGood, NU3E and got following measurements:

- From balun to 20m trap: 485 cm
- From 20m trap to 40m trap: 362 cm
- From 40m trap to the end of the arm: 530 cm

You can find a complete description of the antenna (including descriptions of the balun, used wire, etc) here and here (in Russian, but Google Translate should manage; please email me if you got any questions).

Since 20m trap acts as a loading coil on 40 and 80 meters and 40m trap acts as a loading coil on 80m the antenna turned out to be much shorter than a full-size 80m dipole, and thus probably less efficient on both 40m and 80m bands. I would like to estimate what is the efficiency of the antenna on these bands *relative* to corresponding full-size dipoles (not an absolute efficiency). The problem is I'm not a mathematician and don't know much about antenna theory.

I was thinking about the following method:

It is based on the fact that the current distribution in the antenna is sinusoidal; it radiates more in the proximity to the balun and almost doesn't radiate at the end of the arm. The radiation and size of the coil are considered neglectable.

I used SciPy to calculate an efficiency of the dipole on 40m band:

```
>>> from scipy.integrate import quad as integrate
>>> from math import cos, pi
>>> wl = 40 # 40 m band
>>> bc = 4.85 # 485 cm before the coil
>>> ac = 3.62 # 362 cm after the coil
>>> integrate(cos, 0, ((bc)/(wl/4))*(pi/2))[0] + \
...         integrate(cos, ((wl/4 - ac)/(wl/4))*(pi/2), pi/2)[0]
0.847610828074005

```

... and got 84.76% efficiency comparing to a full-size 40m dipole. Naturally this is only a rough estimate, and I'm not interested in calculating a very-very accurate value.

Now I have two questions. 1) Is this method more or less OK or is it completely wrong? If it's wrong could you please suggest a better method? 2) Can this method be generalized for 2 and more coils? The problem is that I don't know in which phase the current is between two coils. Thus currently I can only estimate an upper (70%) and lower (41.1%) bounds for 80m, by ignoring one of the coils, and tell that the actual efficiency is somewhere in between (55.5%).

## Accepted answer (score 6, by Glenn W9IQ)

I applaud you for diving into this topic. The notion of trap efficiency has been driven largely by antenna marketing FUD (Fear, Uncertainty, and Doubt) with implicative phrases such as "no lossy traps". Since then, hams have been wringing their hands at the thought of all of those losses in their favorite trap antenna. Here is a current example of such an advertisement:

Unfortunately, your integral approach to the analysis of trap loss will not present usable results. You have effectively pieced together two different antennas while calling the missing current the loss. In order to understand the underlying issues, it pays to briefly explore wave mechanics as they apply to a dipole antenna.

From a wave mechanics perspective, when current initially begins to flow at the feedpoint of a dipole into one of the legs, it travels along the length of the wire until it hits the open end of the dipole. Because the wire has a finite thickness, there is a small amount of self capacitance present at the end. Since this capacitance does not present the same impedance at which the current was flowing, it forms an impedance discontinuity. Any impedance discontinuity forms a complex reflection coefficient that sends (in this case) all of the current traveling in the opposite direction.

Once this reflected current reaches the feedpoint of the antenna, the current standing wave pattern on the antenna fully is established. It has a near sinusoidal shape.

We can repeat the above wave mechanics from the perspective of a voltage wave that will also develop a voltage standing wave. It is the ratio of the voltage standing wave to the current standing wave that determines the impedance at any point along the antenna wire. This is the mechanism by which the feedpoint impedance changes when moving from a center fed to an off center feed dipole arrangement, for example.

When we insert a trap somewhere along the wire, consider what changes. The current starts from the feedpoint as before but when it reaches the trap, there is an impedance discontinuity that establishes a complex reflection coefficient. In this case, part of the current is reflected back toward the feedpoint and part of the current continues through the trap, toward the end of the wire. The portion of the current that reaches the end of the wire is reflected back as before. But when the reflected current reaches the trap, this is another impedance discontinuity. So part of the current passes through the trap and heads for the feedpoint and part is reflected back towards the end of the antenna. Clearly, the trap has significantly altered the wave mechanics compared to simple wire dipole and as a result, the analysis has become very complex.

Despite the very complex wave mechanics, we can still reason that any resistive losses attributable to the trap are largely due to the current passing through the trap. The challenge though is in describing the current profile associated with the trap. Most of the credible analysis you will find in this regard uses computer modeling based on NEC to assess the losses. Unfortunately, I have not found any credible field measurements that have validated the NEC modeling of trap loss.

Most of the well constructed NEC models suggest that a reasonably constructed trap will have losses << 0.5 dB. One such example is this analysis by W8JI. It is notable however, that through the use of bold type and lots of exclamation marks, there seems to be implicit surprises and contradictions noted by the author. Perhaps some of this is attributable to no apparent consideration of the underlying wave mechanics.

Then just when you start to get a grasp on the wave mechanics, it turns out that the inductor itself can have standing waves along its length. Here is an interesting lab picture from Dr. David Knight that shows a wave traveling along an inductor is reflected at the impedance discontinuities that occur at the ends of the wire of the inductor. The picture shows a gas discharge tube in close proximity to an inductively excited coil:

This suggests that a more rigorous analysis should include any standing wave effects associated with the trap itself.

## Answer (score 5, by Cecil - W5DXP)

"The ARRL Antenna Book" uses the ***lumped circuit model*** for HF loading coils which is an inaccurate thing to do in a ***distributed network*** circuit with reflections. The helix model in EZNEC presents a much more accurate picture as does the distributed network model or Maxwell's Equations.

My web page at **www.w5dxp.com** has a lot of information on HF loading coils, some that contradicts the conventional "wisdom" on the topic. In general, an HF loading coil can be treated somewhat like a transmission line with a characteristic impedance and electrical length. There is also a largely ignored current "bulge" inside a loading coil that affects losses in the coil. That "bulge" can cause the loading coil to have the highest ***standing wave current*** in the system. Notice how "The ARRL Antenna Book" has the current decreasing in the bottom section between the feedpoint and the bottom of the coil and a constant current through the coil while, in reality, ***the standing wave current*** actually increases in the bottom section and increases even more through the loading coil. There's just too much information to be included here. Please visit my web page at **www.w5dxp.com** and digest the articles on loading coils.

## Answer (score 3, by Phil Frost - W8II)

Calculating the current distribution on the antenna might be a way to determine the radiation resistance, but to arrive at efficiency will require incorporating loss in the equation. It will be tricky: as Cecil notes the current in the trap could be quite high. Depending on the kind of trap there may be significant dielectric losses to take into account. Ground losses are also relevant and quite site-dependent. Ultimately the complexity is high enough an empirical approach may be more feasible.

I would note a low SWR across a wide band suggests low efficiency. A plain half-wave dipole made of thin wire should have a [2:1 SWR fractional bandwidth in the neighborhood of 6%](Calculating%20bandwidth%20of%20antenna.md) if losses are low. Loading coils should reduce that bandwidth. So if your trap dipole has a bandwidth wider than that, it's a fair inference that antenna efficiency isn't great.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12967/estimating-the-efficiency-of-a-shortened-loaded-antenna, by Aleksander Alekseev - R2AUK, Glenn W9IQ, Cecil - W5DXP, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
