# Why did I lose my FM radio signal?

*Tags: propagation, rfi · score 4*

## Question

My lady and I were driving on the interstate recently when we noticed an unusual phenomenon. We were listening to the radio (an FM signal), and only over a couple of bridges did we entirely lose our signal. I had some ideas explaining this but I'm not sure, so I am asking for your help. What caused this?

To clear things up a bit:

- It happened over three bridges in a thirty mile stretch. Each was over a river (not sure if that matters for reasons of over-water architecture or aquatic radio effects), but we crossed several other bridges that did not cause this phenomenon.
- Our signal was excellent the whole drive except on these few bridges, when it suddenly disappeared (white noise) and reappeared immediately after crossing.
- The bridges were concrete with no supports from above, no street lights, etc. There was no difference in obstructions above the vehicle for the entire drive.
- I have spent a lot of time driving with the radio on and have never experienced such a loss of signal with no explainable obstruction. I can only assume that the construction of these few bridges is unique.

## Accepted answer (score 2, by Martin Ewing AA6E)

The likely source of this problem is not that the FM signal went away, but that it was overwhelmed by a local interference (RFI) source. Certain electrical systems, like high-intensity lighting, can generate a lot of "white noise" in the VHF range, including the FM broadcast band. It is quite possible that the bridges' lighting system (or some other electrical system) was active when you drove over.

You did not say what time of day was involved. You might notice whether the lights were on. The RFI problem would be worse for weaker FM signals. You might try tuning in other, more local (stronger) FM stations to see if they can get through the radio noise.

## Answer (score 2, by AG5CI)

You said that you just hear white noise and not man-made interference, so I think the most likely explanation for what you are seeing is that you are in a multipath null.

These occur when a signal arrives at your receiver via a direct path and a dominant reflected path of almost the same amplitude. When the total distance travelled by the reflected wave is a multiple of one-half wavelength different from the distance travelled by the direct path, the reflected wave will be 180 degrees out of phase and will cancel the direct path. It is possible that the reflection is coming from a body of water, which would explain why this is occurring only on a bridge.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5133/why-did-i-lose-my-fm-radio-signal, by Sam, Martin Ewing AA6E, AG5CI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
