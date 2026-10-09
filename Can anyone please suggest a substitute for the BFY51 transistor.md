# Can anyone please suggest a substitute for the BFY51 transistor?

*Tags: electronics · score 3*

## Question

I have to replace a faulty BFY51 Transistor. I could not find one in the market since they have been discontinued. What is a suitable replacement?

## Answer (score 3, by Phil Frost - W8II)

Searching Mouser for:

- NPN, BJT discrete transistors
- max collector-base voltage >= 60 V
- max collector current >= 1 A
- gain-bandwidth product >= 50 MHz
- TO-39 package

yields 13 results. 2N3019, the cheapest and most available result, seems like a reasonable replacement. Of course without knowing the precise details of the circuit it's impossible to say for sure if it will work.

If this is in any sort of push-pull amplifier, you should probably replace all the transistors and not just the faulty one to maintain symmetry in the circuit.

There seems to be nothing special about BFY51 besides the TO-39 package which isn't very common. Using a similar search at your favorite parts source I bet you can find some other replacements which are cheap and available in your area.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/8990/can-anyone-please-suggest-a-substitute-for-the-bfy51-transistor, by Kunu_Apple, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
