# What limits a PIN diode or varicap from being used in a "Software Defined [Radio] Filter"?

*Tags: software-defined-radio, equipment-design, filter, capacitance · score 9*

## Question

A PIN diode varies its capacitance based on a DC bias, and a Varicap exhibits this effect even more clearly. What limits the use of "solid state variable capacitors" like these for dynamically filtering (low power/received) RF signals?

The question at change LC parameter digitally is related, but was asked in the context of a tunable **oscillator**. That is already a ± "solved problem" in the SDR world. What would be useful in conjunction with a DCO that can operate in a 24–1766 MHz range would be a correspondingly flexible bandpass filter to limit receiver overload/aliasing!

## Accepted answer (score 13, by Neil_UK)

What limits the use of "solid state variable capacitors" like these for dynamically filtering (low power/received) RF signals?

The main issue is bandwidth.

Although there are some varicaps that claim a 10:1 variation (or more) in capacitance, not all of this is useable. One end of the range may be low Q, or have a very steep curve. Once you have a varicap on a board, with pads and bias connections, you'll often find that the useable capacitance swing at the tuned circuit is no more than 4:1, giving you only 2:1 swing in centre frequency.

Even if you did have a varactor that gave you more swing, or a construction technique that reduced the effect of strays, changing the LC ratio alters the impedance of the filter. There's only so much change you can make to the impedance of the resonators before a good filter becomes a bad filter.

You may only want to operate in an octave. However you've asked specifically about SDRs, and the main benefit of those is a very wide frequency range.

You could switch inductors into the filter, with the switching strays further reducing the capacitance swing available. Or you could build multiple filters and switch between them. Both of these add to the complexity. Once you have accepted the complexity of further switching, it often makes more sense to build a few, good, fixed frequency filters with stable components and switch between them.

## Answer (score 6)

Nobody mentions distortion (IM2 and IM3) of PIN diodes and varicap diodes. Tuning (center frequency) limitation range, required band switching and further requirements. Best solution is to start with a good system that can handle the dynamics without filtering. As W8II Phil Frost proposes.

** Mentioned Q-factors (Brian K1LI) of 1000 are not feasible in a normal receiver and not necessary. Filter Q_loaded of 100 is practical; then unloaded Q is not necessary to be higher than 250. **

## Answer (score 6, by Brian K1LI)

Technically, the utility of a variable capacitor in a receive filter depends on the amount of available capacitance variation and its *Q* - the quality factor, which is the ratio of the capacitor's reactance at the operating frequency to the series parasitic resistance. (In some applications, parasitic series inductance may also be a factor.) Commercially, price is a primary concern.

Fixed-value ceramic chip capacitors commonly have a *Q* value of 2000 or more and, obviously, no variability - at a *very* low unit price. Perusing an online distributor's catalog, I see varactor diodes with capacitance ratios of around 10:1 down to around 4:1, some with *Q* factors over 1000 but most with *Q* factors in the hundreds or less - and with prices of 15X to 150X that of a fixed cap.

When taken together, fixed-value capacitors deliver the needed cost-performance balance for all but a small fraction of all such applications.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18255/what-limits-a-pin-diode-or-varicap-from-being-used-in-a-software-defined-radio, by natevw - AF7TB, Neil_UK, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
