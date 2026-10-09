# Aside from repeaters, what station types allow automated transmissions?

*Tags: united-states, legal, automation · score 10*

## Question

I know repeaters don't have to have a control operator at the radio in order to transmit given certain conditions are met.

Are there any restrictions to setting up automated stations which transmit upon receiving specific transmissions from their operators or other operators, but do not act as repeaters? I know beacons are a special case in that they transmit on a schedule.

What restrictions apply to unattended, automated stations?

The [specific problem I'm trying to solve](How%20would%20one%20automate%20HF%20communications%20to%20a%20specific%20location.md) involves automating a connection between two distant radios. The originating radio needs to make several transmissions in sequence due to a user instructing it to, without giving it specific frequencies, sequences, and data to transmit (ie, the radio decides what to transmit). The receiving radio, however, may not have a control operator nearby. It still has to listen, and if it gets a "call" from the originating radio it needs to respond, even if there's no control operator nearby.

Under what rules would this type of automation be acceptable?

## Accepted answer (score 3, by PearsonArtPhoto)

Digital signals are allowed, so long as they follow this FCC regulation:

§97.221 Automatically controlled digital station.

(a) This rule section does not apply to an auxiliary station, a beacon station, a repeater station, an earth station, a space station, or a space telecommand station.

(b) A station may be automatically controlled while transmitting a RTTY or data emission on the 6 m or shorter wavelength bands, and on the 28.120-28.189 MHz, 24.925-24.930 MHz, 21.090-21.100 MHz, 18.105-18.110 MHz, 14.0950-14.0995 MHz, 14.1005-14.112 MHz, 10.140-10.150 MHz, 7.100-7.105 MHz, or 3.585-3.600 MHz segments.

(c) Except for channels specified in §97.303(h), a station may be automatically controlled while transmitting a RTTY or data emission on any other frequency authorized for such emission types provided that:

(1) The station is responding to interrogation by a station under local or remote control; and

(2) No transmission from the automatically controlled station occupies a bandwidth of more than 500 Hz.

[60 FR 26001, May 16, 1995, as amended at 72 FR 3082, Jan. 24, 2007; 77 FR 5412, Feb. 3, 2012]

In any case, if there's a human on one end, I would think it would be considered remote control, and thus eligible for those rules. But just in case, I would stick to these regulations.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1025/aside-from-repeaters-what-station-types-allow-automated-transmissions, by Adam Davis, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
