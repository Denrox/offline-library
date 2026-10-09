# How to calculate power loss between radio and antenna

*Tags: antenna, rf-power, math · score 5*

## Question

I have a 5W HT that only kicks out about 1W by the time it hits my antenna (which I understand is the norm). How do I go about calculating power loss in various equipment?

## Accepted answer (score 4, by Dan KD2EE)

There are a few possibilities.

First of all, in larger assemblies (mostly important in repeater design) each component will have a parameter called insertion loss. This is the loss, in dB, through that componenet - the loss caused by inserting that component in your feed line. Filters have insertion loss, as do duplexers, and even inline wattmeters and adapters, although the last two should be pretty low. Typically this is about 0.5 dB for each filter or other component, at least in the installations I've seen.

Then you need to add in loss due to feedline. Different types of feed line have different losses at different frequencies. For example, to get the loss you've described (5W to 1W), and assuming a UHF HT in the 440MHz band, and 50 feet of RG-58 coax (a common small diameter coax) equates to about 5.6dB. This is a parameter that you would look up in a table or a graph from the manufacturer of the coax you're using.

You may also have some loss at the antenna itself. Especially "rubber ducky" antennas, which are electrically shorter than a true quarter wave antenna and compensated with loading coils, will have a certain amount of loss, also computed in dB. This basically accounts for the reactive and resistive losses in the antenna, decreasing the actual emitted power.

Finally, to calculate your actual radiated power, you can simply add up all these values. Every 3dB equates to cutting your signal in half, and 10dB equates to one tenth of your original power getting out. You would compute the actual power by multiplying your transmitter's power by $10^{(-\mathrm{loss~}(\mathrm{in~dB})/10)}$

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/406/how-to-calculate-power-loss-between-radio-and-antenna, by Dan, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
