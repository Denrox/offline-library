# Low power indicated on tuner

*Tags: hf, rf-power, antenna-tuner, swr-meter · score 3*

## Question

Please forgive my extremely basic question, I am brand new on HF and have issues with my setup.

I have a Chameleon MPAS antenna in vertical configuration connected to an AT-100 ProII tuner with a 50 ft long chocked coax cable, which is jumped to my FT-991A. The antenna is supposed to operate between 6 and 160 meters and I'm trying to operate on 40 meter band on 100W. After quite the clicking, the external tuner indicates an SWR around 3 and the radio indicates an SWR between 1 and 1.5. I can hear other transmissions pretty well, but they are getting a lot of noise from my end, rendering me unintelligible. The tuner indicates much lower power, around 30W.

I know the question is rather vague, but what can cause the drop of power? What should I try to fix the issue? Any recommendations are highly appreciated.

73, VA7HUN

## Accepted answer (score 3, by Kevin Reid AG6YO)

Your antenna tuner is not succeeding in finding a good match (indicated by the SWR of 3). This means there are high standing waves — and therefore high voltage — in your feed line between the antenna and the tuner, and power will be dissipated in the components of the tuner and in the feed line — or rather, *more* power than if you had a good match.

Remember that if you start with 100 W and end with 30 W, that's just -5 dB, or a little less than 1 “S meter unit”. Someone who finds you unintelligible now will still find your signal a little low even if you manage to radiate your entire 100 W.

That said, you can and should try to improve this situation. Your tool to do this is adjusting your antenna.

First of all, since you're using a vertical antenna, the #1 most important thing is that it has a good ground/counterpoise/radials (whatever you want to call it, it serves the same function). If you have none, and you have a good choke/balun, then theoretically your antenna would not radiate! You **must** provide what I like to think of as “the second half of the antenna”.

- If your antenna is mounted outdoors on the ground, lay out horizontal wires on the ground radiating out from the base of the antenna. A ground rod driven into the earth may also be useful but is not solely sufficient (because soil is never as good a conductor as wire, though its conductivity does vary with the local soil composition).
- If it's on a pole, and the pole is not metal run a wire (of equal length to the antenna) back along it.
- If it's on a railing or other structure, make sure you have metal-to-metal contact in the mount; if the structure is not metal, add whatever horizontal wires you can manage.

For your particular antenna, counterpoise connection is made through a ring around the “Base Connection” threaded stud on the bottom end. If the supplied wire doesn't work for your situation, then build something that does.

Second, if your antenna's vertical element has any adjustable length elements, try changing them. You've presumably already tried “as long as possible”, so you'll have to go shorter; don't worry about theory, just change it a bit, see what that does to your SWR, and repeat.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22122/low-power-indicated-on-tuner, by kataik, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
