# Use a TV coax and balun for a poor-man's OCFD?

*Tags: antenna-theory, coaxial-cable, antenna-system, balun, feed-line · score 8*

## Question

Can I use TV coax and a cheap TV balun to build a poor-man's OCFD? Marginal performance is acceptable if it saves money. If I could listen to 10% of transmitters within a 100 mile radius that would be acceptable. And as for the coax length, probably no more than 20 feet.

Just getting started and not a lot of cash. Want to do lots of listening on both my RTL-SDR and Pixie 2 40M QRP kit. (Probably would build two antennas, one for each radio.) I already have a 75-300 ohm TV balun and lots of CATV coax. Per this page when an OCFD is 20-25 feet above ground I should use a 4:1 balun, which matches the 75-300 ratio, if I am not mistaken. And 25 feet is about the max height I can get by slinging up in the trees around my house.

I am aware that using 75 ohm line on a 50 ohm Pixie will result in at least a 1.5:1 SWR, if not higher. And the RTL-SDR already has a 75 ohm input, so there's that. But I'm not going for excellent performance, just want to be able to listen to some of the transmissions in my region. Would be cool to pick up overseas as well, but that may be wishful thinking.

I may transmit, but that would not be a priority.

Oh and it wouldn't be strung up 24x7, just when I wanted to go listen then taken down the rest of the time. So I'm not concerned about lightning/rain/snow/wind.

## Accepted answer (score 5, by Edwin van Mierlo)

OK, let me try to answer this, but this answer may also be qualified as unqualified.

If you have a 50 Ohm receiver, and connect a perfectly (Z=R) 75 ohm antenna system, then your VSWR would be 1.5, and the "load mismatch attenuation" will be about 0.177dB. (with antenna **system** I include feedline)

I doubt that you would actually notice this.

However, you are using an RTL-SDR dongle with a source impedance of 75 ohm, and your feedline is 75 ohm, you use a proper 4:1 balun for a 300 ohm antenna, then you should be good to go. Even when you change over to a 50-Ohm receiver the loss due to mismatch is negligible.

The unknowns here is the suggested balun, and its behaviour when used with the OCFD. Unknown is also the quality and specifications of the "TV coax" you are planning of using.

As you are starting, and as you are only listening (no TX), I would actually fully agree with the answer given by Mike Waters unqualified or not.

Without knowing the very specifics of the TV-balun, and TV-coax, it would be hard for anyone to come up with a qualified or quantified answer for your particular question.

However, I did started off in this hobby as a SWL. And I have used unspecified components and material to build a range of antenna's.

- rule 1: any antenna is better than no antenna
- rule 2: any feedline is better than no feedline
- rule 3: it is a hobby in which you can go mad... watch your wallet
- rule 4: it is fun to experiment

For antennas I have used from rain gutters to water pipes, as feedline I have used from TV-coax to speaker-wire.

I have used a step-ladder as antenna...

Have I used TV-baluns ? -- yes I have, with various succes, pulled it down, swap in/out, try again

Have I used "some coax" ? -- yes I have, with various succes, sometimes it was just deaf... which means: replace.

Have I used a TV-balun with TV-coax and a OCFD ? -- no, I have no practical or qualified response to that...

As an SWL, work with the materials you have, work with what can be got cheaply, experiment, direct feed your OCFD, use the TV-balun... the succes rate is determined on what you hear, not what is calculated upfront. Then if you want to squeeze every single micro-dB out of your antenna system, then you can look at different materials/components, and budget for such.

And even when you calculate all this upfront, the moment you hang it outside in a tree or near a building, over real ground, the calculations may be off.

You do mention "may transmit", and just a word of caution here. If you really want to TX, then I would suggest to design/build an antenna for this with known components in order to avoid damage to your transmitter. This answer was written for RX not TX.

Have fun! It is a great hobby, and you will be surprised what you can receive with very little.

## Answer (score 4, by sm5bsz)

TV coax typically has foam dielectric and very low loss. On receive it does not matter if you use 50, 60 72 or 75 ohm cable. With short cables, losses are also not important. The cheap TV balun could be problematic, particularly if you want to transmit. It is trivial to make a 1:2 transformer to get the 4:1 impedance transformation you need, but it is hard to get bandwidth larger than 10:1.

I suggest you go ahead without worrying so much about what is theoretically optimum. Start activity - then find what are the annoying limitations of your set-up. Once you know, (if you find any) you can put more interesting questions to the forum:-)

## Answer (score 3, by Mike Waters)

Just Do It! :-)

You should build it with those materials you have. What have you got to lose? I believe it will exceed your expectations.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9068/use-a-tv-coax-and-balun-for-a-poor-man-s-ocfd, by SlowBro, Edwin van Mierlo, sm5bsz, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
