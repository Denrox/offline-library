# Why are vacuum tubes still used in amateur radios?

*Tags: equipment-design, history, vacuum-tubes · score 14*

## Question

I wonder, even in this modern generation why the outdated vacuum tubes are used. In other electronic circuits they have been replaced by more efficient (and small) transistors years ago. Why they are still used?

## Accepted answer (score 15, by Scott Earle)

The last mass-produced vacuum tube was the **Cathode Ray Tube**, Thankfully those are now going the way of the dodo, replaced with much more practical LCD or OLED displays.

(**Edit**: it turns out the magnetron is still mass-produced, for microwave ovens. Although apparently semiconductor replacements already exist, and soon the magnetron will go the way of the CRT.)

However, for some applications a vacuum tube is still more practical.

Vacuum tubes are (by their nature) high voltage, low current devices; semiconductors are by contrast lower voltage, higher current devices.

The failure mode for vacuum tubes in case of over-voltage is mostly arcing. This does damage the tube, but if it's caught in time it need not be catastrophic. Since the tube's components are made of metal, they tend to go up in resistance (thus limiting the current passing through them) as their temperature rises.

The failure mode for semiconductors tends to be self-destruction. Semiconductors have an awkward property that as they get hotter the resistance goes down, and this leads to thermal runaway, where the device gets hotter still, which lowers the resistance even more, until the device is destroyed.

So in a high-temperature environment, vacuum tubes can be more robust. And this especially applies in high-power applications.

Where high-power amplifiers are made of semiconductors, they tend to run at around 50v and tens of amps. Where vacuum tubes are used, they tend to run in the hundreds of milliamps (which is a lot for a vacuum tube), but in the thousands of volts. The final result is the same because volts x amps makes watts.

For this reason, you will still find transmitters around the world that use vacuum tubes (valves, as they are known in the UK), an example of which is highlighted in this article about the BBC's long wave transmitters from 2011.

Power semiconductors can be very expensive, especially ones that can work at high radio frequencies. It can still be cheaper to have an amplifier with one or two tubes as the 'final', with all the high voltage inside it, than it is to have a much lower voltage, safer semiconductor amplifier for amateur use. The tube amplifier will tend to be more robust, too.

Wikipedia says something very similar about how tubes are more robust at higher powers, on their page on radio transmitter design

## Answer (score 10, by Kevin Reid AG6YO)

As far as I know, vacuum tubes are used in newly-manufactured radio equipment (as opposed to still-in-use old equipment) for one purpose: **high-power amplifiers.** The advantages of vacuum tubes in this application are essentially from the fact that the tube can be built as a large and sturdy device.


Semiconductor devices may fail due to overheating which changes the properties of the semiconductor material in ways which lead to further heating and destruction; vacuum tubes can run hot and be made of large metal structures which are more robust against heat *and* can conduct it away to external heat sinks more readily.


Semiconductor devices may fail due to excessive voltage across them, and improving voltage rating is a difficult engineering problem — vacuum tubes can have physically large elements which the high voltage would have to arc between (through vacuum) to cause failure. In RF applications, high voltages may arise at the output of an amplifier due to poor impedance matching — which can happen while in operation due to changing frequency or damage to the antenna or feed line.

## Answer (score 9, by user10489)

Vacuum tubes are neither outdated nor less efficient. See https://spectrum.ieee.org/semiconductors/devices/the-quest-for-the-ultimate-vacuum-tube

The above IEEE Spectrum article talks about a vacuum tube amplifier that is more efficient than any solid state amplifier.

This is just one example of active research on vacuum tubes.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13344/why-are-vacuum-tubes-still-used-in-amateur-radios, by Sumithran, Scott Earle, Kevin Reid AG6YO, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
