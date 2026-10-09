# How to construct a loop antenna for receiving HF?

*Tags: antenna, diy, loop-antenna · score 5*

## Question

I have a unused hula-hoop in my garage, and I ran some stranded speaker wire around it once, and attached one side of the wire to the coax shielding, and the other to the coax core wire. Is this the correct way to construct a loop antenna for receiving HF (500kHz to 30MHz) range frequencies?

## Accepted answer (score 3, by Adam Davis)

That will work a little, but you might want to consider adding a variable capacitor to get more performance out of it by making the antenna resonant at the frequency you are interested in receiving.

Alternately add a high impedance amplifier at the antenna, such as in this DIY hula hoop antenna.

Note that this will only by good for reception, though. A hula hoop of 4 feet in diameter is going to have a resonant frequency nearest the 10 meter band with a single loop of wire, and this will have a greater impact on transmission than reception.

## Answer (score 8, by Phil Frost - W8II)

Just about *anything* connected to your feedline makes an antenna. A lot of the concerns in transmitting antennas (low SWR, high efficiency, etc) are of diminished importance for receiving antennas, so it's surprisingly easy to make a perfectly good receive antenna with very little design effort.

You don't necessarily need the antenna to be resonant or "tuned". This will significantly increase the *sensitivity* of the antenna at the resonant frequency, but may not increase its *performance*, which for a receiver, probably means having a high signal-to-noise ratio (SNR). This is because tuning the loop will make it more sensitive to both signals and atmospheric noise. The only circumstance under which this will increase the SNR is if the antenna isn't already sensitive enough to overcome the internal noise of your receiver.

In fact, if you desire operation from 500kHz to 30MHz, you might want you antenna to be *not* resonant. A small loop resonated with a capacitor has a very high Q factor. The consequence of this for your antenna is very small bandwidth. It so small that inexpensive AM receivers (the consumer kind) use just the antenna bandwidth to select a station. If you resonate the antenna with a capacitor, you should expect only a few kilohertz of bandwidth without adjusting the tuning capacitor.

Whether you use a tuning capacitor or not, the impedance of this loop isn't going to be anywhere near 50Ω. The resulting high SWR means higher losses in the antenna and feedline, however as with the lowered sensitivity of a non-resonant antenna, this isn't a problem as long as the antenna is *sensitive enough*. See [What is the relationship between SWR and receive performance?](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md)

You may additionally find that this design might not do a good job of isolating common-mode currents, and consequently the [feedline works as part of the antenna](Using%20a%20balun%20with%20a%20resonant%20dipole.md). This isn't a problem in itself, except when you consider that you want to move the antenna away from your house, where there is less noise, but you can't do that if the feedline is the antenna. Whether or not this is a problem for you depends on where the noise is that you are trying to avoid, and how the surroundings of your antenna tend to unbalance it. You can always [test for common-mode currents](How%20to%20detect%20common-mode%20currents%20or%20RF%20in%20the%20shack.md) if you suspect this is an issue.

So, is this the "correct" way to make a loop antenna? As should be clear from the above, only you can tell. You will have to do some testing and gather some data to determine if the antenna is working well enough for you, and if so, congratulations, it's correct enough. If not, a more complex design might be necessary.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1383/how-to-construct-a-loop-antenna-for-receiving-hf, by cj5, Adam Davis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
