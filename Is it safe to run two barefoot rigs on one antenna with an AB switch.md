# Is it safe to run two barefoot rigs on one antenna with an AB switch?

*Tags: rf-power, antenna-system, equipment-operation · score 6*

## Question

I have a Daiwa CS-201A two position switch. The single side is connected to by quarter wave vertical (40m). The A and B sides are connected to an IC-7300 and TS-830S.

The switch is claimed to have 60dB of isolation. It also shorts the unused port to ground.

If I transmit 100W (50dBm) from the TS-830S to the antenna, am I correct in that about -10dBm will leak to the other side into the IC-7300?

I tried it and saw about +40 over S9 on the 7300. The service manual for the 7300 says never give it a signal over 20dBm (0.1W).

Am I safe doing this? How can I tell if it’s too much?

UPDATE: I did some testing with an Elecraft XG3 signal source. It produces signals at -107dBm (1uV), -73dBm (S9), -33dBm (S9+40), and 0dBm.

Following the instructions using the 1uV signal and a DMM on the speaker output, the MDS is around -135dBm and -142dBm with the preamp off and set to 1, respectively.

Also, the -73dBm signal is showing just shy of S9 on the S meter. That worried me a little, but I saw in the August 2016 QST magazine article that the ARRL test showed an S9 with a 70uV signal. So there's an error of about 3dB (which is also the S unit increment on this rig's meter).

So I think my receiver is still okay.

I also tested the isolation of the switch by hooking the 7300 to port A, the signal generator to port B, and a dummy load to the common port. With switch in the B position (allowing a direct path from the signal generator to the dummy load), I set the signal output to 0dBm and noted the S meter deflection on the 7300. It was around S5.

I don't know exactly what signal level that is, but it's less that what it read when I fed -73dBm directly into it. So even if we overestimate the received signal at -73dBm, that's still at least 73dB of isolation- if I'm thinking this through correctly. This was done on at a frequency of 7.020MHz. I think the switch claims an isolation of 60dB at 600MHz. It appears the isolation improves as you go down in frequency.

Added a bounty for feedback on the tests and the data. Is it really possible for the switch to have that good of isolation? Is there anything else I should look into? Do the tests seem valid? Am I in the clear running two rigs on this switch?

## Accepted answer (score 4, by Aleksander Alekseev - R2AUK)

S9 corresponds to 50 microvolts or -73 dBm. Thus S9+40 is -33 dBm. In theory, since it's much less then 20dBm your 7300 should be fine. HOWEVER I believe that +40 is just a maximum level your transceiver can show. Given that the attenuation of your switch is 60 dB and you are using 100W (50 dBm), -10 dBm will leak. It's much more than -33 dBm but you are still in the safe range.

From personal experience I used a DIY switch with measured 58.7 dB attenuation in the same manner with a 100W transceiver and an RTL-SDR, which maximum input is 10 dBm. RTL-SDR showed a large signal level as well, but worked just fine.

This being said I wouldn't recommend to trust the manufacturers claim regarding the attenuation level of the switch. It's always a good idea to measure it using a **low-power** signal generator (if you don't have one you can solder a simple Clapp oscillator) and an oscilloscope (or your transceiver).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13125/is-it-safe-to-run-two-barefoot-rigs-on-one-antenna-with-an-ab-switch, by Paul, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
