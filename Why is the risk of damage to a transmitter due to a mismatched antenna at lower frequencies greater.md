# Why is the risk of damage to a transmitter due to a mismatched antenna at lower frequencies greater?

*Tags: antenna, impedance, antenna-tuner, impedance-matching · score 9*

## Question

A quick follow-up to [this answer](How%20can%20I%20safely%20transmit%20without%20an%20antenna%20tuner%20or%20SWR%20meter.md)

... If the impedance mismatch is large, you risk damaging your radio, particularly on the lower frequencies ...

I'm sorry to be so dense, but uh why is the risk of damage to the Tx due to an antenna mismatch greater at lower frequencies? Is it merely that the wavelength is longer?

## Answer (score 5, by user2338215)

Another phenomenon that might play into the impression that HF transmitters are more susceptible to damage from high VSWR is feedline loss. Feedline loss increases as frequency increases. So at HF frequencies the power reaching the antenna feedpoint is higher due to lower feedline losses, and for the same reason the signal reflected back from the antenna feedpoint toward the transmitter is also higher when it reaches the transmitter. But at VHF frequencies the same feedline will absorb more of the signal going in both directions: making the feedline more effective as a dummy load. So for two antennas, one HF and the other VHF with identical VSWR measured at the antenna feedpoints, using identical feedlines, the VHF transmitter will see a lower VSWR at its antenna connector. This effect will be more apparent for higher-loss feedlines (e.g., coax cable) and less apparent for low-loss feedlines (ladder line, air-dielectric cables, etc.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1898/why-is-the-risk-of-damage-to-a-transmitter-due-to-a-mismatched-antenna-at-lowe, by VU2NHW, user2338215. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
