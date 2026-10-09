# RTL-SDR dongle - what antenna should I use for APRS receive only?

*Tags: antenna, vhf, rtl-sdr, aprs · score 4*

## Question

I was following this guide to setup an iGate using an RTL-SDR dongle and a Raspberry Pi. It worked, and I have been able to test it by seeing some APRS packets from a separate transmitter (Arduino+BaoFeng HT) I made be relayed through that IGate. However, when I moved the IGate to another room in my house, there was a significant decrease in the number of packets that were successfully received by the IGate. I am thinking that I should put a better antenna on the dongle. Currently the antenna I have on the IGate is some 4 inch rubber ducky antenna that I scavenged from an old 2G/3G cellular modem.

Can you suggest what criteria I should use when shopping for a better antenna for the IGate?

I am in the USA and so use frequency 144.390 MHz.

## Answer (score 6, by Kevin Reid AG6YO)

Here are the fundamentals of improving VHF antennas from what you've got:

1.

"Rubber ducky" (loading coil shortened) antennas are less efficient and more frequency-selective than un-shortened antennas. Choose an antenna which is a straight length of wire. (The exact length is not critical for receiving as long as it's in the neighborhood; you may get essentially as good results from a VHF "scanner" antenna as from a 144 MHz specific one.)

2.

Ordinarily, "get the antenna better line of sight to the transmitter" would be the first thing I'd list, but that's evidently not your first problem since you started in the same room. Still, in order to use it at longer range you should consider planning an outdoor antenna installation — this may mean either installing the electronics in a weather-shielded enclosure or using a feed line between the antenna and the electronics.

3.

A monopole-type antenna depends on the "ground" provided by the objects it's attached to. This does not mean it needs to be attached to earth, rather, it means that the metal of the feed line, PCB and any attached cables function as part of the antenna structure. In order to get more predictable good performance, you should choose an antenna type that has its own ground plane, or paired elements in some other form. These can include:

 - Vertical antenna with built-in "radials" (wires extending horizontally).
 - Magnet-mount antenna on top of any handy metal structure or even a steel pizza pan.
 - "Whip" wire antenna mounted onto a bulkhead connector (female-female coax coupler with threads and a nut for panel mounting) or NMO mount, installed in the middle of a horizontal sheet of metal. (This requires separate care to weatherproof but might be appropriate for temporary or experimental installations.)
 - Vertical dipole (coaxial dipole, or standard dipole with horizontal center feed).

The common feature of all of these designs is that the antenna consists of/is attached to *two* large conductive objects.

Finally, note that once you have a good antenna, you may find that the system *doesn't* work when the transmitter is in the same room. This would be because the receiver is overloaded and cannot decode the signals properly. If you need to do short-range tests, you can install an attenuator on either the transmitter or receiver antenna connection, or install a dummy load on the transmitter (there'll still likely be enough leakage to get through).

## Answer (score 4, by Aleksander Alekseev - R2AUK)

Rubber ducky antennas are not very efficient indeed. Also for best performance they may require a ground plane or radials, which I guess you could omit.

Personally I used RTL-SDR Blog Multipurpose Antenna (i.e. a regular dipole) for this purpose quite successfully:

One observation I made while experimenting with APRS is that using a broadcast FM filter helps a lot. I was using this one:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13101/rtl-sdr-dongle-what-antenna-should-i-use-for-aprs-receive-only, by Anssssss, Kevin Reid AG6YO, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
