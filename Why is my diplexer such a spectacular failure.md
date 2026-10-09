# Why is my diplexer such a spectacular failure?

*Tags: diy, swr-meter, duplexer · score 10*

## Question

I'm trying to create a diplexer for the 2m and 70cm bands so that two antennas can share a feedline to my "shack". My radio is a Yaesu FT60 handheld, 5W max.

I have home made a j-pole for 2m, and a neat little ground plane antenna for 70cm, both of which show an SWR under 1.2:1 throughout their respective band, according to my Rig Expert. Both antennas have been analysed under various different feedline and mounting arrangements, with SWR curves staying very consistent - pretty confident about these results.

So I found this circuit on the internet:

I simulated it in LTspice out of curiousity and the response looked legit, so I whipped up a little single-sided PCB and soldered the components on. (without my magnifiers and with a very wonky tip, sorry)

I put this PCB in a stylish aluminium alloy box, with short stubs of RG58 connecting the I/O solder pads on the board with SO-239s mounted to the box.

Unfortunately, with the diplexer installed on my main feedline (~25 feet of LMR-240) and each antenna connected to its respective SO-239 with about 3 feet of RG58, I'm looking at between 3:1 and 4:1 across both bands.

I have carefully examined and electrically tested the PCB and the RG58 stubs/connectors for dead shorts or other issues but can find none.

Is there something *obviously* "wrong" about what I've done here?

(not sure what tags are most appropriate for this question, suggestions welcome)

Cheers!!

## Answer (score 5, by Brian K1LI)

Like you, I modeled your diplexer in LTSpice, but I don't find the results to be acceptable. At 147-MHz, the input impedance is 87$\Omega$; at 443-MHz, it's 24$\Omega$. Also, the crossover frequency is about 350-MHz, which seems too high.

Tonne Software offers Diplexer Designer to address your requirement. Creating a low-pass / high-pass design with a crossover frequency of $f_{cross} = \sqrt{147*435}$ = 253-MHz delivers better results:

The ~33-dB rejection shown by Diplexer Designer's plot function are confirmed by LTSpice:

and the 50-$\Omega$ impedance presented to the generator on each band is well-controlled:

These plots were made possible by performing an AC analysis on the LTSpice circuit and taking advantage of the ".net" LTSpice directive, as shown in the LTSpice diagram below:

## Answer (score 5, by vu2nan)

You have soldered a 68nH inductor instead of 100nH!

Maybe the layout and the wiring also play a key role.

Here's a vintage commercial one.

It's quite compact. The size, inclusive of the coaxial sockets, is 4" x 2" x 1".

Here's the schematic.

Tin plating is observed inside the enclosure.

There is no PCB and the wiring is point-to-point. Connections to the coaxial socket centre pins are direct (coaxial cables are not used). 'Common' connection to the coaxial socket bodies is via the enclosure itself.

Capacitors are miniature disc ceramic. The ground end of C1 and C3 are directly soldered to the enclosure.

## Answer (score 2, by Ngineer)

The added capacitance of the RG58 stubs may also be an issue. I suggest using flat copper strip instead between the port connectors and the PCB. While you can probably get away with SO239's for just 2m, N connectors (or similar UHF connectors) are really mandatory here.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16622/why-is-my-diplexer-such-a-spectacular-failure, by Brian K1LI, vu2nan, Ngineer. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
