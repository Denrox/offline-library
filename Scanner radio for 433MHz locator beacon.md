# Scanner radio for 433MHz locator beacon

*Tags: receiver, uhf, beacon · score 3*

## Question

I am looking for a recommendation of an inexpensive scanner radio that should be used to locate animals equipped with 433MHz locator beacons. The beacons (based on DRA887TX) will send periodic tones. The radio needs to have the ability to be connected to a Yagi antenna. I was looking at the Baofeng UV5R scanner. Since I never used anything like this I would like to know if this is useable or not.

## Answer (score 4, by Kevin Reid AG6YO)

I am looking for a recommendation of an inexpensive scanner radio that should be used to locate animals equipped with 433MHz locator beacons.

First, let me clarify some terminology: you don't need a *scanner*, just a *receiver*. A scanner is a type of receiver which monitors a large range of frequencies, but you know the exact frequency of your beacon.

The beacons (based on DRA887TX) will send periodic tones.

I just looked up a datasheet for the DRA887TX and it says it uses ASK (amplitude-shift keying) modulation. It's not clear what the levels are or if it's actually OOK (on-off keying, like Morse code but not necessarily the same patterns). In any case the behavior will depend on exactly how you use the module in your beacon circuit.

The key point, however, is that this is *not* frequency modulation (FM). This means that if you use a FM-only radio such as the Baofeng UV-5R, you will hear *silence* when picking up the transmission. Silence is distinguishable from the noise you hear when there is no signal at all, but this isn't exactly pleasant to listen to.


If your beacon is transmitting an audio-frequency wave (pulse train, rather) into the DATA pin of the transmitter module, then you could use an AM receiver to pick up the tone. (*Not* a regular "AM radio", because those cannot receive at 433 MHz). Some other models of handheld radios (e.g. the popular Yaesu FT-60) have this capability.


If you are just turning on the transmitter periodically and not doing any actual modulation (this is the simplest circuit design), you will need a receiver suitable for *CW* (continuous wave), or *SSB* (single-sideband), reception.

So to summarize, you likely need a *receiver* (or transceiver) with these specifications:

- **Frequency coverage** including 433.92 MHz.
- **Modes** including either CW or SSB.

I'm afraid I'm not personally familiar with what products are available with these specifications that are suitable for the purpose, as opposed to being large and expensive.

(Well, you could get an RTL-SDR dongle paired with an Android phone. That's cheap if you have the phone already. Not the best performance, nor battery life, though.)

But now that you know what to look for, you can do some research. It's probably also worth looking for information specifically for direction-finding/"fox-hunting".

The radio needs to have the ability to be connected to a Yagi antenna.

Any radio which has an antenna port can be connected to a Yagi antenna. You may need some type of adapter or pigtail cable.

You may wish to consider using a loop antenna as opposed to a Yagi — this is a popular choice among "fox hunters". It is more compact and allows for getting a much more precise determination of the direction, but you have to listen for the *absence* of the signal (null) rather than its presence.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5853/scanner-radio-for-433mhz-locator-beacon, by optronik, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
