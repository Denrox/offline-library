# Measuring losses from reactive near-field interactions in simple antennas

*Tags: antenna-theory, vertical-antenna, measurement, theory, end-fed-antenna · score 3*

## Question

## Question:

How can we measure the **total losses due to reactive near-field interactions** relatively simply, without far-field strength tests or mapping out the entire near field distribution?

I've included some background and a problem statement below to better contextualize my question:

## Background:

- Discussions on antenna system losses typically cover:

 - Transformer inefficiencies
 - Coax losses
 - Matching network losses
 - Ground losses (counterpoises, poor grounding)
- **This post is not about those losses**.
- Instead, the focus is on **losses caused by near-field reactive effects**.

### The Problem: Near-Field Reactive Losses

- **Near-field magnetic and electric fields** store, dissipate, or bypass power.
- **Example 1: Vertical Monopole Losses**

 - Ground-mounted with few radials → high losses due to grounding inefficiency.
 - Near-field interaction with lossy ground further increases loss.
 - Losses are especially significant when base-loaded.
- **Example 2: End-Fed Half-Wave Antennas**

 - **Different from vertical monopoles** → Feed point dominated by electric fields.
 - Often used with **poor counterpoises**, leading to increased ground interaction.
 - Harder to experiment with because moving the feed point changes other characteristics.
- **Example 3: Loop Antenna Near Structures**

 - Conductive/magnetic structures near the antenna **absorb or distort** the near field.
 - Common example: **building's steel structure, piping, wiring, nearby power lines, etc.** causing unexpected losses.

#### The Carbon Fiber Mast Issue

- Carbon fiber is **10,000x more resistive** than stainless steel/nichrome.
- **Not magnetic, but still conductive** enough to interfere.
- **Small separation distance** (0.2–0.3 mm) between the antenna and mast can cause coupling.
- **Key interactions**:

 - **Voltage maximum** → Dominated by electric field (capacitive coupling).
 - **Current maximum** → Dominated by magnetic field (inductive coupling).
- **Lifting the mast slightly above ground (30–50 cm) might help**, but field-induced currents still occur.

### The Question: Measuring Near-Field Losses

- How can we **measure current or monitor near-field losses** without far-field strength tests?
- **Can we measure total near-field losses?**
- *Without using intricate instrumentation or elaborate measurements* to map out the near-field distribution. Keep the measurement system to a practical level for amateur research projects.
- Possible approaches:

 - **Impedance curve & bandwidth analysis**

 - Compare bandwidth with & without obstructing structures.
 - Could bandwidth changes indicate reactive near-field losses? (Probably, unless other losses and the radiation do not change.)
 - Any example of such measurement used to answer the same question?
 - **Near-field probes** (E-field & H-field)

 - Place around antenna and compare readings before & after adding obstacles.
 - Need to distinguish **resonant frequency shifts vs. actual losses**.
 - Near-field probes give quantitative measurements but without globally comparable references, so the technique is primarily used for qualitative analysis or specific troubleshooting.
 - Any example of such a technique used to answer the same question?

#### Key points

- **Is there a reliable, practical way to measure near-field losses?**
- Common methods rely on **far-field system efficiency**, but this post seeks **simpler, direct measurements**.
- Any thoughts or techniques to **quantify near-field losses** would be appreciated!

## Accepted answer (score 3, by tomnexus)

Two ways I've measured this, and two I've read about:

**By comparing gain - for antennas with well-controlled radiation patterns**

Once I developed cutting charts for a "rubber duck" handheld antenna - an open helical spring of copper-plated steel, impregnated with soft black rubber. Cut to length for your frequency, with a plastic cap.

I measured the efficiency of this antenna by comparing its signal strength to a simple copper wire monopole, both mounted on a reasonably large groundplane. (It was terrible: -6 dB, or 25% efficient, at 150 MHz). I was careful to measure the received power at a reasonable distance but not so far that reflections from the rest of the room would be significant. In the main lobe of the monopole's elevated pattern - about 15 degrees.

This method only works if you can swap for a known high-efficiency antenna, and can control the environment fairly well. OK for a VHF/UHF monopole, not very good for a HF Hustler-type antenna.

**By measuring Q, and Re(Z) and comparing to theory or simulation**

For a base-loaded 108" whip antenna mounted on a vehicle, there are several options for the loading coil. Some use an open wire coil, but a ferrite core coil can be more efficient. Then the coil needs to be made with care, keeping steel parts out of the magnetic field as much as possible (no metal end caps!).

In this case the incumbent antenna had an air core inductor. Its losses were sufficient that the antenna would offer a good match to 50 ohms (a few percent efficient at ~7 MHz). The new antenna with a ferrite core was about 6 dB more efficient, and this had two notable effects: the real part at resonance was only 12 ohms so required a small parallel capacitor at the feed, and the Q was noticeably higher, such that you had to be careful to take your hand away while tuning, close the vehicle doors, etc, to get it tuned correctly.

The actual efficiency of the antenna, with its substantial ground loss, coil&ferrite resistance and whip resistance, could be calculated from the Q, compared to the theoretical Q of the same length whip with a perfect inductor.

This new base load quickly took over the market for HF antennas on trucks, they appreciated the extra 6 dB of radiated power.

**A massive outdoor test range**

The US navy I believe, made a test range for measuring HF antenna effiency, with a similar principle to my first example above. The range was about 1 km long, with transmit and receive sites both on the beach, water between them, and no obstacles nearby to cause reflections.

Total antenna efficency could be calculated by measuring field strength. Antenna efficiency excluding ground loss could be calculated by comparing a full length antenna to the compact antenna under test.

I read a paper about this 20 years ago, I can't find it now.

**WSPR antenna comparisons**

On a continent with many WSPR receiving stations, you can compare HF antennas with similar radiation patterns, by transmitting a low power signal and looking at the WSPR signal reports. It helps to transmit at several different (low) power levels. Very high (> 0 dB) and very low (<-20 dB) reports should be excluded, but reports in the middle can be quite accurate when averaged over several cycles.

This won't work for very different antennas, say a vertical monopole compared to an end-fed horizontal dipole, as there will be permanent changes in received power that can't be averaged out.

It's also possible to do this test while receiving, again selecting the stations carefully before averaging. I've also used this to measure the effect of a local noise source (fish pond waterfall pump).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23385/measuring-losses-from-reactive-near-field-interactions-in-simple-antennas, by Ryuji AB1WX, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
