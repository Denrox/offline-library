# What is this vertical antenna with radials pointing up

*Tags: antenna, hf, vertical-antenna · score 5*

## Question

I work next to "Koninklijk Marine Kadettenkorps Afdeling Oostende" (Royal Marine Cadet Corps Ostend). They have an antenna that I've been wondering about for years now:

It is a vertical antenna, likely HF bands with four radials angled about 45 degrees from the vertical. So far, completely normal.

However, the verticals are pointing **up**. I've never seen this kind of antenna. For I long time I thought maybe someone just made a mistake while putting it together, but I can't honestly believe no one would have fixed it over time.

I am not proficient in any NEC program to simulate it myself. What is this kind of antenna used for?

## Accepted answer (score 2, by Dieter Vansteenwegen)

Found it through help from a friend.

It is a differential correction (dGPS) transmitter for Ostend on 312kHz.

A seemingly similar antenna (for same frequency band) can be found for example on the Banten website., with the datasheet here: Datasheet.

In case the datasheet ever gets lost (dead link), the most important things to note are:

- Frequency: 200-1800kHz
- Max power: 250W
- Capacitance: 130pF (@300kHz)
- Vertical polarisation

The radials would be to increase bandwith.

Still looking around to find more on the antenna design though...

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21687/what-is-this-vertical-antenna-with-radials-pointing-up, by Dieter Vansteenwegen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
