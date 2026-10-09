# Why is coax loss logarithmic?

*Tags: rf-power, coaxial-cable, electronics, transmission-line · score 4*

## Question

With DC hookup wire, losses are directly proportional to length. If the resistance of 100m of wire is 10 ohms then the resistance of 200m of wire will be 20 ohms.

But we measure coax loss in *decibels* per given length. For example, this chart lists RG-8X at 10MHz as having a 1dB loss per 100ft. So 200ft of this coax would have only 2dB of loss. This is *not* twice as much loss! In fact in this case it happens to be "half" as much (in decibels) as twice the loss [in "loss"ables?].

What I mean is: if we start with 1 dB of loss for the first hundred feet, twice that loss would be 4 dB (since adding approximately 3 dB is mathematically the same as multiplying by two). But instead of 4 dB of loss, we only have 2 dB of loss.

What's even weirder about this is that coax gets *less* lossy as the frequency decreases. Going back to the chart we see a 2.5dB/100ft loss at 50MHz, 1.0dB/100ft at 10MHz, 0.5dB at 1MHz. Surely at 50/60Hz coax must be some sort of superconductor, then?!

How do we get this scenario where at UHF frequencies a transmission line is so much *worse* than double the power loss (basically wherever the loss per 100ft exceeds 3dB…but wait, why should the unit length matter… hmmm…), but at HF frequencies it's so much *better*, when comparing the logarithmic losses to the linear resistance of a conductor?

## Accepted answer (score 4, by Phil Frost - W8II)

Firstly I would note that your initial statement isn't true. Indeed, the *resistance* of a wire increases with length, but resistance isn't loss in the same sense of transmission lines where loss is measured in *power* or a ratio of powers. Consider:

$$ I_\text{source} = I_{R1} = I_{R2} = \sqrt{1 \over R_1 + R_2} $$

$$ P_{R2} = I_{R2}^2 R_{R2} = {R_2 \over R_1 + R_2} $$

Replacing the source with a constant current or a constant voltage source we can make some linear relationships to length, but under those conditions source power changes with length also. This isn't the same sense of "losses" used in transmission lines which compare how much *power* from the source makes it to the load.

But this doesn't answer your question: although the relationship isn't linear, neither is it what's expected of a transmission line:

$$ P_\text{out} \propto 10^{-l} $$

It's a basic property of transmission lines that if the line is infinitely long, or terminated in a matched load, then the source will see the same impedance no matter how long, lossy, or not lossy the transmission line is. This holds for all frequencies, even DC.

There's no way to do that with simply a series resistor. But it can be done with a T attenuator. Here's an example of a 50Ω, 1dB attenuator:

The impedance seen by V1 is:

$$ (R_2 + R_4) || R_3 + R_1 = 50\:\Omega $$

Since V1 sees 50Ω, input power is:

$$ (1\:\mathrm V)^2 / 50\:\Omega = 0.02\:\mathrm W $$

I'll not go through the math, but the power in R4 is 1dB less, or:

$$ 0.02\:\mathrm W \cdot 10^{-1/10} = 0.0159\:\mathrm W $$

This property of not changing the impedance seen by the source holds true only

You could then imagine a transmission line as any number of these T attenuators connected together. As more are connected the total conductor resistance (R1 + R2 + ...) increases linearly, but each additional attenuator adds another 1dB of attenuation.

Alternately, you can take that 1dB attenuator and divide it into two 0.5dB attenuators. And then keep subdividing infinitely until each attenuator along the length of the line is an infinitesimal section of the line.

At this point, we are getting close to a decent model of a transmission line. Missing though is any way to transfer power efficiently since the whole thing is a resistor, and there can't be a wave in it, since a wave requires a notion of time and there's no time term in the definition of resistance.

Solve that by adding to the model the inductance of the conductor, and the capacitance between the conductors:

Since these inductors and capacitors are lossless, as long as their contribution to impedance is much larger than the resistive elements the loss will be low. Furthermore, the definition of capacitance and inductance are differential equations with time, the mathematics can support a wave.

Losses increase with frequency for (at least) three reasons:

1. Skin effect
2. Dielectric losses
3. Radiation losses

The resistive elements in the transmission line model are more accurately functions of frequency, due to these effects.

As frequency increases, skin effect constrains the current to a thinner cross-section of the conductor. This means less conductivity overall, increasing resistive losses. This is why larger-diameter coax has lower loss: there's more conductor surface area, and thus less resistive loss.

Dielectric losses occur as the voltage alternates between opposite polarizations. Reversing the polarity of some dielectric (say, PTFE) takes some fixed amount of energy. With increased frequency this reversal occurs more times per second, meaning it consumes more power. This is why air-dielectric transmission lines have lower loss: it takes much less energy to reverse the polarity of air than something like PTFE.

Radiation losses occur in coax for example when the shield is not a perfect, solid conductor. Consider coax with a braided shield: it does not provide perfect coverage, but has holes in it. At low frequencies, these holes are minuscule relative to the wavelength, making them negligible. As frequency increases the holes appear increasingly large, leading to a less complete containment of the fields within the coax, and more radiation. This is why coax intended for high-frequency use tends to incorporate foil shielding, sometimes multiple layers of it.

## Answer (score 3, by Mike Waters)

**You are mixing units.**

In the case of the wire, you specify resistance. But dB refers to power, not resistance.

## Answer (score 2, by Juancho)

In a DC (or low frequency) power line, current is constant and the voltage drop is due mainly to resistive losses. So voltage drop is proportional to wire length. Constant current and voltage drop proportional to distance gives power loss proportional to distance.

In a transmission line (assuming no standing waves), the relationship between current and voltage is given by the characteristic impedance of the line. Losses occur due to series resistance **and** parallel conductance across the dielectric.

So both voltage and current are reduced along the line, and thus the non linearity.

If, say, you get 3dB loss in the 1st 100m section of line (i.e. half the power), then you'll only have 1/2 the power entering the 2nd 100m section. The 2nd section will dissipate 1/2 of that (1/4 of the total power), and so on.

As frequency increases, the losses on the dielectric increase significantly.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7353/why-is-coax-loss-logarithmic, by natevw - AF7TB, Phil Frost - W8II, Mike Waters, Juancho. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
