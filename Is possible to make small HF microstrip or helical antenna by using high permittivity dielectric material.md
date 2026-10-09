# Is possible to make small HF microstrip or helical antenna by using high permittivity dielectric material?

*Tags: antenna, propagation, rf-power · score 5*

## Question

Is possible to make small HF microstrip or helical antenna by using high permittivity dielectric material like SrTiO3 ?

## Accepted answer (score 1, by on4aa)

Yes, you can! Most of us have two arrays of these as the rods and cones in the retinas of our eyes.

The permittivity of the dielectric even does not need to be that high. I used high-density polystyrene $(\epsilon_r=2.55)$ to build a 10GHz dielectric rod antenna with a measured gain of 20.5dBi.

Dielectric rod antennas support the propagation of a surface wave along the rod. At the end of the rod, this surface wave will interfere with the space wave, also launched by the feeder. Together this creates the large directivity of this type of antenna.

Once you understand dielectric rod antennas, you will also understand long Yagi-Uda antennas because the space between the Yagi elements can be regarded as an artificial dielectric.

## Answer (score 3, by Phil Frost - W8II)

Yes.

The electrical dual of an antenna loaded with a high permittivity material is the loopstick antenna. Loopstick antennas are common in portable AM receivers.

The antenna consists of some turns around a high permeability core. This core effectively multiplies the magnetic field by aligning its own magnetic domains with the magnetic field due to the current in the coil.

Likewise, a material with a high dielectric constant, or permittivity, can be used similarly to multiply the electric field. This can be used to construct an antenna with an effective aperture much larger than would otherwise be attainable.

Because these antennas are electrical duals, what is true about the loopstick antenna will be analogously true of a dielectrically loaded antenna. Like the loopstick, an antenna loaded with a high permittivity material will have a reactive impedance, though it will be capacitive rather than inductive. Like the loopstick, or indeed any small antenna, as size goes down, so does operating bandwidth. And like the loopstick, the properties of your antenna will be limited by the dielectric material.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2291/is-possible-to-make-small-hf-microstrip-or-helical-antenna-by-using-high-permi, by abduoman11, on4aa, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
