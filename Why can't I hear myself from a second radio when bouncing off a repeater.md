# Why can't I hear myself from a second radio when bouncing off a repeater?

*Tags: repeater · score 12*

## Question

I am a relatively new ham, and haven't joined any club yet or participated in any nets. I have, however, hit a repeater just to know I can do it. I was told my sound was scratchy (no surprise there) but I want to hear how bad it is. I tried listening to myself from a second radio, but didn't hear anything.

**My setup:** A BaoFeng UV-5R connected to the antenna through a 25 ft cable. The antenna is a Tram 1185 Amateur Dual-Band Magnet Antenna or something similar, and is mounted on my roof about 20 ft above the ground. I'm broadcasting at 5W, and I know the radio is set up correctly because I've had people respond to me.

**What I did:** In the evening when the repeater was free, I keyed up on the BaoFeng, while listening to another 5W handheld with a rubber duck antenna nearby. The second radio didn't make any sound until I stopped broadcasting, then both radios played the beeps from the repeater indicating the end of broadcast. This is on the 2m band, and the repeater has a 600kHz offset.

**What I think is going on:** My guess is that my broadcast is so close to the second radio that it is hurting my SNR to the point where the second radio can't isolate the signal on the frequency it's listening on. Is that because my cheap BaoFeng is transmitting spurs or other out-of-band noise? Is it because the other handheld isn't filtering out noise well enough? **Is this something common when radios are so close, or is it specific to my equipment/setup?**

## Accepted answer (score 12, by Glenn W9IQ)

You are experiencing what is commonly called desense (short for desensitization). The strong signal of your transmitter overloads your receiver making it unable to demodulate the much weaker, on-channel signal.

If the filters throughout the radio provided a much narrower bandwidth, this effect would be mitigated. But front end filters with less than 600 kHz bandwidth are not practical for an ordinary radio. On a 2 meter repeater, for example, such filters consist of 4 to 6 "cans" that are each 8-12 inches in diameter and ~24 inches tall. This allows the repeater transmitter and receiver to share an antenna while operating on 600 kHz spacing.

You may have some success by reducing your transmit power to the lowest level needed to hit the repeater. Separating the radios further, coax cables and antennas can also bring a measure of improvement.

## Answer (score 3, by mike65535)

Even driving too closely to another ham operating similarly to your scenario can do the same.

Say you and a ham buddy are talking to one another from your cars using a repeater, and you drive to the same place to meet. As your cars approach each other, his TX will overwhelm your RX (and vice versa) and you will experience the same problem.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10211/why-can-t-i-hear-myself-from-a-second-radio-when-bouncing-off-a-repeater, by Bernem-KG7NUB, Glenn W9IQ, mike65535. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
