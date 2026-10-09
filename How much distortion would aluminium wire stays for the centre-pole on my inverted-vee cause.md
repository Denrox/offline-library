# How much distortion would aluminium wire stays for the centre-pole on my inverted-vee cause?

*Tags: antenna, antenna-theory, inverted-vee · score 3*

## Question

I used nylon rope from the nearest hardware store to stay the centre-mast on my inverted-vee for the 20. The centre-pole is a long long looong bamboo. The trouble is rain here really isn't friendly to nylon; a year - 2 years at most.

Ham rope/Kevlar/Dacron are beyond my means. A brother operator advised against using MS/GI wire citing both corrosion and distortion in the propagation pattern.

The net lists any number of towers (I believe most of these are high-quality aluminium).

How much distortion would aluminium wire stays for the centre-pole on my inverted-vee cause?

## Answer (score 3, by Phil Frost - W8II)

Maybe a little, maybe a lot. It depends on the particular geometry of that wire. Your best bet would be to either build it and see, or use some simulation like NEC to predict what will happen.

But consider: aluminium wires supporting the center of the antenna are not that different from the conductive feedline that's already there. Provided your wire runs right down the middle of the antenna, and the [dipole is properly balanced](Using%20a%20balun%20with%20a%20resonant%20dipole.md), then your added wire will have very little effect, just like the ideal balanced feedline running up to the ideal dipole. This is because the electric field around the dipole is perpendicular to the line of symmetry, so any conductor along the line of symmetry will have no electric field along its length. No electric field, no current, no radiation.

Of course reality is usually a little more complicated. Still, this is a well-solved problem: AM broadcast towers have metal guy wires that must be isolated from the antenna. You can use egg insulators or tuned sections to help accomplish this.

Further consider, aluminium is a good conductor, so losses will be low, so if your wires become part of the antenna, so what? If the resulting antenna + wire stays is still an effective radiator, hasn't your goal been accomplished?

You could even *intentionally* make the stays part of the antenna, and make yourself a sort of fan dipole. Try cutting the guys at a length to cover some band your current antenna does not, and connecting it in parallel. This could be considered a variation on the fan dipole.

Additionally, there is no particular reason to avoid steel if it's just for mechanical support. Steel is cheaper, has higher tensile strength per unit cost, and stretches less. There are plenty of steel cables acceptable for outdoor service. Any metal you use for a wire is going to potentially carry current, so you might as well pick one on its mechanical merits. Unless you are doing the fan dipole thing, or otherwise managed to get very significant currents on the stays, steel's lower RF conductivity is not a problem. Consider: towers are steel, and the guys on professional AM broadcast stations are steel.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2269/how-much-distortion-would-aluminium-wire-stays-for-the-centre-pole-on-my-inver, by VU2NHW, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
