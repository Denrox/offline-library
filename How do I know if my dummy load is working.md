# How do I know if my dummy load is working?

*Tags: dummy-load · score 9*

## Question

I understand why a dummy load is used, but (aside from it getting hot) how do I know if it's doing it's job and doing it's job well?

In my specific case, I'm using a Hack RF One SDR and a Souked SMA Dummy Load 50 Ohm.

## Accepted answer (score 11, by Kevin Reid AG6YO)

A dummy load, or terminator, consists of a non-inductive power resistor (or multiple resistors in series and parallel) and a heat sink, both rated for the maximum power to be dissipated.


The simplest test on a dummy load you can perform is to **measure it with an ohmmeter** — it should be 50 Ω (or whatever the specified impedance is). Wiggle the connections while you're doing this to make sure it does not have an intermittent open circuit — I've found this to be a problem with some cheap terminators.


The above test tells us that it is 50 Ω at DC, or 0 Hz. It is possible that its impedance will be something else at higher frequencies; if it is, this is a design flaw (or limitation), because this impedance is affected by the geometry of the conductors between the resistor and the input connector. If you wanted to test this property, you would want an **antenna analyzer** which can sweep over the relevant frequency range and report the impedance or SWR, which you would check for being reasonably close to 50 Ω.

If you already have a transmitter, then you can in principle use a *SWR meter* combined with the transmitter, but most SWR meters that are sold separately are not sensitive enough for this little power to produce any reading at all. Additionally, the entire point of using a dummy load at all in this low-power situation is to avoid impedance-mismatch reflections damaging the transmitter (or triggering protective power fold-back), and if you need to test the dummy load then you in principle don't know whether there will be reflections or not, so it's not a safe test. In theory.


A dummy load should have the expected impedance, but so does an antenna. The difference between a dummy load and an antenna is that the dummy load mostly does not radiate. To test this characteristic, you would **use a receiver** to determine the radiated signal strength — ideally one with a signal strength meter (S-meter or RSSI). (You could use a *field strength meter* for calibrated results, but if you have that specialized gear...)

Note that there will always be *some* radiation — if not from the dummy load, then from the transmitter. No shielding is perfect. (And the HackRF One has no shielding, anyway.)


The final characteristic of a dummy load is power handling capability. To test this, increase transmit power until you smell smoke, then buy a replacement!

But you're not going to manage that with the HackRF One. I wouldn't even expect any noticeable warmth.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5585/how-do-i-know-if-my-dummy-load-is-working, by M6JNY, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
