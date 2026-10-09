# How does a receiver know the exact frequency in the channel to "listen to"?

*Tags: frequency, bandwidth · score 5*

## Question

I am reading about how radio communication works and I have an unanswered question.

We have wideband channels with 25kHz of radio spectrum. The transmitter modulates a signal and sends it.

The receiver that captures that particular channel and receives the signal. But how does it know to which frequency it has to tune in?

There is a 25 kHz channel size, so there are so many different frequencies that it could be as the signal is modulated. How does the receiver decide?

## Accepted answer (score 9, by Phil Frost - W8II)

The signal is not at exactly one frequency. The only signal that exists exactly at one frequency is an unmodulated carrier, and such a signal contains no information.

As soon as the carrier is modulated, the signal's energy is spread over a wider bandwidth. So to receive any signal containing information, the receiver must listen to some range of frequencies, in your case a 25 kHz channel.

## Answer (score 6, by user3486184)

It may be easier to think of the receiver as receiving all frequencies. The job of the receiver is not to tune to a single frequency. Its job is to filter out everything that's not at that frequency, or in a band around it.

So when you tune your FM receiver to 144.2500 with a 25 kHz bandwidth, you're telling it to reject all frequencies that are more than 12.5 kHz below 144.2500, and all frequencies that are more than 12.5 kHz above 144.2500.

Other frequencies are still there, they still hit your antenna, and still show up (to some degree or another) at the antenna connector of your receiver. A big part of the receiver's job is to filter out all the frequencies you don't want to listen to - leaving only the signal that you do.

## Answer (score 5, by Zeiss Ikon)

The receiver "listens" to any and all signals in its receive bandwidth (talking about AM, CW, or sideband here, FM handles everything differently). Generally, there will be only one strong signal that gets through the receiver's filter, and that (plus atmospheric or man-made noise) is all you'll hear.

If there are two stations within the filter width, however, they'll get mixed together (you can sometimes hear this in AM broadcast, if stations in adjacent cities are on adjacent frequencies, or at night when the signals can propagate hundreds of miles). In this case, your radio *doesn't* "know" what signal to listen to -- it just detects and amplifies whatever signal it receives.

Some radios have adjustable filters that let you narrow the receive band -- this is especially common with SSB and CW, where the signal you're after can be quite narrow (around 3 KHz for SSB and as little as 150 Hz for CW). In this case, you can adjust filter width wider to make it easier to find a signal, then narrow it to ensure you can hear the one you're after. Still and always, however, the radio just reproduces whatever signal comes in through the filter width.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14783/how-does-a-receiver-know-the-exact-frequency-in-the-channel-to-listen-to, by kkris1983, Phil Frost - W8II, user3486184, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
