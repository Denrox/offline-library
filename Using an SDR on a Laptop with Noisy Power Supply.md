# Using an SDR on a Laptop with Noisy Power Supply

*Tags: rfi, power-supply · score 5*

## Question

I'm going to start this off by saying I'm very new to this and I don't really know a lot so any detailed information would be much appreciated.

I have just started using an SDR (a cheap RTL model) with my MacBook Pro laptop. The laptop itself is a 2012 and the power supply is a bit older, I bought neither new. I've discovered that while the computer is on battery power I get very little or no interference on 1-30 MHz bands. I will also note, I'm using a Ham It Up upconverter to get access to the HF bands.

When I plug the computer into its power adapter I get a ton of interference, so much so it makes it difficult to actually receive even local AM stations. When the computer is on battery, no such interference. I do have a travel-charger which is a lower wattage for the computer, and when I connect it there is an uptake in interference but it is manageable.

My question is, what can I do to the power supply to reduce its interference? I'm not sure if the interference is coming in to the system via the line or if the interference is coming in to the radio via the air. I'm not even sure if that makes sense, but I hope it does.

Again, any help would be appreciated. I don't have / want to sink a ton of money into this as a project, for right now I can take the easy way out and unplug the laptop from the wall outlet and play around for a 2-4 hours before plugging it back in again.

Thanks in advance.

## Answer (score 5, by Kevin Reid AG6YO)

This may or may not help your particular situation, but when using a laptop power adapter, it can help to use one that is *grounded.* For Apple power supplies in the USA, this means swapping out the folding plug for a cord (which on recent models may not be a stock item, but should have been original equipment with yours).

Any ungrounded computer power supply will add AC line noise to the chassis and signal ground of the computer, compared to no adapter or a grounded adapter.

(Note that this change will do nothing if your outlets are missing the actual ground wiring. If you find out that's the case, you can consult our local Home Improvement Stack Exchange on options for fixing that.)


You can also try adding a choke to the cable between the power supply and the laptop. Get a ferrite ring (not a snap-on "bead") of a ferrite material suitable for suppressing noise on the frequencies you want to receive, then wind several turns of the DC power supply cord through the center of the ring (as if you are making a toroidal inductor, which you are), as close to the power supply as possible. (But don't make it so tight as to damage the cable!)


Try connecting a USB extension cable between the receiver and the laptop. This adds distance from any any *radiated* noise (radio waves as opposed to noise carried on cable shields or USB power).


Variant: Try using a USB hub with its own power supply. Being a digital device, this will be a noise source on its own, but may be a simpler and less troublesome one. (Its stock power supply might be a noise generator itself, but you can add a choke and even try replacing it with a better supply — even a linear one, if you don't mind the heat.)


Variant: Use an *active USB extension*. This is basically a one-port USB hub with an extra-long cable — because it is an active device it can be longer than a passive extension cable while still maintaining signal integrity. You can even get converters to optical fiber, for complete electrical isolation (though I haven't priced those out, only heard they exist).

## Answer (score 2)

The common-mode isolator helps. For lower frequencies (< 1 MHz) it is almost impossible to have high isolation with just one or more ferrite rings. May be this helps: a common mode isolator specially for high-sensitivity outdoor E-field antennas. See picture. My receiver is RSP1A and/or RTL-SDR and I have not any noise from computer and/or power supply, nor from switch-mode supplies in my house. Remote antenna, free standing, 10 meters coax. Technical info: 3 uH * N^2 for the toroid, so 50 wdg makes 7500 uH. Isolation max 5 kOhm at 2 MHz. Signal loss < 1 dB up to 30 MHz (use twisted Cupper-enamel!). PA0FSB

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16407/using-an-sdr-on-a-laptop-with-noisy-power-supply, by TitanShadow, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
