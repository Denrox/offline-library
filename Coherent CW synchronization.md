# Coherent CW synchronization?

*Tags: cw · score 7*

## Question

When using coherent CW, how is the receiver frequency and/or Morse Code dot clock synchronized to the transmission precisely enough to allow for synchronous decoding?

## Accepted answer (score 9, by Phil Frost - W8II)

According to Coherent CW ... "The More You Know About a Signal, the Easier it is to Copy" by Peter Eaton, WB9FLW and George Heron, N2APB:

Coherent software has several other convenient features in addition to auto-tune. It has a fine tuning aid that measures the incoming 800 Hz audio signal (with 0.1 Hz resolution!), and a frame-phasing tracking loop that determines if the SNR would be better had the window ended 1 cycle (1.25 ms) earlier or 1 cycle later. The program adjusts the 100 ms processing frame slightly forward or backward depending on the trend of the signal over time. Thus, once synchronization has been established, Coherent is able to adjust the phasing as necessary to maximize the SNR, further reducing the need for rig stability and frequency standards. All that's necessary is a reasonably stable transceiver (or a DDS VFO, as in our case), the Sigma-Delta interface board and a computer.

This is a form of clock recovery, as used in many digital modes.

The clock is set to 100ms intervals, by definition of the protocol. To begin, the receiver arbitrarily starts its clock, so the receiver and transmitter are clocked at the same speed but some arbitrary phase.

For each 100ms interval, the receiver actually calculates *three* correlations:

- one aligned with the current clock
- one slightly ahead of the clock
- one slightly behind the clock

The output of each of these correlations is a number from 0 (no carrier detected at all, space) to 1 (only carrier detected, mark). Of course in the presence of noise, the actual numbers are somewhere between those extremes, and the difference between the mark and space values gives you some idea of the SNR. For example, if the SNR is very poor, a space might be 0.02 and a mark might be 0.06. If the SNR is very good, a space might be 0.02 and a mark 0.99.

Looking back at the past few periods, we can then ask, would the SNR be better if the clock phasing were shifted forwards or backwards? If so, then we shift the timing a little bit. Eventually synchronization is reached.

Frequency synchronization is more obvious. They don't really say how the incoming frequency is measured, but a likely technique is autocorrelation of the signal. This gives you a direct measurement of the predominant frequency of the signal, and the difference of this to the correlation filter (800 Hz in the quoted design) gives you a frequency error signal. This error signal is usually low-pass filtered to prevent excessive wandering due to noise, and then by adjusting the receiver's tuning we can drive the frequency error to zero.

It's not described in the excerpt above, but another trick is used to eliminate the requirement for exact phase coherence between receiver and transmitter. The receiver actually correlates the received signal with two filters, which differ by a 90 degree phase shift. This guarantees that whatever the relative phase of the stations, the signal will be received. This is not unlike using a circularly polarized antenna to receive a linearly polarized transmission: it doesn't matter if the transmission is polarized vertically, horizontally, or something in-between: it will be received equally well by the circularly polarized antenna. The cost is a 3dB loss, but the gain is the lack of requirement for phase coherence, which is difficult to implement without impracticably stable components, or a second channel for synchronization.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1542/coherent-cw-synchronization, by hotpaw2, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
