# Is this mystery antenna suitable for ham radio?

*Tags: antenna · score 4*

## Question

Brand new amateur radio license holder, and I know next to nothing. I just got my mobile radio: Anytone D578UVIIIPlus. The base station accessory bundle I also got, came with this vertical antenna: AnyTone Tri-band Mobile DMR Antenna. I'm interested in setting up my antenna in my attic above my ground floor office, but when looking in my attic I found a mystery antenna from the previous owner already hanging there.

What type of antenna is this mystery antenna, and is it suitable for ham radio?

Mystery Antenna - Bottom View:

Mystery Antenna - Cable Connection:

Mystery Antenna - Top View:

## Answer (score 10, by tomnexus)

This is an old classic TV antenna called a YUCOLP.

From Kraus Antennas:  
It covers the 54 to 890 MHz TV bands:

- LPDA for 54-108 and 174-216, using a trick of bending the dipoles forward so they can work both at $\lambda/2$ and again at $3\lambda/2$.
- Corner Reflector Yagi for UHF giving better gain and F/B than the LPDA would provide there but only from >500 MHz.

It probably doesn't work so well at 145 MHz, but the LPDA part could probably be cut down to work there. The front part is not useful for ham bands without extensive modification. It also looks like it's not assembled with the forward sweep, if it needs it, and one of the elements is damaged.

If you measure all of the elements and their positions we can make suggestions as to how you might modify it. For transmitting I think you will have another problem - the thin wires that make up the boom of the LPDA indicate that it's probably a 300 ohm feed, with some sort of balun/transformer for the 75 ohm coax. This won't work so well for transmitting. A replacement transformer will be yet another thing to design and build.  
For just getting on the air, if you want to build your antenna, it would be better to build a simple ground plane antenna. You might still re-use some bits of this one for the metal elements.

## Answer (score 4, by niels nielsen)

Thus is a vhf/uhf tv antenna for local reception. With a little care you can salvage the tubular aluminum elements by drilling out the pop rivets that hold them into the plastic fitments, which can be similarly salvaged. Then you can assemble something like a 2 meter Yagi out of the salvaged parts. There are sources on the web that explain how to build ham antennas out of disassembled TV antennas like this.

## Answer (score 3, by Ryuji AB1WX)

The photo is not very clear to tell with confidence, but at least a part of that antenna looks like a log-periodic antenna. I'm not sure if the photo includes two antennas or the boom is bifurcated or something else, but it may be optimized for terrestrial TV broadcast VHF and UHF bands. Again, the photo is unclear but that coax terminal looks like an F connector typical of consumer broadcast receiver sets.

If that is made for broadcast receivers, that antenna probably lacks amateur band coverage (whereas a true wideband log periodic would).

I wouldn't consider using that antenna for amateur radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23182/is-this-mystery-antenna-suitable-for-ham-radio, by Jared, tomnexus, niels nielsen, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
