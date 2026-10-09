# Troubleshoot ICOM IC-745 intermittently shows no power on transmit

*Tags: hf, rf-power, icom, equipment-troubleshooting · score 3*

## Question

I have an old IC-745 I bought used last year. Recently it seems to be malfunctioning intermittently. It is receiving well on all bands as far as I can tell. Sometimes when transmitting, there is no RF power shown on the meter. I've tried the built in SWR meter when this happens, and there is no movement of the needle when I adjust the RF power with the meter in SET mode. My NanoVNA shows an SWR of < 1.1 on the frequencies I'm using (40m, 20m), so there doesn't seem to be any problem with the antenna.

The transceiver has seemed to work well (aside from being noisy, which is probably due to living in a city). I've received good signal reports since this began, but have only tried when the meter is working and showing a low SWR.

What's the best way to troubleshoot? I'm guessing the first step is to figure out whether the problem is actually low power or just a bad meter? I don't have an HF wattmeter, but have ordered one. I do have an oscilloscope and NanoVNA. Any suggestions on what this could be and how to troubleshoot?

## Answer (score 6)

Without any radio shack tools? Connect a bulb to the antenna output to indicate RF. Two times 12 volt 5 Watt in series (rear light of car bulb) can indicate RF. Reduce RF power before hitting the TX-button.

Problem is similar (looking) to the problem with an IC-720 that I owned. Reason was the rotary switch used for the band pass switching. Poor contacts. The built-in program, in the IC-720, was a cleaning sequence. Rather annoying rattling sound. That should stop after 30 seconds maximum.

In my 720 there was no RF in some cases, just as your description. Most of the time it was possible to recover from that by manually selecting another band: the rotary switch was forced to move and did work at the second or third attempt.

When the 745 has a similar switch than it must be cleaned. But the Icom is a service-unfriendly construction... Succes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18165/troubleshoot-icom-ic-745-intermittently-shows-no-power-on-transmit, by elplatt. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
