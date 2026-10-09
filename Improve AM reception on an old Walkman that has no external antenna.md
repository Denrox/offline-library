# Improve AM reception on an old Walkman that has no external antenna

*Tags: antenna, am, reception · score 3*

## Question

I have an old Philips walkman that has AM/FM radio. I tried AM radio. Really I can get clearly 2 country radios. I caught very poorly 4 foreign radios or different countries, but they have lots of noise.

I plug in headphones with quite a long cable, and those headphones are plugged into the splitter that came with it, so that it can connect to headphones input and mic input since it's a complete headset. However this does not improve much the quality.

The frequency range in this walkman is from 530 to 1180 KHz I believe, since the lowest number says 53 and the highest number says 118 and below it says "10x". I guess it means you have to multiplay those numbers by 10 so that you have the KHz number.

The walkman doesn't have any external attached antenna, since I guess headphones do that function, however is that an easy way of improving the reception of AM signal? Is there a headphones cord optimal length?

## Answer (score 4, by Zeiss Ikon)

The genuine Sony Walkman, and most of the Walkman-style radios from other makers, did indeed use the headphone cable for their antenna. My experience (with an early 1980s Sony model) was very good on FM, and even then AM was mostly talk, news, and sports, so I didn't listen much on that band.

That said, AM radio isn't what it used to be. Fewer stations broadcasting at lower power means you may not nave a broad selection of strong local stations. Further, many AM stations (at least in America) now broadcast a digital sideband (which carries station and track ID information as well as the HD/stereo signal if offered) that can come through as a "buzz" or similar distortion in the analog signal.

As you note, most "pocket" size AM sets have a tuner that covers the whole band with less than half a turn of a small wheel; these are almost impossible to tune with high precision. Add that to the relatively poor discrimination of many less expensive pocket AM sets, and it's fairly likely your antenna isn't the problem.

## Answer (score 2, by hotpaw2)

A tunable high-Q loop antenna, such as:

https://www.amazon.com/Kaito-Tunable-Passive-Antenna-Panasonic/dp/B001KC579Q/

placed near your small AM radio can inductively couple into the internal ferrite antenna or RF front-end, and add to their gain.

Here's an example of one built around a crate than you can put your radio inside:

https://swling.com/blog/2017/06/how-to-build-a-milk-crate-am-broadcast-loop-antenna/

Basically, you construct a large (larger than your radio), multi-turn air-core inductor, and tune to stations in the AM band using an air variable capacitor. The much higher Q of the large air-core inductor and air variable capacitor can also help separate adjacent frequency AM stations better than the tiny dial on your pocket radio.

If you just want to add a long wire antenna, and have a large enough yard or field to put it in, around 250 to 750 feet of wire suspended above ground might be suitable for improving AM broadcast band reception.

## Answer (score 2, by Scott Earle)

I would recommend getting a multi band radio that can receive these and other frequencies. In the late 1980s I used to listen to AM radio using an old FRG-7 communications receiver. I **loved** that thing - it was a joy to use. Even its power switch was big and red, just like they should be! The only problem with that was that it worked best with a large external antenna. But you could make a ferrite bar antenna (effectively a magnetic loop antenna for LF/VLF) that would work well enough to pick up some distant long- and medium-wave stations.

The world has moved on, however, and many stations have now closed down and moved to the internet or VHF (usually on FM). A communications receiver and a decent antenna will help you find the long-, medium- and short-wave stations that are still broadcasting, as well as the many radio amateurs out there across the globe. Maybe one day you might even hear me! :)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15117/improve-am-reception-on-an-old-walkman-that-has-no-external-antenna, by Lorthas, Zeiss Ikon, hotpaw2, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
