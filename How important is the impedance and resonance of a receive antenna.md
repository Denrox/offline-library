# How important is the impedance and resonance of a receive antenna?

*Tags: antenna-construction, hf, rtl-sdr, swl · score 7*

## Question

I'm very new to shortwave radio, as evidenced here:

[Can an antenna be too powerful for certain receivers?](Can%20an%20antenna%20be%20too%20powerful%20for%20certain%20receivers.md)

I want to build a longwire receive-only antenna for the HF frequencies.

I've been using the source:

SWL - Shortwave Listening

as a guide, but it isn't clear whether it's using 50 or 75 ohm coax cable.

The source says that if you use a coax you should also use a balun, but I don't know whether it should have a 9:1 ratio like the source says or whether I should calculate the impedance of the antenna.

Should the antenna be a specific length to receive the HF frequencies best?

I have a decent amount of space to work with so an antenna 75 feet long or less will be doable.

Do I need to worry about SWR?

I'm wondering whether I even need to consider all this as I'm just making a receiving longwire; I'm pretty sure I need a coax as I live nearby other houses (i.e. sources of noise), but do I need to have a transformer, antenna tuner, match impedance, etc. or am I just overthinking this?

The way the antenna system will be hooked up to a RTL-SDR dongle - this might be important to some answers.

## Accepted answer (score 6, by Glenn W9IQ)

The answers given so far provide good food for thought. I would like to add a slightly different perspective.

Today's home is loaded with sources of RFI (radio frequency interference). Routers, computers, wall warts, LED lamps, solar inverters, video cameras, etc. all are potential sources of RFI that interfere with the weak signals of short wave signals from distant countries. More and more, the need to keep the antenna system away from these local RFI sources is the reality of short wave listening. Not only must the antenna be distanced from the RFI but care must be taken that the feedline, typically coax, does not pickup these local RFI sources.

Antennas such as long wires and end fed "half waves" suffer from common mode currents on the feedline. These common mode currents cause the coax to pickup local RFI sources and couple them into the receiver. This problem can be mitigated by using a balanced antenna, such as a dipole, and connecting the coax to the dipole using a wide band, 1:1 current balun. This will minimize the local RFI pickup.

Is this over-thinking the issue? Some may say yes. But anything from a coat hanger to a log periodic antenna on the top of an 80 foot tower will receive signals. It is only a question of effectiveness for the effort and expense. You will need to make that determination.

## Answer (score 3, by glen_geek)

The simple case would be a 75 foot wire whose far end is an open-end tied to a high support, and whose near end feeds directly to your SDR-dongle. It is assumed the dongle is a single-ended input whose other termination is RF-grounded through your PC.  
It is likely that your SDR-dongle has a low-impedance antenna input, perhaps 50 ohms. At some frequencies, this will work well. At other frequencies a poor match delivers less power to your SDR-dongle. A 75 foot wire would favour the low end of the HF frequency space, where it mimics a quarter-wave vertical. As the frequency goes higher, a poorer match to a low-impedance SDR would be where your antenna mimics a half-wave end-fed wire.  
Does this poor match make the antenna useless at certain frequencies? Certainly not, if your SDR receiver noise floor is decent....(a sensitive receiver). For transmitting, a good match would be more important for the health of a transmitting power amplifier but of less importance for a receiver where signal loss creates insignificant heat (nanowatts).  
Adding some coax between antenna-end and SDR might change the impedance that your SDR sees, and also change the frequency spans where the antenna is decently matched (and poorly matched). Coax will likely add some small signal loss too.  
For casual listening, throw up a good long wire, whose end comes conveniently-close to your SDR, and a short length of coax to make up the difference. If a band-segment becomes particularly interesting to you, a simple L-section tuner could improve signals, if that band-segment is poorly matched. But many receivers have enough sensitivity that perceived improvements may be minor. Fussing over a "proper" receiving antenna, especially over a wide frequency range like the whole HF spectrum is not worth the trouble if "casual" listening is a goal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10137/how-important-is-the-impedance-and-resonance-of-a-receive-antenna, by fishfritters, Glenn W9IQ, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
