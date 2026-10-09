# Asynchronous vs. Synchronous data transmission speed

*Tags: digital-modes · score 4*

## Question

Humans are asynchronous receivers, they can pick up words at any time, even if spread out, can combine into a sentence. Data rates are as fast as someone can hear/talk/copy code.

All of the fast digital modes are Synchronous, example the HF digital voice has a lag between someone talking and their voice getting out because of the initial sync code.

On a particular radio Wikipedia page, it claimed these data rates:

AM/FM Synchronous: 12/16 kbit/s

AM/FM Asynchronous: Below 4800 Baud

What aspect of digital technology allows the data rate to be much faster if the transmission is synchronous.

## Answer (score 3, by Phil Frost - W8II)

Wikipedia is plain bonkers. The manufacturer's data sheet is more enlightening:

**Waveforms/Modes of Operation**

Implemented and Planned

- AM/FM

 - Non-secure voice
 - Non-secure narrowband voice (FM)
 - **12 and 16 kbps secure voice**
 - **12 and 16 kbps secure synchronous data**
 - **Secure asynchronous data to 4800 bps**

[...]

- ANDVT

 - Secure narrowband voice (LPC-10, MELP Vocoders)
 - **Secure 2400 bps synchronous data**

Notice it says "bps" and "kbps" which mean "(kilo) bits per second". There is no "baud" anywhere in the spec sheet. Whoever wrote that Wikipedia article must not know the difference.

Secondly, we can't infer from any of this that synchronous communications are faster than asynchronous communications. All we can infer is that this particular radio implements a number of modes. Some are fast, and some are slow. Some are synchronous, and some are asynchronous. You can even see that the *slowest* data listed in the datasheet is ANDVT, and it is described as "synchronous".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2306/asynchronous-vs-synchronous-data-transmission-speed, by Skyler 440, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
