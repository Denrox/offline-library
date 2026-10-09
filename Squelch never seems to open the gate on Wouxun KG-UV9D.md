# Squelch never seems to "open the gate" on Wouxun KG-UV9D

*Tags: ht, equipment-troubleshooting, squelch · score 5*

## Question

I just got my Technician's license a few weeks ago and I'm trying to figure out if this is user error or if I need to return my radio.

My understanding of squelch is that when the received signal strength exceeds the squelch threshold the radio starts playing the audio for whatever it is receiving. When I have the squelch set to '0' I get a ton of static as well as hearing anyone who is talking from the repeater and the green RX light on my HT lights up solid; as expected. However, if I set the squelch to '01' then I get nothing at all.

At first I just assumed that my dinky HT just couldn't get a very strong signal from the repeater and was unable to distinguish the activity from the static. However, I noticed that sometimes when the squelch was turned up a notch that I would see the green RX light illuminate for significant stretches of time. If I turn the squelch back down to '0' I was able to confirm that there were actually people talking.

It seems to me that these signals shouldn't cause the light to illuminate unless the radio is receiving something over the squelch threshold. This leads me to suspect that when squelch is set to a non-zero value it is failing to actually activate the speaker when the signal is strong enough and I have a faulty device.

Am I missing something here?

## Answer (score 4, by Kevin Reid AG6YO)

I'm not familiar with the exact behavior of that model of radio (and the manual was not very helpful), but a *possible* explanation in general is that you have CTCSS/DCS squelch enabled, and the repeater is not using the same tone/code.

However, for this to match the observed behavior it would have to be the case that a squelch setting of '0' disables tone squelch as well as power-based squelch. If that's true, then what you're seeing is:


When you disable squelch entirely, you can hear the signal.


When the squelch is on, the RX light is telling you that there is a signal meeting the power squelch criterion (so the receive circuit is active) but it isn't meeting the CTCSS/DCS criterion (so there is no audio).

In order to fix this, you need to make one of two changes to the radio settings. I can't advise you on how to do this because I couldn't make enough sense of the manual at a quick skim.


Disable CTCSS/DCS squelch. Then the squelch will work as you describe in your question.


Enter the CTCSS tone or DCS code actually used by your repeater, so that it can activate the squelch.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5995/squelch-never-seems-to-open-the-gate-on-wouxun-kg-uv9d, by Matt KI7CMZ, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
