# Multipath propagation

In radio communication, **multipath** is the [propagation](Radio%20propagation.md) phenomenon that results in radio signals reaching the receiving antenna by two or more paths. Causes of multipath include atmospheric ducting, ionospheric reflection and refraction, and reflection from water bodies and terrestrial objects such as mountains and buildings. When the same signal is received over more than one path, it can create interference and phase shifting of the signal. Destructive interference causes fading; this may cause a radio signal to become too weak in certain areas to be received adequately. For this reason, this effect is also known as **multipath interference** or **multipath distortion**.

Where the magnitudes of the signals arriving by the various paths have a distribution known as the Rayleigh distribution, this is known as Rayleigh fading. Where one component (often, but not necessarily, a line of sight component) dominates, a Rician distribution provides a more accurate model, and this is known as Rician fading. Where two components dominate, the behavior is best modeled with the two-wave with diffuse power (TWDP) distribution. All of these descriptions are commonly used and accepted and lead to results. However, they are generic and abstract/hide/approximate the underlying physics.

### Interference

Multipath interference is a phenomenon in the physics of waves whereby a wave from a source travels to a detector via two or more paths and the two (or more) components of the wave interfere constructively or destructively. Multipath interference is a common cause of "ghosting" in analog television broadcasts and of fading of radio waves.

The condition necessary is that the components of the wave remain coherent throughout the whole extent of their travel.

The interference will arise owing to the two (or more) components of the wave having, in general, travelled a different length (as measured by optical path length – geometric length and refraction (differing optical speed)), and thus arriving at the detector out of phase with each other.

The signal due to indirect paths interferes with the required signal in amplitude as well as phase which is called multipath fading.

### Examples

In analog facsimile and television transmission, multipath causes jitter and ghosting, seen as a faded duplicate image to the right of the main image. Ghosts occur when transmissions bounce off a mountain or other large object, while also arriving at the antenna by a shorter, direct route, with the receiver picking up two signals separated by a delay.

In radar processing, multipath causes ghost targets to appear, deceiving the radar receiver. These ghosts are particularly bothersome since they move and behave like the normal targets (which they echo), and so the receiver has difficulty in isolating the correct target echo. These problems can be minimized by incorporating a ground map of the radar's surroundings and eliminating all echoes which appear to originate below the ground or above a certain height (altitude).

In digital radio communications (such as GSM) multipath can cause errors and affect the quality of communications. The errors are due to intersymbol interference (ISI). Equalizers are often used to correct the ISI. Alternatively, techniques such as orthogonal frequency division modulation and rake receivers may be used.

In a Global Positioning System receiver, multipath effects can cause a stationary receiver's output to indicate as if it were randomly jumping about or creeping. When the unit is moving the jumping or creeping may be hidden, but it still degrades the displayed accuracy of location and speed.

### In wired media

Multipath propagation is similar in power line communication and in telephone local loops. In either case, impedance mismatch causes signal reflection.

High-speed power line communication systems usually employ multi-carrier modulations (such as OFDM or wavelet OFDM) to avoid the intersymbol interference that multipath propagation would cause. The ITU-T G.hn standard provides a way to create a high-speed (up to 1 gigabit per second) local area network using existing home wiring (power lines, phone lines, and coaxial cables). G.hn uses OFDM with a cyclic prefix to avoid ISI. Because multipath propagation behaves differently in each kind of wire, G.hn uses different OFDM parameters (OFDM symbol duration, guard interval duration) for each media.

DSL modems also use orthogonal frequency-division multiplexing to communicate with their DSLAM despite multipath. In this case the reflections may be caused by mixed wire gauges, but those from bridge taps are usually more intense and complex. Where OFDM training is unsatisfactory, bridge taps may be removed.

### Mathematical modeling

The mathematical model of the multipath can be presented using the method of the impulse response used for studying linear systems.

Suppose you want to transmit a single, ideal Dirac pulse of electromagnetic power at time 0, i.e.

$$
x(t)=\delta(t)
$$

At the receiver, due to the presence of the multiple electromagnetic paths, more than one pulse will be received, and each one of them will arrive at different times. In fact, since the electromagnetic signals travel at the speed of light, and since every path has a geometrical length possibly different from that of the other ones, there are different air travelling times (consider that, in free space, the light takes 3 μs to cross a 1 km span). Thus, the received signal will be expressed by

$$
y(t)=h(t)=\sum_{n=0}^{N-1}{\rho_n e^{j\phi_n} \delta(t-\tau_n)}
$$

where $$N$$ is the number of received impulses (equivalent to the number of electromagnetic paths, and possibly very large), $$\tau_n$$ is the time delay of the generic $$n^{th}$$ impulse, and $$\rho_n e^{j\phi_n}$$ represent the complex amplitude (i.e., magnitude and phase) of the generic received pulse. As a consequence, $$y(t)$$ also represents the impulse response function $$h(t)$$ of the equivalent multipath model.

More in general, in presence of time variation of the geometrical reflection conditions, this impulse response is time varying, and as such we have

$$
\tau_n=\tau_n(t)
$$

$$
\rho_n=\rho_n(t)
$$

$$
\phi_n=\phi_n(t)
$$

Very often, just one parameter is used to denote the severity of multipath conditions: it is called the **delay spread**, $$T_M$$, and it is defined as the time delay existing between the first and the last received impulses

$$
T_M=\tau_{N-1}-\tau_0
$$

In practical conditions and measurement, the delay spread is computed by considering as last impulse the first one which allows receiving a determined amount of the total transmitted power (scaled by the atmospheric and propagation losses), e.g. 99%.

Keeping our aim at linear, time invariant systems, we can also characterize the multipath phenomenon by the channel transfer function $$H(f)$$, which is defined as the continuous time Fourier transform of the impulse response $$h(t)$$

$$
H(f)=\mathfrak{F}(h(t))=\int_{-\infty}^{+\infty}{h(t)e^{-j 2\pi f t} d t}=\sum_{n=0}^{N-1}{\rho_n e^{j\phi_n} e^{-j2 \pi f \tau_n}}
$$

where the last right-hand term of the previous equation is easily obtained by remembering that the Fourier transform of a Dirac pulse is a complex exponential function, an eigenfunction of every linear system.

The obtained channel transfer characteristic has a typical appearance of a sequence of peaks and valleys (also called *notches*); it can be shown that, on average, the distance (in Hz) between two consecutive valleys (or two consecutive peaks), is roughly inversely proportional to the multipath time. The so-called coherence bandwidth is thus defined as

$$
B_C \approx \frac{1}{T_M}
$$

For example, with a multipath time of 3 μs (corresponding to a 1 km of added on-air travel for the last received impulse), there is a coherence bandwidth of about 330 kHz.

---

*Source: Wikipedia, Multipath propagation (https://en.wikipedia.org/wiki/Multipath_propagation), by Wikipedia contributors, CC BY-SA 4.0.*
