# Powering transceiver and SWR/power meter from same supply?

*Tags: transceiver, swr-meter, power-supply · score 6*

## Question

I'm mostly sure this will be ok, but I'd like to confirm.

I have a switching power supply (can't remember the model right now, but it's for ham use, 13.8V/30A) and I'd like to power both the FT-857D as well as the power/SWR meter from it.

Is there any reason I shouldn't do this?

## Accepted answer (score 5, by Glenn W9IQ)

This should not be a problem at all. It is commonly done this way. Hopefully the switching supply has been designed for ham radio use. If not, you may find some "birdies" on your receiver which are remnants of the switching frequency of the supply getting into your receiver and potentially interfering with desired signals or simply causing annoying tones (thus "birdies").

A good safety practice is to have a low amperage (~1 amp) fuse on the outlet of the power supply to which the SWR meter positive wire is connected. This prevents overheating the wires and risking a fire in the event of a short circuit somewhere downstream.

Your transceiver power cable probably already has in-line fuses to protect it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10156/powering-transceiver-and-swr-power-meter-from-same-supply, by Rimio, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
