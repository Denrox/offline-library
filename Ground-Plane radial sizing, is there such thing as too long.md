# Ground-Plane radial sizing, is there such thing as too long?

*Tags: antenna-theory, antenna-construction, vhf, uhf, radial · score 3*

## Question

I'm just trying to make sure I understand the theory correctly.

I have some triband VHF/UHF/800MHz antennas, I need to mount on a tower so I plan on using a "mobile to base" conversion kit. The kits i'm mostly looking at are specified for VHF/UHF, which in my mind should be sufficient for 800MHz.

The way I understand it is that the radials should be **at least** 1/4 of the wavelength of the antenna, so if the antenna is operating in the 800MHz range the radials that are much longer than 1/4 wave of the 800MHz frequency will not be detrimental in any way at that frequency.

Does anyone see any problem with my reasoning?

[Update] ---

I just edited my post to provide an example photo/diagram. I'm looking at a system like this, but the anennas I'm using are multiband VHF/UHF/700/800. So my resoning is that the ground plane radials should be sized for the VHF band, and that the extra length for the higher frequencies will not negatively affect the antenna. My understanding is that the radials provide a reflective plane which just must be at least a quarter wave length. I hope this provides some clearification.

## Accepted answer (score 2, by Phil Frost - W8II)

Infinitely long radials are ideal. So to directly answer your question: no, there is no such thing as "too long".

However, infinitely long radials work because the current in the radials approaches zero as distance from the base approaches infinity. At some point the current is negligible, so truncating the radial at any point makes no significant different. As a rule of thumb, 1.5 wavelengths is long enough to be considered infinitely long.

More problematic are radials which are not very much larger than a 1/4 wavelength, but are also not resonant. Because the end of the radial is close enough to be significant, the impedance of the radials matters. And because they aren't resonant, they will introduce a reactive component into the impedance. Compensating for that reactance may require modifying the length of the vertical element or introducing a matching network to compensate. This may or may not be a significant problem. Modelling or empirical measurement is the way to figure it out, since it depends on the specific lengths involved.

But I understand your underlying problem is getting the antenna to work on 3 bands. If the bands are related in frequency by an odd multiple (for example, 70 cm is 3 times the frequency of 2 meters) then just make the radials a 1/4 wavelength on the lower band and they will also be resonant (or close enough, no need to be exact) on the higher band.

For bands that are not harmonically related, another solution is to have a pair of radials that's resonant for each band. Each pair of radials is effectively in parallel: the one that's resonant will have a minimum impedance and thus will take most of the current. The other radials will not be very significant because their relatively high impedance means they have low current. A *fan dipole* works on this principle.

Or if a lower band already requires radials that are at least 1.5 wavelengths for some higher band, you can probably not worry about dedicated radials for this higher band since the radials are long enough to be considered infinitely long.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16996/ground-plane-radial-sizing-is-there-such-thing-as-too-long, by Frank, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
