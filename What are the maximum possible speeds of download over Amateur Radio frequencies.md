# What are the maximum possible speeds of download over Amateur Radio frequencies?

*Tags: software-defined-radio, mobile, internet · score 3*

## Question

In this scenario, I would have a base station connected to a modem that essentially allows me to access the internet/local network via radio, irately I am not fully aware of what information I need to provide to have a proper answer, as I am new to the community, but I am more than willing to learn.

tl;dr: how fast can one transmit and receive at half-duplex on any given amateur radio frequency?

## Accepted answer (score 4, by Marcus Müller)

## maximum rate

There's no upper boundary really other than SNR. There's no general number.

There's what information theorists call *channel capacity*, which simply relates the amount of bits per second you can get, at most, theoretically, across a channel of given bandwidth $B$ at given signal-to-noise ratio. The formula simply states

$$C=B\log_2 \left(1+\text{SNR}\right)$$

The idea is simple: the better your SNR, the more different symbols you can tell apart, which means a single symbol carries more bits of information. The higher the bandwidth, the more symbols per second you can send.

Note that this is a theoretical upper limit, and doesn't say how you'd go about implementing something that does that rate. In radio communications we often come pretty close to this boundary with modern systems. Just don't expect something as "technologically braindead" as ax.25 to even nearly achieve that. But, for example, there's amateur radio bands with relatively large bandwidths in the upper microwave region, and with a good (read: low-noise) link on a large bandwidth, Gbit/s are certainly feasible. It all depends on how you use your spectrum and how much spectrum you've got and how little noise there is on that!

The derivation of that formula isn't that simple; the core takeaway is just that

1. Transport capacity doesn't care about the carrier frequency at all. It cares about bandwidth and SNR.
2. You can't say how much data you'll be able to transport without saying what technology you want to employ there.

## internet access

I'm not sure amateur radio is what you need at all. Most jurisdictions simply forbid encrypted / private communications over amateur radio frequencies, and that means that you wouldn't even be legally allowed to open a HTTPS website (which, luckily, are most important websites these days) or check your emails via IMAP over TLS (and I must happily say that only very few email providers of mostly lesser reputation still allow unencrypted access).

I think you might really prefer to just get commercial ISM-band equipment to build a directive link in unlicensed spectrum (as opposed to spectrum you access under amateur license), even if that limits the available power (and thus the SNR, the thus the rate). Often, that's the cheaper choice, and sometimes even the faster: where I'm from, HAMNET, which is an internet-alike backbone access technology, is legally restricted to 5 MHz of spectrum in the 2.4GHz region, whereas plain WiFi uses 40 MHz. Sure, the Ham allocation allows higher powers, but as you can see from the formula above, you'd need 256 times the power of WiFi (at same noise level) to achieve the same as an eightfold bandwidth increase.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10141/what-are-the-maximum-possible-speeds-of-download-over-amateur-radio-frequencie, by user11905, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
