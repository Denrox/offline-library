# How to use GNU Radio to demonstrate FM demodulation without baseband signals

*Tags: software-defined-radio, gnuradio, fm · score 3*

## Question

Using GNU Radio, I'm currently trying to create a flow graph containing a simple demonstration of how FM modulation and demodulation works. Since the target audience is not accustomed with complex baseband representations, I'm trying to do so relying only on real-valued signals.

Obviously, what I'm trying to do is clearly not the intended way to use a SDR tool, and it comes as no surprise that most blocks available in GNU Radio take complex signals as inputs.

Fortunately, producing an FM modulated signal is pretty easy:

As can be seen in the plots, everything works as expected:

However, I'm having trouble creating an FM demodulator. I've tried to implement a PLL-based demodulator but GNU Radio does not allow loops to happen outside of blocks, and I've tried using the PLL blocks that GNU radio provides by only inputting real part and zero imaginary part. I've also tried many other things, including trying to convert the passband FM signal to a complex baseband representation (something which I'm trying to avoid) before using the FM demodulation block, but without success.

Given the above, is there actually a way to do FM demodulation within GNU radio (any technique will do) while avoiding complex baseband representations?

## Accepted answer (score 2, by hobbs - KC2G)

Maybe a slope detector could work? GNU Radio supports real-valued filters (using the Decimating FIR Filter block, or one of the convenience wrappers like High Pass Filter). There's no real envelope detector block, but the "RMS" block comes pretty close to being a combined envelope detector + lowpass, or you could write your own in Python.

Obviously it's not going to be great but you should be able to get some intelligible sound out of it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21756/how-to-use-gnu-radio-to-demonstrate-fm-demodulation-without-baseband-signals, by JMaravalhasSilva, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
