# How can I calibrate a SWR meter?

*Tags: diy, measurement, calibration, swr-meter · score 10*

## Question

I would like to build my own HF (1.8 - 30 MHz) SWR meter, however I'm not sure how I can calibrate the meter without an accurate power source. I'm targeting a power capacity of 150 W so I can use it with my HF radio. However, my test equipment at hand does not include a directional wattmeter, and I wouldn't trust the power meter on my radio when the radio is turned off.

I have a number of precision RF sources, but most of those don't exceed 1W in output power. I can get a good 100W+ 50Ω load, spectrum analyzers, and oscilloscopes, but nothing that I would really consider "power RF".

Can I calibrate or validate my meter without an accurate power source or accurate directional wattmeter?

## Answer (score 4, by Phil Frost - W8II)

There are many ways you could calibrate. For measuring SWR, try this:

Attach a 50Ω dummy load to your transmitter. The SWR should be 1:1. Then, attach two 50Ω dummy loads in parallel, giving you an effectively 25Ω load. The SWR should be 2.

It seems you also want to measure power, and not just SWR.

If you have some attenuators available, you can put them on your transmitter's output until you are within the acceptable range for your spectrum analyzer. Then measure the power for that, and add to the measured power the power absorbed by the attenuators.

Or, you could transmit into the dummy load, then measure the voltage with the scope (provided it has sufficient bandwidth), and calculate the power from $P=V_{RMS}^2/50\Omega$. If you use a high impedance probe ("high" meaning anything $\gg 50\Omega$) then the scope won't affect the measurement much. 50Ω in parallel with 10kΩ is still 50Ω, within your measurement error.

## Answer (score 2, by Warren  VA7WPX)

Mike Bryce covered a 3:1 dummy load in QST, in Feb 2013, this will NOT give you an accurate input power reading, but WILL generate a known SWR.

The technique uses a 150 ohm resistive load creating an SWR of 3:1, with enough current/watt capacity, and an adequate heat-sink, so you do not overload the dummy load's thermal limits, when you transmit from the desired transmitter. Your SWR meter can be calibrated while you have your transmitter keyed and attached to this 3:1 dummy load. I believe there is no reactance or inductance involved in this dummy load, it's purely a resistive load, but at the "wrong" resistance, which SHOULD creating a 3.0 readout on a properly calibrated SWR meter. I would think even a tiny amount of transmitter power (say 0.5 to 1.0 watts at HF) should work admirably.

http://connection.ebscohost.com/c/articles/85802751/three-one-dummy-load

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1637/how-can-i-calibrate-a-swr-meter, by W5VO, Phil Frost - W8II, Warren  VA7WPX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
