# Measurement/calibration error after OSL calibration on VNA

*Tags: measurement, calibration · score 5*

## Question

Purchased a HP 8711A some time ago to learn how to make better measurements.

I've tried doing an OSL calibration with a 75ohms Agilent cal kit. When reconnecting the short after succesful calibration, I would expect to have a return loss of 0dB across the whole calibrated frequency span.

However, what I consistently get is something like this:

I know it's only .5dB, and this might be the limits of the hardware, but what I don't understand is that I can replicate this exact behaviour: after every calibration, RL of the short starts around 0dB in the beginning of the frequency span, and ends around .5dB.

If these are measurement errors, I'd expect the outcome to change between different calibrations.

Or am I wrong somewhere?

## Accepted answer (score 2, by Dieter Vansteenwegen)

Seems like I was indeed wrong. The displayed trace displayed was Data/Memory (hence the /M in the top of the screenshot). After redoing the calibration and selecting Data for display, the unit is within +/- .04dB in the whole range. My mistake... Thanks to Default95401 on the Yahoo HP/Agilent test equipment group for pointing that out...

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6831/measurement-calibration-error-after-osl-calibration-on-vna, by Dieter Vansteenwegen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
