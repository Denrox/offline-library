# How to properly simulate a crystal filter being pulled?

*Tags: electronics, filter · score 5*

## Question

After reading [k1zmt's answer](Shifting%20Frequency%20of%20a%20VHF%20Crystal.md) to the question of how to change the resonant frequency of a quartz, I wondered how to simulate a quartz filter to check that result.

I went with the following model of a simple quartz filter:

The "loop" in the center, encompassing Cp1, L1, Cs1 and R1 is the classical equivalent small signal model of a quartz resonator; values are mostly "lifted from old exercise sheets and memory", so might not be very useful.

C1, the quartz model and C2, form a single-stage crystal ladder filter.

No matter how I adjust L_pull1, and dimension Rsrc==Rload and C1 relative to L1, I can't really change the resonant frequency in any significant way (beyond the accuracy of ngSPICE).

So, I'm almost certain I'm setting up this simulation incorrectly, or am using an insufficient model of a quartz.

How does one correctly simulate a quartz filter in SPICE (or similar, free software)?

## Accepted answer (score 4, by glen_geek)

OP's model is close to a 100 kHz crystal. These old crystals were once used as frequency calibration sources in an oscillator. I cannot recall seeing these used as a filter. The ratio of parallel-to-series capacitance for quartz is in the 250 ballpark, so OP's 2pf/0.01pf seems reasonable.  
I have one of these in HC16/U "can". It's a BIG CRYSTAL, whose Cp1 measures 7.4 pf.  
Cannot measure its motional parameters (L1, CS1, R1) with a "sqirrelly" function generator, but it sharply resonates very near 100kHz.  
One of the big problems with using a single crystal as a bandpass filter is its "Cp1" capacitance...this is the real, measurable crystal plate capacitance with quartz as the dielectric. OP's crystal is 2pf, mine is 7 pf.  
This parallel capacitance causes stop-band attenuation to be poor. Single-crystal filters might try to compensate for this capacitance in a bridge circuit (this crystal is a 12MHz HC49 measured device):

The resulting band pass filter has a centre frequency very close to the crystal's series resonant frequency. The transformer above is a 1:1:1 turns ratio that couples energy from primary to centre-tapped secondary with very high coupling. This transformer would be wound on a ferrite core with three identical windings. Inductance was 20uH in the plot below.  
An alternative using can use two 180-degree signal sources instead of the transformer. For example, an SA612 mixer has two 1500-ohm outputs on pin 4,5 that are out-of-phase. One drives the crystal, while the other drives the compensation capacitor. As with all bridges, some adjustability should be provided - perhaps the 3.5pf capacitor should be variable.

You can have a null frequency below or above resonance by adjusting "C1" (3.5 pf). When C1 is equal to C3, you get no nulls (purple plot). Without the bridge compensation, you get a null above resonance (green plot), and you can see that the stop-band frequencies below resonance are less-attenuated.  
Pass band is a function of R1 (30 ohms) and RL(30 ohms). Larger values give wider pass band, but poorer stop band. In any case, the stop-band floor is pretty poor, so we usually use more than one crystal in a band pass filter.  
OP asks about shifting the filter's peak...  
If one compares the purple "3.5pf compensated" plot (above) with "0pf compensation" plot, you might see that this crystal could be shifted *above* series resonance, up as far as 12.0238 MHz where parallel resonance occurs. However, this gets tricky, because now you have a low source resistance transformed by the crystal up to a higher load resistance.  
Here's an attempt to shift the **filter's resonant peak** upwards, above its series-resonant frequency of 11.996 MHz. One of these attempts (purple, below) sets the filter's peak frequency very near 12.000 MHz. An extreme example (orange, below) shows a filter peak up nearer to crystal parallel resonance (12.0178 MHz). It is unlikely you could manage a load impedance of 5 Mohm in parallel with 1 pf.  
These are all impedance-matched filters, where the signal-source resistance is matched to the filter's load resistance RLx.  
The filter's floor is rather skewed as well, with poor stop-band below resonance. Above resonance, the crystal's 3.5pf internal parallel capacitance provides a nice null.  
I should also note that this characterized 12MHz crystal was denoted by the manufacturer as a "parallel resonance" type (rather than "series resonant type"). You might see that the purple filter above at exactly 12.00 MHz uses a 23.5 pf capacitor - very close to the manufacturer's specified "load capacitance".

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22570/how-to-properly-simulate-a-crystal-filter-being-pulled, by Marcus Müller, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
