# How does a 1:4 current balun work?

*Tags: balun · score 3*

## Question

I'm having little difficulties understanding the following schematic:

I understand the part regarding current distribution. I understand why this schematic suppresses common mode current. Also I realize that if Z1 = V/2I was 50 Ohm than the balun converts the impedance to Z2 = 2V/I, 200 Ohm.

What I don't understand is the voltage part on this schematic. Why the voltage is +3V/2 and -V/2 in the right part (2V in total), where V/2 came from in the middle part and what does it mean?

## Accepted answer (score 6, by Phil Frost - W8II)

It's a confusing diagram.

Some of the voltages are differences between points you might intuitively assume. For example, the $2V$ at the right is the voltage across the entire load (which also confusingly, is modeled by two identically named series resistors).

But the other voltages are implicitly relative to the ground symbol attached to the connector shield.

Lemma: the voltage across any winding must be the same since we are considering only the differential mode and the transformers are the same. Hopefully that's intuitive enough.

The voltage across any winding must be $V/2$ (though the polarity may differ). Consider this circuit:

By the KVL, the voltages around this circuit must add to zero. Since the voltage across the connector is $V$ by definition, the windings must each be half that.

Now start at the point labeled $-V/2$ and follow back to ground:

Having gone through one winding (minding polarity) the voltage is one times the winding voltage, or $-V/2$

And the other point labeled $3V/2$:

This way goes through a winding and the connector, so the voltage is $V + V/2 = 3V/2$.

The difference between these points is:

$$ 3V/2 - (-V/2) = 2V $$

which is the output voltage you'd expect considering conservation of energy or just what a 4:1 balun is supposed to do.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15115/how-does-a-1-4-current-balun-work, by Aleksander Alekseev - R2AUK, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
