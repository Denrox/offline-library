# Only noise, no signals whatsoever on HF

*Tags: rfi, ft8, reception · score 5*

## Question

Last night there was a power outage at home. I was able to see a LOT of stations on 20M (FT8). As soon power returned, all of them disappeared. You can see in the waterfall very clearly when power returned:

The odd thing is, noise is around 7 here at home. But when power went out it dropped only to 6.

Also, today I went to my dad's and he was seeing lots and lots of stations. I left WSJT-X open, and when I came back, there were only two decodes, out of dozens at his place.

I'm not sure what's going on. My antenna is a dipole, tuned to the right frequency. Measures SWR 1.1. My rig is a Kenwood TS-450S. My dad's antenna is also a dipole, and his rig is an Icom IC-765. We're only 700m apart.

I've tried adding a balun and a choke. The choke made a big difference by dropping the noise levels by 1.

What can I do to troubleshoot this?

## Answer (score 4, by Brian K1LI)

There is a lot you haven't told us about the current situation that could be helpful. Since your dad lives so close, perhaps you can make various substitutions to identify the problem.

For example, what do you hear from the speaker or headphone jack of the TS-450S when using your station antenna? If you hear nothing, then you should expect to see nothing on the waterfall display; if you hear signals but don't see them on the waterfall, then the problem is probably in the radio-to-computer interface or in the computer's audio system.

If you hear nothing from the TS-450S, take it to your dad's and listen with his antenna. If you hear more signals, the problem is your antenna; if you still hear nothing with the TS-450S when he does hear signals with his transceiver, the problem is probably in the TS-450S.

## Answer (score 2, by pappad)

QRM is extremely common nowadays due to a great increase in switch-mode power supplies that tend to desensitize nearby receivers, hence the reason why many Hams put up a shack away from the house.

Simply because there isn't noise on the exact frequency you're on, doesn't mean you're not experiencing interference. You might want to try a band pass filter for 20M, and that may help compensate for your radio's poor selectivity.

For example, if someone is blasting bass at 100Hz super loud, you may not be able to hear the 1000Hz you might normally be able to.

Personally, where I'm at, I also cannot operate on 20M very well due to noise from my neighbors. Antenna polarization helps, but does not solve the problem.

There is such a thing as RF noise cancellation, and MFJ makes such a component such as this, but I haven't tried it: http://www.mfjenterprises.com/Product.php?productid=MFJ-1026

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14636/only-noise-no-signals-whatsoever-on-hf, by hjf, Brian K1LI, pappad. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
