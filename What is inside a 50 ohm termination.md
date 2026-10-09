# What is inside a 50 ohm termination?

*Tags: rf-power, frequency, connectors, reflector · score 9*

## Question

I see RF applications requiring 50 ohm termination to avoid any open port reflections. Curious what is actually inside a 50 ohm termination connector. Is it simply a 50 ohm resistor? But then it is rated for certain frequency range, so makes me think it is something more than a resistor.

## Accepted answer (score 12, by tomnexus)

It depends on the frequency range the termination is rated for, and the power handling required. High power and high frequency is very difficult.

At HF, any old non-inductive 50 Ω resistor will do. For higher power, we'd put many resistors in series and parallel, perhaps on a heat sink or in a can of oil.

At VHF and UHF I've made very good terminations with a pair of 100 Ω chip resistors soldered flat on an SMA connector.

Above this, the inductance of the resistors gets too much, and they start to be made of a carbon impregnated board, with an appropriate surface resistivity to match the transmission line, and gradually absorb the power. This could be done with a gentle taper in the stripline on the lossy board, to further improve its high frequency behaviour. The very best are sold for calibration of network analysers, these are thousands of dollars each.

For a high power, low PIM, well matched load, we've also used a long roll of thin .078" rigid coax. The loss of 3 dB per metre, over 5 metres, both ways, adds up to a 30 dB return loss, even if the other end is an open circuit. With a mere mortal termination on the far side, this can be even better. In ohms, the impedance including all inductance of the connections is within 0.5 Ω of 50 Ω, even at many GHz, no mean feat.

A termination will have a specification for return loss, which is the reflection it produces in a 50 Ω system, and the frequency range this is valid for. A cheap one will be say 20 dB return loss from DC up to 1 GHz. A better SMA one might be 30 dB up to 8 GHz. Really good ones will be over 40 dB return loss, and/or work up to 10s of GHz, depending on the connector used. Mini-Circuits have an excellent selection of modest priced ones on their website, but look at Weinschel and HuberSuhner for fancier ones.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12189/what-is-inside-a-50-ohm-termination, by eecs, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
