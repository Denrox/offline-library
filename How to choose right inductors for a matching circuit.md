# How to choose right inductors for a matching circuit

*Tags: rfi, capacitance, inductor · score 5*

## Question

I would like to chose an inductor to make a matching circuit. Operating frequency is 6.1 GHz. I am more concerned with self resonance frequency and Q of an inductor.

Would an inductor with SRF > 7 GHz and Q > 10 be okay at above frequency?

## Answer (score 2, by Phil Frost - W8II)

Would an inductor with SRF > 7 GHz and Q > 10 be okay at above frequency?

Could it be made to work? I suppose. But any discrete inductor at 6 GHz is going to have significant non-ideal behaviors that you will need to model (or empirically measure) to get an accurate match. At the SRF the inductive reactance and capacitive reactance are equal, but this does not mean below the SRF the capacitive reactance is zero, so you'll need to include that in your model.

Moreover, you'll need to consider how repeatable and stable these parameters are. The answer is usually "not very".

For these reasons (and also cost), transmission line stub matching is usually used at these frequencies. I suggest starting with the Smith chart tutorial at fourier-series.com to get an intuitive understanding of the technique. Then you can research some of the practical considerations and fabrication techniques.

## Answer (score 2, by OH2FXN)

As others have pointed out, the discrete components, suchs as capacitors and inductors, start to be quite challenging in higher frequencies. In general, transmission lines tend to have lower losses and higher repeatability around your frequency.

**Long story:** While the transmission lines might be better for practical applications, I wanted to share the simulations I did for this problem to help to understand the challenges. Consider a $75 \Omega$ load that you want to match to $50 \Omega$ source. Most practical loads would have also a imaginary component and vary as function off the frequency, but constant resistance will do nicely in this example. One solution, at 6 GHz, would be a 0.25 pF parallel capacitor and a 1 nH series inductor. The left hand side of the figure shows a maximum in the power transmitted to the 75 $\Omega$ load resistance R_load (blue curve) and that the feed impedance is $50 \Omega$ at 6 GHz (green curve). This means that the load got matched at that frequency.

In reality, the 1 nH inductor has also some capacitance between the legs and windings (C1) and some resistive losses (R1). See the right hand side of the figure. Parallel inductor and capacitor in series with your load create a band stop filter: low frequencies cannot pass the capacitor and the circuit seems like inductance. At high frequencies the circuit behaves like a capacitor. In the middle, at the resonance frequency, the impedance is very high and no current can flow through the circuit.

The self resonance frequency found on the datasheet of the inductor corresponds the frequency at which the inductor starts to behave like a capacitor, that is, above the resonance frequency the parasitic capacitance of the inductor is the easier path for the current flowing through the component.

The component values for the better model of inductor can be calculated from the equations. Parallel capacitor from the self resonance frequency: $C = 1/((2\pi f_{res})^2L)$. And equivalent series resistance from the Q value: $R = 2\pi f_{res}L/Q$. The simulations show that with all non-idealities taken into account, the matching circuit is quite horrible and also the power delivered to the resistor has dropped significantly.

The situation can be improved by optimizing the matching network while taking into account the non-idealities of the inductor. The figure below shows one solution: it turned out to be impossible to get the circuit tuned with 0.25 pF parallel capacitor: if the inductor value decreases and SRF is constant, the value of parasitic capacitor gets up and the circuit is newer matched to $50 \Omega$. For practical inductors, this probably would not be the case: by removing turns from otherwise identical inductor the capacitance would actually drop. A few sample inductors from Farnell had tolerances of e.g. 0.5nH $\pm$ 0.2 nH.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3798/how-to-choose-right-inductors-for-a-matching-circuit, by Shiva Mudide, Phil Frost - W8II, OH2FXN. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
