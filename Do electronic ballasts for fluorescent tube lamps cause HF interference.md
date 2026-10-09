# Do electronic ballasts for fluorescent tube lamps cause HF interference?

*Tags: hf, rfi · score 3*

## Question

I am going to build a new home and I would like to use energy-saving fluorescent tube lamps in some rooms. Manufacturers are currently pushing electronic ballasts a lot in favour of switchstart series ballasts.

I have no experience with electronic ballasts. Should I be wary of them? Do these electronic ballasts cause more LF, MF or HF interference?

## Answer (score 2, by jcoppens)

There is another reason to be wary... Electronic ballast manufacturers sell them in all shades. I recently bought a batch of them, one of which broke down quite quickly. Being the electronics engineer, I dismantled the ballast and checked. And noticed that several components where missing.

I considered this enough motive to draw the circuit and noticed that the missing parts were:


about filtering RF interference


and protective circuitry (in fact, only a $0.02 diode) which switches off the oscillator if one of the filaments of the tube was bad, thus avoiding potential electronic component breakdown.

So I took all the ballasts back to the seller and selected one, only slightly more costly, and never looked back. They've been doing their job for over 6 years now.

Conclusion, buy a reputable brand... even if it's slightly more costly.

A note about the RFI itself: It will probably not be the electronics themselves that cause the RFI. The oscillator and choke use ferrite cores which are quite autoshielding. The real culprit for the RFI is the cabling in the tube mounting apparatus (and not to forger the tube itself).

## Answer (score 2, by Dan KD2EE)

To the question in your title - do they cause interference - the answer is absolutely yes. However, it's hard to answer which causes *more* simply because there is a lot of variation between manufacturers and models. QST (the US ARRL magazine) recently ran an article on this topic - the conclusion was that the number one factor in RF interference, regardless of band, was whether the unit was labeled for residential use or not.

Our FCC places stricter limits on residential ballasts than on commercial for RFI. I cannot find any specific regulatory information for the EU, but I suspect that you'll also be able to find residential units, as many of the big-name brands sell the same product worldwide and get it fully approved to every country's requirements.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/525/do-electronic-ballasts-for-fluorescent-tube-lamps-cause-hf-interference, by on4aa, jcoppens, Dan KD2EE. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
