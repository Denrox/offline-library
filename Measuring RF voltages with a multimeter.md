# Measuring RF voltages with a multimeter

*Tags: measurement, voltage · score 3*

## Question

Is it possible to measure RF voltages with a multimeter? I have a multimeter which can measure AC voltages up to 600V RMS, but I'm not sure because I don't know if it assumes the signal to be 50Hz, or at least not several MHz.

I'd like to know the RMS value of the voltage on my antenna. When measured with my multimeter, it shows it's beyond 600V~ RMS. When I measure just before my last inductors I have about 350V~ RMS.

I have a scope which goes up to 400V peak-to-peak on the screen (I'm not sure about its maximum ratings), but I'm reluctant to try, because I'm not sure if the measurements of my multimeter are correct, and I wouldn't like to damage my scope.

So: is it likely that a simple, common multimeter can measure RF voltages? I've seen this circuit which suggests that it's not possible and you have to put something in between the RF and the multimeter:

However, they're rectifying the RF voltage, so they in fact measure with the DC input. My multimeter has an AC input - it's unclear to me if a circuit as this one is still needed in that case.

## Accepted answer (score 1, by Phil Frost - W8II)

For an ideal meter, sure, it's possible. However, most multimeters are not designed to work at RF. There are all sorts of problems: what effect does the input capacitance have on the measurement? What's the characteristic impedance of the leads? Most multimeters don't take these things into account because the only AC voltage they are designed to measure is 60 or 50Hz.

The rectifying circuit in your question is a good solution. Note that you don't really need to use coaxial cable: since the output is DC, it hardly matters what kind of cable you use. The "cable" might just be the leads of your multimeter. You can also stick a sensitive analog meter (something on the order of microamps) directly on a circuit like this and get a decent RF detector.

With an ideal rectifier, what you will measure with the meter (set to DC) is the peak-to-peak voltage of the RF input. Of course, no matter what diode you use, it will be anything but ideal at RF. There is at least the forward voltage drop of the diode to take into account (which can be reduced by using a Schottky or germanium diode). Real diodes also have capacitance, and all the components are going to have some inductances, and these reactances are going to filter the input signal in a way which may or may not be significant for your frequency of interest. However, if all you care about is a qualitative measurement of the input, a simple diode rectifier is quite sufficient.

It's also worth mentioning because it's not always obvious, but if you have a receiver, that can make a valuable piece of test equipment. A cheap SDR (like the SoftRock kits) coupled with the audio card of a computer makes a pretty decent RF frequency analyzer. If you also have an RF signal generator of known power (check eBay), then you can also calibrate your test equipment to give quantitative measurements.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3559/measuring-rf-voltages-with-a-multimeter, by Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
