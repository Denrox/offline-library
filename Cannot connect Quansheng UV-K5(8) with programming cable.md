# Cannot connect Quansheng UV-K5(8) with programming cable

*Tags: ht, radio-programming · score 5*

## Question

I bought a Quansheng UV-K5(8), and I am impressed by the audio quality, there appears to be a better ratio of signal to noise out of the speaker on listening, and it's a nice little radio, though with some quirks.

I also bought a Baofeng programming cable that is promised will work with the Quansheng UV-K5, which is in every sense the same as my Quansheng UV-K5(8). **This is a Kenwood style programming cable, not to be confused with the USB-C cable which only charges the radio.**

However, while the cable works with my Baofeng UV-13 Pro perfectly, I cannot get it to programme the Quansheng UV-K5(8), the software will not connect to the radio.

I have tried both MacOS Montery and Windows 10. The Baofeng UV-13 Pro works with its proprietary software on Windows 10 so the cable works.

On both systems, plugging in the cable finds the USB-to-Serial chip and creates the serial port, but there is no possibility of connecting to the Quansheng, I tried for hours on both systems, trying Chirp, generic drivers, hideous Quansheng USB drivers that only work if you set your Windows display language to Simplified Chinese, Quansheng provided firmware flash tool (Just to try to get something to connect) but it is impossible to connect the Quansheng radio on either system.

I'm almost certain it's the right cable, I'm very certain it works, the radio works in every other way, so I'm thinking something like:

1.

The cable works with Baufeng UV-13 Pro, and is advertised to work with Quansheng UV-K5 but doesn't work with Quansheng UV-K5(8), I think this very unlikely;

2.

The radio is broken in some way;

3.

The Quansheng-provided driver for Windows 10 and the generic driver for the USB to Serial on both Windows and MacOS somehow don't work;

4.

The serial port settings (Buad, parity, stop bit, etc) are different for the Baofeng that works and the Quansheng that doesn't, but nobody on the internet seems to have documented this, so it's unlikely.

I can't find a more suitable cable online, Please I need any help or ideas!

## Accepted answer (score 6, by spl)

**Solved:** You have to push the Kenwood programming cable plug end into the UV-K5(8) **super hard** it almost feels like it will break, blue light, turn on radio, 2 minute fix after hours of pain.

**Note this is the kenwood style programming cable, not the USB-C charging cable whis is unrelated to this issue.**

Works beautifully on Mac with Chirp and no dubious manufacturer / 3rd party drivers!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22054/cannot-connect-quansheng-uv-k5-8-with-programming-cable, by spl. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
