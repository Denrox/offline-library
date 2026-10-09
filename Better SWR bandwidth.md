# Better SWR bandwidth

*Tags: mobile, impedance-matching · score 5*

## Question

Good day,

I have a Kenwood TS-480HT with a Wolfriver coil and a stainless steel whip in my car.

I find that on 40 meters I can get the SWR at around 1.4 (using an MFJ 269) at 7.1000 MHz. But the SWR goes high (2.5 to 3.0) very quickly if I go closer to 7.0000 and even higher if I go closer to 7.2000 (past 6.0).

This also happens on 80 meters.

Is there a way I can increase the SWR bandwidth?

## Accepted answer (score 6, by Phil Frost - W8II)

A low SWR bandwidth is a consequence of shortening the antenna for mobile use. SWR bandwidth is related to the antenna system's Q factor, the ratio of energy stored to energy dissipated per cycle. A higher Q means less SWR bandwidth.

Decreasing Q will increase SWR bandwidth. That can be done by decreasing the energy stored, or increasing the energy dissipated.

A smaller loading coil will decrease energy stored, but will require a longer whip.

Distributing more current over a longer length of the antenna will increase the energy dissipated by radiation. This can be done by moving the loading coil up, thus leaving a longer section of antenna below the loading coil with high current. Or a capacitive hat at the top of the antenna increases current overall. But in either case there's some cost to be paid: higher wind loading, a longer whip, or a bigger loading coil with associated loss.

Of course energy dissipated can also be increased by increasing losses, but that's not really desirable. So if it makes you feel better, a low SWR bandwidth suggests a good, efficient antenna!

## Answer (score 3, by hotpaw2)

Capacitive hats (spokes, discs, or loops) on the tops of vertical antennas are reported to increase SWR bandwidth, as well as increasing radiation resistance (the loading inductance or antenna length may need to be (re)adjusted for resonance). Downside is an increase in wind loading.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14909/better-swr-bandwidth, by Danny, Phil Frost - W8II, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
