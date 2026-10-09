# (When) does a transceiver re-reflect 100% of reflected power?

*Tags: antenna-theory, impedance-matching, feed-line, transmission-line · score 5*

## Question

There has been a long discussion of one question [here](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md). Phil, W8II and I agreed that it's better to post a separate question.

There are several sources (some editions of "The ARRL Handbook", "Reflections: Transmission Lines and Antennas", Understanding SWR by Example) where you can find plots like this one:

Let's say the antenna impedance on a given frequency is 250 Ohm, the feedline is 50 Ohm. Between the antenna feed point and the feedline SWR = 5, ~44% reflected power. The model says that 44% of the transmitted power will be reflected from the antenna to the feedline, re-reflected by the transceiver, and go back to the antenna. If the feedline is lossless, eventually 100% of power will be radiated, regardless of SWR. If the feedline has losses, there will be additional losses as the plot shows.

The problem is that none of the sources explains well **why the transceiver suppose to re-reflect all the power**. Actually, in "Reflections" on p13-5 it's said that the model is not valid for modern solid-state PA. This is what the long discussion was about.

Phil suggested that what actually was meant is that *a tuner* between the transceiver and the feedline re-reflects the power (a tuner is lossless for this model), not the transceiver per se. If this is true, I don't quite understand the situation either. On one hand, it is stated that since the PA sees 1:1 SWR there is no reflected power going through the tuner. This makes sense. But for **received** signals, we say that the same tuner matches whatever impedance it sees to 50 Ohm and passes all the signals through to the transceiver. I don't see how it's possible for the same device to pass signals in one case and reflect in another when signals go in the same direction, to the transceiver.

So actually I have several questions: 1) is the described model accurate for modern transceivers? 2) if yes, is a tuner required? if no, why? 3) does the tuner actually passes the received signals and reflects the transmitted signals?

## Accepted answer (score 3, by Jens)

The Question addresses a persistent confusion which is widespread especially in the ham radio community and can be tracked down to some published material (here no names!) and has survived since many years.

However, a clarification can be straightforward and does not require complicated math. This answer starts from the “Total Feedline Loss” equation that had been derived in a previous thread and often appears in ham radio publications:

Behind this correct loss equation there are crucial assumptions for its validity, including (1) The characteristic impedance of the feedline (e.g., coax) must be a real (not complex) value, which is reasonably satisfied at higher RF frequencies (but probably not for 40m, 80m, 160m bands for which additionally the physical line-length may become much shorter than the electrical wavelength on the line). – The second (2) assumption is much more relevant in the context of this thread: A (lossless) tuner is assumed at the input of the feedline. This tuner performs complex conjugate impedance matching such that the transceiver can feed its maximum available power into the feedline.

Because of reflections at the far-end, e.g., at the feed-point of an antenna, a fraction of the transmit power (in terms of voltage/current waves) returns to the input of the feedline. There, the returning waves feel the output impedance of the matching network (tuner). This impedance is the complex conjugate of the feedline input impedance; it determines, together with the feedline characteristic impedance (e.g., 50Ω coax), the extent of reflection expressed by the (complex) reflection coefficient. Note, there is no total re-reflection. Such total re-reflection would require an infinite, or a zero, or a pure reactance impedance; all these cases do not apply here, regardless of the tuner being a lossless LC network which transforms the output impedance of the transceiver (e.g., 50Ω).

However, the above “Total Feedline Loss” equation is frequently derived based upon a perception of total re-reflection and results from an infinite geometric series. And, indeed, the equation is correct! So, what is going on? Well, applying the idea of total re-reflection is a somewhat dirty way to arrive at a correct equation. The end-result for the total loss is the same, regardless of either applying the fake of total re-reflection, or the true physics of the actual phase-accurate superposition of partially reflected voltage/current signal components and applying the true reflection coefficient. Although the end-result is the same, the bouncing-steps during the transient period are quite different. The above “Total Feedline Loss” equation is valid, although its derivation is very often flawed, which leads to confusion, paradoxes and such concerns like expressed in the Question.

(Credit: Cartoon by Tayfun Agül)

Under the condition of complex conjugate matching, the “Total Feedline Loss” formula does not show explicitly the reflection coefficient that is relevant for the re-reflection of voltage/current signal components that return to the feedline input.

Of course, when arriving at the feedline input, the same partial re-reflection applies not only to a returning fraction of the transmit signal, but equally also to any receive signal; there is no difference, assuming the Tx and Rx signals are similar in frequency, implying similar reflection coefficients.

The following experiment illustrates the difference in bouncing-steps. We assume a system that is easy to calculate (and easy to measure!). A lossy 50Ω coax is terminated into an ohmic resistor of 290Ω. This load resistor implies that half of the forward power is reflected at the load, $$|Γ|^2=|(290-50)/(290+50)|^{2}=0.5$$ The coax line attenuation is 3dB (i.e., L=0.5). The coax length is a multiple of (λ/2); such length-choice avoids here the hassle of complex values and implies that the feedline input impedance is also ohmic; it is 104.9Ω (obtained by calculation, or Smith Chart etc.). We assume a (lossless) LC tuner that matches the feedline input impedance of 104.9Ω to the transceiver output impedance (say, 50Ω). Thus, the tuner output impedance (seen when looking from the feedline into the tuner) is adjusted to be also 104.9Ω. The signal components that return to the feedline input, experience reflection with a coefficient $$Γ_s=(104.9–50)/(104.9+50)=0.35$$ or $$|Γ_s|^2=0.13$$ (instead of any faked $|Γ_s|^2=1$).

Inserting the values into the “Total Feedline Loss” equation gives a system loss of 5.44dB (or linear 0.2857). If the maximum available power from the transceiver is 100W then – after the bouncing has finished – a steady power of 28.57W is delivered to the load resistor.

Connecting to the diagram in the Question, our system loss of 5.44dB includes the 3dB “Line Loss in dB When Matched” plus 2.44dB “Additional Loss in dB Caused by Standing Waves”; note our SWR is here (290/50) =5.8. The transceiver pumps 100W into the feedline. Part of this power (28.57W) is dissipated in the load at the end of the feedline; the remaining part (71.43W) is dissipated in the feedline which is quite lossy (here 3dB, means 50W matched line loss plus 21.43W additional loss due to SWR). There is no power going back into the transceiver because it is (via a (lossless) tuner) impedance-matched to the input impedance of the feedline. All power of 100W remains, and is dissipated, inside the system of feedline plus connected load. This applies regardless of the actual reflection coefficient (here $Γ_s=0.35$) being different from 1.

@sm5bsz (comment on separate Answer): “… *regarding the diagram … It shows the fraction of the power sent into the cable that is converted to heat. (The rest is delivered to the antenna.)*” (quote) That is a misleading statement. The curves in the diagram show only the loss due to SWR. The total loss (and thus the total power converted to heat) is higher by the added Matched Line Loss of the cable on its own.

For comparison, we also consider the case of a lossless line (L=1). The “Total Feedline Loss” becomes 0dB, regardless of mismatch at the load side. The input impedance of the feedline is now identical to the load resistor (remember the line being a (λ/2)-line), and the tuner is adjusted for an output impedance of also 290Ω. The reflection coefficient at TL input becomes $Γ_{in}=Γ=0.71$. The power delivered to the load resistor – after the bouncing has finished – equals now the maximum available power of 100W from the transceiver.

The following table shows the bouncing for the two cases of line attenuations and for the “Reality” of true **partial** re-reflection, and for the “Misconception” of **total** re-reflection. $T_L$ is the one-way delay time of the coax. The lower the line loss (in dB), the more evident become the transient discrepancies, and the bouncing will take longer until the steady state is reached.

The “Reality” cases can be verified by measurements and by simple simulations; here is a simulation schematic (LTspice) for the discussed second case of 0dB feedline loss. The voltage $Us$ is scaled accordingly for a maximum source power of 100W.

**More general:** If the condition of complex conjugate impedance matching (e.g., by a tuner) is satisfied at the input of the transmission line, also the reflection coefficients $\Gamma_{in}$ at TL input and $\Gamma_{s}$ of the source (or tuner output) are complex conjugate to each other, $$\Gamma_{s} = \Gamma_{in}^{\ ^{*}}$$ This implies $$|\Gamma_{s}| = |\Gamma_{in}| = L\cdot |\Gamma |$$ where $\Gamma$ is the reflection coefficient at the load, and $L$ (linear) is the Matched Line Loss. Therefore, we can rewrite the formula for the “Total Feedline Loss” as function of $|\Gamma_{s}|$ explicitly: $$ -10\log \left( L\frac{1-|\Gamma |^{2}}{1-L^{2}|\Gamma |^{2}}\right) = -10\log \left( L\frac{1-(|\Gamma_{s}|/L)^{2}}{1-|\Gamma_{s}|^{2}}\right) $$ Obviously, the complex conjugate matching at the TL input (e.g., by a tuner) does **not** imply $|\Gamma_{s}|=1$.

If no complex conjugate matching applies at the transmission line input, the “Total Feedline Loss” formula (in dB) becomes $$ -10\log\left( L\cdot\frac{1-|\Gamma |^{2}}{1-L^{2}|\Gamma |^{2}} \cdot \frac{4R_{s}R_{in}}{|Z_{s}+Z_{in}|^{2}} \right) $$ where the (complex) $Z_{s}=R_{s}+jX_{s}$ is the (Thévenin equivalent) source output impedance at the given operating point; and the (complex) $Z_{in}=R_{in}+jX_{in}$ is the input impedance of the transmission line. – If the two impedances are complex conjugate to each other (tuner case), $Z_{s}=Z_{in}^{\ ^{*}}$, the corresponding last quotient in the above total loss formula becomes 1. Note the characteristic impedance, $Z_o$, of the transmission line is still assumed to be a real value. (Obtaining/measuring the two impedances $Z_{s}$ and $Z_{in}$ is perhaps beyond the scope of this Question.)

An Excel tool downloadable at www.rfclb.space/#TLine does all calculation and allows for “Total Feedline Loss” trade-offs considering different approaches of impedance matching by a tuner (far-end; near-end; complex conjugate matching; zero-reflection), or tuning by simple feedline extension; the tool covers also the case of complex characteristic impedance of the transmission line.

**Conclusion** answering to the 3-fold Question:

(1) The diagram in the Question and the “Total Feedline Loss” formula are correct; both are based upon the condition of complex conjugate matching (CCM) at the feedline input, achievable for instance by a lossless tuner. This principle applies regardless of (modern or heritage) technology used in the transceiver. – (2) Whether a tuner is required depends on the situation and the question to what extend the CCM condition can be, or is already, achieved by the feedline system, including the transceiver, i.e., w/o insertion of a tuner. – (3) No, the tuner cannot distinguish between (a) transmit signal components that, due to reflection, might return to the feedline input; and (b) any receive signal. Partial re-reflection applies for both signal components, regardless of being Tx or Rx related. The CCM condition does **NOT** imply any necessity of “total re-reflection” with $|Γ_s|=1$.

$$ $$ **PS:** For those who wish to further dive into the nitty-gritty-down-in-the-weeds technical details, here is a diagram for a re-reflection assessment at the feedline input.

## Answer (score 2, by Phil Frost - W8II)

This model makes two simplifying assumptions:

1. losses are uniform throughout the transmission line, and
2. there is a lossless tuner between the transmitter and the feedline adjusted such that the transmitter sees a matched load

The first assumption isn't directly relevant to your question and is discussed in more details in [the answer you linked](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md).

Now about the second assumption, realize "the transmitter sees a matched load" implies "the transmitter sees no reflected power". This is because any apparent deviation from the characteristic impedance of the feedline must be the result of reflected power. If the transmitter sees no reflected power and yet the antenna is known to be mismatched and thus did reflect some power, if the transmitter didn't see that reflection it must be because the tuner re-reflected the power back at the antenna.

More rigorously, the tuner is a 2-port network which when properly adjusted presents a reflection coefficient which cancels any reflected power.

Let's say looking at the antenna through the feedline, a reflection coefficient of $\Gamma$ is observed. We then want a tuner with a scattering matrix of:

$$ \begin{bmatrix} -\Gamma & ?\\ ? & ? \end{bmatrix} $$

This means for a wave going into port 1 of the tuner (from the transmitter) of amplitude 1, a reflected wave back out port 1 of amplitude $-\Gamma$ will be observed.

With such a scattering matrix, the transmitter will see a reflection coefficient of $\Gamma$ from the antenna, and $-\Gamma$ from the tuner, for a sum reflection coefficient of zero, meaning the transmitter sees no reflected power and a matched load.

We assume the tuner is lossless and passive, which means the sum of squares of the values in any column of the matrix must be 1. Squares, because power is proportional to the square of amplitude. And a sum of 1, because no energy is lost or added. So:

$$ S_{11}^2 + S_{21}^2 = 1 \\ -\Gamma^2 + S_{21}^2 = 1 \\ S_{21}^2 = \Gamma^2 + 1 \\ S_{21} = \pm\sqrt{\Gamma^2 + 1} $$

The math is telling us we could make a tuner which inverts $S_{21}$ or not; in practice we will have to pick one or the other when we build the tuner, so I'm just going to arbitrarily pick $S_{21} = \sqrt{\Gamma^2 + 1}$

Therefore, we can fill it a bit more of the matrix:

$$ \begin{bmatrix} -\Gamma & ?\\ \sqrt{\Gamma^2 + 1} & ? \end{bmatrix} $$

The tuner is also passive and made of isotropic materials, and therefore is a reciprocal network. This means $S_{mn} = S_{nm} $, in other words, the matrix is symmetrical across the diagonal. So we can fill in more of the matrix:

$$ \begin{bmatrix} -\Gamma & \sqrt{\Gamma^2 + 1}\\ \sqrt{\Gamma^2 + 1} & ? \end{bmatrix} $$

Again because the tuner is assumed lossless we can infer $S_{22}$ from $S_{21}$:

$$ \begin{bmatrix} -\Gamma & \sqrt{\Gamma^2 + 1}\\ \sqrt{\Gamma^2 + 1} & -\Gamma \end{bmatrix} $$

With the tuner's scattering matrix calculated we can answer all kinds of questions about how waves will reflect or pass through the tuner.

We've already discussed how power into port 1 (from the transmitter) is partially reflected ($S_{11} = -\Gamma$), and this cancels the reflection that is seen from the mismatched antenna. But what about receive?

Because a tuner is reciprocal, the same thing happens on receive: some of the power from the antenna is reflected back at the antenna. Is that a problem?

Not really. An antenna is also a 2-port device: one port being the feedpoint, and the other "port" being free space. The antenna is also reciprocal and nearly lossless, so its scattering matrix is nearly the same as the tuner, just with the sign flipped. This means power into the free space port (the signal we wish to receive) will see some non-zero reflection coefficient (a mismatch), but it will also see the opposite reflection coefficient from port 2 of the tuner, the two summing to zero.

What about this business of solid-state versus tube PAs?

The distinction really has nothing to do with tubes vs. transistors, but rather the typical design around them. Nearly all tube amplifiers include a tuner: they must because the output impedance of a tube is very high, and thus a poor match for coax. Moreover, the output impedance varies with frequency and temperature, so the matching network must be variable. More moreover, in the days before transistors a coax feed wasn't as common as it is today. The feedline might be twin-lead with an impedance anywhere between 200 and 900 ohms, or even a random wire with who knows what impedance. A transmitter would be expected to drive all of these loads.

For example:

This is from a page by Greg Latta. Note the variable capacitor and switchable taps on the inductor: this is an L-network and could be used as an antenna tuner on its own. Tuning this network is part of the standard operating procedure for a tube PA, so in practice a tube PA always has an "antenna tuner".

Solid-state transmitters on the other hand don't necessarily have this feature. The output impedance of a transistor is lower and more stable, and thus it's feasible to design the circuit to drive a 50 ohm load without variable components.

For example here's the PA for the Softrock RXTX:

Q7 and Q8 are the PA finals: notice there's nothing matching them to the load except a fixed transformer, T4. (There is a filter that follows this, though at a glance it appears to have a 50 ohm input and output and thus serves no purpose in matching.)

Of course many solid-state radios (especially modern ones at higher price points) include an automatic tuner for convenience, making them similar to tube PAs.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18318/when-does-a-transceiver-re-reflect-100-of-reflected-power, by Aleksander Alekseev - R2AUK, Jens, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
