# Losing Low Frequencies in AM transmission

*Tags: software-defined-radio, gnuradio · score 3*

## Question

I've been using a USRP software-defined radio to try to send an amplitude modulated signal to a very basic receiver, basically just a piece of wire as an antenna, over a very short distance. The signal, a wav file of me counting to ten, is transmitted clearly enough to be understood by a human, but not by a speech-to-text program. The received signal is also clearly much higher in frequency than the transmitted signal. I took FFTs(illustrations provided below) of the sent and received signals and it seems clear to me that the lower frequencies in the signal are not being transmitted as strongly. The solution I've been trying to work on is adjusting the signal I'm transmitting by amplifying the lower frequencies of the signal and attenuating the higher frequencies using Python to modify the original wav file. My question is whether this seems like a viable solution or not? Is it possible to make up for a transfer function that is making it difficult to transmit the low frequency parts of the signal by amplifying those parts of the signal in the file to be transmitted?

Here is the GnuRadio flowchart I'm using for the USRP transmission:

## Accepted answer (score 4, by Kevin Reid AG6YO)

You are not making an AM transmission, because you have not added a carrier. Without a carrier, what you have is *double sideband* (DSB) modulation, which will not be properly demodulated just by an improvised detector.

To create the carrier, **add a constant value** to the signal (between the Multiply Const and Float To Complex stages).

Constraints:


The carrier should be of greater amplitude than the peak level of the modulating signal, to avoid *overmodulation*.


You should also make sure that the final signal does not exceed a level of ±1, which would cause it to be clipped (distorted) by the USRP's DAC or a preceding float-to-integer conversion.

Together, these constraints mean that for best dynamic range your carrier should have a value of 0.5, and the input signal, if it had a maximum range of ±1 (which I believe is true for GR WAV sources, but your file may be significantly quieter), should be multiplied by 0.5, so that the resulting signal has a range of 0 to 1.

I would recommend visualizing your signal by adding a GUI FFT Sink in parallel with the UHD sink, to observe that it has the proper spectrum of an AM signal. If you wanted to simulate the effects of quantization and possible clipping, you could do so by converting the signal to short or byte and back before feeding it to the FFT sink.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5052/losing-low-frequencies-in-am-transmission, by pineapplevendor, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
