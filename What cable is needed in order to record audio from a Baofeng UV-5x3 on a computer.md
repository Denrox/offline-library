# What cable is needed in order to record audio from a Baofeng UV-5x3 on a computer?

*Tags: baofeng, connectors, audio-interface, audio · score 3*

## Question

I would like to be able to connect my radio to my computer in order to record audio. It seems like this would just be a matter of getting the right cable, but after trying a few cables (listed below), I'm realizing it's not that simple. I would like to be able to record audio so that I could save morse to practice decoding, record call signs so I can update a log book later on, and - somewhere down the line - be able to do something like record connections with satellites / ISS).

**My Setup**

- Baofeng UV-5x3
- MacBook Pro running High Sierra (10.13.5)

**What I've tried**

I have naively attempted to use these cables to connect to my Mac:

- Retevis 2 Pin to 3.5mm Adapter (with a male-to-male audio cable)
- BTECH APRS-K1 Cable (tried this both with and without a APRS-K1 Cable, Reverse Connector Adaptor, which was shipped along with the first cable)

In both cases, the Mac doesn't receive any audio. Thinking that the issue might be with configuring the Mac's audio, I tried connecting each cable to my car's auxiliary input (which I can use to play audio from my iPhone). There again, I didn't hear anything from the radio.

After searching online, I've seen a lot of people just use their computer's external microphone to record audio. It seems like there should be an easy way to send radio output directly to a computer, though.

**Related**

I found that these existing questions provided interesting information, but didn't quite answer my question:

- [How to hook up my computer's audio output to my CB Radio?](How%20to%20hook%20up%20my%20computer%27s%20audio%20output%20to%20my%20CB%20Radio.md)
- [Confusion about radio-computer interfaces: TNC, CAT, TRRS, Wolphi Link, ...?](Confusion%20about%20radio-computer%20interfaces%20TNC%2C%20CAT%2C%20TRRS%2C%20Wolphi%20Link%2C.md)

## Accepted answer (score 2, by Scott Earle)

I built an audio interface that connected from an HF radio to my Mac, a few years ago. Obviously, I was concerned with ground loops and hum and suchlike, because I intended to use the interface to transmit too, so I used audio transformers as well.

But the one thing I found that surprised me was that (as mentioned in comments by Kevin) the Mac has a slightly odd audio connection system. As Kevin says, it’s a TRRS arrangement, but in order to make the Mac ‘see’ that there is a microphone connected, you need to put a diode between one of the Rings and ground. This is to allow the macOS to detect whether a microphone is present or not, and thus enable incoming audio.

I just used a regular small-signal silicon diode (1N4148 I think), and suddenly the Mac could ‘see’ that there was an audio input and allowed incoming audio through.

Use a continuity tester on a pair of Apple-compatible headphones with a microphone to determine which Ring should have the diode, and which way round it should be.

Of course, to be ultra-paranoid about the safety of your expensive computer when connected to a famously ‘cheap’ radio, you might want to consider an audio transformer too :)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11583/what-cable-is-needed-in-order-to-record-audio-from-a-baofeng-uv-5x3-on-a-compu, by Jim, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
