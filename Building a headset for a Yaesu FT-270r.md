# Building a headset for a Yaesu FT-270r

*Tags: diy, ht, yaesu · score 3*

## Question

I'm trying to build a headset for my Yaesu FT-270r, which replaced a FT-250r. I had a working setup with the FT-250r. An electret microphone element connected to the MIC/PTT pin of the four-way connector, and a 2k2 resistor with one end connected to MIC/PTT pin, and the other end to the PTT switch and then the other side of the switch to ground.

The problem I'm having with the 270 is that if I just have the mic element across the MIC/PTT pin and ground, it activates the PTT regardless of the state of the PTT switch. If I add enough series resistance that merely connecting the mic element does not activate the PTT, then the PTT switch works correctly.

However, with enough series resistance that the PTT switch needs to be pressed to activate the PTT, I'm getting no (or maybe very low) audio. If I don't use the series resistor, I get good audio, but of course that's not much use if I'm transmitting all the time.

Maybe I'm doing something wrong, but it's such a simple circuit, and I re-built it from scratch after the first version didn't work. So I'm a bit perplexed.

Is anyone aware of a difference between the 250 and the 270 in this area? Any other ideas?

## Answer (score 2, by Kevin Reid AG6YO)

This sounds very similar in interface to the FT-60, which I recently prototyped such an adapter for.

Try **putting the microphone and PTT switch in series**. This is how the MH-37A4B earbud headset for the FT-60 seems to be wired, and ensures that the resistance is high when PTT is not engaged.

In my case, I then found I had to add *parallel* resistance (2.2 kΩ, not rigorously chosen) across the element to engage PTT, which will also of course reduce the audio level, but may be better than what you are trying.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6834/building-a-headset-for-a-yaesu-ft-270r, by KV6M, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
