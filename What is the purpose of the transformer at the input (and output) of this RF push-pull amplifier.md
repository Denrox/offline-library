# What is the purpose of the transformer at the input (and output) of this RF push-pull amplifier

*Tags: amplifier · score 9*

## Question

Firstly, feel free to move this to Electronics SE if it's not on-topic, but it's strongly related to ham radio and RF circuitry.

Reading Hayward's classic "*Solid State Design for the Radio Amateur*" and looking for inspiration, I came across the following push-pull PA design that I didn't quite understand (Chapter 4, Pg 62).

I don't have a problem with T1 and T2, **it's T3 and T4 I'm struggling with**. T1 is a straightforward 4:1 impedance transformer; it doubles the current at the output and so "looking back into" T1 the source appears to have 4 times less impedance. No problems there. T2 has the dotted secondary tied to ground and so the current flowing into the dot (transformer action) leaves the other end of the secondary negative. Now we have anti-phase signals of equal amplitude at the transistor bases, turning each transistor on and off alternately. Again no problems there, it's straightforward push-pull action.

But here's where the wheels fall off for me! **What's the purpose of T3 (and T4 which I believe has a similar purpose)?** Here's what the author says: "*The third core [in the input section of the amplifier] ensures that the load presented to T2 is balanced. Each transistor sees a driving impedance of 6.25 ohms*". I've included a hand-sketched re-arrangment of the circuit to help me understand and I can sort of see how the current produced by the full potential of the balanced signal (anti-phase peak-to-peak) is driven through one or other transistor bases. Does this account for the halving of impedance "seen" by each transistor as the author says? **But then, wouldn't this happen anyway, without T3??**

## Accepted answer (score 6, by Phil Frost - W8II)

T4 is just this idea:

Sometimes it's done this way:

The primary of XFMR1 is equivalent to T4 from the question.

Since T4 provides the collector load for the transistors, it's a factor in voltage gain. For a differential-mode input, the collector currents correspond to magnetic flux in the same direction in T4, thus T4 presents a high impedance and voltage gain is maximized. For undesirable common-mode input (which could come from dissimilar gain in the transistors), magnetic flux cancels and T4 looks like a short to Vcc, minimizing voltage gain.

You're right T3 isn't ideally necessary, but it serves to keep things balanced despite variation in components. Consider a simplified case where the load is just a pair of 10 ohm resistors that might vary by +/- 10%:

T2 (ideally) requires that the current is equal in each of the windings, but since the resistors are not equal, the voltages across the resistors are not equal. The addition of T3 remedies the situation: in the common mode it appears as a short to ground. Thus, at the right side of T2 there will always be equal but opposite currents *and* voltages. Or as the author puts it, T3 "ensures that the load presented to T2 is balanced".

## Answer (score 3, by Brian K1LI)

T4 is the collector DC feed transformer. The inductance of each side of the transformer acts as an RF choke at the amplifier's operating frequency. The antiphase connection of the windings prevents DC saturation of the core material.

By coupling the currents in the bases of Q1 and Q2, T3 is a lossless means to compensate for the wide variation in transistor parameters that are to be expected. This reduces distortion and improves stability.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11872/what-is-the-purpose-of-the-transformer-at-the-input-and-output-of-this-rf-push, by Buck8pe, Phil Frost - W8II, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
