# What is the capacitors purpose on a balun?

*Tags: balun · score 4*

## Question

Per the subject, what is the capacitors purpose on a balun?

Used a lot on wire wound ferrite toroidal baluns.

## Accepted answer (score 2, by Andrew)

Adding a capacitor to a balun like that is not standard practice and is probably a bad idea.

A bulun is supposed to be a somewhat frequency independent device which cancels out common mode current and a soon as that capacitor is added the unit becomes a tuned circuit with a limited bandwidth.

My guess is that someone added the capacitor to adjust the SWR, which might fix a matching problem but will also limit the bandwidth of whatever antenna system this is used with.

## Answer (score 12, by webmarc)

Without having the ability to measure this particular one, I expect that it's to counteract the inductive reactance introduced as a side-effect of the balun design/implementation.

Edited to add: check out [this semi-related answer](EFHW%20works%20only%20on%20one%20band%20-%20what%20am%20I%20missing.md). In constructing his balun, he used a prototype with a variable capacitor to find the value with lowest SWR for his application, which implies a matching function.

## Answer (score 3, by Tony)

The capacitor in the photo is to help the unit work better on the higher HF bands, can we leave it there as things will get rather technical.

The example in the photo is really not a Balun, I don't want to get into deep waters, but it is a simple transformer wound onto a suitable toroid material good at HF frequencies. This type of transformer is often used in End Fed Half Wave (EFHW) antenna matching units and are usually 49:1 ratio.

As you probably know the ends of a half wave antenna are at a high voltage and virtually no current, whereas at the centre of the half wave antenna you have the reverse situation high current and low voltage.

If you try and feed a half wave antenna at the end you will have an impedance in the order of several thousand Ohms. The SWR if you just fed this with coax would be enormous and your rig would certainly not be happy, even if you used the internal ATU.

EFHW matching units permit a match from say, 2500 Ohms to the 50 Ohms that you need to match the coax and of course the input impedance of virtually every modern HF transceiver.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17240/what-is-the-capacitors-purpose-on-a-balun, by t252, Andrew, webmarc, Tony. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
