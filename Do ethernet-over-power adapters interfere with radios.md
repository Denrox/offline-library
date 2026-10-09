# Do ethernet-over-power adapters interfere with radios?

*Tags: rfi · score 7*

## Question

I remember not long ago seeing a lot of chatter in the ham community about large-scale "Broadband over Powerline" (BPL) systems causing harmful interference across several bands. Does similar interference happen with SOHO "Ethernet over Power" (usually called "HomePlug") networks?

HomePlug networking is a convenient way to extend home computer networks, when WiFi is impractical or undesired, without having to run cables across the house. However, I would not want to recommend this to anyone if it is a known RFI offender.

If these devices are known to cause RFI, is there anything the end-users can do to reduce or eliminate their impact without having to actually replace them?

## Answer (score 4, by Scott Earle)

There has been an ongoing debate about this in the UK, where the system is called PLT for "Power Line Telecommunication".

See articles on The Register (slightly sarcastic tech news site) for more on the subject. Two such examples are here and here. Of course the general feeling the manufacturers are trying to engender is one of the Luddite radio hams being stuck in their ways and trying to stand in the way of progress, and my feeling is that they are succeeding in this goal.

It has been proven to exceed the level of radio emissions allowed by the relevant EU regulations, but equipment is still being manufactured, sold, installed and used.

Yes, it interferes with HF. No, the regulatory bodies don't seem to care.

## Answer (score 2, by Koos van den Hout)

Short answer: Yes.

Longer answer: Homeplug devices use HF frequencies (0-30 MHz) to transport data. Active networks cause a lot of noise, idle networks will cause a recognizable ticking sound. "Good" homeplug devices have specific notches for air traffic control, shortwave broadcast and amateur frequencies. I have tested this myself with a Devolo interface and visualized the results with Gqrx at To my shame as a radio amateur I must admit I still use a PLC (ethernet over powerline) connection in my home network (the devices are now gone). A clear notch for the 20 meter band, but serious amounts of noise outside that band.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2032/do-ethernet-over-power-adapters-interfere-with-radios, by KJ4JTN, Scott Earle, Koos van den Hout. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
