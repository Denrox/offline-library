# How is "clarifier" control helpful?

*Tags: yaesu, equipment-operation · score 15*

## Question

My radio-club recently got a Yaesu FT-225RD transceiver and I'm trying to digest its manual (available for download here). This is the first ham radio that I'm learning how to use, so I could be missing something obvious.

On the front panel there's a knob marked CLARIFIER and the manual has following description for it:

The clarifier control allows a means of offsetting the transceive or receive frequency by ±4 kHz from the frequency established by the main VFO dial.

I do understand that radio's frequency will drift with time and that not everyone's rig will be spot on channel and that in such cases minor adjustments may be needed to improve reception.

What I don't understand is when would use of clarifier be preferable to use of the main frequency dial. From what I can see, the main dial offers pretty good resolution for frequency adjustment and clarifier isn't a fancy name for a fine-tune knob I've seen on on radio receivers for commercial FM band from the same time period.

UPDATE: One thing that I didn't find relevant to the question at first is that in addition to the clarifier knob, there is a clarifier switch as well which is used to set clarifier to one of 3 settings: transceive, receive and off. This would imply (at least in my opinion) that in transceive setting, the clarifier would affect frequencies of both transmission and reception.

## Accepted answer (score 13, by Phil Frost - W8II)

I think "RIT", for "receiver incremental tuning", is a better name for that knob because it more directly explains what it does: it tunes the receiver, without tuning the transmitter. The result is that you receive and transmit on different frequencies. It is similar to [operating split](Why%20do%20some%20DX%20listen%20on%20a%20different%20frequency%20than%20they%20transmit%20on.md), with less frequency separation.

This is most useful when you've already started a contact, but now you want to change your tuning. If you re-tune by adjusting the main VFO, you also move your transmitter. Now the other guy will have to re-tune to you, then you re-tune to him, and so on, until you have walked out of the band.

Tuning could be off for any number of reasons. There are some people who aren't very good at accurately tuning SSB, or perhaps they just don't mind the [weird way it makes voices sound](Why%20does%20SSB%20have%20the%20hollow%20voice%20sound.md), or they have old equipment without a stable VFO. Listen to any SSB net for an example. I suspect this is the origin of the term "clarifier". In CW operation, not everyone tunes accurately to their sidetone frequency. Especially in CW operation, you might want to tune your receiver to get the signal into a narrow filter passband, or to get some noise in the stopband.

## Answer (score 6, by Noji)

The ***clarifier*** is simply Yaesu's term for **RIT** (receiver incremental tuning) and **XIT** (transmitter incremental tuning), and can be used for either of those two adjustments, or turned off. **RIT** keeps your transmit frequency constant while you adjust your receive frequency. This way, when you're talking to a group (like in a net), you can more clearly hear the one ham who's off-frequency while everybody else in the group can hear you without detecting any change in your frequency. **XIT** performs the reverse function, in that it keeps your receive frequency constant while you adjust your transmit frequency. In both cases, tuning with the big knob will adjust both the transmit and receive frequencies simultaneously, while tuning with the RIT or XIT will adjust only one of them.

## Answer (score 3, by Pete NU9W)

For a single contact, as you say, it's pointless. When you're talking as part of a group and one or two members are slightly off frequency it lets you temporarily tune your receiver for their signals without leaving the main frequency that everyone else is on. When it's on it "clarifies" their signal; when it's off you hear the rest of the group clearly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1467/how-is-clarifier-control-helpful, by AndrejaKo, Phil Frost - W8II, Noji, Pete NU9W. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
