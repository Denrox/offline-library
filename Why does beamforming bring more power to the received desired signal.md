# Why does beamforming bring more power to the received desired signal?

*Tags: antenna, phased-array, dsp · score 4*

## Question

Consider a normal array model with $N$ element. The output of the array is given by,

$$\mathbf{y}=\mathbf{w}^H\mathbf{x}=\mathbf{w}^H\mathbf{as}$$

where


$\mathbf{a}=[a_1,...,a_N]^T=\in\mathbb{C}^{N\times 1}$ is the manifold of the desired signal (I ignore the noise for simplicity).

 - $T$ denotes the transpose.

$\mathbf{s}\in\mathbb{C}^{1\times M}$ is the desired signal

 - $M$ is the number of snapshots and
 - the power of $\mathbf s$ is $\sigma_s^2=\operatorname E(|\mathbf{s}(t)|^2)=\operatorname E(\mathbf{ss}^H)=\frac{1}{M}(|\mathbf{s}(1)|^2+...+|\mathbf{s}(M)|^2), \mathbf{ss}^H=|\mathbf{s}(1)|^2+...+|\mathbf{s}(M)|^2$
 - $t$ is the time index,

$\mathbf{x}\in\mathbb{C}^{N\times M}$ is the desired signal incident at each antenna, $\mathbf{x}(t)=[\mathbf{x_1}(t),...,\mathbf{x_N}(t)]^T=[a_1\mathbf{s}(t),...,a_N\mathbf{s}(t)]^T$


$\mathbf{w}\in\mathbb{C}^{N\times 1}$ is the receiving weight (where $\mathbf w = \mathbf a$),


$^H $ denotes the conjugate transpose and


$\operatorname E$ denotes the expectation.

Therefore the power of the output $y$ is given by, $$P_y=\operatorname E (|\mathbf{y}(t)|^2)=\frac{1}{M}(|\mathbf{y}(1)|^2+...+|\mathbf{y}(M)|^2)=\frac{1}{T}(\mathbf{y} \mathbf{y}^H)=\frac{1}{T}(\mathbf{a}^H\mathbf{ass}^H\mathbf{a}^H\mathbf{a})=\sigma_s^2(\mathbf{a}^H\mathbf{a}\mathbf{a}^H\mathbf{a})=\sigma_s^2(N\times N)=N^2\sigma_s^2$$

I think the power of the desired signal that incident at the receiving array is, $$P_{inc}=P_{x_1}+...+P_{x_N}=\operatorname E(|\mathbf{x_1}(t)|^2)+...+\operatorname E(|\mathbf{x_N}(t)|^2)=\frac{1}{M}(|\mathbf{x_1}(1)|^2+...+|\mathbf{x_1}(M)|^2)+...+\frac{1}{M}(|\mathbf{x_N}(1)|^2+...+|\mathbf{x_N}(M)|^2)=\frac{1}{M}a_1\mathbf{s}(a_1\mathbf{s})^H+...+\frac{1}{M}a_N\mathbf{s}(a_N\mathbf{s})^H=\sigma_s^2a_1a_1^H+...+\sigma_s^2a_Na_N^H=N\sigma_s^2$$

($\operatorname{tr}(\mathbf A)$ denotes the trace of $\mathbf A$)

then the beamforming brings gain of $N$ to the power of the received desired signal.

What confuse me is why the total power of desired signal is changed. According to my understanding, the power should remain unchanged as the signal power incident at the array is certain and beamforming won't add power to it.

I think I was wrong but I don't know where. Is it related to the concept of effective array and directivity gain? Am I calculating the desired signal power that incident at the array before beamforming right?

I add the figure below to help me explain my problem. My question can be summarized as **why** the received signal power after beamforming (which is power of $y(t)$) is $N$ times of signal power of incident signal power or signal power before adding up? Is there a physical explanation for this?

## Answer (score 3, by hotpaw2)

I don't understand the parameters of your equations.

But ignoring the equations and answering the text of the question: beam forming depends on frequency and phase. If the phase of the output of two beam forming elements is equal in magnitude but opposite in phase at the angles and frequency of measurement, the received output power output from that 2 element array is zero. If the phase and power are the same, the output power can be doubled. etc.

Antenna directivity is associated with a (spherical) angle of EM wave incidence and frequency. The number of elements can affect an antenna's effective aperture size. But that's also angle and frequency dependent.

## Answer (score 2, by webmarc)

Since the originating signal is not a unidimensional, laser-like effect, but rather an inverse-square-law wave... an enormous percentage of the original signal is neglected by a single element antenna system and a minuscule percentage is captured.

Adding additional elements does not increase the power of the transmitted signal, rather the amount of RF neglected by the array is decreased.

When your reference power is what is transferred to a single element (instead of the transmitted power), then you have positive gain.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18715/why-does-beamforming-bring-more-power-to-the-received-desired-signal, by tyrela, hotpaw2, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
