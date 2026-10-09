# How to receive a signal from multiple sources simultaneously (helical antenna)

*Tags: antenna, receiver, digital-modes, software-defined-radio · score 3*

## Question

I'm working on a system (theoretical at the moment) whereby I wish to receive data from multiple sources all transmitting at the same time. I've read that a helical antenna is capable of this. I'm also aware that multiplexing can be used if the sample rate required to receive each signal is small enough that the you could effectively switch between the different signals. Is this the process that is referred to when I've read about helical antennas or are they otherwise beneficial when receiving multiple signals?

## Accepted answer (score 9, by Kevin Reid AG6YO)

I'm working on a system (theoretical at the moment) whereby I wish to receive data from multiple sources all transmitting at the same time. I've read that a helical antenna is capable of this.

I'm afraid you're misinformed. **No single antenna, no matter what the design,** can be better than another at receiving multiple signals at once. A receiving antenna doesn't know anything about "one signal" or "two signals"; it just collects radiation and turns it into current in the feed line.

There are ways in which you might optimize the antenna for your particular purpose, but they will depend on details you haven't given. In particular, are the “multiple sources” you refer to at fixed locations? If so, you can use a directional antenna, designed to have more gain in those particular directions. However, this only improves signal-to-noise ratio; it does not help separate the signals.

If you use **two separate directional antennas** pointed at the two sources, then you can receive them independently by having two separate receivers, of course. (Connecting two directional antennas to one receiver [is just making one more complex directional antenna](Connect%20two%20receiving%20antennas%20to%20the%20same%20radio.md).)

I'm also aware the multiplexing can be used if the sample rate required to receive each signal is small enough that the you could effectively switch between the different signals.

A high sample rate in a software-defined radio can help with receiving multiple signals, but it's not a matter of “switching”. The sample rate determines the maximum *bandwidth* — the size of the slice of the RF spectrum that you receive. If you are trying to receive two signals *at different frequencies*, then you can receive them with a single SDR device, programmed appropriately, if they are close enough together to fall simultaneously within the receive bandwidth, like this:

```
|Signal1|        |Signal2|
|       |        |       |
|       |        |       |
| <----------------------- Receiver bandwidth ----------------------> |
|             |       |        |       |                              |
|             |       |        |       |                              |
---+-------------+-------------+-------------+-------------+-------------+---
162.40        162.42        162.44    ^   162.46        162.48        162.50 MHz
|
|
Receiver LO frequency

```

This is not helpful if the two signals you want to receive are at the *same* frequency. But if they are, they are probably transmitting in bursts or using some other type of multiplexing to avoid interfering with each other. What you do at the receiver entirely depends on what the transmitters are doing.

You might wish to ask a different question (posted separately, please): tell us *about the signals you want to receive* (what are they, are you making the transmitters or do they already exist, etc), and ask how to build a receiver for that.

Is this the process that is referred to when I've read about helical antennas or are they otherwise beneficial when receiving multiple signals?

No.

If you edited your question to include links to what you've read about helical antennas, I might be able to explain what they're actually saying.

## Answer (score 3, by Phil Frost - W8II)

There is nothing special about a helical antenna that makes it more suited to receiving multiple signals simultaneously than any other kind of antenna. In fact one might argue the opposite: a helical antenna is directional, and if your sources are in many directions this will make it difficult or impossible to receive all of them at once.

To receive multiple sources, you will, by definition, do some kind of multiplexing. What you describe, "switching between the different signals", sounds like time-division multiplexing. There are many other kinds, where multiple sources might be differentiated based on:

- time,
- frequency,
- location,
- polarization,
- any of these in combination,
- and many more.

Wikipedia has a more detailed summary.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2414/how-to-receive-a-signal-from-multiple-sources-simultaneously-helical-antenna, by FraserOfSmeg, Kevin Reid AG6YO, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
