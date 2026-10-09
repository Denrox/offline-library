# How do I couple two VHF Small Signal Amplifiers together?

*Tags: impedance, equipment-design, amplifier · score 3*

## Question

I have managed to build single stage VHF amps ok using the transistor's S-Parameters to determine the load and source reflection coefficients for a specific gain and stability considerations.

Simple LC SMT components were used for transforming the source and load impedances (50 ohms) to the necessary load and source reflection coefficients for the transistor.

However, I need to increase the signal level a little more so I want to build a two stage amplifier. Now assuming I don't overdrive the second stage, I have not for the like of me been able to figure out how to couple two stages together without effecting the load reflection coefficient value of the first stage and the source reflection coefficient value of the second stage.

I believe the input impedance of the second stage needs to be transformed to the load reflection coefficient impedance equivalent value of the first stage. Simple enough to see on a Smith chart.

However, if we look back from the output of the first stage toward the input of the second stage through the network, the input of the second stage will not "see" the correct source reflection coefficient impedance value to maintain the intended gain values of each of the individual stages. Just as with the single stage amplifier, the matching network designed to transform the source impedance (50 Ohms) value to the necessary input reflection coefficient value, will not transform the input impedance(not the input reflection coefficient value) of the transistor back to 50 Ohms at the input.

Thus explaining why my VNA doesn't "see" 50 Ohms looking into the input of the amplifier through the matching network unlike if we were just doing ordinary impedance matching. Then the VNA would "see" a 50 Ohm match to the 50 Ohm driving source.

I'm wondering if it would be easier to use a canoe to go to mars or am I just missing something very fundamentally simple here.

Can anyone set me straight on this conundrum?

Let me rephrase the question this way and analyze just one of the LC networks - the one from the 50 Ohm load toward the collector at the output of the second stage.

It is my understanding that the job of the matching network is to transform the 50 Ohm load to the needed load reflection coefficient and its corresponding impedance that the transistor needs to "see". This Z would be the conjugate of the actual Z needed at the collector because the collector is considered the source at this point.

Now, if we look back through the matching network from the collector to the 50 Ohm load, the actual Z(not the conjugate of the actual Z) at the collector would be transformed back to 50 Ohms. I say the actual Z at the collector is transformed through the network back to 50 Ohms because at this point, the collector would be considered the load.

Is this correct?

I'm used to the idea of impedance matching where the load Z is always transformed to the driving or source Z. When it comes to the input of these small signal or linear amplifiers, it is strange to me when the source Z of 50 Ohms needs to be transformed to the load Z or what becomes the input reflection coefficient at the base of the transistor for a certain set gain.

To confuse matters more, as in the first part of this post, I was under the impression that the input impedance of the amplifier S11 without matching, was the impedance that was transformed through the input matching network back to the driving source as in a normal matching procedure. Now I'm thinking that this is incorrect because the impedances on at least one side of the network in this case would not match. In other words, since the source Z needs to be transformed to the input reflection coefficient equivalent impedance at the base, it must be that impedance(not the VNA measured input impedance(S11) before the matching network is put between the base and driving source) that is transformed back to the 50 Ohm source. It now seems that if it didn't, there would be no match at the input of the network and there would be standing waves and a loss of drive level there.

Is this correct?

If this is correct, then the 50 Ohm microstrip between the two stages would provide the necessary impedance at the output of the first stage and input impedance of the second stage to maintain the original design values of the matching networks when the two stages are connected together. It seems obvious to me that without the microstrip, the series capacitor in the output network and the series capacitor in the input network used for coupling would combine and become an entirely different value thus altering the original design needed in that part of the the amplifier.

Is this correct?

## Accepted answer (score 2, by tomnexus)

In general I would analyse a series of cascaded RF networks from right to left. Start with the final load on RF OUT, then compute the impedance seen looking into the input of stage 2, which is the impedance seen by the output of stage 1 (keep the microstrip length at zero), and from this you can compute the impedance seen at the input of stage 1, which is what's seen at RF IN.

For working out the cascaded gain, impedances, noise figures etc, I don't think you need to look "forward" from one stage to the next. You might do this to calculate the reverse isolation of the chain. It might be relevant for stability analysis - perhaps the second stage stability is affected by the output impedance of the first stage. (The simplest would be if there is ample stability margin, so no need to work out exactly what will happen if the source impedance changes slightly).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22013/how-do-i-couple-two-vhf-small-signal-amplifiers-together, by Thomas L, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
