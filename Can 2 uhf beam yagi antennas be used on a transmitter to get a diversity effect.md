# Can 2 uhf beam yagi antennas be used on a transmitter to get a diversity effect?

*Tags: antenna-theory, uhf, frequency, yagi · score 3*

## Question

I'm having a problem getting a good signal up to a repeater site on UHF. I'm running 20W in a neighborhood with lots of trees, and the signal is fading in and out due to trees and the wind.

I can't run any more power. Would 2 UHF Yagis mounted side-by-side, spaced 1 wavelength apart, using the same length coax (50 ohm each; this will make 25 ohms which can be made back to 50 ohms w/ a piece of RG62 35 ohm cable).

Would this give a diversity effect, say when one is noisy and the other may have a good signal getting to the repeater?

## Answer (score 3, by Marcus Müller)

For diversity gain, you'd need to have two receivers (or you just switch to the currently "better" antenna; that's called *selection combining* in MIMO technology and kind of is the worst possible diversity mechanism).  
So, no, with two antennas and only a single receive chain, there's no diversity gain.

You can, of course, build an *antenna array*. That would actually work by using a impedance-matching combiner to make the reception of both antennas combine constructively. You'd basically achieve a higher directivity by adding *array gain* to your *antenna gain*.

Also, I wonder how you can put two antennas at "1 wavelength" distance for the whole UHF band – that covers wavelengths from 10 cm to 1m.

I'm not sure it would help *much* with the fading problems – these might be happening at larger scales.

As a more general comment: *Diversity* happens when you have two different signal paths transporting the same signal; *different* in the sense that the random effects on the signal are independent. That will almost certainly not happen for large-range communication with transmit antennas that are a mere single wavelength apart – I'd not expect any significant gain due to independent signal paths ("multipath") in an outside scenario with two close antennas pointing in the same direction.

In indoor scenarios (e.g. your usual cheap Wifi router with more than one antenna is a diversity/MIMO transceiver!), there's way more diverse multipath, and hence, antennas placed a mere more than half a wavelength apart have a serious chance of picking up a combination of at least two independent paths. Mathematically, the system is modelled such that:

- We assume one channel response from each transmit to each receive antenna
- We then put these into a table (and for reasons of simplicity, let's assume these channel impulse responses are completely characterized by a single complex number)
- We then consider that each receive antenna sees the sum of all the channels that "go to it", applied to the transmit signal
- And then we consider that the table from above is simply a matrix, and we can multiply that matrix with the transmit signal vector (ie. a vector with the entries of what each transmit antenna sent) to get the output at each receive antenna

With that model in mind, we can let the transmitter choose a transmit vector, so that the process of

1. taking a vector of the signal to be transmitted
2. an arbitrary mapping to a transmit vector
3. applying the channel matrix
4. and then applying a matrix that we can also arbitrarily choose

gives us multiple, independent channels, over the air, mathematically.

If this is of interest to you: that usually happens by applying a singular value decomposition to the (estimated) channel matrix, so that this matrix gets split into unitary (hence, nicely invertable) matrices and a diagonal matrix (which means that whatever you put into that diagonal matrix in one element has no effect on the other elements).

## Answer (score 3, by Dick Reid)

In your post the thing that leaps out is about using a horizontally polarized Yagi to contact a repeater which is commonly a vertical antenna. The signal loss in this situation is large. Try your Yagi antenna with the elements pointing up and down and see which orientation better, horizontal or vertical. Does this make a big enough difference?

As for diversity reception your idea of combining horizontal and vertical signals is one approach. The most simple is switching between two antennas. The ARRL Antenna Handbook goes a step farther suggesting a separate radio for each antenna and listening to both radios.

A simpler approach is have one arm of a UHF/VHF dipole in a vertical position to provide both polarizations in one antenna. *(This not a ground plane antenna which is vertically polarized).* Here is the antenna model information and 4NEC2 model if you want to tailor it to your situation.

A host of more sophisticated diversity methods exist — as you have found. Because phased vertical and horizontal Yagi antennas were not found you have a research project.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7677/can-2-uhf-beam-yagi-antennas-be-used-on-a-transmitter-to-get-a-diversity-effec, by Randy Cunningham, Marcus Müller, Dick Reid. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
