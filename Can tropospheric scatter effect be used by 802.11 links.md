# Can tropospheric scatter effect be used by 802.11 links?

*Tags: propagation, wifi · score 6*

## Question

What are the lowest EIRP and antenna gain requirements that make possible use of troposcatter at the distances of 100 to 150 kilometers assuming conventional WiFi (6 Mbit/s data rate with OFDM/BPSK modulation)?

While this is unlikely to work in practice (for legal reasons, among others) I'm curious if such links can be established.

## Accepted answer (score 5, by Phil Frost - W8II)

I don't see why not. Of course, it's subject to the biggest problem with troposcatter: extremely high loss.

Let's work out an example to see how bad this is. Let's say we want a link at a distance of 150km. Borrowing numbers from [this question](What%20is%20the%20average%20fade%20margin%20required%20for%20proper%20operation%20at%202.4%20GHz.md), let's further assume that we need -84dBm at the receiver to make the link work. And just for now, let's assume we have an ideal, free-space path between the stations. We can apply the Friis transmission equation to determine the EIRP necessary to make this work:

$$ \begin{align} P_r&=P_t+20\log_{10}\left(\frac{\lambda}{4\pi R}\right) \\ -84\:\mathrm{dBm}&=P_t+20\log_{10}\left(\frac{0.125\:\mathrm m}{4\pi \cdot 150000\:\mathrm m}\right) \\ -84\:\mathrm{dBm}&=P_t - 143.6\:\mathrm{dBm} \\ 59.6\:\mathrm{dBm}&=P_t \\ \end{align} $$

So, our free-space path losses are -143.6dBm, and we'd need an EIRP of about 60dBm to make it work, assuming an isotropic receiving antenna. If we can have a 40dBi antenna at each end, then we'd need a -20dBm transmitter. Easy.

Only trouble is that paths of this length aren't even remotely like free space. There's probably a planet in the way. So say we want to use troposcatter...what are the additional losses?

Mike Willis has a great article on troposcatter, which includes all sorts of empirical models and stuff. However, it's nicely summarized by this graph:

These are losses *in addition to* the ideal case we just calculated. For our example of 150km, we can see losses of about 62dB. That brings the minimum EIRP to 123dBm, or again assuming our 40dBi antennas, transmitter power of 43dBm.

Certainly feasible, even after adding margins for noise. With higher gain antennas, on the edge of possibility with consumer equipment.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1497/can-tropospheric-scatter-effect-be-used-by-802-11-links, by Deer Hunter, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
