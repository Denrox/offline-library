# Why is my experiment to produce 3rd order harmonics by saturating a receiver not working

*Tags: receiver, amplifier, testing, education · score 3*

## Question

I've been trying to devise an experiment to produce a third order harmonic in radio receiver that's been saturated, but I'm not seeing the expected results.

My understanding of the theory is that when you drive an amplifier ***( refer to the diagram below )***, past the point of linear operation whether by an on or off frequency signal, it will produce harmonics of and primary frequencies input into it. ( See diagram below ) I thought I could observe this effect with a handheld two-way radio and 2 signal generators I have on hand.

My experiment set up is thus: A multiple band, 2-way FM transceiver, programmed to to receive on 471MHZ and two signal generators. One signal generator generates an FM 157MHZ signal, modulated with a 1kHz tone, the other signal generator is used to produce an unmodulated CW carrier. Note that 157MHZ x 3 = 471MHZ. I expected that I could use the CW signal to force the receiver into non-linear operation causing the amplifier to produce 3rd order harmonics of the 157MHZ FM signal injected below saturation.

First I inject the 157MHZ signal into the 471MHZ radio. At about -60 dBm the receiver of the radio would open and produce a fairly clean 1k tone: this to me indicates that the FM signal forced the receiver into non-linear operation, causing the 3rd order harmonic, 471MHZ to be demodulated on the radio. This I expected. Next, I used a combiner to inject the 157MHZ FM signal and the CW signal into the receiver. I injected the FM signal first to find the spot where the receive became non-linear and demodulating the 1k tone. I decreased the FM signals power just below the threshold. Then I turned on the CW generator and increased the power slowly. I assumed that the CW signal would drive the receiver into non-linearity causing the receiver to produce the 3rd order harmonic of the FM signal, and thus the receiver would open up with the primary FM signal injected at a lower power than by itself.

The results were not what I expected. No matter what frequency or power level the CW was set to, it didn't seem to affect when the receiver opened up. If the FM signal was set so that it's 3rd order harmonic was being received, I could overload the receiver by cranking up the CW wave though, so I know it was getting into the receiver. I was expecting that the CW signal would force the receiver into non-linear operation, and that I would be able to receive the 3rd order harmonic of the FM signal at a lower threathold than by itself. Anyone have an idea why I didn't see what I expected?

## Answer (score 4, by Phil Frost - W8II)

Receivers have passive band-pass filters at their input. Except possibly ferrite cores (which are unlikely to be used for a filter above HF), the components used to construct these filters are very linear. For a receiver tuned to 471MHz, the output of your signal generators at 157MHz is surely well within the filter stop-band.

Although the filter's stop-band attenuation isn't infinite, and this means at some power you could still saturate the receiver, it's going to require a very high power for the fundamental, after being attenuated, to have enough power to cause significant nonlinear behavior in the active components behind the filter.

Further consider, the signal generators produce harmonics as well. The receiver's filter attenuates the fundamental from the signal generators, but not the harmonics.

So, it's likely you're just hearing the harmonics of your signal source, and not overloading the receiver.

If you want to observe non-linear behavior in your receiver, you need to generate two or more *in band* signals. The two tone test is a common way to do this.

The image you included that mentions "IM products" hints at this. It sounds like with your setup you're trying to measure harmonic distortion, but "IM products" refers to intermodulation products. Unlike harmonic distortion which produces spurious signals at multiples of the fundamental, IM distortion produces spurious signals related to the difference between two signals and multiples of that difference. Since the distortion products lie much closer to the signal or signals of interest, this makes them much more difficult to remove with a passive filter, and thus much more problematic in practice.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18439/why-is-my-experiment-to-produce-3rd-order-harmonics-by-saturating-a-receiver-n, by Frank, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
