# Importance of Ferrite Size in Coax Choke Balun

*Tags: rf-power, balun, transmission-line, ferrite, choke-balun · score 9*

## Question

The question is quite simple: When making a coax choke balun, does the size of the ferrite matter, and if so, why?

I have seen design notes that say to use a single FT240-43 toroid for powers up to 400W, and then to use two stacked FT240-43 toroids for powers up to 1 or 2 kW. I am specifically talking about choke baluns here, I understand that other designs operate differently. In a choke balun, the ferrite is only stopping current from travelling along the outside braid of the coax - it does not see the main transmitter power (as this is contained inside the coax).

Example:

*Image used with permission - source [M0TAZ Blog*]

My understanding of the theory is that these ferrites are only (ideally) effective on currents along the outside of the coax - the currents that are to be choked - and the internal currents are not affected.

Since the purpose of this is to reduce the current flowing along the coax screen outer to nothing, why does the ferrite need to be so large? A typical configuration would see a choking impedance of above 3kΩ even at the LF bands, so I am at a loss as to why such huge large masses of ferrite are needed.

I assume the basis for such "rules" is that the ferrite will saturate if there is not enough of it. But will it?

I am ignoring things like AL value, etc., since this can be achieved over a range of ferrite sizes/turns.

## Accepted answer (score 5, by Chris K8NVH)

When making a coax choke balun, does the size of the ferrite matter, and if so, why?

Simplest answer: If the choke impedance is low enough to allow some common mode power through, then there is a possibility of overheating. The bigger cores either dissipate heat better or provide higher impedance.

Another way to say the same thing: As long as the choke impedance is high enough, ferrite size does not matter. "High enough" depends on a lot of factors, but "5,000 Ohm" seems to be the target.

Jim Brown, K9YC, has a publication ("A Ham's Guide to RFI, Ferrites, Baluns, and Audio Interfacing" http://k9yc.com/RFI-Ham.pdf ) which goes into this in great detail. A small excerpt from Revision 7, 2019 (page 30) states 1 of 4 criteria for using common mode chokes as baluns:

Dissipation The choking impedance must be high enough to reduce common mode current to the level such that the choke cannot overheat and damage the core or the coax

Jim Brown advocates choke impedance to be around 5,000 Ohm. Some older references considered 1,000 Ohm to be sufficient. But it depends on how much power you are running and how imbalanced your antenna is.

## Answer (score 3, by carloc)

I believe the choice of the core size is twofold.

As from K8NVH good answer a minimum impedance is needed for the balun to do its job. A common mode impedance much higher than differtial ones involved makes sure the balanced to/from unbalanced convertion takes place.

This somehow drives the size of the core for its mechanical dimensions shall allow the cable winding.

A second point is avoiding core saturation which would turn into heat, reduced impedance and balun effect and possibly intermodulation.

This is obviously power dependant, one simple way to reckon core size is ferrite maximum induction and its cross section found on relevant datasheets.

From the electrical point of view one can just consider the balun as an ideal transformer

converting, say Vp=100V@50ohm (200W) single ended into +Vp/2=50V/0V/-50V=-Vp/2 balanced.

This is done by 1:1 transformer built on the core by the two windings made of the inner and braid of the coaxial cable. Each of these windings developes the same voltage (1:1 turn ratio) "shifting" the output voltages as required.

Just the same as any transformer it ideally let the power go through without "eating" any significative part of it. Then of course losses come into play.

And now, back to K8NVH point form a differnt point of view, the balun impedance is now clearly what is also called magnetizing inductance of a transformer.

Again, just any other transformer, core induction is ruled by frequency, voltage across and number of turns.

Back from basics Faraday-Neumann-Lenz law states that $$ v=\frac{\mathrm{d} \Phi_\mathrm{B}}{ \mathrm{dt}} $$ for each turn and given a supposed uniform field inside the core we have total voltage given by $$ v=N\, A \frac{\mathrm{d} B}{ \mathrm{dt}} $$

where N is the number of turns and A the toroid cross section.

If we finally take the hypothesis of sinusoidal voltage and induction we boil down to

$$V_\mathrm{P}\sin \omega t = N\,A\,\omega B_\mathrm{max} \sin \omega t $$

which after removing time dependance gives the relation between the peak voltage and the maximun induction.

$$V_\mathrm{P}= N\,A\,\omega B_\mathrm{max}$$

This at the lowest working frequency could be used to reckon peak voltage the windings on the core can bear at the core manufacturer maximum specified induction.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16771/importance-of-ferrite-size-in-coax-choke-balun, by M1GEO, Chris K8NVH, carloc. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
