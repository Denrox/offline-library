# Is 20m noisy, or do I have a lot of local interference?

*Tags: hf, rfi, noise · score 7*

## Question

I'm making my first ventures into HF with a Yaesu FT-450D and a homebrew 20 Meter inverted-V antenna a local ham helped me set up.

I've noticed that the 20 Meterm band seems to have lots of background noise (QRN) everywhere in the band.

The S-meter is sitting at 7 constantly.

By comparison, 30m is at 5, 40m is 1, and 10m is at 1. Of course, this is connected to the same 20M antenna.

Is this amount of noise normal, or am I more likely picking up something nearby that means I should change my antenna setup?

**Additional notes answering comments**

- I'm near Saint Louis, MO.
- Noise has been steady at this level as long as I have it connected to the antenna. No change between daytime and evening.
- It sounds somewhat similar to static you might hear on old analog TV stations, or AM radio sets. It does *not* sound like a 60hz hum.

**Resolution(ish)** - Confirmed with a local ham that when 20m is dead, he reads background noise less than S1.5 at the most with his setup. - Powering down the entire house (all breakers off) and running the radio off the car brought noise down to S3 or so. - Investigation into individual breakers eventually led to my Uninterruptible Power Supply units. I have 5 in the house on 4 different circuits. Powering each one on individually incrementally increased the base noise level from S3 (all off) to S7 (all on).

So I will research eliminating noise from UPSs separately (and probably asking a separate question). I will also be adding a 1:1 choke as soon as I can build one.

## Accepted answer (score 4, by Glenn W9IQ)

Make certain you have a 1:1 choking balun at the apex of your antenna. This will reduce or eliminate the possibilty of common mode currents on your feedline causing it to pickup local interference on receive.

Some other troubleshooting ideas:

Check your radio's power supply for noise by substituting a battery and disconnecting the PS from the wall.

Run your receiver on a battery and turn off your main breaker. (Remember to shut any desktop computers down first. It's not good for them to abruptly lose power. Laptops, tablets, and phones are fine because of their batteries.) Make sure any battery powered computers/tablets are fully powered off. If the noise reduces, turn off all branch breakers, turn the main breaker back on, and one by one turn on the branch breakers noting any change in noise.

Install an additional 1:1 balun close to your radio. This sometimes helps prevent local noise pickup on the coax outer shield.

Check your coax for any open or marginal connections - especially the shield connections. Try substituting other coax.

Eliminate any tuner, linear, SWR meters, and patch coax cables and note any change in noise levels.

If you have a lightning arrestor on your coax, try temporarily bypassing it.

Try temporarily removing any station grounds leaving the AC safety ground in place.

Take your transceiver to a location in the country with a portable antenna and running off batteries to eliminate receiver problems. Alternatively take it to another ham's QTH that isn't suffering from noise to check it.

Borrow or rent a battery powered spectrum analyzer and walk your QTH and the neighborhood sniffing for RFI with a small dipole or loop.

After eliminating all other possibilities, call the power company and let them know you suspect a cracked insulator or bad transformer is causing RFI. They have techs that specialize in these sorts of problems.

## Answer (score 4, by user10471)

At my home, background noise is typically S6-S9 pretty much all the time on anything lower than 20 meters. 17 and up is generally less noisy, although I occasionally will have some really strong noise on 10m. In investigating this, I tried running my radio (IC-718 with a 40m cut OCF dipole, mildly sloping wires, peak at about 25 feet, directly over the house) on a battery and shutting off the entire house electrical system. This dropped the noise level to about S3-S5. However - as I switched on breakers one-by-one, I found one breaker seemed to raise the noise level more than the others, but I could not figure out where the noise was being generated, as I disconnected all the loads I could find on that circuit, and still had the noise.

One local ham suggested that it could be my doorbell transformer, as apparently they have some kind of thermal device on the transformer that can get noisy, but I cannot find my doorbell transformer! Your situation sounds similar to mine, except that 40 is very noisy for me, also. It could also be that using the 20m antenna on 40, the mismatch might be causing a loss of sensitivity. If it is any way possible to change the antenna location, see if the noise seems to lessen as you move it away from the house.

## Answer (score 2, by Dick Reid)

House alarm systems turn the wiring into an antenna generating RF. The usual process of switching off the power and adding back breaker by breaker can be confusing. The battery backup will kick in and make it seem like the circuit is NOT off when it actually is off.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9342/is-20m-noisy-or-do-i-have-a-lot-of-local-interference, by Adam KC0DAD, Glenn W9IQ, user10471, Dick Reid. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
