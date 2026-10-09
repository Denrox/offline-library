# Good wire for wire antenna?

*Tags: antenna, antenna-construction, wire-antenna · score 21*

## Question

What properties should I look for in a good wire for building a wire antenna? Could anyone recommend something specific for me?

## Answer (score 15, by Dan KD2EE)

Because of the skin effect, which causes most of the electric current to be concentrated around the outer surface of the wire at high frequencies, larger gauge wire is needed for RF than for an equivalent DC current. As a general rule of thumb, 16 gauge is sufficient up to 100 watts, but 12 would be ideal. Any system exceeding 100 watts really needs to have the actual current and skin effect calculated, and that is dependent on frequency and also somewhat on antenna type.

Since most antennas are used outdoors, you must use outdoor-rated wire. You can use uninsulated wire, but it is much better to use insulated wire for safety purposes if there is any chance that someone could come in contact with the wire while you are transmitting. If you are using insulated wire, make sure the insulation code (which is printed along the wire) has a "W" in it - it stands for water-resistant. Some examples are XHH **W**, SOO **W**, or TH **W** N.

Stranded copper or copper clad aluminum are the most common - copper clad aluminum is somewhat stronger and has the more conductive copper on the outside, where the current is concentrated. Stranded wire is ideal for flexibility and ease of soldering and crimping.

## Answer (score 10, by on4aa)

Here is an answer for the European hams among us. Printable copies are available from my web site.

## Wire myths

There happens to be a lot of fuss out there about antenna wire. Most amateur radio shops sell "special" antenna wire at unreasonably high price, whilst most of the claims made about these wires are untrue. The situation reminds me a bit of the many loudspeaker cable myths. However, for those living in Europe, a less expensive and even better alternative exists.

## What I use

For all my wire antenna projects I always use extremely flexible and comparatively cheap black-coloured 4mm²-sized **tinned HO7 V-K 4 wire.** As a comparison, 4mm² corresponds to about AWG 11. "HO7 V-K 4" is the European harmonisation code for this wire. Rather unfortunately, this harmonisation code did not foresee a means of specifying the property of being "tinned". So, **make sure to specify "tinned" when ordering this wire!** In Belgium, the country of its original manufacturer, tinned HO7 V-K 4 is more commonly known as *"VOBst 4 carré."*

## Tinned HO7 V-K *x* specs

**Tinned HO7 V-K 4** is a 4mm² wire made out of 51 tinned-copper braided strands and insulated with a 0.8mm thick layer of soft PVC. Tinned HO7 V-K wire is also available in other cross-sections, the last figure in the wire code indicating the conductor area in mm². Below spec links list all available wire sizes. However, at least for permanent installations, I would stick to the 4mm² size. Keep in mind that at radio frequencies the skin effect greatly reduces the current carrying capacity of any wire. Additional benefits of this wire gauge are its greater breaking strength and a slightly broader VSWR bandwidth.

- HO7 V-K spec sheet
- VOBst spec sheet

The tinned-copper braided strands are what make the wire so *extremely flexible.* The tin around each of the copper strands makes soldering the wire a breeze and, moreover, prevents the copper from oxidizing, especially in salty coastal environments. After all, VOBst wire is designed for use in bathrooms and on board of ships. Nevertheless, I always make sure to cap the wire ends with a dot of solder and clear glue to prevent moisture from entering through capillary action. It is better to be safe than sorry!

## Modelling PVC insulation

The 0.8mm thick black-coloured soft polyvinyl chloride (soft-PVC) insulating sheet is perfectly UV-resistant; it will withstand exposure to sun rays. For those who would like to model wire antennas with NEC, the only data I have found for the relative permittivity $ε_r$ of soft PVC is the wide range of 4.0 to 8.0$^1$. The 4nec2 internal manual mentions a range of 4.0 to 5.0 for soft-PVC without quoting any reference. The actual value for a particular sample will depend on the amount of softener used in it; more softener will result in a higher permittivity. However, *a value of $ε_r=5$ would be a plausible estimate for most PVC-insulated wires.*

Most of NEC-2-based antenna modelling programs (e.g. 4nec2 and EZNEC) will model insulated wires. Please, refer to their respective user manuals for more information. L. B. Cebik, W4RNL (SK), also wrote about modelling insulated wires with NEC-2.

## Leave some sag!

I have been operating my antennas for many years now without any issues despite some severe weather, salt and strain exposure. Of course, be sure to leave some sag when hanging up wire antennas. Check out Owen Duffy's, VK1OD, antenna wire catenary calculator to know how much sag would be required for your particular application.

## Electrical supply store

I am not selling this wire! If you are living in Europe, the good news is this wire can be ordered from your local electrical supply store. It is normally deliverable without much delay. To give you an indication of its price; in November 2006, I bought from a wholesaler 100m VOBst 4mm² for €66.33 (incl. VAT) and 100m of the lighter 2.5mm² VOBst for €40.35 (incl. VAT).

## References

1. The American Radio Relay League, Inc. The ARRL handbook for radio amateurs. In: 69 ed.; 1992:p.35–34.

## Answer (score 7, by Tom Horne W3TDH)

Be sure that the wire that you use is acceptable legally as well as physically. In any place were the National Electric Code (NEC), that is used in much of the United States, is enforced as law the minimum size of wire that can be used for an amateur radio transmitting antenna is number fourteen American Wire Gauge (14AWG). For people in other parts of the world that is equivalent to 1.63mm diameter or 2.08 square mm. If you use a smaller gauge in such an area subject to that code than any harm that might result from the antenna failing and falling into contact with people or things is entirely on you. For the sake of those who may be able to make direct use of the information the applicable section of the NEC is

ARTICLE 810 Radio and Television Equipment

III. Amateur Transmitting and Receiving Stations — Antenna Systems

810.52 Size of Antenna.  
Antenna conductors for transmitting and receiving stations shall be of a size not less than given in Table 810.52.

The table requires 14 gauge for lengths up to 150 feet with larger gauges for longer lengths dependent on the type of wire used. The important thing to know is that fourteen gauge is the smallest size of wire permitted for a amateur radio antenna and that there are no exceptions to permit a smaller gauge for any reason in areas were the NEC is enforced as law.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/140/good-wire-for-wire-antenna, by Timtech, Dan KD2EE, on4aa, Tom Horne W3TDH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
