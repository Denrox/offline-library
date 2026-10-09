# Can an oscilloscope be used as an RF voltmeter?

*Tags: rf-power, measurement, icom, testing, repair · score 6*

## Question

I just recently acquired a slightly functional Icom IC-735 HF radio, and am trying to resurrect it.

The service manual outlines procedures that specify the use of an RF Voltmeter, which I do not own. I do have a Tektronix 2236 dual channel 100MHz analog scope. Is there any reason I cannot use the scope to obtain the Voltage measurements (at least, the ones that don't approach the BW limit of the scope)?

## Answer (score 5, by Andrew)

One of the functions of an oscilloscope is actually to measure RF volts, just make sure to use the x 10 function to minimize loading on the circuit you are measuring, and keep in mind that some high impedance circuits will still be affected even if you use the x 10 function.

## Answer (score 3, by hotpaw2)

Maybe.

If measuring a circuit output that expects a load impedance, such as a 50 Ohm coax or antenna, then to measure the RF voltage at that point with an oscilloscope, you should terminate that circuit output with the expected impedance (a dummy load), and measure the voltage waveform across that impedance load with a much higher impedance probe (x10 or x100 or resistor divider).

Also make sure the peak voltages and currents are well within the specified limits for your scope input. If you exceed the power input limits, then you may end up with smoke instead of a RF voltage measurement.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17987/can-an-oscilloscope-be-used-as-an-rf-voltmeter, by Andrew, hotpaw2. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
