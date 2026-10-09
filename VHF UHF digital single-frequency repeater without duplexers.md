# VHF/UHF digital single-frequency repeater without duplexers?

*Tags: repeater, digital-voice, tdma · score 7*

## Question

Some digital voice protocols are time slotted (TDMA), i.e. the transmitter of a station is not on all the time, and multiple stations may transmit digital voice on the same frequency at the same time by transmitting small digital bursts, one by one.

For example, DMR (MotoTRBO), which is already somewhat popular in amateur radio circles, has a duty cycle of slightly less than 50%, and two voice transmissions can be retransmitted by the same repeater at the same time.

Would it be possible to make a digital "simplex" voice repeater which would listen on one time slot and immediately repeat the received voice frame on the next time slot, on the same frequency? Do such repeaters exist for some protocol?

It'd work fine with a single antenna, and wouldn't require duplex filters. Much easier to set up than traditional voice repeaters.

## Accepted answer (score 5, by BM2NHC)

There are currently products from multiple major and minor DMR equipment manufacturers to support single frequency repeater (SFR) function. They may have different names but essentially do the same thing: Repeater input on time slot 1 and output on time slot 2.

What is not certain is whether SFR is interoperable between different manufacturer equipment. From the description by each manufacturer it appears to be interoperable.

Motorola:

Extended Range Direct Mode enables repeater operation on a simplex radio channel. Radios on an ERDM channel transmit on one slot and receive on another slot - the frequency is the same.

With this you get:

- Repeater-like coverage
- No need for a 2nd frequency - your simplex channel can be reused.

In this configuration, dual slot operation is not possible and you need to be using a SLR series repeater. IP based dispatch solutions, like SmartPTT Plus and TRBONET Plus, are supported. It also only supports single site conventional operation so no trunking or IPSC.

This feature requires R2.7.0 firmware and is supported on all current generation MOTOTRBO radios. My understanding is that this feature will also work on other makes of DMR radios.

Hytera:

Full Duplex and Single Frequency Repeater

The UHF model variants of the MD785i are also available with Full-Duplex function and can thus also be used as Single Frequency Repeaters (SFR). In Repeater Mode the mobile radio boosts the range of a direct connection between conventional DMR devices without having to use a base station or repeater. In very concrete terms for users this means they now have more freedom of movement and considerably more flexibility.

Belfone: Repeater and Base Station

BF-SFR600 is our new single frequency repeater solution which is also able to function as a base station within a system. As a single frequency repeater, BF-SFR600 allocates one timeslot to receive a signal and the other to transmit it at the same frequency, using DMO mode to extend radio coverage.

## Answer (score 4, by Adam Davis)

Would it be possible to make a digital "simplex" voice repeater which would listen on one time slot and immediately repeat the received voice frame on the next time slot, on the same frequency?

Yes, the protocol could be used this way. It wouldn't be simple to setup without the radios specifically supporting such a mode of operation, though. You could use two radios for the repeater - each set the the opposing timeslot, feeding into each other, with VOX enabled, but it would be, at best, a hack and probably wouldn't be very robust without additional control equipment. It would eliminate the need for resonant filters, though.

Do such repeaters exist for some protocol?

I understand that some Hytera radios support this mode. Mototrbo radios support TDMA operation, but when in TDMA mode you select a single time slot for both transmitting and receiving. The repeater would have to be set up to to always receive on one time slot and transmit on the other, and the users would have to set their radio to receive on the correct timeslot, except when they want to transmit. At that point they'd have to manually switch the radio to the other timeslot, then when done immediately switch it back to the timeslot the repeater transmits on. This is not automated in the Mototrbo radios, so they couldn't easily be used for this.

But it is possible, and it may be interesting to do, merely from the viewpoint of eating up only one 12.5kHz channel and removing the need for expensive, large filters.

## Answer (score 3, by SClark)

What you describe is exactly how TETRA DMO repeaters work. They use 4 time slots on a single frequency, using 25MHz bandwidth. The repeater receives on time slot #1 and transmits on slot #4.

See for instance TETRA DMO modes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/490/vhf-uhf-digital-single-frequency-repeater-without-duplexers, by oh7lzb, BM2NHC, Adam Davis, SClark. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
