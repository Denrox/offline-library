# Rolling QRM from 3000-10000 kHz - What Is It?

*Tags: noise · score 9*

## Question

Video

I was lucky to catch the QRM start this morning @ approximately 10 AM Pacific Standard time. It was wide, starting around 3000 kHz up to 10000 kHz.

It starts fast then slows to a crawl. The noise has pronounced high/low bumps as you'll see in the video. Almost like a train with high/low boxcars rolling through ...

The rolling was faster before I started recording.

Once it stops, it is very still with minor drift +/- and is present until approximately 10 PM Pacific Standard time. When it stops rolling, it does not start up again. It present periodically throughout the bands from 80 -> 30 meters.

Before and after 10 AM/PM, it is not present anywhere that I can see.

What would cause rolling QRM like this?

I caught it yesterday and powered-down my house at the breaker only leaving one circuit up for the radio and switching circuits to validate whether or not it was the house. To the best of my knowledge, it is not my house but something in the environment radiating RFI.

Living in Las Vegas, NV, we have a lot of solar rooftops that could perhaps contribute to this in some way. However, it lasts until 10 PM which is far past sunset.

- Radio FT-950
- Astron RS-35M power supply
- Active Mini-Whip antenna

## Answer (score 2, by bryon)

I've seen similar 'roving' signals emanating from low quality switching type power supplies, which can generate noise at multiple harmonically related frequencies.

Since you've mostly ruled out local sources, you might have to do a bit of sleuthing with a small directional loop antenna and a portable receiver. A cheap RTL type SDR receiver with a down-converter for HF hooked to the USB port on a laptop PC can work well for this, such as one of the AirSpy radios, as you can monitor lots of radio spectrum at once. A small wire loop antenna maybe 8-12" diameter should provide enough directivity, as long as there's enough signal. The hours of operation suggest maybe a device used by a nearby neighbor who is home during the day - maybe a television or radio power supply, or a charger for a laptop or tablet.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10376/rolling-qrm-from-3000-10000-khz-what-is-it, by user11702, bryon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
