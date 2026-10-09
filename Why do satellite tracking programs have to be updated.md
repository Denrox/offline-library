# Why do satellite tracking programs have to be updated?

*Tags: satellites · score 4*

## Question

So I've heard every once and a while you have to update your satellite tracking software because of the fact that the satellites are falling towards Earth. Why can't the program automatically calculate every factor in so it doesn't have to update it?

## Accepted answer (score 4, by Malcolm VE2DDZ)

You must update the orbital elements that your satellite tracking software uses to predict the location of satellites in order to get continued accuracy in the predictions. Sometimes the orbital elements are not known exactly for a new or relatively unimportant satellite. More importantly, the orbital elements can and will change over time. Low earth orbit satellites will slow down due to friction from the remnants of atmosphere at their altitude. All satellites will have their orbits affected by the gravitational influence of other bodies. Although the principal gravitational effects will be from the Earth, Moon and Sun, other objects will also influence the orbit.

## Answer (score 5, by PearsonArtPhoto)

There are at least 4 significant things that make satellites difficult to exactly determine:

1. The position and velocity of a satellite is only known at any one time with a finite precision. Without a perfect knowledge of where the satellite is and how fast it's moving, it's impossible to know where it will be in the future.
2. The atmosphere is quite uncertain, sometimes it will drag more, other times drag less. The amount depends on the amount of solar activity. Also, the drag depends on the orientation of the spacecraft, so an anomaly in the spacecraft pointing can cause problems in determining where it is.
3. There are complex gravitational factors that can influence where the spacecraft is. These are very difficult to program in.
4. Thrusting, either in the form of an active propulsion from the spacecraft, or being hit by space debris or other objects, can cause problems.

Bottom line, it's just a hard problem to figure out, and it's much easier to get periodic updates to the satellite positions. But if you can't get them for a while, you should be fine for a period of time, several weeks at least. If you can't get them in that period of time, then your best bet is to try listening for the W1AW broadcasts, which give out the amateur satellite element sets.

## Answer (score 2, by hotpaw2)

Some of the factors, such as friction against the upper atmosphere, can have the same sort of predictive problems as with lower weather prediction (non-linear dynamical "chaos", or sensitivity to initial conditions that is well beneath measurement error). A satellite in orbit is also part of an N-body system, which does not have a clean closed form trajectory solution.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1346/why-do-satellite-tracking-programs-have-to-be-updated, by Skyler 440, Malcolm VE2DDZ, PearsonArtPhoto, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
