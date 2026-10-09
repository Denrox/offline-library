# "Coaxial capacitors in line” in E4E04?

*Tags: united-states, license, rfi, filter · score 6*

## Question

I've been studying the U.S. license examination question pools. For the most part, it is reasonably obvious what the questions and answers mean even when I am not yet able to come up with the answers on my own. However, the correct answer to this question in the Extra class pool is confusing me:

E4E04 (D)  
How can conducted and radiated noise caused by an automobile alternator be suppressed?

A. By installing filter capacitors in series with the DC power lead and by installing a blocking capacitor in the field lead  
B. By installing a noise suppression resistor and a blocking capacitor in both leads  
C. By installing a high-pass filter in series with the radio's power lead and a low-pass filter in parallel with the field lead  
**D. By connecting the radio's power leads directly to the battery and by installing coaxial capacitors in line with the alternator leads**

What is the purpose of specifying “coaxial” capacitors? Why does it say “in line”, which in the absence of further information I would interpret as “in series”? I would think that low-pass rather than high-pass filtering would be desirable.

Is this just a sloppily phrased answer, or is there something subtle here?

## Accepted answer (score 4, by Phil Frost - W8II)

What they mean by "coaxial capacitor" might be described by more people as a feed-through capacitor. For an example, see Tusonix 4300-002LF at Mouser. The datasheet contains these images, which are pretty informative:

Thus, the two leads are effectively a wire, ideally having zero impedance between them. However, this conductor also has some capacitance to the case, which is usually connected to ground. This particular part is designed to be dropped in a hole the size of the case, then soldered in place. Another design has a tab on the case for screw mounting.

The advantage of this arrangement is that it's possible to use as a filter on some wire with high $\mathrm{d}v/\mathrm{d}t$ without creating a stub which could also act as an EMI radiator. It's also possible to preserve the continuity of a shield or enclosure, and get a really good connection to it. With an ordinary capacitor, the ground connection would go through a lead, which would have more inductance and resistance, reducing the filter effectiveness.

There's a similar looking, but different thing: *axial*-leaded capacitors. These are frequently electrolytic. Example:

There's nothing special about this capacitor. Sometimes this arrangement of leads just fits better.

## Answer (score 3, by Kevin Reid AG6YO)

While writing the question I found a picture that clarifies the “in line” part on this web page I found in a search, Radio Frequency Interference: A small vessel guide:

To cure alternator noise, which is pulses radiate from the output lead, it is necessary to filter the output lead as close as possible to the alternator. The most effective filter is a 0.5 microfarad coaxial capacitor. A coaxial capacitor is one which passes current through its center with the capacitor completely surrounding the current carrying lead. As the alternator current flows through the capacitor, it should be rated to handle the alternator’s maximum output current.

...

So, a coaxial capacitor in this context is in fact a three-terminal device of a sort, and this explains why it could be described as being “in line” with the alternator leads.

This doesn't explain why a coaxial capacitor is specifically good for this application, though.

## Answer (score 2, by WPrecht)

Coaxial (also known as cylindrical) capacitors are usually electrolytic type capacitors and are sometimes know as feed-through capacitors when used in automotive applications like is illustrated in the exam question. Feed-through capacitors are designed to withstand very high currents as you'd see across an alternator. The third lead is also to ground reducing the effective series inductance to nearly zero.

As to the structure of the component, I imagine placing the leads on opposite sides of the capacitor simplifies construction and reduces the chance of the leads arcing over considering even a modest alternator these days produces 90+ amps.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1178/coaxial-capacitors-in-line-in-e4e04, by Kevin Reid AG6YO, Phil Frost - W8II, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
