# HF 49:1 toroid unun same ratio more windings

*Tags: balun, toroid, ferrite-transformer · score 3*

## Question

I've been looking for an answer, but no luck so far finding it. It's about windings, and it's effect on HF. 49:1 UNUN transformer. What will happen if we keep the ratio 49:1 and increase the number of windings. Let us say 3 primary and 21 total. What will increasing number of winding do and what effects are expected?

## Answer (score 2, by Ryuji AB1WX)

This is a deceptively tricky question because, to fully appreciate the answer, you need to step beyond the warm, fuzzy world of textbook diagrams and into the cold, chaotic reality of RF transformers. You see, transformers at **radio frequencies** don’t behave the way their **AC power** or **audio-frequency** cousins do. Those are simple creatures—predictable, well-mannered, and generally willing to follow the rules. RF transformers, on the other hand, are like highly caffeinated squirrels—restless, unpredictable, and prone to doing things you wouldn’t expect.

At **lower frequencies**, say **2 to 4 MHz** (or about the **80-meter band**), conventional transformers more or less behave. They step up, step down, and don’t cause too much trouble. So, if you change the number of turns in a **49:1 transformer** while ensuring there's enough **magnetizing inductance**, it should still function *mostly* as expected. But then things get interesting.

As you start cranking up the frequency, **leakage flux** enters the chat. This phenomenon starts sneaking in around **60 meters** and escalates quickly, becoming a full-blown problem at **higher bands**. Here’s what’s happening: not all of the flux generated in the primary actually intersects with the secondary winding. Some of it **escapes**, refusing to participate in the neat, cooperative world of ideal transformer operation. When this happens, it’s as if part of the primary winding is **floating outside the transformer system**, not contributing to energy transfer. The same thing occurs on the secondary side—some windings are left **half-connected** to the system, functionally detached from the core transformer operation.

Now, here’s where it gets frustrating: even if you’re dealing with a **pure resistive load**, the transformer will still show **inductive impedance**. Why? Because some of the flux that *should* be linking the windings simply isn’t. It’s like planning a team project where half the group doesn’t show up, leaving the rest to do all the work. This leads to **extra inductance sneaking into both the primary and secondary windings**, distorting the expected impedance transformation.

And it gets worse! If you keep the turns ratio the same but increase the **absolute number of turns**, leakage flux goes up even more, along with **parasitic capacitance** between windings. This doesn’t just make things slightly inconvenient—it actively **ruins** your high-frequency performance. Sure, your **low-frequency** range might extend a bit, but at the **upper end**, your transformer is now about as effective as a paperweight.

So, what can you do? One common hack is to **shunt a capacitor** across the windings to tame the leakage inductance, forming a **harmless L-network** that doesn’t actually match anything to anything—it just exists to neutralize the leakage inductance and stop it from causing harm. This helps, but only up to a point. If you want **lower loss** and **wider bandwidth**, the best solution is to **ditch conventional transformers entirely** somewhere around **5 MHz to 7 MHz** and move to **tuned transformers** or, better yet, **transmission line transformers**.

A **properly tuned transformer**, where the primary, secondary, or both are resonated with capacitors, can significantly cut down on leakage flux. The catch? You end up with a **narrowband** device—great efficiency, terrible flexibility. If you want **both low loss and wide bandwidth**, you have exactly **one** good option: **transmission line transformers**. These are like the Swiss Army knives of the transformer world—reliable, efficient, and functional across a **wide frequency range**. The trade-off? You don’t get to pick your **impedance ratios** as precisely as you would with **conventional transformers**.

This is why so many **terrible transformers** exist in amateur radio—people try to force **conventional transformers** into **high-frequency applications** where they simply don’t belong. The **49:1 transformer** is a classic case of this. Achieving a **49:1 impedance transformation** with a **single transmission line transformer** is impossible, but people keep using it because they need that ratio for their beloved **half-wave end-fed antennas**. And to be fair, half-wave end-feds are **ridiculously convenient**, especially for portable ops. So, **the 49:1 isn’t going anywhere** anytime soon, no matter how many times we discuss its limitations.

But here’s the thing: if I were building a **half-wave end-fed**, I *wouldn’t* use a **49:1 transformer**. Instead, I’d go for a **9:1 Ruthroff transmission line transformer** paired with an **L-network**—a combination that’s **widely used in automatic antenna tuners** for a reason. This setup is simply **better**.

And if you want to know my *real* opinion? I’d **skip half-wave lengths altogether** and opt for something like a **3/8-wavelength vertical** with **elevated radials** instead of dealing with the weird compromises of sloping or horizontal configurations. But hey, that’s a discussion for another day.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23394/hf-49-1-toroid-unun-same-ratio-more-windings, by lunar75, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
