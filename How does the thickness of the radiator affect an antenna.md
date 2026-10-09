# How does the thickness of the radiator affect an antenna

*Tags: antenna, antenna-theory · score 3*

## Question

Another question ([Metal for antenna construction?](Metal%20for%20antenna%20construction.md)) covered some aspected of this question, but the answers didn't exactly answer it, so I'll make it specific.

Given 2 dipole antennas, resonant at the 2-meter band (146 MHz) exactly, differing in their construction:

1. Uncoated copper tubing with an outer diameter of 19.05 mm (0.75 inches), something like a 3/8 copper tube.
2. Uninsulated copper wire with an outer diameter of 2.053 mm (0.0808 inches), something like 12 AWG copper wire.

Wherein would the difference between them lie?

Since I don't know the answer: I'm wondering if, for example, there would be a difference between their effectiveness, arm lengths, or something else?

## Accepted answer (score 1, by MagnusO_O)

Some rf aspects that could be taken into account.

- Summary: no considerable impact

 - but feel free to read the long version below

Check the answers that have covered the important physical and bandwidth aspects already.

### 1. Skin effect

rf current concentration at the surface are described by the skin effect.

As a rule of thumb the material thickness should be $>5* skin \, depth$. Then the majority of the concentrated current (skin effect) is within the available material.

- current density follows a $e^{-z/\delta}$ relation, so with $z=5*\delta$ that's $<1\%$

 - thicker material has no more considerable impact on losses
 - for thinner material losses increase

Skin depth: $\delta \, [m]= \sqrt{\frac{2\rho}{\omega\mu}}$

- angular frequency: $\omega=2\pi f =2\pi * 146 MHz=917*10^6$ $\frac{1}{s}$
- permeability: $\mu \, [H/m = \Omega s /m]$ (Henry unit)

 - copper: $1.26*10^{-6} H/m$
- resistivity: $\rho \, [\Omega m]$

 - copper: $1.68*10^{-8} \Omega m$

$\delta_{copper\_146MHz} = 5.4 \, \mu m$

In your example $>5* skin \, depth$ is **well fulfilled**, so the tube / wire has no difference.

### 2. Losses

By considering a two-wire transmission line analytical formulas provided by rf textbooks can be applied to assess the losses impact.

For sure that two-wire line isn't the same as a dipole antenna, but it can be used to provide some perspective without electromagnetic simulation.

Surface resistance: $R_s = \sqrt{\frac{\omega\mu\rho}{2}} = 3.1 \, m\Omega$

Series resistance in unit length of a two-wire line: $R' [\Omega/m]=\frac{R_s}{\pi * radius}$

- 19mm tube: $R'=104 \, m\Omega/m$
- 2mm wire: $R'= 992 \, m\Omega/m$

There is a considerable relative difference, but absolute it's still small especially concerning that not even a full wavelength is applied on a $\lambda/2 \, dipole$ (compared to a transmission line that's usually ${>> \lambda}$)

- For effectiveness that consideration also applies.

#### 2.1 Putting it into perspective

With an arbitrary made up two-wire line example.

- assumptions: air with 0 conductane, 2mm wire, d>>a simplifaction

distance: $d=0,01m$

radius: $a=0,001m$ (2mm wire)

$j\omega C' = \frac{\pi \epsilon_0}{ln \,d/a}=0,011 \frac{F}{m}$

$j\omega L' = \frac{\mu_0}{\pi} \, ln \frac{d}{a}= 845 \frac{H}{m}$

$R'= 0.992 \, \Omega/m$ (from above 2mm wire)

#### 2.1.1 Lossless

$Z_0=\sqrt{\frac{L'}{C'}} = 276.12 \, \Omega$

$\lambda=2.0533731 \, m$

#### 2.1.2 Lossy line

$Z_0=\sqrt{\frac{R'+j\omega L'}{G'+j\omega C'}} = 276.12 -j 0.16 \, \Omega$

$\lambda=2.0533727 \, m$

Length of line to have $0.1 \, dB$ attenuation: $3.2 \lambda$

Even the 'higher' series resistance of the 2mm wire has a negligible effect on the impedance of a two-wire line compared to the lossless case (for short lenght like the case of a $\lambda / 2 dipole$).

So the difference in between tube / wire will be also negligible.

#### 2.2 Losses impact on radiation pattern

The losses will affect the current distribution along the dipole length and therefore the radiation pattern.

Anyway based on the previous assessments I won't expect a recognizable impact.

### 3. Diameter impact on radiation pattern

To assess this without electromagnetic simulation programs:

In your case the air $\lambda$ is $2.05 \, m$ and therefore even the $19 \, mm$ tube diameter is $< 1\%$ of the wavelength.

Antenna elements that are applied to impact the radiation pattern usually are in the magnitude of the wavelength ($\lambda$, $\lambda /2$, $\lambda /4$ - but not $\lambda /10$ or $\lambda /100$).

Therefore I won't expect a recognizable impact on radiation pattern for your application.

## Answer (score 5, by Phil Frost - W8II)

Generally, the thicker an antenna is, the wider its bandwidth. So the copper tubing will have slightly higher bandwidth.

Furthermore, the copper tubing will have much more surface area, thus lower resistance, and lower loss.

You'll probably find the length necessary to achieve resonance is slightly different in each case.

But overall, these effects are pretty small. Their more significant differences are cost and mechanical properties.

## Answer (score 3, by K0UA)

The bandwidth of the thicker antenna will be slightly wider Just like for instance on 80 meters people build cage antennas to increase bandwidth on that band, up on 146 the effect will be the same as the percentage of diameter as it relates to the length will be comparable. Not that it will be all that big of a deal at 146 because the entire band while 4 mhz wide is not as wide as the .5 mhz on 80 meters as a percentage. The .5 Mhz of 4 mhz is 12.5% while the 4 Mhz width of 148 Mhz is only 2.7%

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15107/how-does-the-thickness-of-the-radiator-affect-an-antenna, by Amin Shah Gilani, MagnusO_O, Phil Frost - W8II, K0UA. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
