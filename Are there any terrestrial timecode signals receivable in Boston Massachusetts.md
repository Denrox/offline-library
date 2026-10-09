# Are there any terrestrial timecode signals receivable in Boston Massachusetts?

*Tags: snr, wwv · score 3*

## Question

I'm looking for any timecode station (like WWV/B, CHU, etc.) with an SNR > 0 dB that I should be able to receive in Boston Mass.

WWVB at 60 kHz has a phase modulation that one can apparently receive on the east coast, but the signal is borderline to begin with and I'd like something I can see or hear without code gain.

CHU in Ottawa, Canada transmits on 3 frequencies, including 3.33 MHz at 3kW but I don't know if I should be able to receive it. I haven't managed to yet.

Of course I can receive GPS but that's not the point.

## Accepted answer (score 4, by glen_geek)

WWVB propagation does vary in amplitude. And its BPSK phase modulation makes it a bit tricky to lock to. But if you narrow the bandwidth enough, signal is most always above the noise.  
Here's an example plot of WWVB amplitude in a fringe area similar to Boston...left half is night-time while right half is day-time. Each sample is exactly one second long. Bandwidth of this receiver is about one hertz.  
You see three different amplitude samples, because the integrated amplitude each second can take on three different digital codes (low, high, or sync).  
The vertical amplitude scale is arbitrary, proportional to volts, not watts. Antenna was a 0.7 m loop at ground level resonated to 60 kHz. A ferrite rod antenna produces similar results.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10023/are-there-any-terrestrial-timecode-signals-receivable-in-boston-massachusetts, by Martin Klingensmith, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
