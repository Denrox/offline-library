# Can every antenna be used both for transmit and receive?

*Tags: antenna, antenna-theory, gnss · score 10*

## Question

Assuming I have an antenna for receiving GPS signals, can I use it also for transmit — to create a repeater in a tunnel (or some place with no reception)?

## Accepted answer (score 23, by Kevin Reid AG6YO)

**No.** Many types of antennas may be unsuitable for transmitting.


A so-called *active antenna* contains an integrated low-noise amplifier (LNA) for amplifying weak signals. (**This is very common for GPS antennas.**) This amplifier cannot pass a signal in reverse, and could be damaged by transmit power levels appearing on its output. It is possible to have an automatic switch to bypass the LNA when transmitting, but this feature would not be designed into an antenna meant for receiving.


Some designs of antenna, such as the Beverage antenna, contain resistors or other dissipative elements. If they are used for transmitting, the resistor must be capable of dissipating a certain fraction of the power input to the antenna. This is inefficient since that fraction of power is not transmitted, and requires a resistor which will not be destroyed by the heat.


A receiving antenna may contain a ferrite element, which allows it to be much more efficient when receiving than its size would otherwise permit, but which will *saturate* at any significant power, becoming nonlinear and creating harmonic distortion (as well as heat).


A transmitter requires *impedance matching* between the final power amplifier and the antenna. An antenna's impedance varies with frequency, so it has some frequency range over which there is an acceptable match. The same antenna can be used for receiving over a much wider range; antennas used solely for receiving may be deliberately mismatched vs. the intended band to gain other advantages such as being physically small.

An antenna with the wrong impedance at the desired frequency *can* be matched using a matching network or *antenna tuner* (adjustable matching network), but this is still less efficient because there will be additional losses.

This is the least significant problem of all those I have listed: with a good antenna tuner, just about any chunk of metal insulated from other objects can be used as an antenna. The problem comes when non-metallic elements are in circuit as in the other cases.

Since you mention GPS in particular:

You cannot repeat a GPS signal usefully. Or rather, if you did, it would cause your GPS receiver to think it is at the position of the original receiving antenna, not its actual location. (This is because GPS operates by analyzing the combination of signals from multiple satellites, and this combination happens in the receiving antenna.)

It would also be likely illegal to operate such a transmitter, because you are transmitting on frequencies you do not have permission to and interfering with normal GPS operation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5880/can-every-antenna-be-used-both-for-transmit-and-receive, by volatile, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
