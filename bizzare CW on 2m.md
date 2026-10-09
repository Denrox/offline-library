# bizzare CW on 2m

*Tags: cw, 2m-band, signal-identification · score 5*

## Question

I'm currently in Kershaw, SC. Yesterday an automated signal popped up on a 2m simplex freq (147.455 MHz) and has been running since. It sounds like Morse, but it is random letters that don't seem to have any repeating pattern. After every seeming CW letter there's a kerchunk like a repeater tx closing. Online I find no 2m beacons above 144.xxx and no repeaters on this freq. The signal has a very wide bandwidth. My 2m handheld picks it up from 147.450-147.465 and my scanner picks it up well below that and into the 148.xxx range.

Any ideas what this is and what would be transmitting such a signal? I have audio recorded if that's helpful, but this forum doesn't seem to accept attachments.

UPDATE: Origial, and still clearest freq is 147.455. I connected it into fldigi and I get three simultaneous signals in the waterfall at 800hz, 1600hz, and 2400hz. They wander a bit, but stay pretty tight to those spots. I'm picking up the same signal elsewhere too. I've found it on other freq in 2m and I just picked it up on 10m at 28.565.

UPDATE: Here's a link to the audio file on google drive. https://drive.google.com/file/d/1l88BO4wetOJz8nKgb7GbVS2H4krB9BE9/view?usp=sharing

Update: Got on an old radio scanner and found the same signal on multiple frequencies. If anyone is within a couple hundred miles of Charlotte, NC and has a 2m directional antenna, or knows another ham in that area who does, I'd appreciate comments below with Rx grid square and bearing to signal for any of the following. Signal clearest to me: 147.455 Simultaneously transmitting at: 146.005 146.665 147.565 (this is an open carrier, but has the same characteristics, so I suspect it is part of it.) 147.590 Then we exit the 2m band: 148.865 149.295 149.720 150.8825 151.5575 For reference, a station in Spartanburg, SC picked up the signal weakly at 147.455 from a 9e yagi on a 100' tower bearing about 60 deg.

Someone posted the same signal on reddit at the same freq (147.455). Has been picked up in Greenville SC, Cheraw SC, Columbia/Lexington SC, and Ashville NC. That's a 2m signal covering hundreds of square miles. That shouldn't be possible. https://www.reddit.com/r/signalidentification/comments/r856eb/i_found_this_centered_around_147450_and_147455/

If anyone in the Northern SC or Southern NC area has a 2m yagi and can provide an Rx grid square and a bearing on any or all of these frequencies that would really help me triangulate an area that can be narrowed down. Priority is 147.455.

## Answer (score 2, by rclocher3)

Listening to your recording, some of the Morse characters aren't even legitimate for the US, e.g. ··––. The timing seems fairly regular, meaning that the characters seem formed by a machine and not by someone at a straight key, but the timing isn't quite correct. The tone is quite buzzy with square-wave-like harmonics.

I'm just speculating blindly, but to me the most likely scenario is a misguided hobbyist who wrote an algorithm to string dots and dashes together randomly, built a primitive audio oscillator, and connected it to a primitive homebrew transmitter. Maybe there is no proper FM modulation of an audio input, and the transmitter is only capable of transmitting badly-modulated buzzy tones. One wonders why someone would do such a thing: maybe just to puzzle people, or to brag about having the skills to do it.

If the transmissions are ongoing, it wouldn't be difficult to use direction-finding techniques to find the transmitter. That might allow you to knock on the operator's front door and ask them how and why, and of course gently ask them to please stop the illegal transmissions. A directional antenna is helpful, but not necessary: just holding an HT close to the torso to attenuate signals coming from behind, and then rotating around, can provide enough directionality to locate the signal. What really helps is a receiver with a signal strength indicator, and an attenuator; otherwise finding the direction when one is close to the transmitter is difficult, because the signal seems equally strong in all directions. It's quite likely that people in your local ham club have the necessary equipment and experience, so you might consider asking them for help.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20148/bizzare-cw-on-2m, by Aaron, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
