# Steps for eliminating RF interference

*Tags: rfi · score 3*

## Question

I built a little USB dongle I put on my radio. This dongle interfaces audio and PTT to my radio so it can use AllStar link.

The problem is interference. When the radio transmits, I heard a high pitch squeal as well as a lower frequency hum that is not present in the audio when the radio was not transmitting. I shielded the device and put RF chokes on every pin in and out of the device, and that fixed the squeal, but there is still a lower pitch hum coming through the audio port. I confirmed it wasn't the power supply by giving the radio a dead key without the audio in.

What steps can I take to find the problem with the RF interference and eliminate the noise on the transmitters audio?

## Answer (score 2, by rclocher3)

Your problem could easily be a ground loop. In this scenario, your computer and your radio are at different RF or DC potentials, and current is flowing on the ground line of your audio or PTT connections between the computer and the radio; the flowing current causes noise.

So how to diagnose whether you have a ground loop? One way could be to power both the computer and the radio with batteries, which would break ground loops that go through the power lines. If the noise is reduced, then that would make a ground loop look like the problem.

Many "sound card" interfaces between radios and computers eliminate ground loop issues through complete galvanic isolation. In other words, there is no direct electrical connection between the computer and the radio. The audio goes through an isolation transformer, the PTT goes through an optical isolator (an LED and a phototransistor in the same component package), and the grounds of the radio and computer aren't connected. You could try that.

Another possibility could be common-mode currents on your antenna feedline coupling noise into the radio. If that were the case, then you'd likely hear the same noise when using a microphone to key the radio though.

Yet another possibility could be RF getting into your circuit through incomplete shielding. You say the box is shielded, which is good, but are you using shielded cables? Twisted-pair might not be enough.

Good luck.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3755/steps-for-eliminating-rf-interference, by Skyler 440, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
