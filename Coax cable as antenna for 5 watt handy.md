# Coax cable as antenna for 5 watt handy

*Tags: antenna, coaxial-cable, impedance-matching · score 4*

## Question

For a normal 5 watt handy working in VHF or UHF freq with 50 ohm antenna , is it possible to use a same length coax cable instead of a stub antenna, so as to work like a crude antenna. Will this only result in extra capacitance/ VSWR damaging the system ?

## Answer (score 7, by Phil Frost - W8II)

The electrically shortened antennas often found on HTs are not simple pieces of wire, but coils:  
*By Shootthedevgru at English Wikipedia, CC BY-SA 3.0*

The coil adds inductance over the length of the antenna, making it appear electrically longer than it is physically. Without the inductance, the antenna would need to be approximately a quarter-wavelength long.

A length of coax of the same physical length would not have this inductance, so would not be a good replacement.

Besides the issue of length, using a length of coax, with the coax connector attached the usual way, screwed into the antenna connector on the HT isn't an antenna at all since the shield would surround the center conductor which would otherwise be the antenna. It's just a feedline, with no antenna on the end.

## Answer (score 2, by tomnexus)

If you want an antenna at the end of a length of coax, in my experience, simply stripping the last 1/4 wave of coax and leaving the inner exposed, does not work. The VSWR is high and unstable, as the other half of the dipole is completely undefined.

What works a lot better is to carefully extract the inner from the braid, or re-attach the braid, and fold it back down against the coax. So now you have a 1/2 wave dipole, with the coax running down against the lower, grounded half. You could even put some heat shrink over it, but it's better to keep the braid slightly away from the coax.

If you have access to a VSWR meter, try building these and running your hand down the coax. In the first case the VSWR changes dramatically as your hand moves, in the second it will be more stable.

If you want an antenna directly on the HT without any coax, then stripping off the sheath is fine, and a quick and easy way to get a 1/4 wave monopole without soldering. Your tuning will almost certainly be wrong on your first try - either cut it while attached to an MFJ style antenna tester, or try a range of lengths and see which ones work best for getting in to distant repeaters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9907/coax-cable-as-antenna-for-5-watt-handy, by user132257, Phil Frost - W8II, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
