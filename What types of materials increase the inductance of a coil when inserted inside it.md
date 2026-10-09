# What types of materials increase the inductance of a coil when inserted inside it?

*Tags: antenna-tuner, inductor · score 9*

## Question

I'm asking this because of the comments [in this answer](Is%20it%20practical%20to%20use%20a%20slug-tuned%20variable%20inductor%20in%20an%20antenna%20matcher%20%28aka%20antenna%20tuner%20%29.md), that imply that steel (mostly iron) has similar characteristics to ferrite.

Specifically, it is implied that inserting solid steel into a single-layer coil (as is commonly used in an antenna tuner) will significantly increase its inductance at HF, as some ferrite and powdered-iron rods do.

Is this true under any circumstances?

What are suitable materials for this purpose?

## Accepted answer (score 6, by Phil Frost - W8II)

Any material with a relative permeability greater than 1 will increase inductance when inserted into a coil.

Note that permeability is a complex number and frequency dependent. The imaginary part of permeability contributes to loss and appears as a resistance, so the addition of some material in the coil may increase inductance and also add resistance. Generally, the real part of permeability of materials decreases with frequency, while the imaginary part increases. Thus at some frequency, the material becomes useless for constructing inductors.

Many magnetic materials are also non-linear. This is because they work by aligning internal magnetic domains within the material with the applied magnetic field of the core. At some magnetic flux density, the domains are all as aligned as they can be, and can become no more aligned, and thus can not respond to increasing magnetic flux density. This is called "core saturation".

Any ferromagnetic material, such as iron, nickel, or cobalt, has a high permeability. Paramagnetic materials, such as liquid oxygen work as well. Generally, anything that will stick to a permanent magnet indicates a high permeability at 0 frequency.

In practice, ordinary lumps of metal do not make good cores for inductors because their real permeability decreases rapidly with frequency, and inserting them into a RF inductor just makes them hot. A resistor is a much simpler and economical way to achieve the same electrical effect.

Powdered iron cores and ferrite cores are two common materials engineered to overcome these effects to produce useful inductors up to 10s or sometimes even 100s of MHz. Beyond those frequencies even these materials become ineffective. Fortunately higher frequencies also tend to require lower inductances, and thus air-core inductors become practical.

## Answer (score 4, by Mike Waters)

**TL;DR:**  
It's NOT mild steel, brass, or aluminum.

I connected two different inductors to an antenna analyzer, and all of the above materials *decreased* the inductance as they were inserted.

The larger the diameter of the steel I inserted, the lower the inductance and the greater the loss. It was the worst material I tried.

When I inserted some powdered iron (a 2.4" OD T-200-2 toroid core that I happened to have on hand), the inductance increased. The greatest increase by far was when I inserted a short piece of 1/2" diameter ferrite (Amidon R61-050-750) which was left over from a grounded-grid amplifier cathode choke.

From https://www.w8ji.com/steel_wool_balun.htm:

For example, inserting a solid iron slug inside a small RF coil shows a behavior almost identical to using brass or aluminum slugs. Inserting a solid slug of iron might increases the magnetic field concentration and inductance near direct current frequencies, but at some higher frequency eddy currents and the inability of the core to follow field changes cause the flux concentration to decrease.....eventually reaching zero. At some frequency, the counter MMF takes over. Inductance is actually reduced by the core.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14566/what-types-of-materials-increase-the-inductance-of-a-coil-when-inserted-inside, by Mike Waters, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
