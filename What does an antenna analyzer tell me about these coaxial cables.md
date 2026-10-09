# What does an antenna analyzer tell me about these coaxial cables?

*Tags: coaxial-cable, measurement, transmission-line, testing, antenna-analyzer · score 7*

## Question

***Note: more measurements added after graphs below***

I recently acquired a RigExpert antenna analyzer and I am trying to learn how to use it to test cables. I took two cables to start with to try and understand what it shows and what the graphs mean.

1. LMR-240, 7.9m long (2 months old)
2. RG-8/U, 18.3m long (>25 years old)

I thought I would use these two cables to learn how this works. I ran the TDR (Time Domain Reflectometer) sweep on both cables, with an open circuit at the far end. The LMR-240 matches one of the book's SR (Step Response) graph samples, the RG-8/U does not match any of the samples. The book doesn't really explain much about what they mean and I haven't been able to find anything online that explains how to interpret the SR graph.

I get that reflections show up as peaks on the IR graph, is that it? Since there is an open circuit at the end of these cables, I can see the electrical length from the IR graph, about 6.5m (21 ft). The physical length is 7.9m (26 ft), so the velocity factor is 6.5/7.9 or 83% for the LMR-240.

What does the SR (Step Response) graph actually display and what does it mean?

I don't understand what it means when the SR goes negative on the RG-8 cable. The cable is inductive? I tried testing from the other end of the RG-8 cable instead and I got the exact same SR graph, so it's not that something is wrong with that end of the cable. I'm thinking the capacitance of the dielectric is low, making the cable more inductive, messing up the cable's impedance, but that's just a guess based on sample graph for an Inductive Terminated cable.

The detail data for the RG-8/U shows that the impedance is only 20.8 at 16.96m down the cable. Obviously it should be 50 ohms, but perhaps the dielectric is dried out or something like that is bad.

*** New Information ***

I measured the characteristic impedance for the RG-8 cable and it comes out to 32 ohms, off from the expected 50 ohm impedance.

I also reran the TDR scan using the AntScope2 software (PC software provided by RigExpert) and the graph is quite different. First the IR graph is the same, but the SR graph is different, instead of going negative it stays flat. A more normal graph similar to the LMR-240 cable's graph. The odd part though is that it shows the cable end at 4.2 meters instead of at 18.4 meters. For some reason AntScope2 thinks the cable is much shorter.

LMR-240:

RG-8/U:

AntScope2 graph

###

SR graph samples:

## Answer (score 7, by Alexander Antonov)

My name is Alex, I'm the head of technical support at RigExpert. This is actually an interesting question. Our engineers could not give an exact answer why the schedule in the second case behaves strangely. I can offer to perform another experiment - to measure the parameters of the RG-8/U coax cable using the analyzer and the AntScope and AntScope2 software. In all three cases (analyzer and two programs), a bit different algorithm for the operation of the TDR function is used. It will be very interesting to compare the three results obtained. Thus, you can get closer to solving the puzzle. Link: https://rigexpert.com/files/software/Antscope/

*Best regards, Alex Antonov UR4MCB*

## Answer (score 4, by Phil Frost - W8II)

I get that reflections show up as peaks on the IR graph, is that it?

Yes, that's essentially it. Note that the reflections can be negative or positive: for example if you try it with a short at the end rather than an open you should get a negative spike in the impulse response.

Falstad makes (I think) a pretty intuitive way to demonstrate the concept:

open termination

short termination

Note as these simulations are set up, you do see in the graph the initial impulse created by the signal source. In the RigExpert, that's not present: all you see is the reflection (if any).

What does the SR (Step Response) graph actually display and what does it mean?

The step response is simply the integral of the impulse response.

So in the 2nd example, we see this downward trend in the step response. That means the impulse response throughout the entire length is some negative value. It must be a small one, because the cursor says the impulse response is 0.00. Perhaps -0.003 is rounded to 0.00. Or it's a bug in the RigExpert, or an artifact introduced by stray RF pickup.

Assuming it's not a bug, this indicates that throughout the length of the coax, there is something producing a small negative impulse response. Recall that a transmission line model consists of infinitely many segments like this:

In a lossless line, R' and G' are zero. (G' is conductance, so zero conductance means a perfect insulator, or infinite resistance.) The square root of the ratio of L' to C' then determines the characteristic impedance of the transmission line.

In practice R' and G' are only very small enough to be negligible. But what if the transmission line isn't very good, or broken somehow? A conductance fault simulates what happens when the insulation is less than perfect at one spot in the transmission line:

Notice the small, negative impulse as a result. If we instead imagine not just one spot where this happens, but infinitely many such spots across the entire length of the line, we get a likely explanation for what you are seeing in the 2nd case: a small but constant negative impulse response over the length of the line.

So I would guess something (water intrusion? UV exposure? Cheap manufacturing and time?) has degraded the dielectric of your old coax such that it's no longer a good insulator. I'd wager if you measure the loss of this piece of coax you'll feel OK about throwing it in the trash.

Of note, the RigExpert manual gives an example of a lossy line, which has an increasing step response. This is what happens when the problem is significant resistance in the conductors:

Essentially the same situation, except the polarity of the impulse is reversed.

For further exploration, I've assembled Falstad simulations of other cases you might consider:

inductive termination

capacitive termination

series capacitance discontinuity

series inductance discontinuity

shunt capacitance discontinuity

shunt inductance discontinuity

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16610/what-does-an-antenna-analyzer-tell-me-about-these-coaxial-cables, by progrmr, Alexander Antonov, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
