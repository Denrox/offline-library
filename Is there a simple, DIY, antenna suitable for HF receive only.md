# Is there a simple, DIY, antenna suitable for HF receive only?

*Tags: antenna, hf, diy · score 9*

## Question

So the [antenna I'm thinking about doing](What%20impedance%20matching%20do%20I%20need%20between%20my%20300%CE%A9%20feedline%20and%20Softrock%20receiver.md) might be way too large for my property.

Is there another simple, cheap, DIY antenna I could try on my receiver? I know I'm going to want to hook it up and have a listen before the last solder joint has cooled. Ideally it would cover 160 m to 10 m reasonably well.

The most complicated antenna I've built was a Gray Hoverman for UHF reception. It would be nice if it weren't much more complex, but if it's inexpensive and good enough I'm willing to do a bit of work for an antenna I'll use a long time.

I'm not interested in aiming right now, so an omnidirectional antenna would be best. I do have a 25' attic I can use if needed.

*Is almost certainly...

## Accepted answer (score 20, by Phil Frost - W8II)

Receive antennas are the *easiest thing ever*. You just need two things:

1. something that conducts electricity
2. another thing that conducts electricity

Attach one to the center contact on a BNC connector. Connect another to the shield. Boom, done. If you can't find two things, then one can be the Earth.

Alternately, you can use two ends of one thing that encircles something that permits magnetic fields (like, air).

Until you are approaching a significant fraction of a wavelength (like, 1/4 wavelength), then making either thing bigger will get you more signal. However, once you have enough signal that you are well above your receiver's noise floor, more signal won't make you receive any better: it will just give you louder noise. I'd say, however much space you have, make it that big.

Don't worry about tuning, or impedance matching. This also will increase the fraction of the energy received by your antenna coupled to the receiver, but again, once you have enough to overcome the receiver's noise, more is of absolutely no help. See [What is the relationship between SWR and receive performance?](What%20is%20the%20relationship%20between%20SWR%20and%20receive%20performance.md)

Don't worry about polarization. At HF most of your signals will arrive via the ionosphere which is constantly swirling and changing the polarization of received signals. Whatever polarization you pick, it will be the wrong one in 30 seconds, so don't worry about it.

If you really *must* worry about something, worry about getting your antenna away from noise sources. Your house, being full of all varieties of noisy digital electronics, is very noisy. If you can get an antenna away from these things, that's good. You must also take care to avoid making the feedline part of the antenna. See [Using a balun with a resonant dipole](Using%20a%20balun%20with%20a%20resonant%20dipole.md) Although that question asks about resonant dipoles, the answers apply to *any* type of antenna.

## Answer (score 5, by WPrecht)

There is nothing simpler than a random length wire. It doesn't have to be strung up or even straight, though, obviously, those would improve it's performance. Of course the ironic thing about a random length wire antenna is that the most effective lengths aren't actually random. They work best when the antenna is at least a quarter wavelength at the lowest operating frequency, 65' for 80m, for instance.

To maximize the effectiveness, and have something useful down the line, you could build a small tuner. An L-network random wire tuner is probably the simplest matching network in existence, designs about on the net. Like this one: How to Build a Cheap Antenna Tuner or this one: SWL Receiving Antenna Experiments.

## Answer (score 2, by ON5MF Jurgen)

For receiving horizontal antennas pick up a lot less manmade noise than vertical ones. So if I were you I'd try to put up a horizontal one.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1058/is-there-a-simple-diy-antenna-suitable-for-hf-receive-only, by Adam Davis, Phil Frost - W8II, WPrecht, ON5MF Jurgen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
