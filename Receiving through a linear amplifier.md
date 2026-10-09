# Receiving through a linear amplifier

*Tags: antenna, transceiver, amplifier · score 3*

## Question

I want to build a simple amplifier using those Mitsubishi modules (like the RA30H1317M or other RA parts). I know this might seem like a very obvious question, but I am unable to find the answer after searching a while.

When using a linear amplifier with a transceiver, is the transceiver still connected to the antenna when not transmitting or is it essentially disconnected and needs a "special" type of amplifier that will leave it connected so it can receive through the amplifier properly?

## Answer (score 8, by yuiu)

Every linear amplifier designed to work with a transceiver has a bypass circuit which switches the antenna between the amplifier and transceiver.

When transmitting, the transceiver connector is connected to the input of the amplifier, subsequently the output to the antenna.

When receiving, the amplifier circuit is disconnected and the antenna is connected directly to the transceiver connector.

The switching can be done by relays or some kind of electronic RF switches. Many linear amplifiers have the feature to detect the carrier and switch to transmit mode if they detect the transceiver output. Alternatively a separate line to activate the transmitter can be used.

I've looked into the data sheet of RA30H1317M and I don't see any bypass circuit feature. You have to implement it by yourself.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5524/receiving-through-a-linear-amplifier, by Synaps3, yuiu. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
