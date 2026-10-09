# Stacked shell inductor — what's its function/use?

*Tags: electronics, power-supply · score 5*

## Question

I have a device of copper and iron (about 8 kg) which looks like two shell inductors joined so that there is some coupling but high leakage. The windings seem to be identical. Each is a single continuous winding with 4 intermediate taps. I did not see this in use, but when I got it the two windings were linked at one end. The equipment it came from was powered, I think, from normal 240 VAC mains.

It's just my curiosity, but I can't fathom what it might do. Since the windings were linked, it does not provide isolation. If it is a transformer or common mode choke, why so little coupling? If it is two independent auto transformers or chokes, isn't the coupling a problem?

Anyone seen one at work anywhere?

## Answer (score 4, by Vince Mulhollon)

This is likely a **ferroresonant transformer**.

- http://www.electroncoil.com/ferroresonant_transformers.php
- http://www.hammondmfg.com/CVR.htm
- http://www.oltronix.nl/en/ferroresonant-principle

If you wanted a surge protector, a motor-generator would work pretty well. Is there a way to get rid of the moving parts of a MG? Yes.

Most transformers are fairly linear, until you reach a magnetic flux that saturates or they overheat. If you resonated a winding on a transformer and intentionally made it magnetically saturate just at normal voltage output, then if a power surge hit it would try to output a higher voltage but its in saturation so nope; worst case is the output gets some square wave harmonics and of course the transformer would heat up a little.

This transformer is fairly useless without the specs and wiring diagram and the capacitor that resonates the winding. It's easy to repurpose a regular transformer but CVTs are black magic even with the docs so you've basically got a piece of scrap metal.

Usually one winding is a little larger than the other; yours are almost identical. Odd. Other than that, looks like a google image search for “ferroresonant transformer”.

There's one under my desk right now. They're only about 90% efficient, plenty of heat. Also they're heavy. And they always hummmmm. Thats why you don't see many.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2357/stacked-shell-inductor-what-s-its-function-use, by Merlin3189, Vince Mulhollon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
