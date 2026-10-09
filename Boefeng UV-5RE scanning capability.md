# Boefeng UV-5RE scanning capability

*Tags: transceiver, baofeng, uv-5r, radio-programming · score 5*

## Question

Since the factory manual is simple and basic, is it possible to use the Baofeng UV-5RE to do these things?

1.

Listen to FM radio, while scanning 2m and 70cm bands in the background (as in hiking)

2.

Set the scan low and high limit, via keypad and/or PC software, so that scanning only takes place within ham bands (instead full transceiver freq range).

3.

Scan 2m and 70cm 'simultaneously'. Does the radio have multiple (FM/UHF/VHF) receivers inside, or can it jump quickly between frequencies and appear to be 'simultaneously' receiving multiple bands?

4.

What can the PC software do that cannot be done with keypad programming? According to some online posts, "NAME" and "AMI" functions are available. Are there others?

## Answer (score 5, by n0p)

1) listen to FM radio, while scanning 2 meters and 70cm bands at background (as in hiking)?

nope (and only 1 band scanning at a time)

2) set scan hi and low limit, via keypad and/or pc software, so that scan within ham band only (instead full transceiver freq range)?

nope, but you can limit the ranges using chirp

3) scan 2m and 70cm 'simultaneously'. Does it has one or two or three (U V FM) real receiver inside only? Or, it can jump quickly between freq and appear to be 'simultaneous'?

nope. Internally there's only one VFO, so even dual watch is just hopping between bands, not listening on both simultaneously

4) what the pc software can do where keypad programming cannot? Seem NAME, ANI are some, from web posts reading, what others?

using chirp you can set the frequency range (even down to 200mhz / up to 599mhz, but the radio won't work well and you can even burn the PA by txing there) setting cross band repeater on memories (to work satellites) These are the two more useful on top on my head right now

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2076/boefeng-uv-5re-scanning-capability, by EEd, n0p. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
