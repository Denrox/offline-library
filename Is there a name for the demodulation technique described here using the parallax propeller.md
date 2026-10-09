# Is there a name for the demodulation technique described here using the parallax propeller?

*Tags: software-defined-radio · score 11*

## Question

Is this a recognized SDR technique with a name, or is just a combination of DSP, r/f techniques ?

I asked the author, but didn't receive an answer, perhaps because he thought it was "obvious" (not to me, though, an SDR / electronics newbie)

http://forums.parallax.com/discussion/105674/hook-an-antenna-to-your-propeller-and-listen-to-the-radio-new-shortwave-prog/p4

See the third post down by Phil Pilgrim "Attached is a set of traces that may help to explain what's going on in the receiver. ....."

Is this some modified form of Sigma Delta ADC ? :

"If we were using this counter as an ADC, we could set its FRQx to 1 and let it count the number of 1s it sees on A3 in a given interval. This count would be proportional to the average signal strength on A3 during that interval. But we're not going to do that. Instead, all we need is that string of 0s and 1s on pin A4. This is shown as signal "ADC" in the middle of the attached image, in magenta."

More info on the project is in the first post here :

## http://forums.parallax.com/discussion/105674/hook-an-antenna-to-your-propeller-and-listen-to-the-radio-new-shortwave-prog/p1

*Now that I've got your attention, here's the theory behind it. Most consumer radios on the market are superheterodynes. In such receivers, the incoming RF signal is "mixed" with a sinewave coming from a tunable local oscillator (LO).

Mixing is basically analog multiplication, which produces, in addition to the original RF and oscillator signals, signals which are at both the sum and difference frequencies of the two. The output of the mixer is filtered to a single, fixed, "intermediate frequency" (IF) and then amplified. In AM (amplitude modulation) broadcast radios, which tune from 550KHz to 1600KHz, the IF is usually at 455KHz. So, by varying the frequency of the local oscillator from 1005KHz to 2055KHz, one can obtain a 455KHz difference signal from the mixer for the entire broadcast band. The output of the IF amplifier is then introduced to a "detector", which rectifies and low-pass filters the IF signal to produce an audio waveform.

A receiver similar to the superheterodyne is the direct conversion receiver. In such a receiver the "intermediate frequency" is zero. In other words, the LO is tuned to the exact frequency you want to listen to, and the difference signal is simply the detected audio, which can then be lowpass filtered and amplified. But there's a catch: the local oscillator must not only have the same frequency as the desired signal, it must also have the same phase. To understand this, suppose the incoming RF carrier and the LO were 90° out of phase with each other. When multiplied together, these two signals would effectively cancel each other out, and you'd hear nothing. When they're in phase, the positive swings would multiply, returning positive results, and the negative swings would multiply, also returning positive results. But getting the LO to lock onto an incoming carrier can be tricky — especially if that carrier is weak.

One way around this is to have two LOs, 90° out of phase with each other, and two mixers. The idea is, what one LO oscillator misses by having the wrong phase, the other will catch. In fact, the outputs from the two mixers can be combined in such a way that the actual LO phases are irrelevant, so long as they're 90° apart. The formula for doing so is: ····Audio Amplitude = sqrt(I2 + Q2), where I is the output of one mixer (from the "In-phase" LO), and Q is the output of the other mixer (from the "Quadrature-phase" LO). Well, that's enough theory to lay the groundwork for the Propeller receiver. I've really glossed over a lot of stuff, but this is a forum post, not a book, and I want to get to the actual hardware and software.*

*APPLICATION The use of a Propeller counter as the basis for an analog-to-digital converter (ADC) is now well-established. So why not simply attach an antenna to the input of one of these ADCs and see what comes out? Basically, that's what I've done. Here's a schematic:

The antenna (a wire strung across the ceiling of my shop) is connected, through an inductor to both digital ground and earth ground. I used a 330uH power inductor I found in my junkbox. It actually worked better than the ferrite antenna scavenged from a cheap transistor radio. A bunch of enameled wire wound on a plastic sewing machine bobbin worked almost as well, too. I'm sure Beau Schwabe (i.e "He Who Understands Inductors and Knows What to Do with Them") can shed a lot more light on the choice of inductors and why one is needed here. I just grabbed what I had until I found something that worked. My "earth ground" consists of the ground clip from my scope attached to the ground stud on the Demo Board. My scope input return ground and its AC protective ground are connected together, thence back to the breaker box and to a metal grounding rod. (By the way, I live in a fringe area for AM reception. If you live in a city with strong AM transmitters, you may not have to go to all this trouble.)

The antenna also connects, through a capacitor, to pin A3 of the Propeller. This is the "analog" input terminal. The feedback comes from A4 through a 470K 0805 SMD resistor, which I soldered between pins A3 and A4 right on the chip itself. I've omitted the usual filter caps to Vdd and Vss (Gnd), choosing instead to let the inherent input capacitance of A3 do the filtering. This keeps both the input impedance and frequency response of the ADC high, which is necessary for detecting weak RF signals. During positive swings of an incoming signal, A4 will be sending more 0s than 1s to counterbalance it; during negative swings, more 1s than 0s. One counter can do this, set up in the "positive-with-feedback" special analog mode. Unlike the usual ADC usage, though, we're never going to read this counter again. It's just that string of 1s and 0s fed back from A4 that we're interested in. I love the Propeller's counters! I don't know if Chip knew what all could be done with them when he designed them, or if he just had an inkling that, with the right set of features, almost anything could be accomplished. In any event, the counters make ideal local oscillators and mixers! The oscillator part is pretty easy: just configure two counters as numerically-controlled oscillators (NCOs) in quadrature with each other. The frequency will be the frequency of the station you want to tune in. So, if I want to receive KIXI 880 in Seattle, I set up both counters to output 880KHz square waves, 90° out of phase with each other (i.e. PHSB = PHSA + $4000_0000).

Now comes the magic part: the mixers. The counters can be configured to count up whenever two inputs satisfy a Boolean conditional. The Boolean equation can be anything you want: AND, OR, NAND, NOR, XOR, you name it. I used XOR. Each "mixer" counter gets two inputs: the feedback from A4 and one of the LO outputs. If the LO output is low when A4 is feeding back 1s, predominantly (i.e. when the antenna signal is low), the counter will count up at a fast clip. Likewise, if LO is high when A4 is feeding back 0s, predominantly, the counter will, again, count up at a fast clip. In other words, the counter will count up faster when an incoming RF signal is in phase with the LO than when it's not. Moreover, the rate at which it counts up will be proportional to the amplitude of that signal. So, to read the amplitude of a signal in phase with the LO, one need only zero the mixer counter, wait awhile, then read it to see how far up it counted. On average, there will be as many increments during the sample period as non-increments, so the mean (average) count will be half the number of system clocks occurring during the same period. Any signal that's out of phase with LO, or of a different frequency, will contribute as many increments as non-increments, thus having no effect on driving the net count away from the mean.

Therefore, after each sample period, we can subtract the actual count from the mean count to get the instaneous amplitude of the signal. By doing this for both the I mixer and Q mixer, squaring the individual amplitudes, adding them, and taking the square root, we get the signal's amplitude, which can then be fed to the audio output: another counter in DUTY mode, feeding a lowpass filter. (I used A10 on the Demo board, which has the filtering hardware already in place.)

The length of the sample period will affect two things: the audio frequency response and the signal-to-noise ratio. Like most things in life, each of these two desirable qualities increases at the expense of the other, so you have to strike a balance. I got the most pleasing results with a 16KHz sample rate, which yields an 8KHz audio bandwidth. This is about as good as AM radio audio can get anyway, since the stations are spaced 10KHz apart. You can lower the sampling rate to get less static, but the audio starts to sound more "boomy".

SUMMARY

To summarize, the receiver uses six counters (spread over four cogs), as follows: (1) ADC (actually just a digitizing RF amplifier), (2) Local Oscillators in quadrature, (2) Mixers, and (1) Audio Output The counters do virtually all the work. There's not a lot of code required, outside of setting up the counters, reading them, and shuffling data between them via the hub. The attached program is configured as a scanner for the AM broadcast band. It increments continuously by 10KHz steps from 550KHz to 1600Khz, pausing at each frequency for three seconds, which is long enough to tell if something's there. It displays the frequency on a TV monitor, via tv_wtext (included). I've also used it for LF reception below the broadcast band with some minor success. As I stated in the intro, it's not a very good receiver — in fact it sounds pretty crappy and noisy. If, like me, you live in a fringe area, you may be disappointed by its performance. But, even then, it does illustrate the capabilities of those amazing Propeller counters. And that, really, was the main point. -Phil

Update: Owing to advice received from Beau Schwabe, based on his own testing, I've changed some component values. The inductor is now 500uH; the feedback resistor, 10M; the coupling cap, 0.047uF; and the antenna, a 2-meter-long vertical wire. The attached schematic reflects these changes, which did lead to an improvement in performance.*

## Accepted answer (score 8, by Dave Tweed N3AOA)

Very interesting (and clever)!

Yes, the first counter is being used as a delta-sigma modulator to turn the incoming analog signal into a high-speed string of bits. Then the counters generating the I and Q signals are defining the lower-speed sample rate. Two other counters (labeled "mixer") are essentially integrating (i.e., low-pass filtering) the high-speed sample data for each output sample period.

If the high-speed sample rate is 80 MHz, and the carrier frequency is on the order of 1 MHz, the output samples are counts in the range of 0 to 79, roughly 6 bits of resolution.

Since the sample rate of the output is equal to the carrier frequency, this creates a direct-conversion receiver. The sample clock serves the same function as the local oscillator in an analog receiver. In digital terms, the carrier, along with its sidebands, is being deliberately aliased down to DC, which means that the sidebands become the audio that you can hear. The low-pass filtering of the output (partly in the integrators, and partly in the analog output connection) determines the bandwidth that is being received.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6173/is-there-a-name-for-the-demodulation-technique-described-here-using-the-parall, by mstram, Dave Tweed N3AOA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
