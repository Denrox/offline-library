# FCC tracking of unlicensed FRS/GMRS transmissions

*Tags: united-states, legal, fcc, frs · score 16*

## Question

If a transceiver such as the BaoFeng UV-5R is used to transmit over FRS/GMRS frequencies (unlicensed), it is illegal in the United States due to FCC regulations that state that the power must be <0.5W and that the radio must not have a detachable antenna (the UV-5R is rated up to 5W and has a detachable antenna). Realistically, though, I am wondering if and how the FCC actually enforces this?

For instance, if two people decided to use these as high power "walkie talkies", and were careful to select unused frequencies, didn't disrupt other peoples' communications, didn't communicate from home/work (i.e. a static location that identified the person transmitting), and changed frequencies regularly, my questions are:

1) I understand the law, but is it actually enforced? Do they even waste resources trying to catch people doing this if there is no disruption occuring? Are there any documented cases of the FCC actually tracking down and harassing/fining/jailing people for illegal FRS/GMRS transmissions of this sort?

2) How would the FCC actually track down this sort of sporadic, non-disruptive transmission from multiple locations? I understand the concept of triangulation of radio signals, but how is this actually achieved on a nationwide scale and in a way that can promptly lead them to the location of the transmission (so that they can fine/arrest someone)? Are there passive monitoring systems in place in urban areas that can automatically/instantly detect illegal transmissions? Black helicopters with FCC agents flying around hunting for illegal walkie-talkie usage? etc :) What does their tracking technology actually look like nowadays, and what kind of capabilities does it have that would enable tracking this type of transmission?

3) Are there any sorts of identifying signals (some sort of unique identifier) that handheld transceivers such as these emit while transmitting, that allow for the instant identification of the device? (i.e. something akin to an IMEI # for cell phones)

## Accepted answer (score 14, by natevw - AF7TB)

Are there any documented cases of the FCC actually tracking down and harassing/fining/jailing people for illegal FRS/GMRS transmissions of this sort?

You can browse the Enforcement Bureau's Field Notices at http://transition.fcc.gov/eb/FieldNotices/. I did find a few related to FRS violations, e.g. several cases where a company (or even a township water authority!) was using FRS/GMRS for business purposes — even going so far as to set up repeaters.

I didn't find a case of enforcement against simply an individual casually using an unlicensed walkie-talkie in an otherwise non-interfering manner. However, if the FCC truly "didn't care" they would change their rules to reflect that.

Instead, they have recently (May 26, 2016) issued a Public Notice warning that "Persons or Businesses Using Authorized Equipment In a Manner that Violates Federal Law or the Commission’s Rules Are Subject to Enforcement Action". They don't single out "use an uncertified ham handheld on FRS?" in their examples — and in fact they mostly seem to be targeting the use of "authorized equipment" in *un*authorized ways — but it's clear that at least some attention is being paid to the use of "unlicensed" (more properly, "licensed by rule") spectrum.

The ARRL for their part, want you to think of the the FCC's notice as applicable in this case. In their news item covering the notice they add this as their own example: "using an Amateur Radio transceiver on the Family Radio Service."

How would the FCC actually track down this sort of sporadic, non-disruptive transmission from multiple locations? […] Are there passive monitoring systems in place in urban areas that can automatically/instantly detect illegal transmissions?

Most of the NAL documents I've seen are in response to **complaints**. Even the aforementioned public notice doesn't talk about agency resources being bulked up or anything, but merely "If you have reason to believe that radio frequency equipment is being used […] in a manner that violates the Commission’s rules or the Communications Act, you can file a complaint with the FCC."

The liability letters also provide insight not just into *why* enforcement action was taken, but how enforcement is done. For example, when a GMRS licensee was maliciously interfering with a LMRS licensee, one of the transmitting antennas involved was tracked down "using a mobile direction finding ('MDF') vehicle" — i.e. they had to send an agent out driving around to find the perp. Perhaps this is merely parallel construction, but taking their word for it, means enforcement is not cheap.

The FCC does have a High Frequency Direction Finding Center which is apparently fairly precise — whether this is true or primarily a Television detector van-type ruse to keep us honest I couldn't tell you. (It's certainly more plausible in the case of an intentional radiation.)

Of course, due to much more limited UHF propagation you would need a lot more listening stations to address this sort of problem. Perhaps there is public information on this, perhaps there is inter-agency involvement NOT part of the public record (the HFDFC is part of a "Homeland Security" bureau…) — whether the feds are as interested in non-hams out hiking with Baofengs, as they are in tracking the cellphones of everyone attending a political protest… your guess is as good as mine…

Are there any sorts of identifying signals (some sort of unique identifier) that handheld transceivers such as these emit while transmitting?

Radio fingerprinting is a thing, for an example of some of the signal characteristics that might be involved check out Use Real-Time Spectrum Analysis to Characterize a transmitter key-up. Whether the FCC could or would use this as sufficient evidence for liability, I don't know.

## Answer (score 3, by Iceinmind)

It also depends on the legal users of that part of the spectrum who may land up monitoring violations and reporting to FCC. Eg ARRL has monitoring volunteers who monitor for amateur band violations. I would think that it will be in the commercial interest of the cellular companies to monitor any abuse of their frequency spectrum and report t violations to enforcement agencies.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6471/fcc-tracking-of-unlicensed-frs-gmrs-transmissions, by J. Taylor, natevw - AF7TB, Iceinmind. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
