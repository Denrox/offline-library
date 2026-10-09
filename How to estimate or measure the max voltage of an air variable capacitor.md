# How to estimate or measure the max voltage of an air variable capacitor

*Tags: capacitance, magnetic-loop · score 3*

## Question

I have a big box of air-variable capacitors I inherited and want to see if I can use one of them for a low power magnetic-loop antenna for 30m digital.

- How can I figure out if any of them have a high enough maximum voltage?
- If I do this by trial and error I risk damaging my radio right?

## Accepted answer (score 3, by K7PEH)

From the ARRL Handbook...

```
Spacing
inches ___ V_peak

```

1. 0.015 ___ 1000
2. 0.02 ____ 1200
3. 0.03 ____ 1500
4. 0.05 ____ 2000
5. 0.07 ____ 3000
6. 0.08 ____ 3500
7. 0.125 ___ 4500
8. 0.175 ___ 7000
9. 0.25 ____ 9000
10. 0.35 ___ 11000
11. 0.5 ____ 13000

Also note that these are mere recommendations. Actual high voltage you will see of course depends on the reactance and input power to the antenna (a little circuit analysis may be in place) along with frequency needed to determine the reactance of the capacitor.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6293/how-to-estimate-or-measure-the-max-voltage-of-an-air-variable-capacitor, by Arthur, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
