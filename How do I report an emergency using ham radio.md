# How do I report an emergency using ham radio?

*Tags: united-kingdom, emergency, frequency, procedure · score 51*

## Question

If I'm in the wilderness with ham equipment but no phone signal, how would I report an emergency? Is there a particular frequency I would use, a particular protocol or suchlike?

## Accepted answer (score 36, by Walter Underwood K6WRU)

On voice, use "Mayday Mayday Mayday" at the beginning and end of the transmission. This is only for life-threatening emergencies.

http://en.wikipedia.org/wiki/Mayday_(distress_signal)

For other emergency situations, like reporting a wildfire that does not directly threaten you, use "Break Emergency" at the beginning of the call. This is a good guide to making emergency calls:

http://www.dummies.com/how-to/content/operating-your-ham-radio-in-an-emergency.html

The IARU has established global emergency frequencies. They call these "Emergency Centre of Activity Frequencies".

```
15m  21.360 MHz
17m  18.160 MHz
20m  14.300 MHz

```

In the US, 14.300 MHz has an organized group of monitors.

A full list of regional and country-specific emergency frequencies is here:

http://www.iaru-r1.org/index.php?option=com_content&view=article&id=891&Itemid=246

The Wilderness Protocol for VHF/UHF (http://k4jwm.com/wilderness-protocol.htm) is useful if you have line of sight communication. That might not be the case in mountainous terrain. The Wilderness Protocol was started in the US, so I have no idea how often it is used outside the US.

Finally, amateur radio requires practice for effective emergency use. In a group, you need at least two practiced operators, because one of them might be injured. In most situations, a satellite phone is a better and more reliable choice for backcountry emergency communication. I go into more detail on that in this blog post:

https://observer.wunderwood.org/2011/10/12/emergency-communication-in-the-wilderness/

One good way to get practice with back country operating is to participate in Summits on the Air (SOTA). The common SOTA frequencies might also be a good choice for secondary emergency frequencies, because the SOTA "chasers" often monitor those.

## Answer (score 23, by user)

Assuming that you have an amateur radio license makes this easier, but it's quite possible that the UK legal language includes provisions that may be applicable and allow transmission without a license. It depends on the specifics of the emergency in question. I would strongly recommend familiarizing yourself with the relevant definitions in the legal code of your country; it's perfectly possible that an emergency situation allows you to transmit on frequencies you otherwise wouldn't be allowed to, *even if the emergency situation does not revolve around you directly* (for example, you tune your transceiver across the bands without a license and come across an emergency transmission by someone else).

If possible, find a frequency that is actually in use and where you can hear both stations; it makes it much more likely that someone will hear your call. Call **mayday mayday mayday** (life-threatening emergency) or **break break emergency** (non-life-threatening emergency) as soon as is practical (on a handover if you can afford to wait that amount of time), and unless the situation is extremely dire *wait a few moments for acknowledgement*. Hopefully one of the stations will respond with something like *Jim, break for emergency, go ahead emergency*. As the remote operator making such a go-ahead request, you want to be *extremely concise, clear, and unambigiously tell the breaking station to go ahead with its transmission and all others to cease transmission*. Ideally, at this point the remote station operators will have grabbed a blank piece of paper and a writing utensil of some kind, *and be prepared to take notes*. *For the receiving stations to be taking notes is absolutely essential; as a receiver you will not remember the details!* Also, *all* stations able to receive an emergency report should copy it down; if the station making the emergency report goes off the air for whatever reason, the chances are much better that even in the case of heavy interference a complete report can be pieced together by the remaining stations.

Then, I would suggest reporting things in logical order. *Stay calm.* Consider what information is needed to offer assistance. For a wilderness emergency, I'd state:

- The kind of emergency (broken leg, vehicle collision, wildfire, ...).
- The position, in some unambigious manner (for example "Grothwick national park distance 30 miles east of Tadwick, distance 12 miles direction north from trail head on the length 72 miles trail"). Spell out numbers ("seven two", possibly even "seven two point zero" rather than "seventytwo"). GPS coordinates if available will greatly help, but if it's an actual emergency, I wouldn't wait for the GPS receiver to get a fix; you can always complement later.
- The assistance required ("need transportation to nearest hospital", "need fire prevention services", ...)

After that, **STOP.** Say "any receiving station, confirm complete reception of emergency report" or something equally unambigious. Hopefully someone will acknowledge, or at least ask for a repeat of some missed piece of information. *Note that there may be stations listening without transmission capability* so a lack of response does not *necessarily* mean that nobody heard you. The ability for a remote station to acknowledge is why I suggest finding a frequency that is actually in use and breaking into the communications.

With any luck, a remote station will respond with something like "confirming complete reception of emergency report, stand by". *This is the kind of answer you want.* It means they have received everything *and is contacting the proper emergency services* through some alternate channel, whether that is radio relay, telephone, or some other means. Respond with a short "emergency, standing by" to acknowledge. Issue repeat "emergency, standing by" every 20-30 seconds or so to make it less likely that anybody thinks the frequency is free for use. Hopefully, a minute or two after the initial acknowledgement, the acknowledging station will get back to report that emergency services have been notified about the emergency. *At this point, they may relay questions, instructions or otherwise from the emergency services dispatch center. Answer those to the best of your ability, as clearly as you can, just as if you had been calling them yourself.*

**You may notice an overall theme in all this: *clarity*, and the *repeat transmission of "emergency"*.** Both those serve to help everyone involved. A panicked report does not help anybody, as well as that a random radio amateur is less likely to be trained to deal with someone panic-struck than an emergency services dispatch operator. Repeatedly transmitting "emergency" informs others that the traffic should have extremely high priority. Clarity, *including avoiding the use of jargon*, helps non-amateurs copy and possibly relay the message to the emergency authorities. All this helps ensure as speedy a response as possible. **The exact wordings are much less important than doing your best to remain calm and to provide the pertient information as soon as possible.**

In a real emergency situation, I wouldn't worry too much about identification. Do it early if you have the time, but if not, it's better to wait until all essentials have been taken care of. And certainly don't bother with signal strength reports etc. unless the signal quality is exceptionally poor to the point of being outright hard to copy accurately. This is an *emergency report*, not a rag-chewing amateur radio contact!

## Answer (score 7, by JeepEscape)

If this is something you are interested in on an ongoing basis as a volunteer, then you should look into joining RACES and/or ARES in the US, and RAYNET in the UK:

http://en.wikipedia.org/wiki/Radio_Amateur_Civil_Emergency_Service

http://en.wikipedia.org/wiki/Amateur_Radio_Emergency_Service

http://en.wikipedia.org/wiki/Radio_Amateurs_Emergency_Network

http://www.raynet-uk.net/

In fact, during major emergencies and disasters, one or both of these organizations may be the only hams allowed to operate, and it will be a very organized effort.

Outside of that, here are the US regulations for licensed hams:

§ 97.403 Safety of life and protection of property. No provision of these rules prevents the use by an amateur station of any means of radio communication at its disposal to provide essential communication needs in connection with the immediate safety of human life and immediate protection of property when normal communication systems are not available. § 97.405 Station in distress. (a) No provision of these rules prevents the use by an amateur station in distress of any means at its disposal to attract attention, make known its condition and location, and obtain assistance. (b) No provision of these rules prevents the use by a station, in the exceptional circumstances described in paragraph (a) of this section, of any means of radio communications at its disposal to assist a station in distress.

This basically says that under those circumstances in the US, you can operate in any band, in any mode, in an effort to communicate the distress, including the ones you are not licensed for.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/59/how-do-i-report-an-emergency-using-ham-radio, by berry120, Walter Underwood K6WRU, user, JeepEscape. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
