# Is it possible to receive weather satellites with a ham radio rig? (Icom 910)

*Tags: satellites, icom, bandwidth · score 3*

## Question

I would be interested in receiving weather satellites (NOAA and Meteor) with my Icom 910. It has very good filters and could be a better solution than a simple SDR. However, its manual specifies that its -6dB BW for FM is 15kHz, and NOAA's BW is 36kHz and Meteors', 90kHz.

Is there any way to solve this issue (disabling the bandpass filter maybe?) without hard-modding the rig?

## Accepted answer (score 3, by Phil Frost - W8II)

The filtering in an SDR is nearly always superior to the filtering in any analog receiver. This is because it's very inexpensive to implement a digital filter which can rapidly approach ideal behavior, whereas good analog filters are quite expensive.

The only analog filtering required by an SDR is that required to avoid aliasing and overload. Since these filters don't need to have a sharp transition to select a particular channel they can be quite cheap without compromising performance.

The issue with a very cheap SDR, like some $20 RTL-SDR stick, is noise, aliasing, and overload. But even a modestly better SDR, something with a modicum of engineering effort put towards anything but reducing cost, will probably outperform any analog radio.

From a cursory read of the product literature, it looks like there's an option to add a narrow CW filter. The most straightforward modification is probably to build a filter with the desired wider bandwidth and insert in place of this CW module. I'm not sure if it's possible to use the "CW" filter in FM, if not you could always operate in SSB mode and perform the demodulation in software.

Though at this point, you've essentially made an expensive, low-performance SDR. I'd suggest considering the SDR route: the cost won't be too much more than building a custom filter, the effort will be less, and the resulting performance superior.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15531/is-it-possible-to-receive-weather-satellites-with-a-ham-radio-rig-icom-910, by user3141592, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
