# Do I need a precision wattmeter or will a $50 one suffice?

*Tags: antenna-system, measurement, equipment · score 5*

## Question

My transceiver has a built-in wattmeter but I've decided to buy an outboard one to monitor the antenna system before it reaches the ATU. I'm capable of putting out 100 Watts and I see that several manufacturers offer meters in the $50 range that look to be adequate for my purpose.

On the other hand, I see that there are a lot of hams who have opted to spend around 500 - 750 bucks for a portable, lab-grade wattmeter. Is it really that critical to get another 3% - 5% accuracy to be worth the additional cost? Obviously, there are many who believe so. What am I missing to see here? Would I be wasting my money to buy a cheap meter?

## Accepted answer (score 2, by Andrew)

Dax.

One problem with measuring RF power in an antenna system is that there are a number factors which can cause erroneous readings, these being distinct and separate from the basic accuracy of the meter.

Factors which can mess up a watt meter reading are SWR, impedance mismatches, and unwanted single ended currents caused by an unbalanced system.

There are different types of watt meters available which use different types of internal circuits to provide a measurement. Each type has it's own level of inherent protection against system problems.

Watt meter types include those that use a diode detector, a bridge circuit, directional coupler, thermocouples, and others.

For a perfectly matched antenna system most watt meters will give a reasonably accurate reading. Where an antenna system has an impedance mis-match is when lower quality meters will give a more inaccurate reading.

As an example, for an antenna with a bad SWR fed with coax, the reading shown on a cheap watt meter will change depending on where along the line the meter is fitted. This is because the meter power reading is affected by the line impedance, which changes along the length of the line for a system which isn't perfectly matched. A better quality meter will be less affected by line impedance.

Generally speaking, the more expensive a meter is, the less the reading will be affected by system problems such as impedance mismatch.

Then in addition, there is the basic accuracy of the meter which can be considered, which depends largely on the value tolerance and temperature coefficeint of the internal components.

If you just want a general relative reading that is say plus and minus 10 %, the internal meter in your radio is probably good enough, or you can get away with a cheap external watt meter.

More expensive meters will probably be less affected by impdance mismatches.

If you need to get readings which are absolute in accuracy, then more expensive lab instruments would be better.

In general it seems that older style ham radio watt meters from 1950 - 1970 are better than newer models.

Hope that helps !

## Answer (score 3, by Wireless Learning)

**Clearly, the answer is up to you.**

When you measures something, you want an answer. What answer do you want from this new piece of equipment ?

Is your answer very tightly constrained ?

For example you might need such precision for embedded battery powered small devices. Where you can't just have a 10Kg Lead-Acid Battery with tremendous margin in regard of your power consumption.

So ask yourself what do you want to do? What project are you planning to do, and when could you use those .1% or whatsoever precision ?

You are speaking of power devices in your question. If you design such devices and want them to be reliable you will have to use margins in your design. So I don't see the point in measuring a 10Amp current down to the milliAmp, where anyway you would have put a 20Amp component to handle the current and be more reliable.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21148/do-i-need-a-precision-wattmeter-or-will-a-50-one-suffice, by Dax, Andrew, Wireless Learning. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
