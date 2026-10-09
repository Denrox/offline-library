# Dipole increased CM current using choke balun

*Tags: electronics, dipole, balun, choke-balun · score 4*

## Question

My 20 meter inverted vee dipole is fed with 56 feet of 50-ohm coax. The SWR measures 1.2 at the center of the band. According to http://arrl.org/grounding a balanced antenna doesn't need a ground, so my transceiver is not grounded. I've read that an inverted vee lowers the 73 ohm dipole impedance closer to the 50-ohm coax impedance but connecting a coax unbalances the antenna, so I wanted also to test using a current choke balun. I studied [How to determine number of turns for a 1:1 balun?](How%20to%20determine%20number%20of%20turns%20for%20a%201%201%20balun.md).

Within that post, I found [How to detect common-mode currents or “RF in the shack”?](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md). I constructed a snap-on ferrite detector with analog meter.

Without any balun, the CM meter clipped on the coax near the output of the transceiver just barely deflected when transmitting. That was encouraging but I wanted to compare it using a choke balun.

I made a choke balun on a ferrite rod 3" x 1/2" (scavenged from a Hy-Gain 1:1 balun) by wrapping a bifilar winding of 12 turns of #16 magnet wire, each winding in series with a dipole element. I inserted this balun at the antenna feed point. The SWR measured about the same as without the balun, but this time the CM meter showed about 10 times more current than without the balun.

Does that mean that the antenna doesn't need a choke balun, or the balun is not designed right, or both? Even if a wrong number of turns (I planned to test it empirically as Phil Frost suggested), I don't understand how it apparently **increased** the common mode current. Could my testing be bogus because the transceiver is not grounded? (I don't have a ground rod installed yet to connect). I haven't had a chance to transmit to someone but the antenna receives distant signals well so it seems correct in that respect.

## Accepted answer (score 4, by Peter Buxton)

I'm answering my own question after seemingly solving the problem, thanks to the helpful comments I received. Evidently, the ferrite rod core that I salvaged from a Hy-Gain balun was the culprit. I couldn't find any information on what kind of ferrite it is but it was manufactured about 30 years ago. I don't know much about baluns yet but earlier questions I had about that same stock Hy-Gain balun prompted me to post Voltage vs. Current Balun for Dipole.

So the solution is, I wound a new balun per info in http://audiosystemsgroup.com/2018Cookbook.pdf. Although the document says to use a 2.4" #31 torroid core, I had a 1.4" #43 core so I wound it with #20 wire just to test if it would work.  Now there is no increase in common mode current as was measured before, and the SWR is only 0.1 higher than without the balun, so I think this qualifies as solved. Hopefully this post can somehow help others with similar questions.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15181/dipole-increased-cm-current-using-choke-balun, by Peter Buxton. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
