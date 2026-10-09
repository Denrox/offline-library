# Using radio for musical collaboration -- the line between conversation and broadcasting

*Tags: united-states, legal, music · score 7*

## Question

I'd like to collaborate (e.g. play together) with other musicians in my local area and/or beyond.

Coronavirus has made in-person collaboration difficult. Latency makes internet-based collaboration difficult.

Is there a legal way for a group of musicians to play together using amateur radio in the United States?

**Here's what I've found so far:**

The Electronic Code of Federal Regulations (e-CFR), under Part 97.113 (Amateur Radio Service - Prohibited transmissions), lists

(4) **Music using a phone emission** except as specifically provided elsewhere in this section; ...

**Two notes about the above excerpt:**

1. The ARRL glossary defines "phone emission" as "The FCC name for voice or other sound transmissions."
2. Regarding the "... except ...", I can only find one other use of the word "music" in Part 97:

(c) No station shall retransmit programs or signals emanating from any type of radio station other than an amateur station, except propagation and weather forecast information intended for use by the general public and originated from United States Government stations, and communications, including incidental music, originating on United States Government frequencies between a manned spacecraft and its associated Earth stations. ...

I think this is saying it's ok for amateurs to retransmit a signal which includes incidental music if that signal originates from the listed government/spacecraft-related sources.

**Here are questions I believe are unanswered by Part 97:**

- Does "phone emissions" include digitally encoded audio emissions? This would imply it is illegal for a ham radio network to provide access to a musical mp3 file on the internet or any video that contains even incidental music. Both Broadband-Hamnet and HamWAN include a statement to the effect of "... be sure that any internet traffic that will be sent over radio will comply with Part 97 rules." If it were clear that accessing any file on the internet incidentally containing music is not Part 97 compliant, they would probably provide that information. That would mean it's illegal even to transfer (almost) any video game or other software that includes musical sounds using a ham radio network. It would be nearly impossible in some cases for a ham to know they are even doing something illegal. It may be that the mention of music in these regulations was not meant to cover these situations, but instead to allow for so-called "pirate radio" broadcasts to be shut down.
- Imagine there are two individuals having a conversation over ham radio in a perfectly legal fashion. If they begin singing to each other instead of talking, their conversation then becomes illegal? Even if suggested by the language in Part 97, this may not be true in any legally defensible way unless there is some legal precedent that would help draw a line between speech and music (e.g. something relating to the intent of the transmission). A similar discussion is given in a related question [here](What%20defines%20music%2C%20per%20amateur%20radio%20regulations.md).

**A note on why this question is distinct from [what-defines-music-per-amateur-radio-regulations](What%20defines%20music%2C%20per%20amateur%20radio%20regulations.md):**

The question [what-defines-music-per-amateur-radio-regulations](What%20defines%20music%2C%20per%20amateur%20radio%20regulations.md) focuses on short musical sounds for another listener to receive and what defines "music". The accepted answer states "

... Bottom line, if something that is purely incidental to the conversation, or if you are transmitting it digitally, you can actually have a bit of music and not get your hand slapped by the FCC. Thus, the doorbell seems fine, and most likely the types of "Windows Sounds" that sometimes come up, but personally, I wouldn't risk it. If you are trying to broadcast then you are almost certainly in violation of the law.

The answer, just like the question, focuses on the applications of DJing music and sending bell sounds, presumably as indicators to aid in communications. Admittedly, the question does center around the lack of clarity related to the term "music". However the accepted answer does not provide a clear answer to whether musical collaboration in all forms is disallowed on radio, digital or analog. It even could reasonably be interpreted as suggesting (e.g. "... or if you are transmitting it digitally ...") that musical digital audio streams are allowed. Also, in contrast to the applications in the [what-defines-music-per-amateur-radio-regulations](What%20defines%20music%2C%20per%20amateur%20radio%20regulations.md), the application of musical collaboration between two (or more) individuals does not involve an audience. Musical collaboration is more in-line with a conversation than a musical broadcast. This changes the intention of the transmission away from amateur DJing (or so called "pirate radio"), an application that these laws were possibly designed to prevent. Many musicians and music teachers are, due to covid-19, currently struggling with figuring out how to collaborate and teach music remotely. Radio may be the only practical widely available solution for this application. Assuming the intent of the law or the radio operator are legally important, I believe this post asks a distinct question from that of [what-defines-music-per-amateur-radio-regulations](What%20defines%20music%2C%20per%20amateur%20radio%20regulations.md).

**Update -- Part 97 does give a definition of "phone" in section 97.3.c.5:**

(c) The following terms are used in this part to indicate emission types. Refer to §2.201 of the FCC Rules, Emission, modulation and transmission characteristics, for information on emission type designators.

...

(5) *Phone.* Speech and other sound emissions having designators with A, C, D, F, G, H, J or R as the first symbol; 1, 2, 3 or X as the second symbol; E as the third symbol. Also speech emissions having B or F as the first symbol; 7, 8 or 9 as the second symbol; E as the third symbol. MCW for the purpose of performing the station identification procedure, or for providing telegraphy practice interspersed with speech. Incidental tones for the purpose of selective calling or alerting or to control the level of a demodulated signal may also be considered phone.

A couple notes:

- Only "speech emissions" (and not "other sound emissions") are stated to be considered as phone emissions for emissions having B or F as the first symbol.
- From §2.201, the definition of type E information is "Telephony (including sound broadcasting)".
- As far as I can tell, even if speech and telephony both *do* include music, "phone" doesn't include all telephony (i.e. xxExx) emission types.

## Answer (score 6, by Phil Frost - W8II)

Does "phone emissions" include digitally encoded audio emissions?

Yes. For example, FreeDV is a phone emission. FreeDV consists of multiple PSK carriers: first symbol G. These carriers transmit a stream of bits: second symbol 1. And it is designed to take a sound at one station and reproduce it at the other station. That is telephony: third symbol E. Emission G1E fits the definition of "phone" in part 97. This is why the canonical FreeDV frequencies are in the phone section of the bands, and not the data sections.

At least, that's my interpretation. There doesn't seem to be great agreement.

The important part of the "phone" definition is "E as the third symbol". This means "telephony". I don't see how any emission designed to take music at the transmitting station and reproduce it as the receiving station could have any other symbol in the third place.

As far as I can tell, even if speech and telephony both do include music, "phone" doesn't include all telephony (i.e. xxExx) emission types.

True, however, it does include all *authorized* emission types with the third symbol "E". The other emissions that are allowed (somewhere) in the amateur service are CW, data, image, MCW, pulse, RTTY, SS (spread spectrum), and "test". They are all defined in the same area as you found the phone definition. None allow "E" as the third symbol.

So avoiding the definition of "phone" doesn't mean your musical transmission is authorized. If you accept that reproducing music over distance is "telephony", the third symbol must be "E", which can't be CW, data, image, MCW, pulse, RTTY, or SS. So you must either meet the definition of "phone" (in which case you aren't allowed to transmit music) or not (in which case you aren't allowed to transmit anything at all).

You could claim you are transmitting "data" which *happens to be* music, however I'm fairly certain you will lose this case and you'll need the resources to fight it. Furthermore, there are significant restrictions on what data can be which will be a serious technical challenge, not least among them an upper limit of 300 baud.

Imagine there are two individuals having a conversation over ham radio in a perfectly legal fashion. If they begin singing to each other instead of talking, their conversation then becomes illegal?

Technically yes, though I doubt the FCC would care enough to act unless it was a regular thing.

While we can quibble about whether an 8-note chime is "music" and we can make jokes about hams not being able to sing "music", your use case is very clearly music:

I'd like to collaborate (e.g. play together) with other musicians

I'm afraid part 97 is quite clear: no music. I don't see any wiggle room to argue collaborating with musicians isn't music.

Besides the issues of legality, I think you'll find the idea is difficult to implement technically as well. The best-case speed-of-light delay from San Francisco to New York is 14 ms. Real-time collaboration requires less than 20 ms, so most of your latency budget is blown just in propagation delay. If you digitally encode the signal (which would be required if you want music-quality audio) you'll have even more latency from the codec. You'll also require quite a lot of transmitter power and/or antenna gain to get sufficient fidelity and reliability.

Your best bet is to delay the streams to something musically tolerable, like some integer number of beats or measures. For example, NINJAM.

Alternatively, use a radio service which does not have a restriction on music. Amateur radio is unique in having large allocations in HF which can be used for worldwide communication, but if only shorter distances are necessary you could do fine with a pair of WiFi APs and a point-to-point link which come with no encumbrances on the kinds of things you can transmit. WiFi is by no means optimal for latency, but the equipment is cheap and easy to integrate.

## Answer (score 3, by Scott Earle)

I think that the FCC does not want to allow people to send music over the airwaves, due to the (extremely complicated, arcane, and heavily-legislated) issues around the right to perform music in a non-private setting.

For example, if you were to sing a song written by The Beatles, do you have the right to perform that where anyone else is listening? (Unless you licensed it, the answer is "no".) Do you have the right to sing your own compositions in the same place? Probably yes, as long as you hold the rights to those compositions.

If you are just with a group of friends in your own living room or garage, there is no problem as those sounds don't travel very far. If you are transmitting them over the radio, then the FCC gets involved, because the sounds can be listened to by anyone with the right equipment, within a certain range.

If you really really want to do socially-distanced jam sessions, I would suggest using a private communications medium such as over the phone (landline or mobile phone), or maybe something like FRS would be suitable? I don't know what the regulations are about allowed content over FRS or similar services, but they will be a lot more lenient than the regulations over amateur radio.

The point of amateur radio is more to do with the means of communication (e.g. self-training on the technology of radio) than it is to do with the actual content of transmissions, and as such I think amateur radio is a bad fit for what you are proposing.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17364/using-radio-for-musical-collaboration-the-line-between-conversation-and-broadc, by mathandy, Phil Frost - W8II, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
