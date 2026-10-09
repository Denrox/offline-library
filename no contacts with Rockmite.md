# no contacts with Rockmite

*Tags: antenna, diy, qrp · score 4*

## Question

I finished building my [Rockmite ]. It's running off of 3x 18650s, or 12v. I connected it to a MFJ-1840T and held the antenna horizontally in the air (also tried vertically) with my hand. I tried calling clean CQ on 7.030 mHz and get no response. I tried with and without a counterpoise attached to the MFJ. My nanoVNA tells me the antenna has an SWR of ~2. I tried seeing my signal on a websdr 100 miles away to no avail. I'm in a suburb.

I have lots of questions. I also don't know which of the following are necessary or not, or where to start.

- because I'm holding the antenna, should I be expecting nvis contacts only?
- is my hand wrapped around the antenna base heat shrink hurting things? What's the better way?
- how sensitive is my setup to time of day?
- would building a G5RV instead of the MFJ be the thing to get me some contacts? Thus focusing on the antenna instead of more watts.
- would investing in a QRP SDR such as the RS-HFIQ make it possible to chase down band activity and move to more active frequencies to make a contact? Would this help me deduce receiver capability of my antenna setup?
- are newer digital modes other than cw required to be successful in QRP?
- should I join a club and being my setup to others to help me figure it all out with?
- should I climb a mountain peak and try the same thing again?
- do I need to figure out how to get the swr down?
- I type for 2-5 minutes before giving up. How long would it take to get a typical bite (response)?
- do I just need more watts? Am I attempting the rare or impossible? Is the rockmite just not usable in this part of the solar cycle without an amplifier?
- is there something else I'm not thinking of that is making it impossible for me to make a contact?

## Accepted answer (score 4, by Mike Waters)

I see what your problem is.

That's a 1.4 meter long, based-loaded, telescoping, end-fed vertical antenna. It has *significant* losses on 40 meters.

Furthermore, all end-fed antennas require a good RF return, such as a resonant elevated radial or counterpoise. Since you don't mention that, that indicates to me that very little of your signal is actually being radiated.

A full-size, center-fed, 40 meter dipole cut for 7.03 MHz is a little bit more than 67 feet long, and no counterpoise is required. I can almost guarantee you that you'll get some answers with one of those!

**I strongly discourage using a G5RV** for the reasons listed on the G3TXQ page about them.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15987/no-contacts-with-rockmite, by mh00h, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
