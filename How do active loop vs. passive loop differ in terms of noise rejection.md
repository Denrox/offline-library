# How do active loop vs. passive loop differ in terms of noise rejection?

*Tags: rfi, loop-antenna, magnetic-loop · score 3*

## Question

As a urban ham (Harvard Square, Cambridge MA), I'm on the hunt for RFI rejecting antenna configurations. After hours of research, I've come across many strong recommendations for loop antennas, since they supposedly respond less to electric fields. In reviewing my options, I see there are several different classes of these antennas such as:


Passive loop antenna such as the well loved W4OP (store link, eham review) - these often have a variable capacitor tuner with an apparently high Q which supposedly helps with noise rejection. (I suppose this avoids RFI on adjacent bands that would somehow swamp or add noise to the region you're interested in? But why would that be the case at all?)


Active loop antennas the much loved Clifton antenna, the Chameleon, etc - seems to have what looks like a pre-amp but no tuning or variable cap

On further digging, the major advantage of an active antenna would seem to be amplification that pushes signals over the line loss of the cabling. That hardly seems to account for the field reports that active antennas are somehow better at noise rejection.

My question - what is really the best approach for noise rejection in an RFI-washed space (easily 100 families within a 2 minute walk)? Which approach actually provides the best SNR? Does the pre-amp perform some other function that makes up for the apparent lack of tuner? Why don't we see active loop models that also tune? And why does the tuning on the passive loop help reduce noise?

## Accepted answer (score 6, by Phil Frost - W8II)

Loops (active or passive) don't have the RFI rejection capabilities they are often claimed to have. RFI is electromagnetic radiation just like the signal, and it's not possible to design an antenna which accepts one but not the other. See [Can I reduce RFI/noise at the antenna?](Can%20I%20reduce%20RFI%20noise%20at%20the%20antenna.md)

Loops have the same directionality as a dipole, however their polarization is complementary. That can be useful when the polarization of the signal is fixed, such as AM broadcast radio which is always vertically polarized. A vertical monopole or dipole provides no azimuthal nulls, however a loop oriented in a vertical plane can be rotated to position the two nulls towards a source of interference.

Passive loops tune the highly inductive intrinsic impedance of the loop with a variable capacitor. The Q of this resonant circuit is extremely high, giving it a very narrow bandwidth. I'd consider this far more of an annoyance than any kind of advantage: any change in frequency requires re-tuning. However, perhaps if you are using an extremely poor receiver you may notice some improvement by eliminating sources of spurious signals from deficient filtering or nonlinearities. Then again, building a band-pass filter would give a similar advantage and be more convenient to use.

When constructed with special attention to minimizing resistive losses, and with a high-voltage capacitor, passive loops can be used for transmitting. However they are still very inefficient, and I would not recommend a loop for transmitting unless extreme portability was the primary requirement.

Active loops don't try to tune the impedance, but instead have a preamplifier designed to function well with the loop's highly reactive impedance. This has an advantage of very wideband operation. However that can also be a disadvantage: for example if you are near a broadcast station the preamplifier may be overloaded and rendered unusable on all frequencies.

It's unlikely the preamplifier provides any benefit regarding noise. Remember the preamplifier amplifies noise and signal, plus adds some noise of its own. See [How can I calculate the effects of an LNA, antenna gain, etc. on noise performance?](How%20can%20I%20calculate%20the%20effects%20of%20an%20LNA%2C%20antenna%20gain%2C%20etc.%20on%20noise%20performance.md) for more details.

## Answer (score 4, by Glenn W9IQ)

**Poor Loop Gain**

The small (<0.1 wavelength in circumference) loop antenna has very low gain. While the size somewhat lowers the directivity, the primary reduction in gain is due to inefficiency as a result the very low feedpoint resistance. When an antenna has reduced gain, not only are the desired signals reduced, so is any noise (QRN) since noise is another RF signal.

**Directionality**

The loop has a directional characteristic so if it happens to be oriented towards the desired signal (in the plane of the loop) and away from (perpendicular to the plane of the loop) the source of the noise, the noise will be suppressed.

**Loop Q**

Regarding the tuning of the loop as a source of noise reduction, this will not typically be the case. While a loop antenna with its tuning circuit has a relatively narrow bandwidth, it is at least an order of magnitude wider than the receiver's audio bandwidth. As a result, the Q of the loop antenna system has no appreciable affect with regard to noise. It may, however, prevent receiver overload from near frequency QRN.

**Loop Inductive Characteristics**

Concerning the effect of the inductive characteristics of a small loop on locally generated noise, keep in mind that noise is another RF signal. As a result, noise has both an electric field and a magnetic field. Therefore the loop cannot somehow ignore noise to any greater or lessor degree than any other RF signal.

**An Amplified Loop**

An amplified loop simply makes up some of the gain lost in a passive loop. If there is noise present, it will amplify it along with the signal. Arguably the amp actually generates some noise itself but on the lower HF bands, this will not be a factor. The relatively low feedline losses, assuming a matched load, are not a justification for an amplifier on the HF bands.

**Basis for Local Noise Reduction**

The most likely source of observed local noise reduction when using small receiving loops is that they typically do not suffer from common mode currents (CMC) on the feedline. When CMC is present, it will alter the pattern of the antenna and couple noise near the feedline into the received signal. By contrast, most other classic antennas, such as a dipole or monopole, require special attention to minimize CMC. If A/B comparison tests do not factor CMC, the test is likely invalid.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10562/how-do-active-loop-vs-passive-loop-differ-in-terms-of-noise-rejection, by Jeremy Gilbert, Phil Frost - W8II, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
