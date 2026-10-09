# Antenna Aperature for out-of-band frequencies

*Tags: antenna, antenna-theory · score 3*

## Question

I am doing some calculations where I determine power at the input of Rx given some field strength at the antenna. I have a question about the antenna aperture:

$A_e = D\frac{\lambda^2}{4\pi}$  
$D$ is the antenna gain directivity (Rx in this case)  
$\lambda$ is the wavelength

Normally, I think of the frequency of the incoming (or outgoing) signal to determine the wavelength. However, I am wondering if it may dependent on the resonance frequency of the antenna.

In-band the difference between resonance and desired signal is small, however for out-of-band this relation may not hold. I would generally think the aperture size is correlated to antenna size regardless of transmit frequency; i.e. it is not as if the Rx antenna gets bigger just because the transmit frequency decreases.

Alternatively, I can think of $\frac{\lambda^2}{4\pi}$ as "normalization" which means that lowered gain accounted for by D (which would be measured). We then convert the maximum directivity measured into a equivalent isotropic antenna using the factor $\frac{\lambda^2}{4\pi}$.

I know I am not accounting for inefficiencies, to me this is a separate matter. But may also help explain why the incoming power is less than incident field strength.

Edited to add why we don't need to include inefficiencies in this discussion. If we have 2 antennas (Tx and Rx) separated by a distance (the Directivity ).

$\frac{D_{Tx}}{A_{Tx}} = \frac{D_{Rx}}{A_{Rx}}$

If we assume that the Tx is an isotropic antenna then $(D_{Tx} = 1)$

$A_{Tx} = \frac{\lambda^2}{4\pi} = \frac{A_{Rx}}{D_{Rx}} \rightarrow A_{Rx} = D_{Rx} \frac{\lambda^2}{4\pi}$

However, I only want to be clear about how to use effective aperture equation. Therefore, we would assume the maximum amount that could be transferred would be some ideal - then apply inefficiencies due to loss (dielectric, conduction, impedance mismatch, polarization, some other loss).

Therefore, I think $\lambda$ is the transmit frequency and not the resonant frequency.

Can someone provide some clarification/verification?

## Answer (score 3, by tomnexus)

Antenna aperture is just another way of expressing the gain of the antenna. Wikipedia says it best!

Because aperture is expressed in units of *area* we can then multiply by the *power density* of the incoming RF wave, to find the power that is captured by the antenna.

If you operate the antenna at a frequency where its gain drops, then its effective aperture drops too.  
If you tilt the antenna so it's not facing in the ideal orientation, its gain will be lower and its aperture smaller.

In a a few types of antennas, mostly horns and dishes, the aperture is closely related to the physical size of the antenna. For these we use a factor called *efficiency* which is the ratio of electrical aperture to physical aperture. For dishes the efficiency can be as high as 80% *(when everything is working perfectly)* so we start to think of them as simple collectors. Other antennas like a yagi, dipole or an isotropic antenna, have no direct physical relationship between their size and their effective area. In some cases the area can be much larger than the antenna itself.

Effective area must be calculated from the *realised gain* of the antenna, including mismatch. This might be where you are getting stuck.

The gain of a dipole doesn't drop much as the frequency drops. At $\lambda/2$ gain is about 2.1 dBi, at $\lambda/20$ gain is about 1.7 dBi. This is because the strict definition of gain is simply $P_{radiated}\over{P_{in}}$ and in a lossless antenna, all the power is radiated. The pattern just changes slightly as it gets smaller.  
But practical antennas also have a mismatch loss - some fraction of the power on the incoming transmission line is not radiated but reflected back. For very short antennas, most of the power is reflected back.  
So the *Realised Gain* or effective gain of the antenna includes the mismatch, losses in the antenna structure, and the radiation pattern. I summarised this in more detail in another answer.

Including inefficiencies of various kinds is very important, otherwise you are analysing some kind of ideal antenna and asking why it behaves strangely.  
In practice, the effective area of a real antenna will drop if the frequency increases *or* decreases too much from its design frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21630/antenna-aperature-for-out-of-band-frequencies, by oogieoogieful, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
