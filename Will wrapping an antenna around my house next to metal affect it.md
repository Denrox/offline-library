# Will wrapping an antenna around my house next to metal affect it?

*Tags: antenna, antenna-theory, antenna-construction, wire-antenna · score 3*

## Question

My unit is 25' by 25' each side and the front is 22' across. The overhang is about one foot with aluminum and vinyl underneath. If I wrap an OCF dipole (fed with 4:1 balun) around this overhang in close proximity to the aluminum support angle, how will all this affect the antenna? Most of my operating will be QRP - 5 watts or less. I am trying to "hide" most of the antenna.

## Answer (score 2, by Glenn W9IQ)

It is nearly impossible to accurately model this configuration but some general observations can be made.

Placing any antenna, including an OCFD, in very close proximity to other metal objects will generally detune the antenna. This will typically negatively impact the expected SWR- especially in a multiband configuration such as an OCFD. While SWR is not an indication of antenna performance, an elevated SWR may lead to higher feed line loss and may necessitate the need for additional matching measures such as a tuner.

Altering the geometry of a wire antenna, such as wrapping it around a house, will also detune the antenna but more importantly, it will alter its directivity. The impact of this changed directivity is hard to predict - it could prove beneficial in covering more directions, for example. The venerable G5RV dipole design by Louis Varney exploited this type of feature.

When running a low power transmitter, these antenna compromises become more significant. But with that being said, every antenna has compromises. You may wish to simply experiment with your OCFD design to see how it works for you. Having an antenna analyzer available will provide you greater insight as you experiment.

## Answer (score 2, by Jack K6JEB)

Sounds like you face the challenges of many hams worldwide who are trying to get in on the fun while not irking the neighbors, landlords, and/or HOA rules; so firstly, relax and know that you will still have fun and make some contacts with the wire antenna you describe. after all, it's 'amateur' radio because we don't have to have a perfect setup to enjoy our hobby.

You will definitely notice that even a carefully-pruned antenna will detune and behave outside the predicted patterns of that same antenna in (mostly) free space. Anything generally within 1/4-wavelength of your antenna will usually interact with it. Basically, the nearby aluminum support angle will absorb some of that transmitted RF energy. It should be noted that loop designs like quad antennas or horizontal loops are less prone to interacting with nearby objects, so if I were you I would compare, in modeling software, your OCF dipole with a horizontal loop that follows the perimeter of your home. You would still want to use the 4:1 balun at the feedpoint (and you will want to model this as well).

I highly recommend learning to use antenna modeling software. use it not just to model the antenna in free space, but you can also model other metallic objects so you can get a better sense of what you're up against. For me, modeling antennas has helped me decide on what to build and what to retire from my antenna farms. It has helped me avoid some major pitfalls before I even went outside to put up an antenna.

If you're a Linux user, there are a number of antenna modeling applications free for the download:

Antenna modeling software for Linux

For Windows, I highly suggest 4nec2, also free:

4NEC2 site

Macintosh users rejoice, there is cocoaNEC:

cocoaNEC site

Lastly, try putting that antenna up there and see how it goes! It might not be perfect but it will still be better than no antenna.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12225/will-wrapping-an-antenna-around-my-house-next-to-metal-affect-it, by Fred Hogaboom N1KWW, Glenn W9IQ, Jack K6JEB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
