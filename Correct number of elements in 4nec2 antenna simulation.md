# Correct number of elements in 4nec2 antenna simulation

*Tags: antenna, antenna-theory, dipole, antenna-modeling · score 6*

## Question

I am designing a 1.25-wavelength dipole antenna with the 4nec2 software. What I noticed is that the input impedance of antenna is changing greatly when I change the number of segments.

How many segments should I choose?

## Answer (score 3, by tomnexus)

Generally in NEC2, 10 segments per wavelength is good, so 12 or 13 segments depending on where you want your feed.

But you are doing better than just following the rule, investigating the effect of the number of segments!

I'd suggest trying 4, 6, 8, 10, 15, 20, 30 segments per wavelength and comparing the results. The impedance should be pretty constant from 10 to 30. If not,

Watch out for all the other rules too. Segment length to diameter - they must not be too fat; Length to length ratios - joining long and short segments; radius step changes, joining at too narrow an angle so they overlap too much; small loops are difficult in NEC, etc etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5367/correct-number-of-elements-in-4nec2-antenna-simulation, by Shiva Mudide, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
