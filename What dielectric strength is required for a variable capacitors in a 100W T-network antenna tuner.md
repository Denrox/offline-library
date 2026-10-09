# What dielectric strength is required for a variable capacitors in a 100W T-network antenna tuner?

*Tags: diy, antenna-tuner · score 4*

## Question

I would like to build a 100W T-network antenna tuner:

I have a 12-pole wafer switch, 12.5 meters of enameled copper wire (d=1.5mm) and a pair of 12-365pF variable capacitors rated 200V DC (dielectric strength) 250MΩ (insulation resistance).

There are some doubts regarding the capacitors. They are quite small (about 3x3x3 cm) and the plates are placed very close to each other. I have MFJ-971 tuner and it uses much larger capacitors which have much more space between the plates. Although this tuner is rated 200W.

I believe there are three problems. The first one is that the capacitors voltage rate is provided only for DC, but I'm going to apply AC. I don't know whether it's possible to convert DC rate to AC rate. The second problem is that I don't know how to estimate the maximum AC voltage that will be applied to the capacitors in the T-network. Finally, I could just build a tuner and check whether the capacitors will arc, but I don't know how to do it without the risk of damaging the transceiver (Yaesu FT-891).

Basically my question is: how to determine (theoretically, experimentally or both) whether it's safe to use given capacitors in this network?

## Accepted answer (score 4, by Brian K1LI)

I made a NEC model of an antenna with the dimensions of your "long wire" on 14.2MHz, found the values of C1, L1 and C2 that produce a 50$\Omega$ match and simulated the network to observe the voltages across the capacitors with 100W dissipated in the load. The voltage across C1 was 220VRMS, over 300V peak. Given all the variables that I did not evaluate, plus good design practice to allow considerable margin, I would say that your capacitors will not support 100W transmissions.

Qualitatively, this result agrees with the 500VRMS, minimum, recommended in the 100W Z-match in the ARRL *Handbook*.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13198/what-dielectric-strength-is-required-for-a-variable-capacitors-in-a-100w-t-net, by Aleksander Alekseev - R2AUK, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
