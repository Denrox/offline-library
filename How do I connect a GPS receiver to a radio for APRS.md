# How do I connect a GPS receiver to a radio for APRS?

*Tags: baofeng, aprs, gnss · score 4*

## Question

I volunteer with the local search and rescue group as a team medic and a radio operator. The team is new and recently decided to go with the Garmin 64st as our go-to GPS units. Those of us with licenses use the cheaper Baofeng UV-5R and BF-8HP radios. I was volun-told to look into pairing our GPS to the radios for APRS use. I’ve searched around and haven’t found any definitive information, although from what I could find, I gather that NMEA is needed on the GPS to make it work, which our units do have.

I want to know if it’s possible to use the two together, and if so, how.

## Accepted answer (score 2, by Kevin Reid AG6YO)

*Disclaimer: I have no experience with any of the below matters; I'm just writing an explanation of what I've heard.*

Neither your radio nor your GPS unit knows how to encode APRS packets. Therefore you will need to add a device which does, and will also perform the other control/interface functions.

In general, a hardware device which encodes and AFSK-modulates (and in cases other than this, also decodes) APRS packets is known as a TNC, or a tracker for the specific case of sending position reports.

Here's an example of a product that you could use: Byonics TinyTrak3. **I am not recommending this product;** it's just one that I remember people talking about (I haven't personally used such devices).

Since your radios don't know about APRS and don't have an external control interface, you will necessarily be transmitting your position reports on the same frequency as your voice communication (unless you're using a separate radio for APRS). This isn't a critical problem (and CTCSS can be used to mute the data packets for listeners), it just means a little more activity, and that your packets won't go onto the regular APRS network unless you set up your own digipeater or IGate.

Also note that one of the features of the product I linked is “Burst after voice / Send Position Now input”. This means you get to control the timing of the packet versus your other use of the radio, which is appropriate here, as opposed to a completely autonomous system that transmits position reports automatically and does nothing else with its radio.

## Answer (score 4, by watkipet)

If you're OK with using a smart phone instead of a regular GPS, you can use:

- APRSdroid with a Bluetooth TNC for an Android phone
- PocketPacket with an audio level converter you make yourself with an iOS device.

## Answer (score 2, by q74)

1. Forget Baofeng.
2. Buy an old Kenwood THD7 for little more. I have one for 18 years and is rock solid still. It has APRS built-in and many other useful things. You can easily connect it to your PC.
3. take a look at my website: http://www.so6agj.pl/project-gps.php
4. If you need code or hardware instructions please write me a message.

73

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5378/how-do-i-connect-a-gps-receiver-to-a-radio-for-aprs, by john.weland, Kevin Reid AG6YO, watkipet, q74. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
