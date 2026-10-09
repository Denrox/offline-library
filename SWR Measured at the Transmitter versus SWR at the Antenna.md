# SWR Measured at the Transmitter versus SWR at the Antenna

*Tags: antenna, transmission-line, impedance-matching, math, swr-meter · score 9*

## Question

It is fairly well understood that due to transmission line losses, the SWR as measured at the transmitter will be less than the SWR at the antenna.

Some of the new antenna analyzers and some vector network analyzers can 'zero out' or compensate for the losses in the transmission line. This allows them to display the SWR at the antenna while taking the SWR measurement at the transmitter end.

Can something similar be done using a much less expensive, conventional SWR meter or dual needle SWR meter?

## Accepted answer (score 6, by Glenn W9IQ)

Given the matched loss of the feedline and the SWR at the transmitter, we can calculate the SWR at the antenna in three simple steps.

First convert the SWR at the transmitter to the corresponding magnitude of the reflection coefficient (Gamma), or MRC for short within the context of this answer. The MRC is the magnitude of the complex ratio of the reflected voltage wave to that of the incident voltage wave. We can calculate the MRC using this formula:

$$|\Gamma|=\frac {\text{SWR}-1}{\text{SWR}+1} \tag 1$$

where SWR is the SWR (without the :1 notation) at the point of measurement.

For example, if the SWR at the transmitter is 3:1, the corresponding MRC ($|\Gamma|$) at the transmitter is 0.5.

Now we convert this MRC at the transmitter to its corresponding MRC at the antenna by reversing the effect of the losses in the feedline:

$$|\Gamma_{\text{ant}}|=\frac{|\Gamma_{\text{xmtr}}|}{e^{(-2*L_{\text{dB}}/8.6858)}} \tag 2$$

where LdB is the matched loss of the feedline in dB. Note that the division by 8.6858 converts dB loss to Nepers - a more convenient unit for transmission line calculations. The effect of this loss on SWR has been described in [Does Coax Limit the Maximum SWR a Transmitter Sees](Does%20Coax%20Limit%20the%20Maximum%20SWR%20a%20Transmitter%20%27Sees%27.md).

Using formula 2 with a feedline that has a matched loss of 1.0 dB along with the previously calculated 0.5 MRC at the transmitter, we find that we have an MRC of 0.63 at the antenna. We can now convert this to the SWR at the antenna using the formula:

$$\text{SWR}=\frac{1+|\Gamma|}{1-|\Gamma|} \tag 3$$

So we find using formula 3, that the SWR that measured 3:1 at the transmitter is 4.4:1 at the antenna.

These formulas are not too difficult to do on a hand calculator, but by placing them into a spreadsheet, it is possible to construct a nice chart depicting the transmitter SWR versus antenna SWR for a given amateur band:

This idea could be extended to show a differently colored series plot on the chart for each band of interest using the respective matched feedline loss for the band.

Note: It should be pointed out that the antenna SWR as calculated here is technically the *minimum* antenna SWR. This is due to the coax limiting the maximum possible SWR at the transmitter as presented in [Does Coax Limit the Maximum SWR a Transmitter Sees](Does%20Coax%20Limit%20the%20Maximum%20SWR%20a%20Transmitter%20%27Sees%27.md).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9757/swr-measured-at-the-transmitter-versus-swr-at-the-antenna, by Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
