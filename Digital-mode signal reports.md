# Digital-mode signal reports

*Tags: digital-modes, snr, rssi · score 9*

## Question

When operating analog voice, we give a qualitative (or possibly just arbitrary) signal report, 'scoring' the signal either out of a maximum 'five by five', or a maximum '599'. How do you report the quality of the received signal when using digital modes?

When working a digital QSO, what are some different quantitative ways to report received signal quality or strength, and does the specific digital mode have any bearing on what type of report is given?

## Answer (score 6, by Seth)

On digital modes (particularly PSK31) RSQ (Readability, Strength, and Quality) is usually used for signal reports, instead of RST (Readability, Strength, CW Tone). There is some interesting history and background information on the RSQ system available at psb-info.net a site dedicated to the RSQ signal report.

**R = RSQ Readability (Percent characters correctly received):**

- R 1 – 0% Undecipherable
- R 2 – 20% Occasional words distinguishable
- R 3 – 40% Considerable difficulty, many missed characters
- R 4 – 80% Practically no difficulty, occasional missed characters
- R 5 – 95%+ Perfectly readable

**S = RSQ Strength (Signal over Noise rather than S-Meter):**

- S 1 – Barely perceptible trace
- S 3 – Weak trace
- S 5 – Moderate trace
- S 7 – Strong trace
- S 9 – Very Strong trace

**Q = RSQ Quality:**

- Q 1 – Splatter over much of the spectrum
- Q 3 – Multiple visible pairs
- Q 5 – One easily visible pair
- Q 7 – One barely visible pair
- Q 9 – Clean signal – no visible unwanted sidebar pairs

Here is a minified table version I found:

Another way signal reports are exchanged on the digital modes is by giving the Intermodulation Distortion (or IMD).

A quote from the RSQ website about what IMD is:

Inter-Modulation Distortion (IMD) is a report often exchanged during a PSK QSO as a figure of merit for the received signal. It is widely assumed that a very good IMD report for an idling signal is around -30db, a poor report around -20db with the worst possible at -10db.

Howard (Skip) Teller KH6TY who developed the first panoramic PSK31 transceiver and Digipan software advises that great care must be taken when attempting to measure IMD at the receiving station. The following advice was received from KH6TY:

"...IMD is the measurement of the first pair of unwanted sidebands to the desired ones, and if the signal to noise ratio is not around 26 db, you will start to measure the noise instead of the unwanted sidebands, which will be under the noise threshold. Also, if there is any distortion in the receiver, you create a false IMD reading. Whenever I measure a station's IMD, I have to be sure the S/N is good, and then I reduce the RF gain of my transceiver until the IMD stops falling and starts rising. At this point, I believe I have almost eliminated IMD caused by the receiver distorting the signal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/548/digital-mode-signal-reports, by Dan KD2EE, Seth. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
