# In the context of the mixer in my radio, what does balanced and unbalanced mean?

*Tags: electronics, mixer, inductor · score 5*

## Question

I'm trying to understand how the mixer in a radio actually works, at a physics level. When looking at this article and studying the first schematic I realized I really don't understand what balanced and unbalanced means in that context.

Could you explain what the difference is between the signal on either side of the transformer so I can get a better picture of what transformation is happening as the signal passes through that component?

## Accepted answer (score 2, by rclocher3)

Looking at T1, on the unbalanced side of the transformer, one leg of the input is tied to the chassis ground (the zero volt reference); the other leg is driven by a voltage source. Because the voltages on the two legs aren't equal but opposite, the input is said to be unbalanced.

The current in the primary winding of the transformer creates a magnetic flux that induces an electromotive force in the secondary winding. Because the secondary winding includes a center tap that is tied to chassis ground, the output voltage of the two legs of the secondary winding will be equal and opposite, and therefore balanced.

If you're still confused about the "equal and opposite" part, you can look at the secondary winding with a center tap as two windings in series. Let's assume for a moment that the secondary winding is generating 10 V at this particular instant, with the top end being positive and the bottom end being negative; since we're treating the secondary winding as two windings, the top winding will generate 5 V and the bottom winding will generate 5 V. The bottom of the top winding, also known as the center tap, will be at 0 V because it's tied to chassis ground, so the top of the top winding will be at +5 V compared to chassis ground. The top of the bottom winding is also tied to chassis ground, 0 V, which forces the bottom of the bottom winding to be at -5 V. The +5 V and the -5 V are equal and opposite.

## Answer (score 4, by Phil Karn)

A balanced mixer is one that suppresses the local oscillator (LO) input in the output. A double-balanced mixer (like the one you show here) suppresses both the RF input and the LO in the output. This is often accomplished with balanced transformers, hence the name.

Because T1's secondary has a grounded center tap, the voltages on its two "hot" output terminals are always equal and opposite in polarity with respect to ground. Assume the LO has driven T1's top output (+) and the bottom output (-). This forward biases diodes D1 and D2, and because T1's center tap is grounded, the diodes effectively clamp the lower side of T2's secondary to ground. Diodes D3 and D4 remain off.

Holding that state, now consider a second signal fed to T2's primary. Because the lower line of T2's secondary is clamped to ground, the RF input will appear at the IF output "right side up", i.e., in phase; if the RF input is (+), then so is the IF output.

Now reverse the polarity of the LO input to make the bottom output of T1 (+) and the top (-). Diodes D3 and D4 conduct while D1 and D2 remain off, clamping the *top* of T2's secondary to ground so that the RF input to T2 appears *inverted* at the IF output, i.e. 180 degrees out of phase.

But if there's no signal into T2, then the LO input to T1 does not appear at the IF, and by symmetry if there's no LO input signal into T1 then the RF signal into T2 also does not appear at the IF output.

Mathematically, mixing is multiplication. When you multiply two numbers with the same sign (both positive or both negative), the result is a positive number. When the operands have opposite signals (one positive, one negative), the output is negative.

So this circuit multiplies the LO and RF signals and their product appears at the IF output. This is why these mixers are sometimes called "product detectors" when used to detect, say, SSB or CW.

This circuit is a way to multiply two analog signals with simple passive components. The same operation can be done with an exclusive-OR logic gate if a positive input is mapped to a logic '1' and a negative input is mapped to a logic '0'.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6815/in-the-context-of-the-mixer-in-my-radio-what-does-balanced-and-unbalanced-mean, by flickerfly, rclocher3, Phil Karn. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
