# Non-inductive resistors

*Tags: electronics, impedance · score 5*

## Question

When we use a "non-inductive resistor" to check the output impedance of say an unun, say 50ohm 1:1, what resistor type is actually non-inductive, or does it not really matter as long as the leads are short and frequency is low? I know there's non-inductive resistors with bidirectional windings, and some other non-inductive types but which would be the proper (or most ideal) type(s) to use? I'm thinking of getting some hence the question!

## Accepted answer (score 7, by tomnexus)

For measurements the best resistor is a surface mount one - an 0805 resistor is non-inductive to a few GHz. Even better is to use two reststors, usually 100 ohms each, one each side of the coax.

A 1/8 W or 1/4 W carbon film resistor is also fine for HF, its leads are the main source of inductance and they're shorter than the rest of your unun circuit.

The whole non-inductive resistor story comes from the design of *dummy loads* which need high power resistors. These are often wire wound and hence high inductance. There are thick film high power resistors available for terminating high power lines.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20696/non-inductive-resistors, by t252, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
