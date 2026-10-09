# Can I estimate range of a low power transmission based on power (in mW)?

*Tags: range · score 3*

## Question

I've read that radio range is influenced by a lot more than the power output of the transmitter. From what I've seen, line of sight and interference can be much more significant factors.

Is that also true for really low power transmissions, or is there a way to estimate the range based on power? I'm talking about cases like the transmitters they used to make to "connect" your MP3 player to your normal car radio (pre bluetooth and "aux" inputs), or walki talkie's in the same room?

## Accepted answer (score 5, by Glenn W9IQ)

When a transmitter and receiver antenna are in line of sight with one another, we can calculate the effective loss of the path based on the distance between the transmitter and receiver antenna, the gain of those antennas, and the frequency involved:

$$ \text{Path Loss (dB)} = 20\log(d) + 20\log(f) +32.44 - G_{\text{TX}} - G_{\text{RX}} $$

where

$d$ = distance in km  
$f$ = frequency in MHz  
$G_{\text{TX}}$ = transmitter antenna gain in dBi  
$G_{\text{RX}}$ = receiver antenna gain in dBi

So for example, a 1 km path at 400 MHz with 0 dBi antennas on the transmitter and receiver would have a free path loss of approximately 84.5 dB.

We now need to know the minimum receive power level that the receiver requires to properly decode or playback the information or signal from the transmitter. Let's use an example of a moderate receiver with a minimum signal requirement of -113 dBm. This would correspond to a 0.5 uV signal into a 50 ohm input impedance.

Since the receiver requires at least -113 dBm and we will lose 84.5 dB just due to the path losses, the transmitter must supply at least a -28.5 dBm signal (-113 dBm - 84.5 dB) or approximately 1.4 milliwatts of power.

If there are objects in the path that may absorb or reflect RF power, then these effects must be added to the above analysis. An example of this based on your question would be to model the effect of a human body between the transmitter and receiver. Depending on the frequencies involved, this may have no effect at all or it may increase the path loss and therefore require a higher power transmitter, a more sensitive receiver, or better (higher gain) antennas or some combination of these.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9522/can-i-estimate-range-of-a-low-power-transmission-based-on-power-in-mw, by just.another.programmer, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
