# How does the material of a fishing-pole mast affect antenna performance?

*Tags: antenna-construction, wire-antenna, dipole, vertical-antenna · score 5*

## Question

I'm a newly-licenced ham and currently starting out with HF. My home doesn't allow for a permanent setup. I can therefore only operate portable from parks and such, with limited TX power (my rig goes up to 20W), so an efficient antenna seems important to ensure the best rate of success.

Of all portable antenna configurations I've tried, I've had the most success with a monoband 20m vertical consisting of a 5-meter fiberglass fishing rod with a wire spirally wound(*) around it top to bottom and 4 radials laying on the ground.

I would now like to try working the bands that lie lower down (for now 30, maybe 40 meters), but for that I'd have to get myself a longer mast, and all the 7+ meter fishing rods that I could find have at least some carbon fiber content.

CF is conductive, so logically it must interfere with the antenna's operation, possibly throwing off the tuning and/or causing resistive losses in the carbon. I'm also considering hoisting a speaker wire dipole on such a mast. In that case, again, it seems that a conductive mast must interfere with the twinlead section of the feedline.

How significant is this effect in practice, and how exactly does a poorly conductive mast affect antenna performance for the configurations mentioned?

clarifications: (*) the spiral is a very spread-out/slow one, pitched just enough so that the wire would sit tightly against the mast without flapping around in the wind. It is nowhere near tight enough to count as a loading coil, so the antenna should be considered equivalent to one where the wire runs up in a straight line.

## Answer (score 2, by Ryuji AB1WX)

When using a carbon fiber mast as a vertical antenna support, I think one factor is to lift the bottom end of the mast from the ground or any surrounding conductive structure. I didn't run a simulation to demonstrate how big or small this effect is, but some RF current from the antenna feedpoint will get diverted straight down to the ground, if the mast comes near the ground.

Since the carbon mast is floating from the radiator and the radial system, the current induced in the carbon fiber cannot be directly reduced by increasing the conductivity of the radiator element (since the boundary conditions are different for those two parallel conductors, and we don't even know what it is for the carbon fiber). Instead, any mechanism to keep a decent spacing between the two would be more helpful. The space doesn't even have to be uniform, but even a centimeter or two would be useful. However, the loss due to this mechanism is probably much smaller than the radiator current diverted to the ground, so I wouldn't put too much effort into it.

With the above two points, I don't feel any difference between carbon and fiberglass in the antenna performance.

If you magnify the photo, you'll see that I used a white fiberglass tube (with a stopper screw) to lift up the bottom of SOTAbeams Carbon6 mast. This interrupts the path diverting the radiator current to the ground.

A dead tree works well, too. I've also used wooden and bamboo trekking poles as a way to extend and insulate the carbon mast with good results, though requiring a bit more work.

Lifting the feedpoint by 1 meter or more above ground has another significant advantage of minimizing ground loss. When a vertical monopole is placed on or near the ground, the near field from the radiator directly interacts with the ground soil, creating another pathway for the radiator current to be diverted to the ground. This effect can be minimized by lifting the feedpoint and using an elevated radial system.

Sidenote: my feedpoint has a Ruthroff transformer (1:1, 4:1 and 9:1 tapped) to drive the same 5.2m-long element on all bands between 30m and 10m. My feedline is actually made from 93ohm coax to further help the impedance transformation so that the tuner in KX3 never sees a range of impedances that are inefficient to match. On that 93ohm coax, I have a Guanella transformer as a common mode choke.

I use 5.2m-long vertical radiator along SOTAbeams Carbon6 mast, with a radial loop, with the feedpoint lifted above the ground with fiberglass tube. When I QRV on 40m for SOTA, it is usually daylight NVIS hours, so the best results I got so far was to attach another 5 or 6 meter horizontal wire from the top to make an inverted L, and then use a tuner to match. A center-loading is second best, and base-loading least effective.

ADDENDUM

Feedline transformer and Anderson Powerpole. This transformer can take 100W but I only run 10W in this setup. I built a beefier one for my bicycle or SUV station setup.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18838/how-does-the-material-of-a-fishing-pole-mast-affect-antenna-performance, by Ivan R2AZR, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
