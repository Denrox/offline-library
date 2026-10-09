# What safety procedures should be followed when developing and testing a high power amp?

*Tags: rfi, rf-power, amplifier, testing, safety · score 3*

## Question

I'm designing a 300W power amplifier using the MRF300AN from NXP targeting a center frequency of 146 MHz.

Obviously I need to keep my fingers out of it and test into a dummy load, but generally speaking when testing an amp design, how do you do it safely to prevent:

- RF burn
- Excess radiation
- Spurious emissions
- Other considerations?

## Accepted answer (score 5, by Ben Madison KO4UXC)

1. Get yourself a dummy load.
2. If your gut is telling you your doing something stupid you're doing something stupid.
3. Keep the power supply switch near by.
4. Always assume it's live.
5. If you have doubts about a mod or an idea don't do it unless someone more experienced helps you with it or gives you advice.
6. Assume your capacitors are still charged, check them every once in awhile.
7. Ground your bench properly.
8. Take your tests in increments. Adjust slowly up but quickly down.
9. Treat the project like your spouse or friends and it won't hurt you back.
10. Handle any tubes with care and keep your hands clean free of oils when touching them.
11. Turn off the project when you leave it for long periods of time.
12. Have a list of emergency back up numbers incase you didn't listen to your gut.
13. If it has fuses take them out when working on your project.
14. Unplug what you are working on before you reach for wires.
15. Don't use tools that have metal handles.
16. Use your brain.
17. Get some fresh air after some soldering work.
18. Keep yourself focused on what you are doing,
19. If your project is smoking, unplug the power supply.

## Answer (score 4, by hotpaw2)

If you do have to stick a scope probe or adjustment tool into it, take off all your rings, watches, bracelets, necklaces, etc., before reaching into anything (or around any uncovered circuitry) that might be powered with a high current power supply or high amperage battery.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20362/what-safety-procedures-should-be-followed-when-developing-and-testing-a-high-p, by KJ7LNW, Ben Madison KO4UXC, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
