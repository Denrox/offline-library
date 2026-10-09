# Cordless phone consistently experiencing RFI

*Tags: rfi · score 4*

## Question

I've tried several cordless phones (most recently KX-TG570), and all seem to frequently pick up terrible RF interference. I have a neighbor that is a ham enthusiast, with large antenna masts on the first rooftop, and it does seem to coincide with his use periods. I'd prefer not to bother him about it, but if I could solve it another way, that would be great.

I've tried wrapping the phone cord in a loop to act as a filter. I also asked IP about it, and they said I never upgraded to VOIP yet. Would that really help this case? I would think the cordless hand units themselves may pick up the RF interfernce and maybe not just the physical rj11 line.

I read a few other threads about internet interference, but in my case I'm more concerned about phone line RFI here.

## Answer (score 5, by rclocher3)

First, let me say that most hams would be delighted to have such a polite neighbor! I would encourage you to contact your ham neighbor. Most hams are more than pleased to help neighbors with interference problems, rather than give the hobby a bad name. Also many hams that are active in HF (the ones with large antennas) are good at hunting down interference problems. If you would keep a record of the times that you have interference, your ham neighbor could compare those times to his log book, which would be a help for troubleshooting.

The interference is likely in the telephone line, or the power cable to the cordless phone base. The first thing that I would try is to get two snap-on ferrite beads (which can easily be found for sale with an internet search), one for the phone cable and one for the power cable, and then wrap each cable around a ferrite bead several times. Good luck!

## Answer (score 5, by Glenn W9IQ)

If the interference is coming into your telephone via the RJ-11 cable, then the type of ferrite material you use to suppress the interference will matter. Engineers refer to the type of ferrite as the "mix", meaning what type of ferrite material is mixed to make up the device. These mixes are simply given numbers that are common place in the industry.

There are two mixes that will help knock down interference from ham radio and CB transmissions: type 75 and type 31. The type 75 material is excellent at suppressing frequencies in the 150 kHz to 10 MHz range. In ham speak, this would cover the 160 meter through 30 meter bands. The type 31 material provides broad coverage from 1 MHz to 300 MHz. This would include CB and the 160 meter to 1.4 meter ham bands.

Ferrite materials comes in a variety of physical shapes but the two that are most usable for your application are the toroid (doughnut looking) and the split sleeve type. Either type will work.

When installing the ferrite, plan on several turns through the core so select a core with a large enough hole for this purpose. The reason is that, in general, the effectivity of the choking action goes up as the number of turns squared. So for example, 4 turns is 16 times more effective than 1 turn. Space out the turns evenly on the core, wrap them tightly around the core, and do not overlap turns.

If you are not certain which core material to use, both can be applied to the same cord. Just place one after the other, winding each one individually. Alternatively, talk with your ham neighbor. Most hams are more than willing to help a friendly neighbor with any interference problems. At the very least, your ham neighbor can let you know what bands he or she is operating on so that you can select the best ferrite mix for the situation.

## Answer (score 4, by Mike Waters)

Good answer, but it should be noted that ferrite mixes are **not** created equal. The choice of the mix depends on the frequency of the interference. What works on the 80 meter ham band (3.8 MHz) might not work if the interference is on CB (27 MHz).

A great resource is K9YC's site and specifically, this PDF there. *There is no better information on common-mode RF choke design anywhere, either online or in print.*

Ferrite-core chokes almost always trump air-core chokes. See G3TXQ's excellent information **here** as to why this is true, and note how air-wound chokes have a much narrower effective bandwidth than ferrite chokes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9351/cordless-phone-consistently-experiencing-rfi, by g g, rclocher3, Glenn W9IQ, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
