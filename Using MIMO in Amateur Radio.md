# Using MIMO in Amateur Radio?

*Tags: antenna, propagation, mimo, phased-array · score 10*

## Question

MIMO, Multiple Input, Multiple Output, is used widely in commercial data transmission. 802.11n and LTE devices use it to increase throughput, link reliability, and channel usage without increasing transmission power or using more bandwidth.

While there are many examples of Amateur Radio enthusiasts building and used phased arrays, I haven't found any examples of MIMO use in the Amateur Radio community.

Are there good reasons MIMO isn't used in Amateur Radio? Are there examples of Amateur Radio enthusiasts building and experimenting with MIMO systems?

It seems that the increasing adoption of SDR and the continued interest in QRP would lead some down this path, but I haven't found any information about it in the Amateur community.

## Accepted answer (score 7, by Sterling N0SSC)

There are a few radios that support diversity reception, but only to minimize effects of propagation rotation and multipath, not to increase data rates. This isn't true MIMO. It's more like SISO where the input is whichever one of two antennas has the strongest signal.

Which brings up another point - data. There really isn't that much data being used on ham radio at the moment. D-STAR is around, then Yaesu came out with a digital radio, and a lot of work is being done on things like Codec2 and FreeDV, but in general, it's not all that prolific.

However, MIMO in ham radio will still be reserved to things like HSMM and HamWan that actually have very large bandwidths. With that, the equipment is off-the-shelf. Some of it has MIMO capability, like 802.11N routers modified for use on amateur frequencies - just like you mentioned in your post.

It would be cool to have MIMO on lower bitrate and digital voice, but I don't think the gains would be that great.

I do undergrad research in statistical channel precoding using SDR MIMO transceivers on amateur bands, and man, is it cool...but people don't have $40,000 to spend on a MIMO IQ vector generator/demodulator. I have yet to see a QRP MIMO homebrew rig, but that would be great!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/774/using-mimo-in-amateur-radio, by Adam Davis, Sterling N0SSC. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
