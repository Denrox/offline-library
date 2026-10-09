# Can I talk 2 Meter VHF across the United States

*Tags: antenna, united-states, propagation · score 7*

## Question

Can I talk on 2 meters from the east coast to the west coast without using repeaters?

## Answer (score 6, by natevw - AF7TB)

Sometimes a VHF signal **can** be heard clearly, thousands and thousands of miles away! The usual mechanism is tropospheric ducting. It's an essentially **random, temporary occurrence**, not something you can rely on.

As a **reliable** means of direct communication, you can **not** expect to talk from east coast to west coast on the 2m band without using repeaters. VHF is not practical for use at distances like that, which would be in the range of 2000–3000 miles beyond the horizon.

VHF *can* propagate [beyond its basic "radio horizon"](How%20does%20VHF%20UHF%20propagate%20beyond%20the%20expected%20%28radio%29%20horizon.md), primarily due to scattering. However, if you look at the charts in that link, you'll see that at a distance of **only 500 miles** there is already **about 240 dB of path loss** you'd need to overcome.

At the legal limit of 1500W, you could transmit a 60 dBm signal. Let's say you need a -130 dBm signal for successful receipt. (This would be an "S3 signal". For VHF, S9 is defined as -93 dBm and each S-unit is 6dB.) Since 60 dBm [the transmitted power] minus 240 dBm [the path loss] is -180 dBm, you need 50 dBm of additional gain to meet that -130 dBm goal.

To put this in perspective, consider this 10 meter long, 14 element Yagi — it's advertised to have 16.63 dBi of gain. Put one of those at each end and you're still almost 18 dB short. You might be able to add a pre-amp at the receiver, but only if the signal is still above the noise at that location. (Since we were aiming for only an S3 signal, I'm not sure how good the chances of that would be!)

I suppose you might use two parabolic dishes each in the realm of 14–16 meters in diameter to get 50 dBm of gain but remember we started with the situation at only 500 miles. The United States is **about 7 dB wider** than that — probably even more so as far as path loss goes. So now we're talking dishes in excess of 20m diameter, at minimum.

In short, trying to use **reliable** atmospheric scattering of 2m signals across the United States is probably harder than bouncing your signal off the moon, i.e. sending your signal out a distance of 1.2 light-seconds and then receiving, after it has travelled that distance *back* again, whatever manages to reflect off the lunar surface! (Earth-Moon-Earth communication has between 251 and 253 dB of path loss.)

(Unless, as another commenter points out, your antennas are reeeeeeeeally high. Plugging two 500,000 ft high antennas into KD4SAI's VHF/UHF Line of Sight Calculator gives you a nice 2000 mile line-of-site distance. The Friis path loss is only about 146 dBm at that range. So, raising the stations to about 95 miles high at each end *does* give you a much more auspicious start, link-budget-wise — if you spend enough on the mast, you could use fairly cheap antennas ;-)

## Answer (score 6, by Scott Earle)

There is a list of distance records on the ARRL website. Looking at these, I would say that it might be technically possible to hold the absolute minimum of what could be called a ‘contact’ (e.g. callsign and signal report exchange) across such a distance perhaps once every ten or twenty years when exceptional conditions are all in alignment.

To answer the second part of the question, all very long distance contacts on VHF are made using highly directional antennas, or an array of such antennas (such as a multi-element Yagi, and usually take place in CW (Morse code) or possibly SSB (single sideband, voice).

## Answer (score 5, by AG5CI)

I believe that you could do so via EME - Earth-Moon-Earth - communication, or "moonbounce". There are tons of resources dealing with moonbounce here.

My understanding is that it has been done before (and is maybe done regularly) on 2 meters via EME while operating within FCC limitations.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9619/can-i-talk-2-meter-vhf-across-the-united-states, by Jim F, natevw - AF7TB, Scott Earle, AG5CI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
