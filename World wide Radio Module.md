# World wide Radio Module

*Tags: legal, uhf, transceiver · score 5*

## Question

currently I am involved in a project were a data link is needed to communicate different devices. This is in one to many configuration and the devices are stand alone. For this project there is need 9.2Kbps, even less, and the expected coverage is not so huge, is just about 500 mts in a rural environment (trees, hills) and the worst part... this device should work around the globe. The problem here is with the approvals.

LoRa could be a solution, but there is some differences in the regions (868/915/923) and the FCC rules and EU rules regarding duty cycle and dwell time are quite different. I thought to use a NarrowBand radio, at 403-470MHz, using licensed channels (no problem to request a license), but these modules are quite expensive. Do you have any idea? do you know any radio module transceiver for world wide?

Many thanks in advance.

## Accepted answer (score 0, by Jordi NC)

I found a LoRa device which covers all the frequencies and I prepared a matching network to cover all range, and after some tests the results were so good, so the problem is solved. Many thanks

## Answer (score 12, by Marcus Müller)

Your problem is that there's really but one globally usable unlicensed band, and that's the 2.4 GHz band.

But that doesn't sound so bad. People think "high frequency = short reach", stemming from the well-known Free-Space Path loss formula

$$P_r = P_t \cdot G_t G_r \left( \frac{c_0}{4 \pi fd} \right)^2\text,$$

where the received power $P_r$ falls with the square of the frequency $f$ (for a fixed distance $d$), assuming you keep the transmit power constant and use antennas that have the same gain $G$ on transmit- and receive-side.

However, what people tend to forget: your antenna directivity at constant antenna area also grows quadratically with frequency, so that it's typically a zero-sum game, if, and that is the great if here, you can have a directive link:

If you want to keep the size of your system the same, this works out, because you can point the antennas at each other, and make a directive link.

If either side needs to be able to move, you usually can't just realign the antennas all the time, and this doesn't work.

However, is this really a problem?

Assuming a gain for one antenna of 6 dB (which is somewhat logical, you don't build an antenna that illuminates the sky if you want to talk to things on the ground, nor do you let it illuminate the ground directly below it), and the other with 0 dB gain, and stay within the world-wide limit of 100 mW (= 20 dBm) for the 2.4 GHz band, your received power at 500 m becomes is 83 dB lower than your transmit power, so -63 dBm.

That's not at all bad! Say, you're using a cheap 1 MS/s device, so you can only do 1 MHz of bandwidth at once, you get a noise power of $N_{[\text{dBm}]}=-174+B_{[\text{dBHz}]}=-114$ dBm (1 MHz = 60 dBHz). That gives you a very comfortable SNR! You should pretty trivially be able to communicate at your rates over that.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16548/world-wide-radio-module, by Jordi NC, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
