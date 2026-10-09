# Identify filter on schematic

*Tags: baofeng, filter · score 3*

## Question

I am analyzing the Baofeng UV5R schematic.

And trying to identify which filter was used in input UHF/VHF RF stage on RDA1846.

It seems to me that it is a 3rd order Butterworth bandpass filter. But i am not sure about topology of the filter.

Can someone help in identifying the type or confirm the type of filter used here. Assistance would be appreciated.

## Answer (score 2, by Marcus Müller)

I don't think this has any particular name. Names aren't overly useful, anyways for this!

The reason I say that is because capacitors like 3 pF are really *tiny* in value; in fact, smaller than the capacitances in transistors, smaller than the parasitic capacitance in inductors, and in the same order of magnitude as pretty short stubs of circuit board. That leads me to believe that they have been added – assuming the circuit is correct¹ – to compensate for some parasitic effect that you can't see from the components alone, but that might well depend on the actual board layout and material, precise component choice and other factors. The values would have been chosen by trail and error (or experience).

So, don't expect any "pure" textbook architecture anywhere here.

Anyway, what would knowing the name help? To get the approximate behavior, you'd put the values in a circuit simulator, anyways. To design a filter, you wouldn't copy an existing design, but go from textbook to design, and optimize / fine-tune (as was done here).

¹ I have friends that deal with bass guitar amplifiers. They tell me that it's pretty common for service manuals to contain extraneous components to confuse at least the totally competence-free class of bootleggers. So, I'm not taking it for granted that this schematic is actually correct!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22509/identify-filter-on-schematic, by Adi Deljanin, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
