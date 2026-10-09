# Antenna - vertical & beam antenna transmit at the same time?

*Tags: antenna, antenna-system, feed-line · score 4*

## Question

Is it possible to use a vertical antenna and a vertical polarized beam antenna at the same time? I have a friend that lives about 7 miles away & I can talk to him on 220MHz FM just fine on a vertical antenna. Another friend that lives about 13 miles away, but there’s a 2000’ foot ‘hill’ between us. We can’t talk on the vertical, but if I use a 4 element beam set to vertical polarization we can talk just fine. Unfortunately, the friend that is 7 miles away is directly off the side off the side of the beam & he can’t hear me when I’m using the beam. Is it possible to use both antennas at the same time & transmit to both of my buddies? The antennas are about 20 feet apart (horizontal separation) and the base of the vertical & center of the beam have about 8 feet difference. Thank you so much for any input or suggestions!

## Answer (score 9, by Ryuji AB1WX)

You can. You need a "power divider" or a "hybrid" suitable for this. Not a tee connector alone. The latter would mess up the matching. You can try to find a commercial power divider/combiner or make one yourself.

One simple way to construct a power divider is to use a tee connector and a 1/4$\lambda$ transformer using a 36$\Omega$ coax. If each of your antennas has good SWR, Wilkinson divider is also a practical approach.

Keep in mind only half of the transmit power will reach each antenna. So your peer will get 1 S unit lower reading. (VHF rigs tend to be 1 S unit = 3dB despite the IARU standard of 1 S unit = 6 dB).

You also want to think about what to do about the receive. If you simply combine the two antenna, the setup is the simplest (same setup for both T and R) but then you will pay a performance penalty in receive because the signal-to-noise ratio is degraded.

You'll get half the signal from either station and about the same noise power (depending on the actual divider/hybrid used and the matching conditions). So, make sure each of your peers is plenty strong before you proceed with this.

Using one receiver on each antenna for receive is a better approach, but you'll need more complicated setup to make it work.

Also, you'll probably have a better chance of making simultaneous contacts on 6m.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23379/antenna-vertical-beam-antenna-transmit-at-the-same-time, by Mike, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
