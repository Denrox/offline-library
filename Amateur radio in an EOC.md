# Amateur radio in an EOC?

*Tags: emergency, procedure · score 12*

## Question

Consider a small town's emergency operations center. While there are amateur radio operators involved, they primarily work for government or public safety, and there is no active ARES participation. The EOC is reasonably well-equipped, with redundant power, (questionable) redundant internet, phone lines, and drop-box public safety radios for coordination or dispatch. Assuming that the EOC cannot guarantee a dedicated amateur operator, but can have an operator working dispatch take on some additional responsibility, what is the highest-impact amateur service to monitor? How should it be operated? (Monitor a specific frequency or set up a scan list? Periodically announce that they are listening?)

Some ideas - monitoring a local repeater has a poor signal to noise ratio, APRS has relatively few users due to the need for specialized equipment, and HF would be somewhat less useful due to the small coverage area. Or am I selling one of these short?

## Answer (score 5, by PearsonArtPhoto)

The two most important parts of any emergency are logistics and communication. There are two primary means of communication which are important.

1. The EOC should have access to a variety of communication systems, including police, fire, phone, internet, and amateur bands, with the ability to clearly communicate with the entire city easily, and the key outlying communities.
2. I don't know anything about police/fire, except that I'm assuming if you ask around the police/fire departments you can find some sort of a suitable rig to assist with communications.
3. Amateur bands are useful for reporting local events to the EOC's attention with a lack of communication. Many of these will come via mobile or even HT, the ideal EOC should be able to receive an HT signal and understand it sent anywhere within it's domain of operations. If it is not possible to do via simplex, then it should be coordinated with local repeaters, many of which are willing to take on such responsibilities.
4. Some ability needs to be available to communicate with the next level up in emergency handling. This could be a county seat, or the state capital, or another designated area. This could be done via a dedicated yagi connection for 2m if fairly close, or even better done over HF bands. At the very least, a 40/80m capable wire antenna should be placed on the roof of the EOC, with the cable running down to the center. This will allow amateurs to bring their own rig to supplement the EOC.
5. If you are running an EOC on a remote island, you probably want a tri-bander yagi antenna (10, 15, 20m yagi), 2-3 elements, which would do wonders for your communication. You'd have to be pretty remote, ie, more than 500 km, for this to be the ideal solution.

I suspect that purchasing and installing a 2m/440 J-pole antenna, HF 40/80m antenna, lightning protection, and the supporting cables will only run \$200 or less, if purchased wisely. A 2m/440 rig could be purchased for another \$200, battery for \$100, and you have a capable setup that should manage in most emergencies, if supplemented by an experienced ham. It would be good to have hams practice using such equipment on a regular basis, maybe once or twice a year.

## Answer (score 3, by WPrecht)

I've been thinking about this off and on since touring my local county's EOC (a very worthwhile trip). Probably monitoring a 2m frequency (that's not a repeater) has the best chance of providing value.

What I have come up with, assuming the EOC could have a licensed amateur available at least some of the time is to have them come on the area repeaters a few times a day and announce that the EOC is monitoring 146.52 (or pick a locally clear frequency) for emergency traffic and to report it there.

You aren't trying to reach people having an emergency necessarily, but to create the general knowledge in the local community that the EOC is monitoring a frequency. Then, if anyone comes along with a problem, they've either heard the announcements or someone on the repeater has and can direct them to the appropriate frequency.

If the EOC's area of responsibility includes some wilderness area, they could also scan the "Wilderness Protocol" frequencies on the specified times.

This solution is the cheapest I could come up with since it only requires one staff member with at least a Tech license (in the US) and common 2m rig with a decent external antenna. If the EOC were to get more $$ or operators, they could consider something more ambitious using more bands or whatever is appropriate in their area.

## Answer (score 3, by catdude)

If a local repeater is operated by a cooperative trustee, having a net control station who would agree to place the repeater into a controlled net status in case of emergency could be useful. In my community the National Weather Service monitors one of our local repeaters during extreme weather events, and one of the skilled net control station will place the repeater into emergency mode during such events.

And the specialized hardware needed for APRS operation isn't as formidable an obstacle as it might have been a few years ago.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/690/amateur-radio-in-an-eoc, by Dan KD2EE, PearsonArtPhoto, WPrecht, catdude. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
