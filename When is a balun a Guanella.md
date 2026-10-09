# When is a balun a Guanella?

*Tags: balun, jargon · score 6*

## Question

I've searched this site, wikipedia, other sites, and haven't found a clear answer:

What features or parameters of a balun or choke put it into the category/definition of a "Guanella"? Where does the name come from?

## Answer (score 4, by hobbs - KC2G)

A Guanella balun is a transmission line device based on a design described by Gustav Guanella in a 1944 paper in Brown, Boveri & Company's internal journal *Brown Boveri Review* titled "New Method of Impedance Matching in Radio-Frequency Circuits". It can be found online here.

Guanella was, evidently, the inventor of the common-mode choke as we know it: a transmission line (coax or balanced line) wound around a core so as to present a high impedance to any common-mode current and "force" the currents on both halves of the transmission line to be equal. This is also known as a Guanella choke or a Guanella 1:1 balun.

Other Guanella baluns combine wideband impedance transformation with choking by using the 1:1 Guanella balun as a building block and basically nothing else. A 4:1 Guanella consists of two 1:1 Guanellas, wired so that they are in parallel on the input side, but in series on the output side. Thus the output sees twice the voltage and half the current, or 4 times as much V/I. Other ratios (such as 9:1) are also possible, but less common.

Any kind of a "voltage balun" is not a Guanella. Anything with a transformer or an autotransformer (where the bulk of the power is coupled through the core) is not a Guanella. Any balun that relies on a delay line to work is not a Guanella. Any balun/unun/impedance transformer based entirely on the action of chokes *is* a Guanella, as far as I know.

... but it's worth noting the existence of the "bad" 4:1 balun, which claims to be a 4:1 Guanella, but saves on materials by winding both chokes on the same core. Not only is this not really a Guanella (putting the two windings on the same core causes some transformer action between them), it's also *not a good balun*, as measured by W8JI, DJ0IP, and others.

## Answer (score 3, by tomnexus)

A Guanella balun or transformer is constructed *so that there is effectively no magnetic flux in the core(s)*. There is of course some, otherwise it wouldn't have any inductance, but the common-mode current is effectively suppressed by the common-mode impedance. The core remains cold, even at the highest operating power.

By contrast the Ruthroff transformer *uses* the magnetic flux to transfer power, much like a regular low-frequency power transformer.

## Answer (score 2, by Phil Frost - W8II)

A Guanella balun is a device which consists of some series and/or parallel combination of transmission lines wound on ferrite cores which simultaneously presents a high impedance to common-mode current and provides a transformer-like impedance transformation between input and output.

Guanella refers to Gustav Guanella. Guanella held numerous patents, but the one most relevant to this particular question is US patent US3025480A. Fortunately for us, US patents must make a number of "claims", which make a suitable definition for a "Guanella balun":

I claim:

1. A four-terminal transmission device for high frequency signals comprising an insulating plate and a pair of parallel metallized strips applied to said plate, to form a two wire transmission line, the adjoining pairs of ends of said line constituting the input and output terminals of said device, and a two-part hollow member of high resistivity magnetic material having a permeability greater than one and arranged with the component parts thereof mounted upon opposite sides of said plate, said member forming a magnetic enclosure closely encircling both said strips of said line.
2. A four-terminal transmission device for high frequency signals comprising a two-wire transmission line being constituted by a pair of parallel wires embedded in a flexible insulating carrier, a layer of high resistivity magnetic material having a permeability greater than one upon said carrier, to provide a composite flexible member comprising said line, said carrier and said layer, said member being wound into a bifilar spiral coil with the opposite projecting ends of said line forming the input and output terminals of said device.
3. In a transmission device as claimed in claim 2, said coil being wound upon a cylindrical core of magnetic material.
4. In a transmission device as claimed in claim 2, said coil being wound upon a cylindrical core of magnetic material with the adjacent turns thereof in close engagement with one another.
5. A transmission device for high frequency signals comprising a plurality of transmission line coils as described in claim 2, a common magnetic core supporting said coils, and means to interconnect the inputs and outputs of said coils, to provide a desired input-output impedance ratio of the composite transmission device comprised by said coils.
6. A transmission device for high frequency signals comprising a plurality of transmission line coils as described in claim 2, a closed magnetic core interlinking said coils, and means to interconnect the inputs and outputs of said coils, to provide a desired input-output impedance ratio of the composite transmission device comprised by said coils.
7. In a wide-band transmission device as claimed in claim 2, said layer of magnetic material having a thickness to provide high inductivity of said coil for unsymmetrical currents having frequencies corresponding to the upper partial frequency range of a desired frequency band to be passed by said device, and the coil mode inductance of said device providing adequate inductivity for the unsymmetrical currents within the lower frequency range of said band.
8. In a wide-band transmission device as claimed in claim 2, said layer consisting of a ferrite having a thickness to provide adequate inductivity of said line to suppress unsymmetrical currents having frequencies corresponding to the upper partial frequency range of a desired frequency band to be passed by said device, and the coil mode inductance of said device providing an adequate inductivity to suppress unsymmetrical currents within the lower frequency range of said band.
9. A four-terminal transmission device for high frequency signals comprising an insulating plate, a pair of metallized strips applied in registering relation to the opposite faces of said plate, to form a two-wire transmission line, and a hollow member consisting of high resistivity magnetic material having a permeability greater than one and enclosing both said strips, said member being composed of two U-shaped parts arranged with the legs of one U abutting the legs of the other U and mounted in slots of said plate adjoining said strips.

Slightly more approachable is some of the description at the start of the patent:

In the case of known balancing transformers used for the symmetrization of high frequency lines or devices, it has been customary to provide a wound up two-wire or Lecher line which, as far as symmetrical currents are concerned, behaves as a straight line, while offering considerable inductive impedance to unsymmetrical or inphase currents. Balanced-to-unbalanced transformers of this type are described, for instance, in United States Patent 2,509,057. Since devices of this type behave analogously to an ideal transformer having a transformation ratio 1:1, it is possible by the combination of two or more devices to provide a balancing system having a transformation ratio differing from one. Thus, by connecting the inputs of two devices in series and connecting their outputs in parallel, there may be obtained a voltage input-output ratio of 2:1, corresponding to an impedance transformation ratio of 4: 1.

Balancing devices of this and other well-known type as used by the prior art are both complicated in design and the number of parts required, as well as costly in the fabrication and assembly thereof.

Accordingly, it is a principal object of the present invention to avoid the disadvantages of the known devices by the utilization of a simple two-wire or Lecher line being passed through or mounted in a magnetic body having a permeability greater than one. By the provision of such a body or sheathing of the two wires, the inductive impedance offered to unsymmetrical or in-phase currents through the conductors is increased considerably, while the mutual inductance between the wires for symmetrical or oppositely-phased currents is increased to only a negligible extent. Arrangements of this type behave, therefore, analogously to a wound up two-wire line of the type described by the above patent and are suited for the symmetrization of high frequency devices for circuits.

So essentially, Guanella acknowledges in the patent that common practice at the time was to wind up a transmission line to create a common-mode impedance. This would be similar to what we might call today an "ugly balun", only at the time coax was not as ubiquitous as it is today. These devices did not involve any ferrite or other magnetic core.

Furthermore, these baluns could be connected in series or parallel combinations to achieve an impedance transformation between input and output, in addition to presenting a high impedance to common-mode current.

Guanella's idea, and the subject of the patent, is to use ferrite to couple the lines together. This made the baluns smaller, cheaper, and more effective.

The most commonly encountered application of this idea is the 4:1 Guanella balun, described in the patent:

By the combination of two or more two-wire lines or devices of the type according to the invention, it is possible to secure a transformation ratio differing from one, as well be described in greater detail hereafter. A an example, since with a proper design of the inductance of the coil DR, FIG. 14, the latter may be practically neglected, it is possible, for instance, to connect the input of a pair of two-wire transformers or devices in series and to connect their outputs in parallel, as shown in FIG. 19. In the latter, the common input junction point will be at a potential intermediate between the potentials of the input terminals 1 and 2 and, if desired, may be connected to a special zero or neutral terminal 0, as indicated by the dotted line in the drawing. A combination of a pair of two-wire devices according to FIG. 19 results in a voltage transformation ratio of 2:1, corresponding to an impedance transformation ratio of 4:1. In an analogous manner, it is possible to connect the inputs in parallel and to connect the output in series, as will be readily understood.

However, the patent is not limited to just 4:1 transformations, but rather any series and/or parallel combination of transmission lines wound on ferrite cores.

The patent by legal necessity is very specific about the kinds of transmission lines, and how they may be wound, and so on. However, for more casual discussion I think we can drop all the specifics enumerated in the claims and consider any kind of transmission line on a ferrite applicable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19912/when-is-a-balun-a-guanella, by Jay Rabe - KJ7TTT, hobbs - KC2G, tomnexus, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
