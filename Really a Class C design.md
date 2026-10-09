# Really a Class C design?

*Tags: amplifier, qrp · score 4*

## Question

In the March 2000 QST there was an article on the Tuna Tin QRP transmitter, which I thought I might build:

The text describes Q2 as a C Class amplifier, but I just can't see how that can be true.

*"It's ouput (of Q1) tickles the base of Q2 (lightly) with a few mW of drive power, causing Q2 to develop approximately 450 mW of dc input power as it is driven into the Class C mode."*

The base biasing on Q2 maintains a quiescent base voltage of 1.4 V, which is plenty to bias Q2 on. I simulated the circuit in LTSpice and then disconnected the oscillator portion and sure enough there was a steady 8.9 mA of collector current. So I conclude that Q2 is in fact in Class A mode.

So, either the article has been wrong for many years (seems unlikely), or there is something here I have misunderstood (more likely :-) ).

So, my question is: Is Q2 operating in Class A or Class C?

## Accepted answer (score 6, by glen_geek)

So, my question is: Is Q2 operating in Class A or Class C?

This is an OOK transmitter (on-off keying) where *both oscillator and final amplifier* are keyed. Keying only the final amplifier (with oscillator running continuously) would likely result in harsh keying, spreading key-clicks over a too-wide bandwidth.  
This rising-amplitude oscillator, driving a biased power amplifier *starts out* Class A at the beginning of key-down. RF power output is tiny. With amplitude still rising, the power amplifier soon bottoms out (as @hobbs mentions). This means that for a portion of the RF cycle, current through Q2's collector is zero. Upon reaching full amplitude, Q2 is likely **OFF** more than it is **ON** - class C.  
Hopefully, when key is dis-engaged, oscillations die out slowly too, so that key-up doesn't "click" as well.  
Keep in mind that this is a very low-power transmitter. This bias arrangement where power amplifier conducts some small DC current (albeit a fraction of RF peak current) is not appropriate for higher power...a high-power RF amplifier often has its base DC grounded through a choke or step-down transformer winding. Such an amplifier rests with no DC current at all during key-up. Other methods are used to mitigate key-clicks.

Here's my LTspice simulated circuit, that excludes the RF output matching/filter circuit...it affects the key-down transient to a small extent.  
Notice that the oscillator's build-up (Q2 in this schematic) is the more important part of a slow click-free rise of amplitude on key-down.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21076/really-a-class-c-design, by Ian_B, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
