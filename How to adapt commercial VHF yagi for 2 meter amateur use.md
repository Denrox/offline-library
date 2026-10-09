# How to adapt commercial VHF yagi for 2 meter amateur use?

*Tags: antenna, antenna-construction, 2m-band, yagi · score 5*

## Question

I recently acquired a Decibel 3-element VHF Yagi that was formerly in commercial service. I connected my MFJ-259B antenna analyzer to the antenna and found its minimum SWR at 155 MHz. I have not measured the boom length or the element lengths.

I'm told this antenna has a "stub match", but that's not a matching system I'm familiar with. There is a small (apparently aluminum) tube a couple of inches above the driven element - on one side is the feed line, and on the other is a small piece of coax that is physically connected to both the driven element and the tube above, but only appears to be shorted to the short tube.

I have measured the impedance of the antenna at 146 MHz to be R = 36 Ohms and X = 40 Ohms.

How can I best adapt this antenna for 2 meter use? I don't think I have the proper tools to trim the element lengths.

Picture of the matching section:

Picture of the whole antenna:

## Accepted answer (score 2, by Glenn W9IQ)

I'm told this antenna has a "stub match", but that's not a matching system I'm familiar with.

The matching system is a delta match with a stub. A delta match cannot cancel out the reactance of the driven element so a stub is added to cancel the reactance. The spread connections of the coax on the tube form the delta match and the vertical bars form the stub.

How can I best adapt this antenna for 2 meter use? I don't think I have the proper tools to trim the element lengths.

As you noted, the antenna is setup for 155 MHz. To "trim" the antenna for 146 MHz, you would need to *add* length to all of the elements since a lower frequency requires longer elements. To optimize the antenna, you would also need to re-space the elements.

The simplest approach to using this antenna on 2 meters is to note the complex impedance (the R and the X) directly at the antenna at your desired two meter frequency. From this a simple matching network can be constructed to provide a 1:1 SWR on the feedline. The pattern and gain of the antenna will not be optimized but it may prove sufficient for your use.

If you are not familiar with designing a matching network, you may wish to measure and report the R and X values at your chosen two meter frequency (directly connected to the antenna without coax) within your question so that I or others may be prescriptive regarding the matching network you will need. It will likely involve only a single inductor and a single capacitor.

[edit]

The OP has an updated post that states the impedance at the feed point of the antenna is 36+j40 at 146 MHz. A matching network consisting of a 26 pF capacitor placed across the antenna connection and a 43 nH inductor placed in series with the center coax connection will change this impedance to 50 ohms and result in a near 1:1 SWR on the coax. Such an inductor can be fashioned as 4 turns of 16 or 18 gauge bare wire spaced out 0.5 inches wound on a 0.25 inch form which is then removed. The final SWR can be adjusted by very slightly expanding or compressing the coil.

Since some antenna analyzers do not properly indicate the sign of the reactive part of the impedance, it could be that the impedance is 36-j40. In this case the capacitor should be 14 pF and the inductor 68 nH. But the capacitor now goes across the coax connections and the inductor in series with the center lead of the antenna. The inductor can be fashioned as above but with 5 turns. You may also choose to use a high quality variable capacitor which can add to the adjustability of the matching network.

These matching networks used to take laborious calculations to derive the correct values. But now there are many programs (e.g. Elsie) and on-line calculators that take the drudgery out of the exercise. My favorite on-line calculator is http://leleivre.com/rf_lcmatch.html. I used this site to calculate the values shown. Here is a screenshot of the result of the first matching network:

I note that other LC configurations are often possible. I chose to illustrate the versions where the DC properties of the antenna were maintained.

Whatever version of the matching circuit that is used, your antenna analyzer can be used to fine tune the circuit. Simply connect the matching circuit directly to the antenna (without coax) and place the analyzer on the coax side (without coax) of the matching network. Adjust until you show R = 49 to 52 ohms and X as close to zero as possible. Remove the analyzer and connect your coax cable. Double check your measurements at the far end of the coax cable. You should see an SWR close to 1:1. If not, your body and antenna analyzer capacitance may have been interacting with the antenna while you were making your adjustments. The matching circuit can be enclosed in a small plastic or metal container to protect it from the elements.

[/edit]

An alternative approach is to carefully adjust the spacing of the coax connections on the delta match. You may be fortunate to find a spacing that brings it into a reasonable SWR range. This should be done with the antenna supported by a non-conducting pole at least 6 feet away from ground and all other objects. This technique still will not optimize the antenna but as noted above, it may prove usable for your needs.

You could just as well re-optimize the entire antenna by modeling it and adjusting spacing, element length, and the matching network. But given your opening comment stating that you lack the tools to "trim" the antenna, I suspect this option is out of the realm of immediate possibilities. In looking at the antenna construction, it also appears that there will not be sufficient boom length to allow the optimization of the spacing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9439/how-to-adapt-commercial-vhf-yagi-for-2-meter-amateur-use, by Aurelia Peters, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
