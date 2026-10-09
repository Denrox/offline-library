# Transmitting Offset for sats

*Tags: satellites · score 3*

## Question

I found some pages on info for satellites, and I got different results. Some said to shift the transmit frequency as well as the receive, some said to keep the transmit the same, but shift the receive during the pass, I am confused on what I should do.

Here is one for UO-14

and here is one for SO-50

Notice one of them shifts the receive frequency as well as the transmit, and the other only shifts the transmit.

## Accepted answer (score 5, by Adam Davis)

The reason you don't need to shift one frequency is that the Doppler shift for the 144MHz band, for a satellite in this orbit, is only about 2-3kHz, which is within the range needed to make contact without adjusting. You can, and you'll get better results if you do, but to make satellite operation easy many do not.

The 440MHz band, however, experiences a Doppler shift of 10kHz, which means that the beginning and end of the pass will fall outside the bandwidth allocated if you don't adjust.

The higher the frequency, the greater the Doppler shift. It's relative to the frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1522/transmitting-offset-for-sats, by Skyler 440, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
