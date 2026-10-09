# What is the point of a SWR/power meter where the needles cross over each other?

*Tags: impedance, rf-power, equipment, measurement, swr-meter · score 8*

## Question

There are SWR/power meters with two separate gauges, and others that have them mounted so the gauge needles cross over each other.

Aside from looking cool, does the cross-over point of the two meters provide specific or useful information?

## Accepted answer (score 10, by W5VO)

A cross-meter is capable of showing you three measurements simultaneously:

- Output Power
- Reflected Power
- SWR

From this image by Axel Schwenke on Wikipedia, you can see that the needle on the left indicates forward power, and the needle on the right indicates reflected power. The observed intersection of the two needles can be used to indicate the SWR of the system. The lines in the middle of the meter indicate what the SWR is for a given forward and reflected power reading.

## Answer (score 7, by user)

A properly calibrated cross-needle power meter such as e.g. the MFJ-842 actually tells you something more than just the forward and reflected power, which as you point out can just as easily be indicated by two separate instruments.

**The intersection of the needles gives you a pretty good indication of the actual standing wave ratio or SWR** because the SWR is directly related to the relationship between the forward and reflected power.

So, there's more utility to this than simply "saving space" or "looking cool". Of course, you could have a *third* meter showing the resultant SWR based on forward and reflected power indicated on two separate instruments, but why bother when you can put all the information into one and at the same time reduce the risk of measurement inconsistencies?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/953/what-is-the-point-of-a-swr-power-meter-where-the-needles-cross-over-each-other, by Adam Davis, W5VO, user. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
