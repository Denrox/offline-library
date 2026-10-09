# Ham radio Internet gateway

*Tags: internet · score 4*

## Question

How does a ham Internet gateway work?

Is it possible for someone to use that to listen for my transmissions (over the Internet without needing a ham radio)?

Wouldn't the Internet gateway need to be setup for the same frequency I'm transmitting on and in the same area, again, no guarantee and highly unlikely?

Ie, if I'm going to be broadcasting in California and I would like someone in New York, Peru, Greenland, etc., is it possible for them to listen? Would it also be available in real-time or close to real-time or would there be a substantial delay.

## Accepted answer (score 2, by Mike Waters)

How does a ham Internet gateway work?

**Check out http://websdr.org.**

All over the world, many amateur radio stations have connected software-defined-receivers (WebSDRs) to their computers, using software specifically designed for the purpose.

Is it possible for someone to use that to listen for my transmissions (over the Internet without needing a ham radio)?

It certainly is! Go have a listen there yourself. And it's free.

Wouldn't the Internet gateway need to be setup for the same frequency I'm transmitting on and in the same area ...

Basically. However, they receive a wide band of frequencies. If someone wanted to listen to you, they would have to tune their Web SDR of choice to your frequency. This quote from http://websdr.org explains:

"A WebSDR is a Software-Defined Radio receiver connected to the internet, allowing many listeners to listen and tune it simultaneously. SDR technology makes it possible that all listeners tune independently, and thus listen to different signals; this is in contrast to the many classical receivers that are already available via the internet."

... no guarantee and highly unlikely?

No guarantee, but I wouldn't say that it's highly unlikely.

If I'm going to be transmitting in California and I would like someone in New York, Peru, Greenland, etc., is it possible for them to listen?

It's possible. But whether they can hear you depends on many factors, which I won't go into because there is another question (somewhere) that answers that here.

Would it also be available in real-time or close to real-time, or would there be a substantial delay.

I've been in conversation with other hams over the radio. When I used a WebSDR to listen to them as well, I have never heard a delay of more than a second compared to the sound coming out of the radio's speaker. Usually, it's significantly less than a second.

**There is also Echolink.**

EchoLink® software allows licensed Amateur Radio stations to communicate with one another over the Internet, using streaming-audio technology. The program allows worldwide connections to be made between stations, or from computer to station, greatly enhancing Amateur Radio's communications capabilities. There are more than 200,000 validated users worldwide — in 151 of the world's 193 nations — with about 6,000 online at any given time.

## Answer (score 2, by Phil Frost - W8II)

How does a ham Internet gateway work?

Someone, or often an amateur radio club, installs a radio at a site with internet access. From there, they upload the received signals to a network of servers on the internet, or host the server themselves.

There are many such services. Here are a few, and by no means exhaustive:

- WebSDR (predominantly independent HF receivers)
- Brandmeister (mostly linked DMR repeaters, anyone can listen via internet)
- DMR-MARC (also DMR repeaters, but this one less open than Brandmeister. No internet listening capability, but no license is required to *listen* on a DMR radio in the US)
- EchoLink (Used to link FM repeaters, also runs as Windows software)
- P25NX (a similar thing to Brandmeister and DMR-MARC, but for P25)
- D-STAR reflectors (similar to DMR except much less mature. You can probably find a place to listen online that isn't broken if you try hard)

Wouldn't the Internet gateway need to be setup for the same frequency I'm transmitting on

Yes.

and in the same area,

Well, the receiver has to be in range at least. The effective range of your transmission will depend on the frequency, power, antenna, terrain, and other factors; and could be anywhere from global to less than a mile.

again, no guarantee and highly unlikely?

I wouldn't say it's highly unlikely. Nearly all digital repeaters, and most analog FM repeaters, are on some kind of linking system. And HF has such a long range, it's quite likely there's a receiver in range somewhere.

Ie, if I'm going to be broadcasting in California and I would like someone in New York, Peru, Greenland, etc., is it possible for them to listen?

Assuming they have internet access, and aren't in some jurisdiction that heavily censors the internet, then yes.

More problematic though is you can't legally *broadcast* in California, or any other part of the US:

§97.113 Prohibited transmissions.

(b) An amateur station shall not engage in any form of broadcasting, nor may an amateur station transmit one-way communications except as specifically provided in these rules; nor shall an amateur station engage in any activity related to program production or news gathering for broadcasting purposes, except that communications directly related to the immediate safety of human life or the protection of property may be provided by amateur stations to broadcasters for dissemination to the public where no other means of communication is reasonably available before or at the time of the event.

Would it also be available in real-time or close to real-time or would there be a substantial delay.

Delay won't be more than a couple seconds, probably less.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17550/ham-radio-internet-gateway, by Walter, Mike Waters, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
