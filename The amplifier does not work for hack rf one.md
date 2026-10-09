# The amplifier does not work for hack rf one

*Tags: amplifier, equipment-troubleshooting, hackrf · score 3*

## Question

Good day! I ask for help with repairing the hackrf one amplifier. Doesn't work at all. Accepts signals without amplifier, and LNA and VGA adjustment in SDR sharp works too! But when I put a tick on "Amp", then all signals disappear. As I understand it, I punched through the static through the antenna input. This is not a program error for sure, since I checked it both on the phone and using a portapack. Everywhere the result is the same - I turn on the amplifier - the signal disappears. At the same time, I tried to transmit signals. Everything works for the transfer. I ask for help in identifying the faulty part. I want to renovate. After reading this article https://pc7x.net/archive/mirrors/hackrf-repair/articles/repairing-the-hackrf/index.html, I realized that most likely my LNA chip (U25 in the diagram) burned out. But after all, the LNA gain control works for me. How so? This article also describes that switches U14 and U12 can be broken. Tell me how to determine what is broken, please.

## Accepted answer (score 0, by Антон)

After a few years, I can write an answer. I solved the problem by replacing the amplifier for the U25 transmitter and the amplifier for the U13 receiver. These are identical chips. They are labeled **81J**. Я заменил на **81R** Just because I had them. These are microchips **MGA-81563**.

## Answer (score 4, by Radio Blogs)

HackRF has three amplifiers in the receive section. The first is a low noise amplifier (LNA) with fixed gain of 14 dB. The second is an Intermediate Frequency (IF) LNA with gain that varies from 0 to 40 dB. Finally, the baseband amplifier gain can be varied from 0 to 62 dB. On the transmit side, there are two amplifiers. The first is an IF LNA with gain that can be varied from 0 to 47 dB. The second amplifier has a fixed gain of 14 dB.

The first amplifier in the receive and the last amplifier in the transmit sections can be switched in and out of the chain. The designers of HackRF picked the same component MGA-81563 with Gain 14 dB, for both these amplifiers. As it turns out, this amplifier component is very susceptible to damage – even when the maximum input signal level of +13 dBm is not exceeded. This has been reported by a number of users. So you will have to indeed confirm that the first LNA is damaged (it often is) and then repair it. More details including a block diagram of the front-end are in the link below. The only issue is that the LNA itself is now obsolete as the manufacturer has stopped making this amp so you have to find one either on amazon or ebay. I think it would be a good idea for the team at HackRF to solve this problem though as there are many good wideband LNA alternatives out there.

## Answer (score 3, by hobbs - KC2G)

There are *three* receive gain stages in the HackRF one. Two of them are on the MAX2837 chip (the ones controlled by "LNA gain" and "VGA gain"), and the third is the MGA81563 preamp, which is either on (+14dB) or off (+0dB), and controlled by the "amp" toggle. You have indeed blown the MGA81563. I did the same thing to one of mine several years back and it behaved exactly the way you described.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18523/the-amplifier-does-not-work-for-hack-rf-one, by Антон, Radio Blogs, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
