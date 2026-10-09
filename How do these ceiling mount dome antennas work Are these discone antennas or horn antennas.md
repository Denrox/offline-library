# How do these ceiling mount dome antennas work? Are these discone antennas or horn antennas?

*Tags: antenna, antenna-theory, bandwidth · score 3*

## Question

The small cone is connected to the larger one. The coax center cable is terminated into the small cone and the coax shield into the larger outer cone.

The screenshots are from this video https://www.youtube.com/watch?v=Pu-o4u3VgR0

Another video from a different manufacturer - https://www.youtube.com/watch?v=y8ky1t3IfLE

They claim wideband coverage from 700 Mhz to 2.5ghz, but I suspect they simply do not do anything.

I have one of them and I think these are the reason my setup is failing.

Could they even work?

I couldn't find any teardown of any dome antenna from any of the big companies except this one - https://www.youtube.com/watch?v=7EB4wqawBv4 - but this seems to be a completely different design.

## Accepted answer (score 3, by tomnexus)

That design is a kind of wideband conical monopole, a fairly standard design.

The slightly conical groundplane should help raise the radiation towards the horizon. A monopole on a groundplane tends to radiate downwards (when mounted on the ceiling) which isn't ideal for the longest-range users. It may also improve the impedance.

If it's done right, it could certainly be an excellent antenna for 700-2500 or higher, with low VSWR and clean radiation patterns. Metal spinning (or just pressing) is a good way to make the parts.

But I'm horrified to see the grounding wire on one side though - this will distort the pattern and affect the VSWR. I suppose it's done to provide a DC short, which is a good idea and may be required by some systems or safety codes, but it will affect the pattern at all frequencies, and the VSWR at some frequencies (may be designed to only affect say 1000-1600 so it doesn't matter).

The coax, if it's a low-loss LMR-195 / HDF-195 will be well under 1 dB of loss, not significant in this case.

In what way is your setup not working? Are you using it for wifi or an indoor picocell or repeater? The best would be to measure the antenna with a VNA, to check the impedance is well behaved in spite of the shorting wire.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21742/how-do-these-ceiling-mount-dome-antennas-work-are-these-discone-antennas-or-ho, by Mavin, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
