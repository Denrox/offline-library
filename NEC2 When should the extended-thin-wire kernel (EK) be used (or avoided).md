# NEC2: When should the extended-thin-wire kernel (EK) be used (or avoided)?

*Tags: antenna, antenna-construction, antenna-modeling · score 3*

## Question

According to the documentation:

*"Studies of the computed field on a segment due to its own current have shown that with the thin-wire kernel, Delta/a must be greater than about 8 for errors of less than 1%. With the extended thin-wire kernel, Delta/a may be as small as 2 for the same accuracy (ref. 3)."*

However, the documentation does not seem to indicate whether the "extended thin-wire kernel (EK)" should *only* be used when the wire diameter is large compared to the segment length, or if it generally provides a more accurate simulation result.


Is it more accurate to *always* use the extended thin wire kernel?


Alternatively, should EK *only* be used when the segment-length to wire-radius ratio is below a ratio of 8:1?

## Accepted answer (score 5, by tomnexus)

I think it's just computing speed, so it's probably safe to leave it on.  
When I first used NEC2 a few hundred segments would take all of your RAM and a minute or two per frequency. So for wide-band antennas you'd want every simplification you can get. Now the fill and solve is an insignificant amount of time.

Here I can quote from the **Supernec MOM TRM** for some more background on the approximations used.  
Read the last paragraph carefully - it seems that the EK is not used at wire junctions at any angle, or when there's a change in radius. So it's only useful on straight fat wires.

3.2. Evaluation of the fields The current on each wire segment has the form :  (65)

where  
The solution requires the evaluation of the electric field at each segment due to this current. Three approximations of the integral equation are used: a thin-wire form for most cases, an extended thin-wire form for thick wires, and a current element approximation for large interaction distances. In each case, the evaluation of the field is greatly simplified by the use of formulas for the fields of the constant and sinusoidal current components.

The accuracy of the thin-wire approximation for a wire of radius a and length  depends on  and . Studies have shown that the thin-wire approximation leads to errors of less than 1% for  greater than 8 11. Furthermore, in the numerical solution of the EFIE, the wire is divided into segments less than about in length to obtain an adequate representation of current distribution thus restricting to less than about 0.08. The extended thin-wire approximation is applicable to shorter and thicker segments, resulting in errors less than 1% for  greater than 2.

...

Despite the seemingly crude approximation, the thin-wire kernel does accurately represent the effect of wire radius for wires that are sufficiently thin. The accuracy range was studied by Poggio and Adams 9 where an extended thin-wire kernel was developed for wires that are too thick for the thin-wire approximation,

...

Special treatment of bends in wires is required when the extended thin-wire kernel is used. The problem stems from the cancellation of terms evaluated at  and  in the field when segments are part of a continuous wire. The current expansion in NEC results in a current having a continuous value and derivative along a wire without junctions. This ensures that for two adjacent segments on a straight wire, the contributions to the  component of electric field at  of the first segment exactly cancel the contributions from , representing the same point, for the second segment. For a straight wire of several segments, the only contributions to  with either the thin-wire or extended thin-wire kernel come from the two wire ends and the integral of  along the wire. For the  component of field or either component at a bend, while there is not complete cancellation, there may be partial cancellation of large end contributions.

The cancellation of end terms makes necessary a consistent treatment of the current on both sides of a bend for accurate evaluation of the field. This is easily accomplished with the thin-wire kernel since the current filament on the wire axis is physically continuous around a bend. However, the current tube assumed for the extended thin-wire kernel cannot be continuous around its complete circumference at a bend. This was found to reduce the solution accuracy when the extended thin-wire kernel was used for bent wires.

To avoid this problem in NEC, the thin-wire form of the end terms in equation (69) through (72) is always used at a bend or change in radius. The extended thin-wire kernel is used only at segment ends where two parallel segments join, or at free ends. The switch from extended thin-wire form to the thin-wire form is made from one end of a segment to the other rather than between segments where the cancellation of terms is critical.

Just a note about simulation accuracy - all modelling, but especially antenna modelling, is sensitive to how the model is constructed. NEC2 is a very fickle beast and while a beginner can get good results simulating a dipole, you can quickly get into trouble trying to model fine details or complex structures. Even just trying to model the 1 inch wide feedpoint of an 80 m dupole could give trouble - you need to know when to approximate to help NEC out. Not to discourage you from trying, but be aware of the limitations. The EK may be useful in your specific case. If you're really trying to get answers about a small detail, 80% of your effort goes into checking that the simulation is valid.

- use a model checker to find violations of rules, overlapping segments, not-quite-touching segments
- simulate over a wide frequency range and look at the graphs to see where the model breaks down - "noisy" graphs are one clue that things are unstable, but not
- try a range of segmentation strategies and check that the results are stable
- just cheat by adjusting the structure to work better in NEC. For example your results could be much more accurate if you simply make the wires much thinner than reality, near the feed point, than if you try to make them fat and then the model becomes unstable.

The SuperNEC Method of Moments Technical Reference Manual "snmomtrm" is over 20 years old. It can still be downloaded from poynting.tech with some effort - use the three dot menu to download the whole folder, extract the zip, extract the zip inside, and you'll find an HTML version of the whole manual. This stuff may all be in the NEC2 manuals too, but the snec manuals were well written in LaTeX, easier to read than the scans.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22863/nec2-when-should-the-extended-thin-wire-kernel-ek-be-used-or-avoided, by KJ7LNW, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
