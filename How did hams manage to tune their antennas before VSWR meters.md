# How did hams manage to tune their antennas before VSWR meters?

*Tags: antenna-system, impedance-matching, swr-meter, testing, history · score 10*

## Question

In the early 20th century --back when the hobby was still new-- before VSWR meters and antenna analyzers were invented, how did radio operators know whether they were tuned for maximum power out?

*This is not asking about antenna tuner design or operation.*

## Accepted answer (score 17, by Mike Waters)

1. Mostly, they used **RF Ammeters** in series with the antenna. The first ones were **hot-wire ammeters** which were *completely mechanical* devices. One end of a thin nichrome wire (or other wire of sufficiently high resistance) inside the meter was coupled directly to the pointer shaft (often wrapped around it); the other end was anchored to the meter case. As the wire got warm and expanded due to the antenna current flowing through it, the spring-loaded pointer shaft rotated clockwise.  
  
Later, an improved RF ammeter design --that featured slightly faster response and improved RF isolation-- used an external **thermocouple** which sensed the temperature of a high-resistance wire in series with the antenna. The thermocouple was connected to a millivoltmeter (or milliammeter?) with the scale calibrated in amperes. The more current, the hotter the wire and the thermocouple junction. The higher the junction voltage of the thermocouple, the higher the meter reading.
2. Another method was a **neon lamp** coupled to the antenna. The brighter it glowed, the higher the voltage.

**In both cases** the operator tuned for maximum, either max current or max voltage, **which indicated maximum power into the antenna**.

That's how I tuned my homebrew transmitters for max back in the late '60s and '70s. My RF ammeter was a WWII military surplus unit (pictured below), and measured from 0-10 amps. The meter was fed from a thermocouple unit inside the case.

Later, at VHF frequencies, [Lecher wires](How%20were%201920s%20hams%20able%20to%20measure%20megahertz%20frequency.md) were also used.

## Answer (score 4, by Rich Morgan - KF9F)

I have been a ham for 58 years. I used an incandescent light bulb for transmit and a fluorescent tube for antenna tuning. Later, I could afford a field strength meter. I have also used Lecher wires for UHF.

Technical details? Go with the glow.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11708/how-did-hams-manage-to-tune-their-antennas-before-vswr-meters, by Mike Waters, Rich Morgan - KF9F. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
