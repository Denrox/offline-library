# Identifying a transmission to myself

*Tags: station-identification · score 3*

## Question

I have a networked remote HF receive-only receiver (Raspberry Pi with an SDR module). When I transmit to myself (to the remote receiver on its listening frequency), say for antenna path testing, or for logging mobile location telemetry (etc.) to my fixed-base server, how should I identify my transmissions? (U.S., amateur license, HF bands using Morse code) What additional stuff (punctuation, etc.) besides a bare call-sign?

## Answer (score 6, by Marcus Müller)

When doing a diagnostic self-reception, it's typically advantageous to give the receiver as much chance to identify the channel as possible.

Wouldn't it be cool if your identification could be used to measure the channel itself? That way, you'd stay on the air for as shortly as possible.

So, you'd typically would want to send something that is spectrally white to sound the channel. Correlate with exactly the same white sequence at the receiver (yielding the autocorrelation of a white sequence, which is a dirac impulse, convolved with the channel impulse response; convolution with a dirac impulse is nothing but a time shift).

Sadly, um, that's typically not allowed as a means of identification, although having a large registry of orthogonal white pseudorandom noise sequences would make for an **excellent** ID database! Instead, identification must be done in a way that a (relatively uninformed) third party can understand (not to mention that in many bands you can't just send arbitrary signal at all, but must use predefined modulations).

Still, within the bandwidths and methods you're allowed to use, don't hesitate to optimize your transmitter identification signal for channel identification purposes!

For example: You've got a 200 Hz wide channel on which you're only allowed to do morse with $\le 20\,\text{wpm}$, which leads to a dot length of ca 50 ms, which leads to an actually necessary bandwidth of about 40 Hz only – but we're not in the business of being as bandwidth efficient as possible!

Unlike usually, if we want to get channel state information, we want to be as wide as legally possible – and that's exactly what you'd achieve by

- generating a dot length of white noise, in your favourite programming language or audio program
- running that on repeat
- Gating that in a Morse fashion
- using a good band-pass filter (as in: Many taps, so that the passband is as wide and flat as possible, and the transition widths narrow, and after that the stopbands strongly attenuated) to get band-limited white noise
- Save the result to a file, and send that to your networked remote
- using AM / SSB to modulate that signal, so that it ends up occupying the channel your remote receiver is listening to

At the receiving end,

- well, receive
- Correlate with the file from above

 - Hint: means filtering with the time-inverse!
 - Another hint: just correlate with the original white noise dot-length sequence, you get an impulse for every dot period of signal coming in after doing the matched filter to the noise-bandlimiting filter (you've just built a matched filter! Yay!)
- Identify your own transmission by the impulse(s) you observe

The beauty in that is:

- you estimate signal power based on the power of what you've actually sent, not "integral", including noise and interference (these are typically uncorrelated to your signal)
- you get a full-bandwidth signal, with which you can get a full-bandwidth estimate of the channel – which means that if your channel is 200 Hz wide, you'll be able to get a more detailed impulse response, i.e. resolving different signal paths more clearly, than if you used say 40 Hz channel bandwidth, whilst still
- using an allowed mode (Morse; §97.305 says "MCW, RTTY, DATA") for identification. A casual listener would hear a noisy (yet potentially strong) signal during your "tone" time; it doesn't disturb them more than an actual CW signal of low bandwidth, yet is more useful to you!

Fun fact: that trick can even be used to (via self-assessment of the person doing that, so take with a grain of salt) operate a GSM base station in a ham band – you can simply pulse the transmit power of the control channel to CW out your station sign. (can't find the video link, sorry.)

## Answer (score 4, by Phil Frost - W8II)

Identification is governed by §97.119:

(a) Each amateur station, except a space station or telecommand station, must transmit its assigned call sign on its transmitting channel at the end of each communication, and at least every 10 minutes during a communication, for the purpose of clearly making the source of the transmissions from the station known to those receiving the transmissions. No station may transmit unidentified communications or signals, or transmit as the station call sign, any call sign not authorized to the station.

There are further rules about special situations, but since you are both the control operator and the station licensee, operating with your normal license, in quite ordinary circumstances, none of those apply. Remember the purpose of the identification is to identify the transmitter: who's receiving is irrelevant. So an ordinary "DE [your call]" would be sufficient.

And if the identification is keyed by an automated device used only for identification, keep it not above 20 WPM:

(1) By a CW emission. When keyed by an automatic device used only for identification, the speed must not exceed 20 words per minute;

## Answer (score 2, by Zeiss Ikon)

As I understand it, the bare call sign in (English) voice or Morse (as appropriate for your license class and the band or sub-band you're transmitting in) is the minimum. You can attach additional information if you wish -- for instance, a couple 2m repeaters I use regularly transmit Morse calls signs like "W4NC RPT". Your beacon could be something akin to that -- but it doesn't have to be. It could be *just* your call sign in Morse.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14421/identifying-a-transmission-to-myself, by hotpaw2, Marcus Müller, Phil Frost - W8II, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
