# 80/160m Shortened Dipole Trap Questions

*Tags: dipole · score 6*

## Question

I seem to have forgotten some things I learned years ago for my amateur radio exams. If I am building a 2 band shortened dipole and want a trap between 80 and 160 do I make the trap resonant on 80 or 160 or elsewhere? I guess I may be mistakenly viewing the trap as a gate that allows certain frequencies and not others. Is this correct thinking (albeit simplified)? Can anyone tell me what I should be shooting for here or help me understand the function of traps in a shortened dipole and how I would go about making a trap for a 80/160 dipole? Full length 80 is fine, with a short 160, would be best.

## Accepted answer (score 2, by WPrecht)

Traps are L-C cicuits that become high impedance at their resonant frequency. It's common to make traps by winding lengths of coax around circular forms like PVC pipe of various diameters. The center conductor of one end is soldered to the shield of the other end, and the remaining center conductor and shield connections are connected to the antenna elements.

The series-connected inner conductor and shield of the coiled coaxial-cable act like a bifilar or parallel-turns winding, forming the trap inductor, while the same inner conductor and shield, separated by the coaxial-cable dielectric, serve as the trap capacitor.

The resultant parallel-resonant LC circuit exhibits a high impedance at the resonant frequency of the trap and effectively disconnects everything after the trap from the antenna. Any inner traps (which are operating below their resonant frequency) function as loading coils and shorten the overall physical length of the antenna.

In your case you'll want at least 3 traps. One will be resonant at the lower end of the 80m band. This will disconnect the 160m portion of the antenna when you are transmitting on 80m. You'll want one between there and the feedpoint with a resonant frequency *above* the highest frequency you'll use on this antenna. This one is really a loading coil to make up for the physcilally short antenna length. The other will be between the 80m trap and the end of the entenna. This one should be resonant *below* the 160m band and will serve as a loading coil on 160m.

A couple of notes are in order:

- Coaxial-cable traps have a relatively high Q, which results in a relatively sharp frequency resonance.
- Which means traps need to be *tuned* for their resonant frequency, you can't use a cookbook approach here, if they are not right on, you've just made a dummy load. To tune the traps, you'll need a dip meter or a sufficiently featured antenna analyzer
- Top band (160m) is a harsh mistress. It rewards the dilligent worshiper who builds full size antennas and punishes all others. You might consider a folded dipole if you have room for a full sized 80m dipole.

**A Further Edit:** A folded dipole is a dipole antenna with the ends folded back around and connected to each other, forming a loop as shown below:

The folded dipole antenna is resonant and radiates well at odd integer multiples of a half-wavelength (0.5λ, 1.5λ, etc.), when the antenna is fed in the center like a regular dipole. It can be made resonant at even multiples of a half-wavelength ( 1.0λ, 2.0λ, etc.) by offsetting the feed of the folded dipole (closer to the top or bottom edge of the folded dipole in the picture).

So you could make an off-center fed folding 80m dipole that will also be resonant on 160m. The feed point impedance will be higher than for a typical dipole, but that's usually not a problem.

## Answer (score 2, by Phil Frost - W8II)

There are many kinds of traps, but the most common kind is a parallel LC circuit:  
*Source: article from w8ji.com*

At resonance, this circuit presents a high impedance. At all other frequencies, it presents a low impedance. So, an 80/160m trapped dipole will be an 80m dipole, with traps at the end of that, with additional wire to resonate it at 160m. To 80m, the traps look like high impedances, effectively disconnecting the extra wire for 160m.

The traps themselves will shorten the amount of wire necessary to achieve resonance at 160m, similarly to a loading coil. However, they don't shorten the 80m section of the antenna. If you barely have enough room for an 80m dipole as it is, you need some additional shortening action.

Easiest is probably to bend the antenna to make it fit. You can stick a 90 degree bend in the antenna and it will still work. The tuning will be somewhat changed, but not radically. You could also add additional loading coils or hats, though these are somewhat harder to construct.

Another option, if an 80m dipole is already very close to your maximum size, is to put up a simple 80m dipole, forget the traps, and instead have a tuning network near the feedpoint that you switch in (or isolate with filters) for 160m operation. The advantage to a trapped antenna is the additional length on the longer bands maintains higher efficiency there, but if your 160m sections are extremely shortened then you aren't gaining any efficiency, but you are making the antenna difficult to construct and tune. If you put loading coils in the 80m sections then you shorten the whole antenna, but compromise performance on 80m when you don't need to. If you have a low-loss feedline, you can even do this with a tuner in the shack, especially considering how low feedline losses can be at 160m.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/826/80-160m-shortened-dipole-trap-questions, by Marcus, WPrecht, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
