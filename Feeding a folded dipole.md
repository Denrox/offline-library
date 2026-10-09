# Feeding a folded dipole

*Tags: antenna · score 5*

## Question

Can I feed a folded dipole constructed of hollow tubing by threading coax through the element to create both an impedance transformation and balun? I have fed coax through the tubing of the dipole from a point opposite the feed point and soldered directly to the open ends of the dipole from inside the tubing. SWR seems ok with 50 ohm cable but a I being fooled into thinking all is ok? A bit hard to explain, the coax is inside the element for 1/2 wavelength.

## Answer (score 3, by tomnexus)

Running the coax through the folded dipole is one good way of feeding it.

Advantages over the more traditional 1/2 wave coax balun:

- No balun required - unbalanced coax all the way to the feedpoint, with guaranteed symmetrical excitation
- Easier to waterproof the feed, as the connections are inside, and you can heatshrink over the feedpoint
- Only one side of the dipole touches anything, the other just hangs open

Disadvantages:

- Matching network may be less broadband than the 1/2 wave feed
- Manufacturing process is a little fiddly

To answer your questions directly:

1.

Yes you can feed a folded dipole by passing the coax through the tube

2.

It doesn't really create any impedance transformation  
(but it does take care of the balancing that's otherwise required)

3.

Your measured impedance seems suspiciously good - as you describe it I would expect you to find a 4:1 VSWR.

**Let me draw a few diagrams**

1) This is the case I believe you are describing:  
  
The coax is hidden entirely inside the pipe, so it has the minimum effect on the patterns, and no balun is required to feed the balanced antenna from the unbalanced input. The coax should see the full 200-300 ohm impedance of the folded dipole, so a bad match without further work.

2) One of these probably describes what you did when you say  
*"When I connect the coax to the folded dipole terminals directly I get an SWR of around 8:1"*:  
  
  
You shouldn't really connect the coax like this, it's not even worth measuring. The effect of the feedline is so profound, especially on the higher impedance of the folded dipole, that you won't learn anything about the dipole impedance.

3) I recommend something like this:  
  
With the coax run through the pipe, the required balun action is taken care of.  
Some impedance transformation is required. In this drawing I've shown a piece of 100 Ohm cable, 1/4 wave long, when I built some of these I used a small PCB across the feed gap, which makes the connections more robust and takes care of the 100 Ohm line. You could also use an actual 4:1 Unun transformer, or even an LC network, though that will be quite narrow band and spoil the dipole.

You can see a photo of a commercial dipole fed "through the pipe" here (not mine!).

## Answer (score 2, by Brian K1LI)

It seems as though your configuration might represent something like the $\frac{\lambda}{2}$ 4:1 coax balun shown in figure 5 on page 18-6 of the ARRL *Antenna Book*:

I've been unable to see the equivalence, but running your coax feedline through the tubing does result in two coaxial lines:

1. the center conductor and the inside of the shield of the feedline
2. the outside of the shield of the feedline and the inside of the antenna tubing

This means that the feedline jacket and the air-space between the feedline jacket and the inside of the antenna tubing comprise the "dielectric" of the second coaxial line. We can't compute the impedance of this second coaxial line without knowing its dimensions and the composition of the jacket material, but it seems as though it would be difficult to control this impedance unless the fit was fairly snug. Since you observe a strong effect on the SWR at the input to the feedling, it's possible that you've hit on a serendipitous combination of variables that produces your desired results, one of which could even be the feedline length back to the SWR meter.

As long as the resulting signal strength is what you expect, it sounds like you have what you need. Nice work!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14713/feeding-a-folded-dipole, by R Johnson, tomnexus, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
