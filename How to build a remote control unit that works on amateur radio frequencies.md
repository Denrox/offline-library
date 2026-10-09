# How to build a remote control unit that works on amateur radio frequencies?

*Tags: diy, remote-control · score 6*

## Question

The only remote control units I have used before was those little cheap 27Mhz puny range cheap units. I would like to build some sort of RC unit, which has a range up to 1km line of sight.

I have a general license. How can I get started with remote control using Amateur frequencies, and what bands allocate remote control?

## Answer (score 2, by imabug)

A remote control is just a radio transmitter (maybe even a receiver if you expect to get data back from whatever you're controlling). To get started, you'll need to learn how to build a transmitter/transceiver that operates at the appropriate frequency.

That's probably the easy part. schematics for VHF/UHF transmitters shouldn't be too hard to find.

The harder part would probably be adding the controls and making them tell the transmitter to send the appropriate modulated signals out, which would require some kind of microcontroller to read the status of the controls, and then appropriately key the transmitter in response. That's probably your next step.

Then you'll need a receiver on the device you're controlling. Receivers are generally fairly easy objects to build, but now you've got to make it control things on your device in response to the signals it receives. More microcontroller stuff.

## Answer (score 2, by Andrew M0YMA)

This might be better as a comment than an answer (Mods feels free...) but...

Given your callsign is from the USA, your terms are different from mine in the UK, but please check the terms of your licence... I could be wrong but I suggest that what you are proposing using ham bands for is outside the privileges contained therein.

Furthermore, *remote control* implies operating on a fixed frequency - therefore if used on ham bands, you are at risk of causing interference (QRM) of other users.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/641/how-to-build-a-remote-control-unit-that-works-on-amateur-radio-frequencies, by Skyler 440, imabug, Andrew M0YMA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
