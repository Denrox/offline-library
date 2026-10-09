# Am I calibrating my SWR meter, SWR-001, correctly?

*Tags: equipment-operation, swr-meter · score 3*

## Question

I have an SWR-001, which seems to be released under two different brands, MyDEL and Sharman. The MyDEL SWR-001 looks like this:

and the Sharman one looks the same except for the label on the bottom left (it looks like Sharman could afford a brand and MyDEL didn't):

In case I'm wrong about these two devices being the same, I have the first one, the one with the label SWR.

The feeder goes from my Icom IC-7300 to the SWR-001 and the SWR-001 in turn is connected to an LDG IT-100 autotuner (which also has the data lead to the IC-7300 for auto-tuning).

After finding an clear frequency, I set my radio to FM mode and 100W. I then set the SWR-001 Range to 300W, Function to CAL, and Power to FWD. I press the PTT and adjust the CAL knob until the needle shows 100W.

Is this procedure correct to calibrate the SWR-001 to measure the SWR?

Should I do it with the tuner turned on or off? The results are quite different and I don't know the theory behind the calibration procedure to be able to figure out what's going on on my own.

Also, it seems this calibration only works at a certain frequency or band and when I change to a different band I should re-calibrate. Is this correct?

This calibration has no effect on measuring power, does it?

## Accepted answer (score 4, by Glenn W9IQ)

The calibration procedure is only used for determining the SWR - the forward and reflected power reading are not impacted. If you change power levels or frequency, you need to perform the calibration again to read the SWR.

The calibrate procedure is to set the needle to the CAL position on the meter, not to the 100 watt reading as you described. Then flip the switch to SWR to read the SWR.

As your LDG tuner adjusts its match point, you will probably need to do a minor tweak on the calibration of the SWR meter. But the job of the tuner is to present a 1:1 SWR to the transmitter so if the tuner is able to find a match, your SWR meter will always show a 1:1 SWR or equivalently, 0 watts reflected power.

It is a good practice to use only 10 watts or so when adjusting your antenna tuner. This helps to reduce stress on the transmitter and the tuner. If the tuner interfaces properly to your transmitter, it may automatically cut power when tuning.

When you read the SWR with the tuner in bypass mode, you are seeing the SWR of your antenna system before the tuner attempts to make this a 1:1 SWR for the transmitter. Take such readings using low power and record them in your logbook. Then later if you suspect antenna problems you compare the readings.

Your IC 7300 has a built in antenna tuner. If you are using your LDG tuner, it is probably best to disable the 7300 internal tuner.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10108/am-i-calibrating-my-swr-meter-swr-001-correctly, by Pablo Fernandez, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
