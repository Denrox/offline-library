# What kind of soldering iron is best for PL-259 (UHF) connectors?

*Tags: antenna-construction, uhf, coaxial-cable · score 5*

## Question

**What do you use to solder connectors onto bulk coax cable?**

Soldering the UHF connector to the coax shield on a PL-259 is described as requiring a bit of "experience and skill" in Dave Casler's video.

**UHF Connectors 274**

The trick is to solder through the four holes in the connector shield to the braid by getting it hot enough for the solder to flow properly - but at the same time, it must be done quickly enough so that the dielectric inside the coax cable doesn't melt and allow the inner conductor to migrate.

Yes, I know that I can buy 'ready-made' cables and that I could use 'crimp-on' connectors but I don't trust them after having bad experiences in the past. An example is crimping a Sta Kon ring connector onto a wire. It makes a good mechanical attachment but over time a high electrical resistance will often develop.

One thing that Dave doesn't mention in his video (besides experience and skill) is that putting one of these connectors on successfully also requires the use of a suitable tool - in this case, most probably a soldering iron.

**So what have you used to do this job properly?**

I have used Weller soldering guns of various wattage, soldering irons of different sizes and have even tried a butane torch. Too small of an element and all the heat of the tip is consumed before the connector gets hot enough to flow solder - and waiting for it to heat back up melts the coax!

The Weller guns don't have much thermal mass in the tip and so they seem to take much too long to get the connector hot - and it melts the coax!

I watched a ham install a connector in his shop one time and he did a marvelous job... BUT - his tool of choice was an old and huge soldering iron that'd been passed down to him from his father and he wasn't willing to sell it.

**So what kind of tool have you successfully used that you recommend for the job?**

## Accepted answer (score 3, by Ben Madsen)

It looks like you may be trying to solder to the reducer rather than the actual connector. If that is the case, try soldering to the connector through the openings in between the threading designed for the screw cap.

The other tip that I've been given is that using a larger sized tip for a soldering *iron* (not sure if the Weller Solder Gun has replaceable tips, my experience has been with irons) allows a faster transfer of heat and can melt the solder more quickly into the desired location.

## Answer (score 6, by webmarc)

I'm going to answer a slightly different question to the one asked... I promise not to be offended if it's ignored or even downvoted (if it receives enough downvotes, I'll delete):

Crimping, with the right tools, can be superior to soldering.

This is contrary to what I learned from my dad and many others growing up, that soldering is king. But it turns out that with the right tools in hand, crimping creates both the needed physical bonding required AND provides some marginal mechanical improvements.

Some sources:

- https://rfindustries.com/crimp-vs-solder-vs-compression-pros-cons/
- https://monroeengineering.com/blog/crimping-vs-soldering-cable-connectors-which-is-best/
- advocating for using both on a connection in a "high vibration environment" such as cars: https://www.motortrend.com/how-to/soldered-crimp-connectors-work-well/
- and believe it or not, NASA crimping standards (who *I believe* reserve soldering for PCB... though I wasn't able to verify this and may well be misremembering) https://nepp.nasa.gov/files/27631/NSTD87394A.pdf

All this to say, in **my** particular operating environment, I've had great and long-lived success with well crimped connections coupled with appropriate weatherproofing measures.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20790/what-kind-of-soldering-iron-is-best-for-pl-259-uhf-connectors, by Dax, Ben Madsen, webmarc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
