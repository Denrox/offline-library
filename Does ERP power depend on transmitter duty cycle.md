# Does ERP power depend on transmitter duty cycle?

*Tags: rf-power, transmitter · score 3*

## Question

I’m building a transmitter and I’m trying to stay under the ERP power limit of my country , which is 0.5 Watt at the frequency I’m working on .

I was thinking about increasing the transmission range . The only way i see is to change the duty cycle and transmit at ERP x 2 power for only half a second . ( though this method doesn’t always increase range )

Would that count as 0.5 Watt ?

## Accepted answer (score 4, by timetraveller)

In the sense that you're asking (if I get your question right), no. ERP, or Effective Radiated Power is not time dependent or averaged across a time period. For example, you cannot transmit a one micro-second pulse of one million watts, drop to zero power for the next 999,999 micro-seconds, and label your ERP as ONE WATT. It doesn't work that way.

ERP is the directional radio frequency (RF) power emitted, measured instantaneously during the emission. A 50% transmitter duty cycle does not change ERP in the sense that you are asking. Note the word "directional". Primarily, ERP is dependent on the power applied to the antenna after factoring in the antenna's gain in the desired direction. A radio station having a directional array or phased towers, let's say with a large gain lobe to the north, will have a greater ERP to the north than to any other direction.

https://en.wikipedia.org/wiki/Effective_radiated_power

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21272/does-erp-power-depend-on-transmitter-duty-cycle, by Alessandro Mini, timetraveller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
