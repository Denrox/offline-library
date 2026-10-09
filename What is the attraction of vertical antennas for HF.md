# What is the attraction of vertical antennas for HF?

*Tags: antenna-construction, vertical-antenna · score 7*

## Question

I understand that MW broadcast stations use vertical antennas because that polarization works much better for groundwave propagation. But in amateur radio, I would assume the focus for communications on the HF bands would be via ionospheric propagation, where the polarization doesn't matter a great deal.

As I contemplate what antenna to install next (after a simple inverted-vee hung out a second story window), I am struck by just how many articles/recommendations and even locals are using vertical antennas for HF communications.

The huge drawback to a vertical seems to be the ground plane required: instead of two light quarter-wavelength wires hung in various fashions across a yard/trees/attic, you instead need a sturdy tower for starters and as the icing on the cake, placement of dozens and dozens of fairly long wires all through your yard.

If you have room for a proper radial system, wouldn't you also have room for a decent loop or inverted vee? What is the attraction of replacing one of the "poles" of a dipole with dozens of almost-as-long radials instead?

## Accepted answer (score 7, by natevw - AF7TB)

Cribbing a few quotes from answers to related questions, here's a start.

From [https://ham.stackexchange.com/a/195/1362](Vertical%20antenna%20on%20HF.md):

The primary advantages of vertical antennas are that they are omnidirectional, and with an appropriate ground plane (radials) yield a low radiation angle; this reduces the number of "hops" that HF signals must make to reach their destination.

This makes a lot of sense: a horizontal dipole will have nulls off its ends, whereas the null of a vertical will point up into space.

From [https://ham.stackexchange.com/a/494/1362](Should%20I%20chose%20a%20vertical%20or%20a%20horizontal%20HF%20antenna.md):

At the lower end of the HF spectrum, the λ/2 height requirement for horizontal antennas can become cumbersome (even though a horizontal phased array may weaken this requirement by allowing somewhat lower heights). A vertical HF antenna can get away with a height of only λ/4.

This is something I keep neglecting to consider: that ideally (at least assuming low-angle radiation is the goal) a horizontal antenna needs to be really really high, i.e. twice as high as a vertical for the same band.

And of course the good old-fashioned [https://ham.stackexchange.com/a/555/1362](Using%20a%20balun%20with%20a%20resonant%20dipole.md):

…the coax shield makes just as fine of an antenna as the dipole. It distorts the radiation pattern horribly, but since a dipole wasn't a directional antenna to begin, it hardly matters. It could mean that you get a lot of RF in the shack, but if you are transmitting with 100W this is unlikely to cause any serious problems.

i.e. sometimes the results of an "antenna" are actually the results of a long leaky feedline plus a generous amount of transmit power. Unless they are operating as loaded end-feds or something, this is the only explanation I can figure out for how HF verticals like the Comet CHA250B might be working in practice with no radials.

## Answer (score 3, by rclocher3)

There are commercially-made verticals that are only 26 feet (8 m) high, that offer decent low-takeoff-angle (DX) performance on eight HF bands (and so-so performance on 80m), assuming that a good radial system has been installed. By comparison, a horizontally-polarized antenna needs to be up fairly high to have good low-angle performance. I seem to recall that a height of λ/2 or higher is recommended for dipoles used for DXing; that's often difficult to achieve for 40m and 80m. By the way, inverted vees have terrible low-angle performance for any direction other than broadside-on.

Any multi-band antenna is a compromise, but if you ask me horizontally-polarized multi-band antennas are more of a compromise than commercially-made multi-band verticals; G5RV-style antennas typically work well on five or six bands, but have two bands that the antenna isn't designed for at all. (Let's please not start yet another G5RV debate here.) Off-center-fed horizontally-polarized antennas can work well, but they make tremendous demands on the balun; when cheap baluns are used, as they often are, then the antenna's performance suffers.

In my opinion, the best reason to use a vertical is that vertically-polarized antennas and horizontally-polarized antennas complement each other so very well. When one works poorly, the other often works beautifully. If you only have a dipole or an inverted-vee up, then I'd advise you to try putting a vertical up also. You might be surprised at what the vertical can pull in that the dipole or inverted-vee can't.

## Answer (score 2, by Scott Earle)

One obvious answer is that a vertical antenna can be made to work in a very small area. The house where I live is a townhouse in a large city, and has basically no land. It is also close to power lines, and so a tower would be totally out even if I had space for one.

What you say about how a vertical can take up as much room as a loop, is true if you put all the radials down to make it work very well. But it can also be bolted on the back of a house with just a few bits of metal on the bottom to act as radials. It won't work as well, but if that's all the space you have then a vertical with a poor ground might well be your only choice.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6300/what-is-the-attraction-of-vertical-antennas-for-hf, by natevw - AF7TB, rclocher3, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
