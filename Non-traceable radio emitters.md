# Non-traceable radio emitters

*Tags: propagation, fox-hunt, location · score 11*

## Question

There are various techniques for locating a radio emitter. But what are some methods to make this really difficult? There is usually a patch to every vulnerability, at least from the world where I come from.

## Accepted answer (score 14, by Manfred VK3AES)

IMO, your question is too general to give a good, specific answer. Also, it would help if you elucidated the motivation for the question.

I am a semi-retired electrical engineer, not a security or RF expert but I'll give it a go anyway.

The first assumption is that the transmitting equipment is hidden from plain sight and other non radio-related detection.

To locate a hidden radio station your adversary must be able to receive the emissions. It follows that you could use a highly directional (beam) antenna which only illuminates the intended receiver. There would be no countermeasure.

The next possibility is that the signal can be received by your adversary but they do not have direction finding equipment within the footprint of your beam. This is potentially the case with (older) satellite transponders which simply re-transmit everything they receive in the transponder's pass band. So, you could beam a signal to such a satellite and as long as the intended receiver is somewhere in the satellite's footprint you can effectively hijack the satellite service (has happened).

Now to the cases where your signal can be directly received by your adversary. AFAIK, there are two basic methods for locating the source of radio signal.

1.

Two or more receivers with steerable, directional antennas (including beam-forming phased arrays).

2.

Three or more time synchronized receivers (spectrum analyzers) which compare the arrival time of a specific signal at their accurately known locations. At one nano-second time resolution, such a system can potentially pinpoint an emission with an accuracy of better than 1 meter, even if the signal is only a very short burst. I know that such systems exist and are deployed around sensitive infrastructure such as airports.

To locate an emission your adversary must know what to look for. That opens up additional possibilities but does not directly relate to your question. Anyway, here are two that I can think of:

1. A radio could potentially masquerade as valid by adopting the frequencies and low-level transmission protocols of a legitimate service.
2. Direct sequence spread spectrum can spread a signal over a bandwidth of many MHz and make it appear as undetectable, random noise to a narrow band receiver. Such a signal may go unnoticed for a long time.

## Answer (score 11, by Martin Kochanski)

Another possibility to look into is meteor burst communication. This is a well-established technology. You beam a VHF signal up into the sky, it bounces off a meteor trail, and your recipient picks up the reflected signal. Since transmission is upwards, picking up the transmitter's location would require being above the transmitter at the time (making certain assumptions about directionality).

There is a short article in NSA Cryptologic Quarterly and a Navy Postgraduate School thesis from 1989. An article I have been unable to locate online is: Elliott, Ronald D. "Meteor Burst Communications in Tactical Intelligence Support," SIGNAL, November 1986, pp. 80-88.

Amateurs, it seems, tend to experiment with lower frequencies, which may have implications for directionality: see, for example, this page. The RSGB also has a page.

It would be interesting to know if anyone on this forum has had any experience with this. It may be well known.

## Answer (score 5, by Marcus Müller)

at least in the world where I come from

Assuming this is the world of arrogant computer security experts (sorry I'm a bit allergic to this):

Well, unlike computers, physics wasn't designed by humans.

So, any signal that contains significant information needs to contain significant power (that's a direct result of Shannon capacity), and if it has significant power, it's also localizable.

Of course, localization resolution is proportional to wavelength. But, so are antennas. So, while you can not be very sure from where an extremely low frequency (ELF, typically used for communication to submerged submarines) transmission came from, but once you look at an aerial picture, you will notice the 500 km long antenna in the Russian forest...

Rodrigo recommended "Burst transmission", but that's really no solution. If I can detect it as anything but noise with a high probability with multiple receivers, then I can also localize it. This is done, and has been done, since the 1970s for bursty military transmissions in HF bands (because they reach very far on earth). For higher frequency signals, you really don't need state actor equipment: a two- or better four-channel MIMO receiver allows you to put an unambiguous direction on where a signal came from. Use two of these, and you know where a transmission came from. In fact, a transmission being a very short burst implies a high bandwidth, and that is *good* for location accuracy. (You need good SNR for low estimator variance, on the other hand, so there *are* limits. It's just not as easy as "use a bursty transmission scheme".)

So, your only choice is to make a signal that someone can't detect as being anything but noise, not even if he correlates multiple observations. Sadly, such signals have practically no information content.

The only thing you can do is hope that you find a part of the spectrum where the propagation properties are so random, and so different in different directions, that the probability of simultaneous detection at multiple points approaches zero. Good luck with that; in essence, that channel would have what is called a "secrecy rate" in physical layer security research (i.e. an observation of one channel doesn't give you all the bits of information in the entropy of a different channel), and we're talking about secrecy rates of < 100 bits per minute for indoor channels. That is an upper bound for how much information you could send there, without giving away information about the channel, and thus your location.

TL;DR: Nope.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16905/non-traceable-radio-emitters, by Chi non salta Pavarotti è, Manfred VK3AES, Martin Kochanski, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
