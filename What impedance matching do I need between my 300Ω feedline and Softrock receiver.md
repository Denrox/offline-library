# What impedance matching do I need between my 300Ω feedline and Softrock receiver?

*Tags: antenna, hf, diy, feed-line, impedance · score 4*

## Question

I will be assembling a Softrock Ensemble II HF receiver, and I know I'm going to want it on air as soon as I build it, so I'm challenging myself to build an antenna for it first.

The plan is to do a simple balanced line inverted V dipole, such as the $4 special, but my receiver has a BNC antenna connection.

The receiver schematic shows the antenna going into an ungrounded BNC connector, then connecting to a transformer which I'll be winding myself from the instructions. However I want to be able to connect all sorts of antennas so I don't want to alter the receiver just for this antenna.

Assuming the BNC isn't grounded, can I just attach a BNC to the 300Ω twinlead and that to the receiver, or should I attempt to do some amount of impedance matching between the twinlead and the receiver? I'm not transmitting, so it won't destroy anything to try, but I'd like to have decent reception.

## Accepted answer (score 2, by Phil Frost - W8II)

Assuming the BNC isn't grounded, can I just attach a BNC to the 300Ω twinlead and that to the receiver

Yes. Impedance matching will mean less losses between the antenna and your receiver, but the receiver's objective isn't energy harvesting. As long as the antenna is sensitive enough and the receiver's gain high enough that the predominant source of noise is RF noise, and not the receiver's internal noise, improving antenna efficiency will do nothing to help you.

In particular on the softrock kit, receiver gain is fixed. If you notice no difference between a dummy load and your antenna on a quiet frequency, try increasing the gain. Increase it just until the RF noise floor is just a bit above the receiver's and your sound card's noise floor: this will give you the highest dynamic range.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1057/what-impedance-matching-do-i-need-between-my-300o-feedline-and-softrock-receiv, by Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
