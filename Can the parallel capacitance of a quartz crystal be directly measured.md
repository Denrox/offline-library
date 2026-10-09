# Can the parallel capacitance of a quartz crystal be directly measured?

*Tags: measurement · score 5*

## Question

A quartz crystal is often represented by this equivalent schematic:

[How to measure quartz crystal motional parameters using a VNA?](How%20to%20measure%20quartz%20crystal%20motional%20parameters%20using%20a%20VNA.md) discusses measuring these parameters with a VNA, and there the most mathematically complex step is determining $C_p$. Is it feasible to measure $C_p$ directly with an LCR meter?

## Answer (score 4, by Phil Frost - W8II)

The impedance of $C_p$ is

$$ Z_p(\omega) = {1 \over i \omega C_p } $$

and the impedance of the other branch is

$$ Z_s(\omega) = R + i \omega L + {1 \over i \omega C_s} $$

and the impedance of the entire crystal is the parallel combination of these:

$$ Z_x(\omega) = \left( {1\over Z_p(\omega)} + {1\over Z_s(\omega)} \right)^{-1} $$

Typical values for an approximately 14 MHz crystal are:

$$\begin{align} R &= 7.37 \:\Omega\\ C_s &= 18.8\:\mathrm{fF}\\ C_p &= 4.15\:\mathrm{pF}\\ L &= 6.57\:\mathrm{mH} \end{align}$$

At 1.4 MHz:

$$ \begin{align} Z_p(2\pi 1400000) &= 0-27393i\\ Z_s(2\pi 1400000) &= 7.37 - 5989128i\\ Z_x(2\pi 1400000) &= 0.000152779-27269i \end{align}$$

An LCR meter is probably just measuring the magnitude of the voltage when applying a known AC current, so it will be off by a factor of:

$$ {|Z_x(2\pi 1400000)| \over |Z_p(2\pi 1400000)|} = 0.995447 $$

So for this particular crystal, measuring the impedance with an LCR meter (assuming no other inaccuracy in the device) at approximately 1/10th the serial resonance frequency of the crystal yields an error of less than 1%.

So, given an LCR meter that can be accurate with a reactance on the order of 30kΩ, this is not a bad way to go.

## Answer (score 2, by glen_geek)

Short answer: measure $C_p$ at a frequency far from any one of the crystal's resonant frequencies.  
Be aware that not only is a crystal resonant on harmonics of its primary (printed) frequency, but spurious resonances also appear.  
It is probably safest to measure the parallel-plate capacitance below resonant frequency. So yes, LCR bridges often use a signal source at low frequency. Since $C_p$ may be in the single-digit picofarad range, care should be taken to reduce stray capacitance of the measurement fixture.  
You might measure $C_p$ with the crystal mounted in the LCR meter, then carefully remove the crystal without disturbing the environment, and measure stray capacitance. The true(er) $C_p$ is the difference between the two measurements.  
For quartz AT-cut crystals, $C_p$ is very roughly 250 times larger than $C_s$.  
You're unlikely to measure $C_p$ so accurately in a LCR meter or bridge that this factor need be considered.  
Ceramic resonators are not as piezo-active as quartz, so the disturbing effect of $C_s$ requires factoring-in its effect on a $C_p$ measurement.  
For example, an ultrasonic transducer was measured where $C_p$ was only 7.5 times larger than $C_s$.  
Quartz has amazing qualities: very piezo-active, temperature-stable. Most other materials that are piezo-active pale in comparison.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17019/can-the-parallel-capacitance-of-a-quartz-crystal-be-directly-measured, by Phil Frost - W8II, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
