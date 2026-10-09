# Is this the Correct Ferrite Core to Reduce RFI as a Common Mode Choke?

*Tags: rfi, ferrite, choke-balun · score 5*

## Question

I have a Flex 3000 connected via RG-11 coax to a inverted V fan dipole tuned for 40m and 20m on my roof. I have an "ugly" balun up on the mast by the antenna. I further have the feed-line going into a lightning suppressor where the line enters into the house and is connected to my 8 foot ground rod.

I realize that my coax is not 50ohm (it's 75ohm) but I'm operating at 80, 40, and 20m. My SWR is 1.1 on 40m and 1.4 on 20m and my ATU takes care of the rest. My understanding is that this should not be much of a factor on HF. In fact this coax is plenum rated so it has the extra shielding as well so it's very well guarded from external interference. Unless of course that extra shielding is having the reverse effect allowing even more RFI to flow down the shielding as it's acting as a fantastic antenna. Hence why I'm trying to do what I'll explain next...

I'm trying to reduce various RFI on 80m and 40m (some 20m) coming into my shack (and also eliminate RFI going out to various devices by my transmissions) but have not had much success. I'm trying to use ferrite cores to help reduce some of this...

I have these Fair-Rite ferrite cores from www.mouser.ca...

Mouser Link

Which should be these specific cores on the Fair-Rite Site...

Fair-Rite Link

My understanding is that these are the #31 material as mentioned in numerous documents, not the least of which is Jim Brown's (K9YC) Guide to RFI, Ferrites, Baluns, and Audio Interfacing (often times noted as the "Bible" of RFI finding and reduction)...

I've played with these toroid cores on an off for the past 3 years. I keep coming back to them as I'm hoping to reduce the RFI in my shack. However each time I've tried to use these cores, they've made exactly zero difference.

For example I have a known source of RFI which is a birdie caused by my main 27" monitor (an Apple model). I see this birdie on 80m. I've tried wrapping the power cord multiple times and no luck. Zero effect. However this is just a birdie so I can deal with it.

Another example is when I'm transmitting I hear the RFI over my speakers in the shack. This is a Logitech 5500 system. It all works from a main sub woofer that all the speakers then connect too. I've disconnected all the speakers and still get the RFI through the main woofer. I've wrapped the power cord of the woofer about a dozen times through two cores each. Zero difference on the RFI leaking into the speaker. As mentioned I use a Flex 3000 so having a PC and a speaker is essential. Again I can get around this and use wireless headphones but it's not ideal.

I've also tried a Bifilar choke as detailed in a presentation PDF from K9YC again starting on page 45 here https://www.qsl.net/w/wa3mej//Articles/K9YC/CoaxChokesPPT.pdf I have a picture of the one I've made...

This was done with #14 THHN wire as detailed in the presentation above on page 47. This was connected to my feed-line on one end and the other end went straight into my flex-3000.

I have various other sources within my house that I'm attempting to deal with but I'm trying to mitigate a few of them with cores. But the cores just seem to make absolutely no difference. Either I've got the wrong cores or I'm missing something and am not doing it correctly? I bought these things and I would've thought I would have at least seen marginal improvements but so far they've been useless.

Any suggestions on what I'm missing?

**UPDATE 1**

Here's some pictures of my antenna setup and my ugly balun. Obviously the height of the antenna is not ideal but this is up on the second floor. I've since added a vertical dipole (Comet 250B) which is not shown. As you can see the balun has coax seal all over it so I'll have to pull all that off and switch out the balun for my ferrite choke. I notice in the pictures that the coax seems to be drooping on my balun which I didn't notice earlier. Could this also be a factor?

I've also included a picture of my new ground setup...

Antenna Setup

Ugly Balun

New Ground Setup

**Update 2**

I've tried to make a quick and dirty version of the RFI detector that Phil Frost - W8II has pointed out. This is based not he link provided in the first answer below.

Here's a couple of pictures of my detector. It include the snap on ferrite with 10 turns of wire through into a breadboard where I just plugged in the components for now. I'm using a 101 nf cap (I assume that it is nF as there is only the number on it) and a 47 Ω and 100 Ω resistor. You'll see a red LED. I don't have any diodes handy at the moment but have them on order. I thought I would try the LED to see if it would work.

Unfortunately I don't get any reading on my multimeter. I have it set to 200mA and I put the ferrite beside my feed line. It just reads 00.0 all the time when I transmit. I'm not sure if that's good as I don't have any common mode current, or more likely I've done the detector wrong.

Here is a picture of my detector and my multimeter.

Detector

Multimeter

## Answer (score 4, by Phil Frost - W8II)

That does look like a fine core to use, and the photo of your construction looks good. Your coax isn't causing any problems with noise.

Try putting the choke at the *feedpoint*, not at the *radio*, in lieu of the ugly balun you have now. A choke at the radio will do little since the coax shield, connector, and enclosure of the radio already form a continuous shield around all the receiving circuitry.

The objective with the balun is to [eliminate common-mode current on the feedline](Using%20a%20balun%20with%20a%20resonant%20dipole.md). A feedline with common-mode current is part of the radiating and receiving antenna, and since it runs into the shack it's close to all kinds of noise generating electronics. A functional balun suppresses common-mode current on the feedline so only the antenna, which is farther away from noise sources, is the only part radiating or receiving. Often this reduces RFI.

Ugly baluns can be ineffective. Since they are a purely reactive impedance they can't dissipate noise power, only redirect it. In some cases the reactance of the ugly balun combines with the common-mode reactance of the feedline or tower to make a resonant circuit which is worse than no balun. A properly selected ferrite on the other hand has a significant resistive component to its impedance, and thus works in all cases as it can convert noise power to heat.

Fixing RFI problems like you describe can be difficult if you don't know what's working and what isn't. If you aren't certain that feedline common-mode problems have been eliminated, trying to fix a noise source by putting ferrites around it is a futile exercise since all the wiring in your home is part of the antenna.

So I suggest you [measure the common-mode current](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) with the ugly balun, and then with the ferrite choke. You might try different ferrite choke designs to find one that works well. The number of turns, core material, and core geometry make a difference. The K9YC presentation you referenced discusses it in some detail. G3TXQ also has some good data. You can use these resources as a starting point for a design and then confirm the results with measurement.

Only after confirming feedline common-mode issues are resolved, go around the house and identify noise sources. Putting ferrites on the cables leaving a noisy device eliminates the "antenna" they use to radiate noise.

## Answer (score 3, by Chris K8NVH)

The answers here are excellent and I have little to add other than to emphasise / RFI problems are hard /

Consider the case of the RFI problem discussed in Electronics Stack Exchange ( https://electronics.stackexchange.com/questions/402021/how-do-i-specify-a-low-rfi-led-driver/402029#402029 ). Everything has been ferrited to death (5000 ohm common mode chokes surrounding all wires connected to the source and the receiver) and yet S9-11 noise levels appear across multiple bands when the device operates. A tiny little transformer, being fed an unfiltered sawtooth current, is radiating enough to make it 30 feet to the properly-choked receiving antenna, ruining several bands.

The fix is to replace the offending device.

Sometimes you do everything "right" and it still just is not enough.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12101/is-this-the-correct-ferrite-core-to-reduce-rfi-as-a-common-mode-choke, by Etep - VE6ETP, Phil Frost - W8II, Chris K8NVH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
