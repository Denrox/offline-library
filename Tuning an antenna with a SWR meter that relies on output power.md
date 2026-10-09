# Tuning an antenna with a SWR meter that relies on output power

*Tags: impedance, antenna-tuner · score 3*

## Question

In my (new) setup, I will have a solid-state HF radio driving an antenna through an antenna tuner. Both my radio and the antenna tuner have internal SWR meters, of the type that requires you to adjust the SWR meter reading based on your output power. My previous experience has been with meters that directly read SWR (either electrically or through cross needles).

I understand how to use these meters to make SWR measurements, but my concern is with the internal protection circuits of the radio. If the SWR is too high, the radio will automatically reduce the output power to protect the radio. When you're tuning an antenna tuner, the SWR may cause the radio to enter or leave this protection region, resulting in an inaccurate measurement of SWR.

How do you approach using an antenna tuner with this type of SWR meter?

## Accepted answer (score 6, by WPrecht)

Most radios with SWR protection don't detect SWR, they just detect reflected power. It's a much simpler (read that as cheaper) circuit to implement and it's what really matters anyway. The manufacturer will have established a threshold for reflected power, based on the MOSFET's tolerance. If the circuit sees more than this it will either clamp it at the threshold level, cut in some sort of limiter or cut out completely.

So I would set the power low (say, 5-10W for a 100W rig) and tune there. Then go to full power. Since SWR is a ratio, you'll have accurate readings without frying your radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/739/tuning-an-antenna-with-a-swr-meter-that-relies-on-output-power, by W5VO, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
