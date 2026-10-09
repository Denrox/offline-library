# Tiger Tail + capacitive coupling... what's the interaction?

*Tags: antenna, antenna-theory, antenna-construction, mobile · score 5*

## Question

I've been working on a 2m setup for hiking. My goal is to have the best possible antenna that can be used while walking, and that won't get damaged if I walk under a low branch or some other forest obstacle.

The setup so far: Off the top of a backpack with a steel frame I mounted a Diamond SRH77CA whip. It is connected by a very short length of coax to the HT in a side pocket of the pack, and then I have a speaker/mic clipped to a shoulder strap:

So far, so good, and the whip has proved to be both rugged and stable in its mounting.

In order to further improve the antenna's performance, I added a "Tiger Tail" counterpoise, following the directions here. (There's more about the theory behind that here.) It's a roughly 19" wire, 14ga, hanging from the base of the antenna down the side of the frame pack. According to the theory, this "transforms the 1⁄4-λ whip into a full-size center-fed 1⁄2-λ dipole". Yay for theory.

The PDF with the directions notes, "The hardest part of using this Tail is getting the wire to hang straight," but with the backback frame right there, I anchored it down the side using small zip ties in a few spots, and it's running straight up and down.

Now, the question: is the steel frame of the pack possibly messing with the performance of the Tiger Tail? Does a counterpoise need to hang in free space to work properly? Or by providing a solid, well-defined counterpoise path with that wire, have I prevented the antenna from capacitively coupling to the steel in the frame?

Thank you for your help, antenna wizards...

## Answer (score 4, by JSH)

I tested your make/model antenna and others in various configurations with and without a tiger-tail on a small 2m HT with results in this article. Here is the money graph...

Needless to say the extra bit of counterpoise helps A LOT and reveals why these 1/4 wave replacement whips on HTs often are no better than the well engineered stubby stock antenna as the above graph suggests.

We took this concept a bit further using a 1/4 wave or so bit of braid strap on a shoulder mounted antenna atop a tactical vest. Needless to say, despite the existence of a lengthy coaxial feedline, the braid strap weaved in a serpentine fashion increased the EiRP also by about 10 dB. That's a mighty fine return on investment. Most of the tak vest is non-conductive ballistic stop material so didn't interfere with the "hot" end of the ground strap... and that's an important point about these 1/4 wave "tiger tails"... the high voltage end needs separation from other conductive and sometimes dielectric materials to perform their best. However we found there was lots of slop tolerable in this approach.

You have that nice metal in your frame so, as others suggest, you may well be better off to tie your antenna "ground" point to the closest frame piece. The only caution I can give is the possibility your frame's connection points may not pass currents... or worse sometimes do resulting in scratchy radio performance. It's just something to keep in mind as you continue your cool project.

## Answer (score 3, by Phil Frost - W8II)

Is the steel frame of the pack possibly messing with the performance of the Tiger Tail?

The frame is definitely interacting strongly with the antenna. With the tiger tail zip-tied to the frame you have something like a twin-lead transmission line made from the tiger tail and the frame tube, so you'll be exciting the backpack frame just as much as the tiger tail.

Whether or not that's detrimental to performance is difficult to say. I'd say if you really want the best possible, set up a field strength meter and measure the radiated power from the antenna empirically. You might find the tiger tail doesn't improve performance significantly, since the frame is already a pretty good counterpoise.

There's not really a reasonable way to add a counterpoise to that setup that doesn't interact strongly with the backpack frame besides possibly mounting the whip over a ground plane such that the backpack is "behind" the ground plane. However, such a ground plane would be pretty cumbersome, and I'd estimate the performance improvement is negligible.

## Answer (score 3, by Glenn W9IQ)

There is a good chance that in your original configuration, the coaxial shield acted as a sufficient counterpoise. This is essentially beneficial common mode current on the outside of the shield.

As Phil correctly points out, the coupling to the backpack frame throws doubt on any theoretical analysis.

You may in fact be more effective by deliberately using the frame as the counterpoise instead of an added counterpoise. Sorry, but "tiger tail" sounds so CBish.

To do relative field strength measurements, simply involve a friend and a receiver with an S meter or other RSSI indicator. You cannot make applicable measurements by yourself without more complex remote monitoring capabilities as the presence of your body in the backpack will also influence the performance of your antenna system.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7876/tiger-tail-capacitive-coupling-what-s-the-interaction, by Dr Marble, JSH, Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
