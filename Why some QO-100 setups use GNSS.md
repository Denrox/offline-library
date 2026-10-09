# Why some QO-100 setups use GNSS

*Tags: satellites, gnss · score 3*

## Question

I'm looking into building a QO-100 setup, but am struggling to find good/easy to understand resources for beginners which would outline the most common approaches and their pros/cons. From what I could gather, there seem to be two main approaches:

1. Use an SDR for RX on ~700Mhz coming out of LNB. TX on 70cm and up-convert to 2.4GHz
2. For RX, use down-converter from ~700MHz coming out of LNB to 2m band, fed into the radio. On TX, same as first approach (TX on 70cm, up-converted to 2.4GHz)

After looking at some existing implementations, I found that some also use a GNSS module to supposedly synchronize some frequency.

1. What frequency is GNSS synchronizing?
2. Why is it a GNSS module and not something simpler, like a crystal oscillator? GNSS feels like complete overkill, if the only goal is to provide an external frequency reference.
3. Why do some setups use GNSS and others don't?

**EDIT:** Here are a couple setups I found are using GNSS for the frequency reference:

1. https://dxpatrol.pt/produto/new-dxpatrol-qo-100-groundstation/
2. https://www.dd1us.de/Downloads/Portable%20station%20for%20QO-100%20English%202020-09-26.pdf

## Accepted answer (score 3, by Dieter Vansteenwegen)

*I'm not an expert*, but to expand on the answer from @Marcus Müller: the GNSS input is used to compensate (or "discipline", hence "Disciplined Oscillator") an internal frequency reference, often a quartz crystal. The output from the crystal is compared to a frequency distilled from the GNSS signal (which itself is based on an atomic standard inside the SV), leading to a much more accurate reference. So:

1. What frequency -> One of the frequencies used internally. Often test equipment has a 10MHz (or 5MHz on older equipment) reference input for the same reason.
2. Why GNSS -> The GNSS signals are based on atomic clocks in the satellites and are free to receive using a "simple" GNSS receiver. Why not use them?
3. Why some and not others: those using GNSS signals as reference are more accurate and stable but more complicated than those relying on an internal quartz crystal. An internal high quality frequency reference is possible as well, but GNSS modules are readily available and quite cheap.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21570/why-some-qo-100-setups-use-gnss, by Tadej Gašparovič, Dieter Vansteenwegen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
