# Will I get cleaner keying by keying the oscillator, or interrupting the amplifier B+?

*Tags: diy, cw, transmitter, equipment-design · score 4*

## Question

One of my goals as a new ham is to homebrew my own transmitter (using vacuum tubes, aka valves). Initially I'll stick with CW for the transmitter, though over time I might build an AM modulator or even attempt an SSB modulator/filter. For the CW iteration, I plan to use a vacuum tube Hartley oscillator, with the tap on the oscillator coil positioned to minimize drift on key-down.

I've read of some CW transmitters with high voltage at the key, suggesting they were interrupting the B+ to the output tubes (for power levels above QRP, this may be several hundred volts; for higher power, it may run to several thousand). Obviously, if I do this, I'd use a relay to keep the high voltage inside the case.

For other designs, however, I've seen reference to keying the oscillator -- either interrupting the output of the oscillator before it reaches the first output tube's grid, or interrupting the plate or grid on the oscillator's own tube to completely stop the RF (potentially also leading to relatively high voltage at the key).

As I understand it, both can work well enough to have survived until transistors replaced vacuum tubes for most applications, and obviously the quality of the keyed output depends on multiple other factors (stability of the oscillator, rise and fall time of the chosen keying control, etc.).

From the standpoint of signal quality, however, is there a good reason to prefer one over the other?

## Answer (score 6, by Brian K1LI)

Highest frequency stability is generally achieved when the oscillator is kept running while some following stage (or stages) is (are) keyed. However, the very high *Q* of a crystal-controlled oscillator permits direct keying. While the cathode, grid or plate of any stage can be keyed depending on design goals and available parts, an oscillator should be keyed outside of the primary frequency-determining circuitry. Cathode keying does not place high AC or DC voltage on the key terminals.

"Chirp" can also result when the *load* on the oscillator output varies from key-up to key-down. This can be avoided by providing a "buffer" amplifier stage between the oscillator and the amplifier. For example, K5DH's 807 CW Transmitter uses a 6AG7 pentode either as a cathode-keyed crystal-controlled oscillator *or* as a cathode-keyed buffer amplifier according to the position of SW1, which brings the V1 cathode to AC ground through a .01uF bypass capacitor. Note that the cathodes of both the oscillator/buffer *and* the amplifier stages are keyed to prevent oscillator feed-through to the antenna during key-up.

Radios like the Heathkit DX-60 and the Drake 2-NT employed a similar architecture but used *grid block keying*, which is thoroughly explained in the cited manuals, placing a high negative DC voltage on the key terminals.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13104/will-i-get-cleaner-keying-by-keying-the-oscillator-or-interrupting-the-amplifi, by Zeiss Ikon, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
