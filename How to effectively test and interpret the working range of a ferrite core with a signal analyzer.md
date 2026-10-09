# How to effectively test and interpret the "working range" of a ferrite core with a signal analyzer?

*Tags: filter, ferrite · score 9*

## Question

I have a couple of ferrite beads that are advertised as effective for suppressing conductive noise around 150kHz. I'm trying to monitor their actual performance with noise filtering.

In my set up I have a ferrite core which I made a number of turns on. I connected the signal from my signal generator and one channel of the oscilloscope to one end of the wire to monitor the input.

On the other end of the winding, another channel of the oscilloscope is connected to monitor the output.

I then conducted a signal sweep from 1kHz to 1MHz and monitored the input and output as shown; input is red, output is blue.

It is noticeable that there is a signal increase at approximately 40kHz before peak at 105Khz and a decrease.

How can I interpret this result (making sense of it with regards to it's actual performance with regards to suppressing noise at 150kHz)?

Is it possible for me to make even more turns to "shift" the graph to the left so that a lower output can happen at even lower frequencies? Is there any impact in the performance if too many turns are used?

## Accepted answer (score 6, by glen_geek)

It appears that all three 'scope probes are set to their "X1" position.  
As such, each probe includes the oscilloscope's internal 1M input resistance in parallel with about 20pF input capacitance. But more importantly, the capacitance of the probe's cable is in parallel too. The total 'scope parallel capacitance is roughly 100pf.  
Since there are *two* probes on the function generator's output, the generator is loaded with about 200pf in parallel with 1M resistance. Both are mostly insignificant compared with a function generator's 50 ohm output resistance, especially below 1MHz.  
The 100pf capacitance from the probe at test-inductor output **is significant**. It resonates with inductance - frequency gives a rough clue of the test-inductor inductance. Since resonance is at roughly 100kHz, inductance would be near 25mH.  
The Q of the resonant peak also gives a clue of resonant losses in the inductor at 100 kHz., shown as R5 (45k) in the circuit below:  
  
The plot below shows V(n001) at the "'scope input". Function generator output resistance is guessed at R3=50 ohms:  
Some function generators have output resistance of 600 ohms. This resistance actually gives a better match to OP's graph:  
Be aware that setting probe to **X10** attenuator setting will dramatically reduce probe input capacitance from about 100pf down to about 11pf. And input resistance changes to 10MEGohm from 1MEGohm.  
A scan to higher frequency might reveal the inductor's **self-resonant-frequency**, which could be used to estimate the value of a capacitor in parallel with R5. It would cause an anti-resonant dip in the plot. This frequency might allow you to estimate the upper limit of the inductor's usefulness as a choke.  
In the OP plot that omits frequency above 1MHz., the self-resonant frequency would either be greater than 1MHz., or else the inductor is so lossy, that it is not visible.

## Answer (score 3, by Jeffrey Phillips Freeman)

So the problem here is that your setup is not sufficient to tell you what you want to know about the ferrite core.

In my set up I have a ferrite core where I made a number of turns on. I connected the signal from my signal generator and one channel of the oscilloscope to one end of the wire to monitor the input.

So in this setup your first probe is basically just sampling the input signal, and your second probe is wired to ground. If this were an ideal circuit where the wires connected to the inductor had no parasitics (namely inductance or capacitance) then all you would see would be two flat graphs with no variation at all.

The reason your seeing variation in the graph is because there is a length of wire between the output of your inductor of some length before connecting to your ground. As such this length of wire has some small amount of parasitics but is also being inductively coupled with your inductor and thus is inducing some voltage swing as seen in the graph. Effectively the red wire your output probe is connected to is creating a transformer with the coil you are testing. This is why you notice a larger impact on the blue line than the red, because the red wire is very short and connected very close to the signal source.

The peak your seeing in the blue line around 0.1MHz also has little to do with the ferrite core's maximum frequency. It is most likely the coils self resonance. You have to understand a coil has parasitic capacitance sitting between each loop of the coil. This essentially causes it to have a relatively large inductance but also a smaller parasitic capacitance. This will cause any coil to self-resonate at a given frequency as you see here. Even if you had an air-core with no upper frequency limit you'd see a similar self-resonance (though at a different frequency). You could test this theory by spreading your coil out. Take the coil you wound there and keep the same number of windings but instead of having it all bunched up to one side of the core try to evenly space it across the core. This will significantly lower the parasitic capacitance and the peak you see should be much less noticable if not go away completely.

So long story short, I'm sorry to say, none of what you have here is really going to help you.

How can I interpret this result (making sense of it with regards to it's actual performance with regards to suppressing noise at 150kHz?

Well you cant, the results are bogus. but lets try to address how you can determine if its good at suppressing noise at 150kHz.. but the answer is, it depends. As a general rule if you start pushing a core past its frequency limit they become lossy. That is your inductor's impedance will shift to have a **real** resistance and the reactance may also be affected. this may or may not be a problem depending on the details.

If all you want to do is reject any signals below 150kHz or any signals above 150kHz and let the others pass, then I would not use an inductor at all. for that you can use a single capacitor in a low-pass or high-pass configuration, capacitors can be a bit less problematic than inductors so its usually what I'd recommend.

For a high-pass filter that only rejects signals below 150kHz then put a 10nF capacitor in series with the signal and a 100 ohm resistor after the capacitor attached to ground. For a low-pass filter that only rejects signals above 150kHz use the same components but swap the resistor and the capacitors position.

The only way you'd have to use a inductor here is if you want a band-pass filter. that means if you want to reject frequencies above **and** below 150kHz and only let frequencies at or near 150kHz pass. For that you would put a 10nF capacitor in series with the signal, and then a 112uH inductor in series with that.

The nice thing is that the inductor's value is low enough that you have no need to use a ferrite core at all, which is really only needed when you need a large value inductor. For a 112uH inductor you can wind an air-core inductor which has effectively no frequency limitations and is much easier to work with than one with a core. for that take some really thin wire and rap it around a 0.5" diameter tube with 200 turns, and make sure the overall length is evenly spaced about 2 inches. Or you can use this online calculator to try to get dimensions that suit you. You can use some clue to ensure the inductor keeps its shape.

If you really do want to try to calculate the upper frequency limit on a ferrite core inductor, though, you'd have to measure the voltage across it and the current through it. You could then look at the phase difference between this two values as well as the amplitude and use that to calculate the complex impedance at a given frequency. Ideally it should have very low real component and most of its impedance would be the imaginary component. This would show as a 90 degree, or very close to 90 degree phase shift between the two graphs when it is operating at an optimal frequency and the phase shift would decrease as the inductor is pushed passed its maximum frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17235/how-to-effectively-test-and-interpret-the-working-range-of-a-ferrite-core-with, by GHGC, glen_geek, Jeffrey Phillips Freeman. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
