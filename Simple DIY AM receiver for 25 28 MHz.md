# Simple DIY AM receiver for 25/28 MHz

*Tags: hf, diy, receiver, am · score 5*

## Question

I'd like to build a **simple AM receiver for 25 and/or 28 MHz** to receive DCF77-formatted time code. It doesn't have to be extremely sensitive or selective - the local clock oscillator will keep time while it cannot receive the time code during my rare HF transmitting activities. Frequency stability should be relatively good (crystal controlled). Could anyone suggest a basic schematic or kit for the purpose?

There's a local 25.000 MHz reference transmitter which has good local coverage, and I'd like to receive that. In addition I'd like to build a version for 28 MHz to receive a local amateur beacon and my own testing transmissions.

Please not that this is not the DCF77 station (77.5 kHz) in Germany, this is a local reference transmitter on **25 MHz** which just happens to use the same time code format.

I'd prefer a traditional standalone receiver (one that doesn't require a computer for SDR), since I'd like to decode the time code in a low-power Atmel microcontroller.

## Accepted answer (score 2, by EEd)

Since OP requires MCU, doesn't have to be extremely sensitive or selective and the 'local' transmitter, one suggestion is

1. Use Arduino (Atmel) to control DDS chip to generate 25MHz + - 77.5KHz
2. Use mixer circuit taken out of Hamitup or similar. Simple transitor, FET, MosFet or diode also ok (for local transmitter)
3. The 25MHz signal, now shifted to 77.5KHz, can be feed to a 'standard DCF77 receiver' (below and also many design on web) which presumably have some degree of band pass filtering in the front end.
4. This setup does not have good image rejection. It will work under specific condition OP requires, local transmitter.

Info DDS and driver here DDS2 DDS info

Alternately, to above DDS with Arduino, another suggestion is the ProgRock and (manual here) which is an interesting solder kit and also fulfills OP's Atmel chip requirement. It uses another DDS chip, Si5351A and outputs square wave instead of sine wave as above chip. Square wave has less favorable spurious response but no problem under OP specified conditions. LPF can be added to make it sine wave.

As OP mentioned building stuff, yet another alternative to consider is to get a HamitUp, removes the oscillator and replace with signal, with suitable level adjustment (no need to be very accurate), from either of the two DDS plan.

After building it, both DDS become a signal generator that you can use it for other task. Like WSPR and a few other digimode transmitter, just change software. Tie 2 balloons and flew around the Earth S11

Happy HAM / DIY. Tens of Euro/USD/Stg/etc., in hands of knowledgeable people, can go far. Hope it helps.

Here is plan for a standard DCF receiver with Arduino decode software. Hardware ant with amplifier module. Signal from the mixer can be coupled to the antenna rod by 3 turns winding at the far end (away from existing coil) of the ferrite rod

## Answer (score 2, by K7AAY)

10 MHz WWV Receiver Experiments has a basic schematic for you as well as some good detail.

However, as per Wikipedia, the 25 MHz broadcasts were discontinued in 1977. I also confirmed at the WWV website that 25 MHz is no longer used.

## Answer (score 2, by Phil Frost - W8II)

The SoftRock SDR kits could qualify as "simple", if you mean simple electronics. Some of them cost as little as $10 USD. They have fixed-frequency crystal oscillators, and you could probably swap the crystal for a nearby frequency in any of the kits as desired. The slightly more expensive and higher part count kits have a LO variable from DC to VHF and are usually limited by the input filters.

Of course, the simplicity of the electronics is balanced by the complexity of the computer necessary to demodulate the received signal, and you'd have to become familiar with SDR operation, but maybe you don't mind.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1172/simple-diy-am-receiver-for-25-28-mhz, by oh7lzb, EEd, K7AAY, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
