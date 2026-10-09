# Is a gradual power-up recommended for non tube based radios?

*Tags: repair · score 5*

## Question

It used to be that if you wanted to power up an old tube radio, you'd use a variac and gradually bring up the line voltage to avoid damage to the radio.

Is this needed or suggested for transformer powered semiconductor radios that have been sitting around unused for decades?

I expect the answer will be no for radios with switching power supplies, but there are a lot of radios with transformer based power supplies, and some even lacking basic regulation. Will it make a difference in preserving such radios?

## Answer (score 4, by Phil Frost - W8II)

So far as I'm aware, the reason for using a variac isn't that there are tubes, but that the radio is old and unused for a long time.

The reason is that electrolytic capacitors rely on a dielectric (insulation between the plates) that is maintained by an electrochemical reaction between the plates. This reaction requires a voltage across the plates to occur. If the radio is unused for a long time, the dielectric degrades, having no voltage to maintain it. With the weakened dielectric, the capacitor is unable to withstand as much voltage without failure. Bringing the voltage up slowly with a variac, or with a current-limited supply gently reforms the capacitors.

The problem is somewhat compounded by two factors:

- old tube equipment was manufactured when electrolytic capacitors were a newer technology, lacking the reliability of modern electrolytic capacitors
- tube equipment tends to operate at a higher voltage than modern transistor equipment

Because of these factors, and that any transistor radio won't be so old, this reforming procedure isn't so much of a concern for transistor radios. That's not to say it has no value, especially for very early transistor radios, but the utility is rather reduced, I'd say.

Also, in the specific case of switching power supplies you mention, bringing the voltage up slowly with a variac is futile. To a first approximation, a switching supply draws a constant power from the input, so if you provide it a lower input voltage, it will just draw more current from the input in order to produce the designed output voltage.

What you *can* do in the general case is at least limit the damage that will occur if a capacitor, or anything else, is busted in a radio of unknown workingness. A current-limited supply is always a good idea. If you don't have a proper current-limited bench supply, at least assure a properly sized fuse is in place. It's possible a component may burn out, but at least you won't set the radio on fire.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1446/is-a-gradual-power-up-recommended-for-non-tube-based-radios, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
