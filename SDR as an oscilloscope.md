# SDR as an oscilloscope

*Tags: software-defined-radio · score 4*

## Question

Can a SDR be used as a general purpose AC oscilloscope with appropriate attenuation at the front end. Have in mind a capacitor to block DC voltages, large resistor say 10 Mohms to limit current and present a high impedance to a signal & a scope probe. Then would need software to convert quadrature signals in to a scope like signal on my computer screen.

## Answer (score 2, by Kevin Reid AG6YO)

I haven't looked into this concept myself, but here's some thoughts on problems you'll have:

The biggest architectural difference between a software-defined radio and a digital oscilloscope is that **a SDR usually has a downconverter in it**. This might be exactly what you want, if you want to bring a RF signal down to baseband and look at the waveform/modulation. But if you're looking for a general-purpose oscilloscope, this means you can't look at the original signal without frequency shifting it back up to what you *assume* is the correct frequency — and you will have lost phase information.

SDRs intended for LF-MF-HF usage will often omit downconversion (performing all frequency shifting in software). But you might find their frequency response cuts off too low, if your "AC" signals are low frequency as RF goes.

You also won't have any of the **input conditioning** of an oscilloscope front-end, unless you build a circuit for that. With your 10 MΩ series impedance — while the SDR is expecting a 50 Ω or 75 Ω input — you may find that you're picking up more signal from other sources than your probe input. (*May.* I'm not confident about this.) At a minimum, I'd expect it to function a lot better with a buffer amplifier (which would also give you a fairly good sacrificial component in case of bad input, if nothing else).

On the other hand, *displaying* the signal is no problem at all. For example, if the SDR you choose has a driver for GNU Radio, then you can launch GNU Radio Companion, connect the SDR source block to a scope block, and you can immediately see the signal. You can also add frequency shifts and other signal processing that might be useful.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14906/sdr-as-an-oscilloscope, by Roy Hopkins, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
