# How to transmit images and video through a hurricane?

*Tags: software-defined-radio, hf, satellites, transmitter, emergency · score 5*

## Question

#### Background

You're in the path of a hurricane, and the eye just passed over your head. There is no electricity (apart from your own generator or battery), there is no mobile network and there is obviously no internet availability. But you do have a working computer with an SDR (20 MHz - 3 GHz) transmitter, Ham-it-up, a Wifi router, a mobile phone and an RPi3, and a few soldering skills.

#### Questions:

1. How can I transmit text, audio, images or videos to the outside world?
2. What are the options available for this?
3. What else is required to construct (or have) to do this? (In terms of antennas and hardware etc.)

First thought is that one should try to use an amateur satellite transmission, since that signal propagation would pass through least possible weather, i.e. straight up.

Second, that one should use some long wave TX that is less affected by local atmospheric conditions.

I was looking at this paper but it only cover VHF (240 MHz) and UHF (700 MHz), so I would imagine HF or LF would be a better choice.

I these days of hurricane season, I'd appreciate any practical or useful answers.

## Accepted answer (score 6, by Glenn W9IQ)

In general, the HF bands (1.8 MHz through 30 MHz) do not have sufficient bandwidth to support live transmission of a video signal. In the US, the FCC does not authorize an emission mode for live video on HF. The lowest available band in the US that supports live video is 70 cm (~440 MHz).

There are, however, options for transmitting pictures on HF. One of the oldest modes is SSTV (slow scan television). Despite the "TV" designation, it is used for sending relatively low resolution, still images. While SSTV used to require significant hardware to implement a station, this has all been replaced by free software that uses a sound card interface. As a result, there still is significant SSTV activity on HF.

A more contemporary method of sending and receiving pictures on HF is with the FLdigi program. It offers user selectable resolution and it has 24 bit color. The integrity of the received image is based on the signal conditions. FLdigi is popular due to its free software and simple radio interface using a sound card.

PACTOR offers error correction capabilities that can improve digital file reception under varying link conditions. The cost to implement PACTOR is generally higher due to the HF modem that is required and the software licensing schemes of the various versions.

## Answer (score 2, by rclocher3)

You're asking for quite a lot: high-speed semi-reliable communication over a long range, with little to no infrastructure. In general that's not possible; if it were, we wouldn't need the internet so much.

Glenn's answer covers the HF options. Satellite is an option if you have a high-gain VHF/UHF antenna, which can be hand-held, but passes for low-Earth-orbiting ham satellites last a few minutes at best and in that time people try to make dozens of contacts, so if you're lucky, you have the equipment and the software to predict passes, and you've practiced beforehand, then you could make a voice contact full of static lasting a few seconds. That's probably not what you had in mind.

There's only one high-bandwidth mode that I can think of that might get video out of the hurricane area, and that's Broadband-Hamnet™, formerly called HSMM-Mesh™. (No, I don't know why someone felt it necessary to trademark the name of a mode.) The idea is that you take a wireless router such as a Linksys WRT54G, load it with custom firmware, and put a high-gain antenna on it. The router uses channels 1-6 of the 2.4GHz ISM band, which overlaps with the upper portion of the 13cm amateur radio band. Your new firmware drives the router to higher power, and range of up to 16 km (10 miles) is allegedly possible with a higher-gain antenna. The router automatically finds other such routers in range, becoming a node in a mesh of nodes. Assuming that a reasonably-dense mesh of nodes exists in range, then you have a connection broad enough to support video.

The problem there of course is that you would need many closely-spaced stations all keeping their equipment dry, their antennas up, and their nodes operational on battery power in a hurricane area. That's a very demanding requirement that is unlikely to be met. Given the current state of the art, I'm not surprised that we don't see video clips on the news of hurricanes in action provided by hams. Sorry!

More information about Broadband-Hamnet™, formerly called HSMM-Mesh™, is available here.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9200/how-to-transmit-images-and-video-through-a-hurricane, by not2qubit, Glenn W9IQ, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
