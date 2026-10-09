# How far can a 2.4 GHz, 1 watt signal go in a rural area?

*Tags: propagation, wifi, line-of-sight · score 8*

## Question

What's the approximate range achievable by a 2.4 GHz signal of 1 watt in semi-urban areas? I can see 2 km from our rooftop. Will a 2.4 GHz signal go that far, i.e. if I send WiFi signals from our rooftop is it possible to catch them on my phone 2 km away?

## Accepted answer (score 11, by Rory Alsop)

This is a strange sort of question, as in reality the signal will go infinitely far (effectively) however you are really asking at what distance might a receiver be able to pick up the signal.

In testing a 2.4GHz signal with a 100mW omni antenna, the furthest distance I could receive a signal with less than 5% retries (802.11b kit) was 2 miles with a 100mW 3dB receiver. I could manage over 5 miles with a directional 10dB antenna, but had some trouble aiming it accurately.

Your phone is going to have challenges at that range, but if you have a specific location, you could use a directional antenna on your rooftop aimed at that location. Even a basic Huber Suhner running at 1W could make that work.

(disclaimer - I used to test 2.4GHz radio kit from Symbol, Telxon, Motorola and Cisco. I can't post the data tables, but more than happy to give indications of what might work)

## Answer (score 2, by Adam Davis)

It's unlikely that the transceiver at the fixed location will hear the relatively tiny signal from your phone 2km away well enough to establish a link.

You need to have more power on both sides to make it work.

Even then, you might need specialized, large antennas or dishes.

Of course if there are no restrictions then you should be able to establish such a link with huge dishes on either end at a fraction of that power.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1463/how-far-can-a-2-4-ghz-1-watt-signal-go-in-a-rural-area, by user40713, Rory Alsop, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
