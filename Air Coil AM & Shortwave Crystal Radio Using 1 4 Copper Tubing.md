# Air Coil AM & Shortwave Crystal Radio Using 1/4" Copper Tubing

*Tags: diy, crystal-radio · score 3*

## Question

Looking to build a crystal radio, need help with the coil. I'm looking to get something to work with 1/4" thin wall copper tubing. Already have some nice diodes and whatever capacitors/resistors I need. I don't care if it is AM or shortwave, I can make more more than one. For shortwave I'll soon be building this

Here is the AM radio I built, and it does really well, I have two stations nearby (within a mile or two) in the mid and high AM band. It uses taps instead of a slider.

So that's about my comfort zone right now, I plan on going all the way though, so post them if you got them.

I already read about how to make the forms for an air coil and reinforcement if needed, so no problem there. I figure I can solder taps onto the coil as needed. **The big problem is my intended size is way outside the norms, so is this possible?**

## Answer (score 3, by Glenn W9IQ)

Congratulations on a nice home-brew project! I started my journey into amateur radio with a crystal set such as yours.

Making the inductor (coil) out of copper tubing is overkill from an electrical standpoint since very little current is involved. But you certainly gain significant mechanical strength and perhaps more importantly, aesthetic appeal from using copper tubing.

It may be best to give you some of the simple math behind your crystal radio design in order to help you with your inductor construction. The inductor and the capacitor form a tuned circuit. Your circuit uses a parallel resonant construction which allows the desired signal to continue to the diode detector and the earphone while all other signals are effectively shorted out. The frequency in Hertz that the parallel resonant circuit allows to pass is given by:

$$f=\frac{1}{2\pi \sqrt{LC}} \tag 1$$

where L is the value of the inductor in henries and C is the value of the capacitor in farads.

Typically we deal with values of capacitors and inductors that are much smaller than a farad or henry. In the case of your first schematic, for example, the capacitor value is shown in picofarads or 10 farads.

For the specifics of winding your inductor, it is best to rearrange formula 1 to find the value of L for a given capacitor value and a given target frequency:

$$L=\left( \frac{1}{(2\pi f)} \right )^2 C^{-1} \tag 2$$

So for your shortwave example, if your capacitor is set to 500 pF (500 x 10 farads) and you wish to receive a frequency of 5 MHz (5 x 10 hertz), then L would be ~2 microhenries (2 x 10 henries).

You can then use any number of on-line calculators to get the winding dimensions for your inductor. You need to pick a calculator that allows you to specify the gap between turns (or winding pitch) such as this one. According to this calculator, a coil 75 mm in diameter comprised of 7 turns of 6.35 mm wire (0.25 inch copper tubing) with a 12.7 mm pitch (a gap of 0.25 inches between windings) would fit the bill.

The tap for the antenna on the coil can be determined experimentally. Simply adjust for maximum signal strength.

With regard to receiving short wave stations using a crystal radio, unfortunately many governments are closing their shortwave broadcast facilities. Crystal radio sets are not particularly sensitive so unless you live in close proximity to operating shortwave broadcast stations, you may not be able to tune in many stations.

Have fun with the project!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12416/air-coil-am-shortwave-crystal-radio-using-1-4-copper-tubing, by user13773, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
