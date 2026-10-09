# Battery sizing for power draw

*Tags: mobile, battery · score 7*

## Question

Note that this question isn't about battery capacity, at least not per se. I have a 100 Watt mobile transceiver. At 12 V and assuming 50% efficiency, that means it draws a little under 20 Amps at full power. It's currently being powered by a pair of 15Ah SLA batteries in parallel.

I'm not concerned about battery life - I know I won't get much which is why there's a solar system keeping the batteries topped off while I'm in the field. But even with high gauge wire, when I key down the transmitter, I get a voltage drop at the battery terminals.

Do I need a bigger battery? How can I determine what size battery I need for a certain load? Amps, Amp-Hours, and Cold Cranking Amps - which is the important factor here?

## Answer (score 6, by Quentin Smith)

Batteries can be approximated as an ideal voltage source in series with a resistor. So it's perfectly normal for a battery's terminal voltage to drop when the current it is delivering increases. To determine whether that's actually a problem, you only need to consider two things:

1. Is the new voltage too low to power your transceiver?
2. Are you exceeding the current rating of the battery?

Most battery spec sheets will list the maximum current draw from the battery. For a 15 Ah lead acid battery, that's going to be at least 10 A, so you should be fine with two in parallel. Yuasa, a lead acid battery manufacturer, has an application manual that shows discharge curves for different currents (page 7). They only list discharge curves up to 3C (meaning, discharging the battery in 1/3 of an hour, or at 45 A per battery in your case), so that's probably what they feel comfortable with for their batteries. You should check your own battery's specifications to confirm.

## Answer (score 5, by Adam Davis)

#### Voltage drop is caused by internal resistance

Using batteries you will always experience a voltage drop when drawing significant currents, due to the internal resistance of the battery. This can be thought of as a resistor that is always in series with the battery, and consumes energy depending on the current drawn from the battery.

It’s the main reason batteries appear to have lower capacity for high current draws, and higher capacity for low current draws. It also accounts for battery heating, and is one of the ways a battery may damage itself.

### Internal resistance depends on the battery

Most general-purpose SLA batteries should have 100 mΩ (0.1 ohms) or less of internal resistance when new. A battery that has a higher internal resistance may be damaged, and will not be as useful as a battery with low internal resistance. It may also be designed that way for high capacity, low current draw applications. You should be able to find the intended internal resistance from the manufacturer’s data sheet. If your cells have a very different internal resistance they may be damaged.

As batteries go, though, 100 mΩ is a lot of internal resistance. At a 20 A current draw you will see up to a 2 V drop. You’ve already done well to put the two batteries in parallel: each will see 1/2 the current, leaving you with a more reasonable 1 V drop when you transmit.

### How to measure internal resistance

You can measure the internal resistance of your batteries by watching the voltage drop at a 1 A load and a 10 A load. The internal resistance will be the same on both loads. So take the two currents and the two voltage drops, and solve for the one resistance common to both. If your SLAs have resistances above 100 mΩ, you may want to put them into a lower demand job and replace them with newer batteries for your radio use.

### How to obtain lower internal resistance

Putting cells in parallel, as you’ve done, is one method that reduces the overall internal resistance of the pack. You could go further and use four 7.5 AH batteries to get even lower internal resistance, for instance.

You can purchase better SLA batteries with lower internal resistance, but there are generally a host of tradeoffs you make depending on the capacity, lifetime, power density, and other factors that should be weighing into your decision. If this is for a specific use, consider asking a new question with your desired use case and we may be able to recommend a few specific battery types and sizes that should better meet your needs.

Generally speaking you might want to focus on SLA batteries meant for high rate discharge applications, such as UPS batteries. These typically have an internal resistance at or below 10 mΩ, which would give you a 0.2 V drop for a single cell driving your 20 A load. Note that even with such batteries, you still have a voltage drop; what you need to determine is how much voltage drop is acceptable, and then choose the batteries that meet that requirement and any other requirements you may have.

You might also want to look into super-capacitors if your transmissions are generally short. By using batteries and super-capacitors in parallel you can reduce the instantaneous current draw on the batteries during short transmissions. This will have the additional benefit of reducing the effect of the internal resistance, giving you more capacity from the battery, and may extend the life of your batteries somewhat.

If voltage drop is unacceptable, you may want to look into voltage regulators that will take the battery power and provide a stable voltage regardless of the load. For radio use this is generally overkill — most radios work well with even a 2-3 V drop, and significant energy is lost in the conversion, so it’s only recommended for special applications.

## Answer (score 2, by rhaig)

Most manufacturers publish their power requirements. 20A sounds like a reasonable estimate.

The more important part of voltage drop is what's due to your wiring. Small gauge and long runs can cause persistent voltage drops. Using heavier gauge wiring like you are, will solve most of that problem.

As was said, temporary voltage drops at the reading on the battery are to be expected. A voltmeter is a very small load that is calibrated to show you the voltage in the system. Adding a significant load (20A draw) on a parallel circuit will result in a measured voltage drop.

You seem to understand your capacity limitations. With a 20A load and 30Ah battery bank, assuming a duty cycle of 10%, you should expect 4.5-5h. Lower duty cycle, longer life.

For better battery calculations, also read about peukerts constant, understand the way batteries are rated (at a rate that drains the battery over a specific amount of time) and experiment with your batteries to figure out their approximate peukerts constant (as most manufacturers don't publish that data).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/552/battery-sizing-for-power-draw, by Dan KD2EE, Quentin Smith, Adam Davis, rhaig. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
