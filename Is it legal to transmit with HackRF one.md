# Is it legal to transmit with HackRF one?

*Tags: legal, fm, transmission, hackrf, germany · score 10*

## Question

Is it legal to transmit using HackRF one (in Germany), the purpose is to do some Lab research and Academic experiments.

for example i want to broadcast an FM signal using HackRF one and try to receive it using another hardware (RTL-SDR).

If no is there another legal alternative?

## Accepted answer (score 8, by Marcus Müller)

You'll need an *experimental radio license* (Versuchsfunk) from Bundesnetzagentur link for research operation.

For demonstration/teaching purposes, a *demonstration radio license* (Demonstrationsfunk für Bildungseinrichtungen) would be in order.

I'm not a lawyer nor have I ever applied for either of these; I'd recommend contacting BNetzA on these aspects. Whenever I contacted them, they were super friendly and swift.

A loophole here **might** (again, ask BNetzA if in doubt) be general low power transmitter licenses as used by e.g. the small dongles that you can plug into your iPhone to make your car stereo receive on FM what your phone is playing. I know that there's a pretty low power limit for these (nW range), but that might be perfectly suitable for your use case. What I don't know is whether the devices in question need to be type-approved (which would rule out the HackRF completely, as it can do **anything**) or whether guaranteeing that your device **won't** do anything bad is sufficient at these power levels.

## Answer (score 8, by hotpaw2)

As for other legal alternatives, one might be transmitting inside a suitably shielded Faraday cage. I’ve seen such facilities at labs where various prototype and pre-production (and competitors?) electronics systems were being tested to measure how far out-of legal compliance they were.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12046/is-it-legal-to-transmit-with-hackrf-one, by A.SDR, Marcus Müller, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
