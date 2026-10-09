# Recomended coax for 100ft (2m/70cm)

*Tags: coaxial-cable, 2m-band, 70cm-band · score 3*

## Question

I recently moved to another house. My setup's current coax is 50ft/RG8x/PL259 (bought in 2018), but it is not enough for connecting my antenna to where I want to place the radio. I believe that 50ft more will be enough. Should I:

1. Buy an additional 50ft rg8x coax?
2. Buy an 100ft RG8x coax?
3. Buy an 100ft coax of "better" quality (RG8, LMR-240, etc.)?

My current home setup:

- TYT MD-9600 Dual Band DMR Digital Mobile Radio (UHF/VHF)
- Tram 1481 Amateur Dual Band Base Antenna

## Accepted answer (score 6, by rclocher3)

According to this online coax loss calculator, the loss of 50 feet of new Belden 9258 RG-8X with an antenna with an SWR of 1.5 is 4.29 dB at 450 MHz (UHF), so the loss for 100 feet of the same coax would be 8.6 dB. If you switched to fancier coax such as LMR-400, the loss for 100 feet of coax would be 2.8 dB.

So if you bought another 50' of RG-8X your coax loss would be 4.3 dB worse than it was before (plus a little more for the connector between the two 50' pieces). If you discarded the RG-8X and installed 100' of LMR-400, then your coax loss would be about 1.5 dB better than it was before.

How much difference would another 4 dB of loss make? (If you're unfamiliar with decibels, see [How big is a decibel?](How%20big%20is%20a%20decibel.md).) 4 dB is less than an S-unit (6 dB), if you're familiar with operating on HF. If you were mainly connecting to repeaters and had good strong signals from those repeaters before, then you probably wouldn't notice another 4 dB of loss when connecting to those repeaters. If you talked to simplex stations with weak scratchy FM audio that you could barely copy before, or digital stations that were right on the edge of the "digital cliff", then you might not be able to copy similar stations if your coax had another 4 dB of loss.

Mind you, these calculations are for the 70cm band. You'll have a lot less loss at 2m.

Another factor to take into consideration is that the rule-of-thumb I was taught is to replace coaxial cable roughly every ten years. Your existing cable already has three years or so in it.

TL;DR if you talk mainly to repeaters, another 50' of RG-8X would probably be fine. If you like to work weak stations on UHF, consider upgrading your coax.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18301/recomended-coax-for-100ft-2m-70cm, by KP4MCG, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
