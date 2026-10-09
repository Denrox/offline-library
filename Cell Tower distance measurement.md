# Cell Tower distance measurement

*Tags: rtl-sdr · score 6*

## Question

I am developing a hobby project to detect/measure the distance between my cell phone and a cell tower (GSM tower).  
I am newbie. I don't even know whether this is possible or not.  
I have following hardware:

1. Raspberry Pi 3
2. RTL2832u

I am planning to use OpenBTS and the FreeSwitch stack in the future for advanced feature development.

## Accepted answer (score 8, by Glenn W9IQ)

One approach would be to capture the GSM Cell ID. This uniquely identifies a particular GSM site. You can then lookup this ID in a database such as one offered by Cobain to determine the tower location. If your application serves a very limited geography, you could build your own database to suit your needs.

In order to calculate distance, you will need to geo locate your receive site through a GPS signal, manual entry, or other means. You could then use Google Map services to show the two points and the distance between them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10158/cell-tower-distance-measurement, by Avadhana Technologies, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
