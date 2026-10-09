# Relations between bit rate, frequency deviation and channel filter bandwidth

*Tags: uhf, transceiver · score 4*

## Question

I just started using a couple of low power radio modules in my project (HopeRF RFM69HCW). I made them work; they successfully transmit messages in a limited range (5-10 meters). Now I would like to improve that range (with a minimal message loss).

My problem is choosing the Bit rate, the frequency deviation, and the Rx Bandwidth for the channel filter (the settings I'm currently using are quite random: Br=19600, Fdev=2*Br, RxBw=Br). So I went on the web looking for a good-looking function describing the relationship between these three parameters and the transmission range, looking forward to writing a function like setBitRate(unsigned int x) {Br = x; Fdev = func1(x); RxBw = func2(x);}.

Instead of that, documents explaining the meaning of those parameters aside (very interesting but often too complex for me, specially those concerning the channel filter), I found some (not many) configuration tables, like this one in the source of the RadioHead RFM69 library (I'll only reproduce a fragment of it here; in this case RxBw is set implicitly and therefore not showed in this list):

```
FSK_Rb2Fd5 = 0,    ///< FSK, Whitening, Rb = 2kbs,    Fd = 5kHz
FSK_Rb2_4Fd4_8,    ///< FSK, Whitening, Rb = 2.4kbs,  Fd = 4.8kHz
FSK_Rb4_8Fd9_6,    ///< FSK, Whitening, Rb = 4.8kbs,  Fd = 9.6kHz
FSK_Rb9_6Fd19_2,   ///< FSK, Whitening, Rb = 9.6kbs,  Fd = 19.2kHz
FSK_Rb19_2Fd38_4,  ///< FSK, Whitening, Rb = 19.2kbs, Fd = 38.4kHz
FSK_Rb38_4Fd76_8,  ///< FSK, Whitening, Rb = 38.4kbs, Fd = 76.8kHz
FSK_Rb57_6Fd120,   ///< FSK, Whitening, Rb = 57.6kbs, Fd = 120kHz
FSK_Rb125Fd125,    ///< FSK, Whitening, Rb = 125kbs,  Fd = 125kHz
FSK_Rb250Fd250,    ///< FSK, Whitening, Rb = 250kbs,  Fd = 250kHz
FSK_Rb55555Fd50,   ///< FSK, Whitening, Rb = 55555kbs,Fd = 50kHz for RFM69 lib compatibility

```

I did try to understand it's logic, but I couldn't. For instance, why does this list suddenly change from Fd = 2*Rb (until line 7) to Fd = Rb (from line 8)?

I found different lists, whit different parameters, but I never found a logic behind them. Does a (even complex) function which relates bit rate, frequency deviation and channel filter bandwidth exist? Or where all these settings likely found experimentally? Am I trying to relate unrelated settings (I admit that I have a poor understanding of them, especially of the third), or am I forgetting some strongly related ones?

## Answer (score 2, by Glenn W9IQ)

There are two primary theorems that come into play to address your question - the Nyquist theorem and the Shannon-Hartley theorem.

**Nyquist**

The Nyquist theorem defines the maximum channel capacity for a *noiseless* channel. His formula to express this is:

$$C=2B\log_2{M} \tag 1$$

where C is the channel capacity in bits per seconds, B is the maximum bandwidth of the channel in Hertz and M is the number of signaling values (2 for binary, 4 for QPSK, etc.)

This formula suggests that we could simply keep increasing the number of signal values and the channel capacity would increase *ad infinitum*. But no real world channel is noiseless so ultimately noise becomes the limiting factor. This is where the Shannon-Hartley equation becomes important.

**Shannon-Hartley**

The Shannon-Hartley theorem describes the maximum channel capacity based on the signal to noise ratio of the channel:

$$C=B\log_2{(1+S/N)} \tag 2$$

where C is the maximum channel capacity in bits per second, S is the signal power, N is the noise power, and B is the channel bandwidth in Hertz.

We can see that the Shannon theorem therefore places an "upper bound" on maximum channel capacity based on the signal to noise ratio of the system and the bandwidth of the channel. For example, with a 30 dB signal to noise ratio (a linear power ratio of 1000) and a 3 kHz bandwidth, the maximum channel capacity is ~30,000 bits per second. If we can improve the signal to noise ratio to 40 dB (a linear power ratio of 10000), the maximum channel capacity rises to ~40,000 bits per second.

**Application in RF Systems**

As the distance between the transmitter and receiver is doubled, the received signal strength is quartered while the noise power remains the same (provided there are no noise sources that come into closer proximity as a result). Thus the signal to noise ratio has been quartered. We can therefore apply the Shannon theorem to determine the effect of doubling the distance between the transmitter and receiver:

$$C_\Delta=\frac{B\log_2{(1+(S/N)*0.25)}}{B\log_2{(1+S/N)}}=\frac{\log_2(1.25)}{\log_2(2)}=0.322 \tag 3$$

So we can see that with each doubling of distance between the antennas, the maximum channel capacity is reduced by approximately 68%.

We can overcome this loss in maximum channel capacity by increasing the gain of the transmit or receive antennas or increasing the power of the transmitter. But it is clear that if no other steps are taken, doubling the distance means we must reduce the bit rate by about 68% to maintain communications.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9911/relations-between-bit-rate-frequency-deviation-and-channel-filter-bandwidth, by noearchimede, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
