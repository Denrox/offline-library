# How to measuring ferrite core efficiency vs frequency

*Tags: measurement, ferrite, transformer · score 7*

## Question

There is an unknown ferrite toroid. I would like to figure out whether it can be used in an audio transformer, or maybe in a 1:4 transformer on given HF frequency.

The experiment I came up with is following. I can wind a 1:1 transformer using this core, connect one winding to a signal generator and the second winding to the oscilloscope with a 50 Ohm dummy load. Then I can measure Vpp vs frequency with and without the transformer and calculate power loss as 1 - (Vpp_with/Vpp_without)^2.

Is this an adequate experiment? Using this method I could also estimate pase shift and temperature stability. Is there anything else I should be mindful of?

## Accepted answer (score 8, by Josh)

To help identify a mystery ferrite core mix, the most common method is to take some measurements to determine the initial permeability (µi). Then compare your results to a table of µi for common core materials. This will put you in the ballpark and likely more than close enough to make an educated guess about the application(s) the ferrite core would be usable in.

The ferrite core's suitability for use at RF depends more on complex permeability at radio frequencies than on audio frequencies. For this reason, it is important to take your measurements using as few turns as necessary to give reliable and accurate readings. More turns relate to increased stray capacitance, which will affect the complex impedance and skew your readings.

How to measure (one method): I will be testing a known Fare-Rite 43 Toroid part number 5943003801 as an example.

Test setup using a cheap LCR meter to measure the inductance of our toroid. I have found that 10-15 tight turns will yield acceptable measurements of most ferrite toroids.

11 turns (blue wire) yielded a measurement of 120uH.

Next, we enter our measured inductance into a calculator like this one along with our toroid dimensions.

In this test, my results were the following:  As you can see, we are almost dead on for initial permeability and well within the datasheet specs for AL(nH) = 1075 ±20%. Once you know the core material type, you can then use that to reference it's usable application.

Ferrite materials can be classified as soft ferrites and hard ferrites. Soft ferrites can handle reversals in their magnetic direction without losing a great deal of energy. The notable feature of these materials is that they resist any current in the core, making them **more efficient**. Hard ferrites hold on to their magnetization very well and are very good at conducting magnetic flux, even at lower frequencies. These are quite inexpensive and not what you want in an efficient high-frequency design.

--

We can perform other simple tests such as testing what frequencies are passed or blocked in configurations like this to help determine if the unknown core will work for our application. Here are a couple of examples.

Here we are injecting a 4Vpp sine wave on one coil of 5 turns around our type 43 core and viewing that signal at both sides of the winding. Notice as we sweep from 25MHz to 1MHz the changes that take place. Most notably, we can see a phase shift as the output signal (blue) lags the input (yellow) more as we go up in frequency (less as we go down). Also, note the output's amplitude is lowest at 25HMz, highest around 8MHz, and matches the input as we approach 1MHz. These are both useful to know in determining what this chunk of ceramic might be good for.

I hope this helps and gives you a simple way to check out your box of inedible donuts! BTW you can pick up cheap LCR meters online or make your own. You might even be able to finagle an antenna analyzer to help you out here, but that is a topic for another post.

73 - NC0H

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15033/how-to-measuring-ferrite-core-efficiency-vs-frequency, by Aleksander Alekseev - R2AUK, Josh. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
