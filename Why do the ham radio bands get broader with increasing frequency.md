# Why do the ham radio bands get broader with increasing frequency?

*Tags: frequency, bandwidth · score 9*

## Question

The ham radio frequency allocations tend to comprise a larger frequency range for increasing frequency ([also see this plot](What%20are%20the%20relative%20bandwidths%20of%20the%20amateur%20bands.md)). For example, the 40 meters band is from 7,0 to 7,2 MHz, thus 200 kHz, while 23 centimeters is from 1240 to 1300 MHz, thus 60 MHz.

Of course, it would not be possible to extend the 40 meters band to 60 MHz since it would cover everything from LF up to 5 meters, but on the other hand, 200 kHz in the 23 centimeters band can deliver the same amount of information (in the Shannon sense) as in the 40 meters band.

For this reason, we tend to use more bandwidth-hungry transmissions techniques on the higher bands, but apart from enabling new applications, such as HAMNET, where we need the higher bandwidth, would this really be necessary?

Is it really only that there are less potential users per bandwidth in the higher frequencies or is there something that would make applications with larger bandwidth infeasible for low frequencies or ones with smaller bandwidth infeasible for high frequencies?

P.S.: Of course, I am happy about every hertz of available ham radio bandwidth and I do not intend to change the allocation. This is only a question out of curiosity.

## Accepted answer (score 8, by Phil Frost - W8II)

There's more space at higher frequencies so the allocations can be bigger.

Consider the difference between 15 MHz and 30 MHz, and the difference between 5,015 MHz and 5,030 MHz. It's a 15 MHz change either way, but in the first case involves a *halving* of wavelength, whereas in the later case the wavelength changes only by a factor of 0.997. Since the way radio waves interact with their environment is largely dependent on their wavelength, we should expect that 15 MHz will be very different from 30 MHz, but 5,015 MHz and 5,030 MHz will be nearly identical.

For example, frequencies below 50 kHz can penetrate seawater, with the lower frequencies penetrating more. So these low frequencies find application in submarine communication, but the entire band of usable frequencies here is less than 50 kHz wide.

HF (3,000 to 30,000 kHz) doesn't penetrate seawater to a significant depth, but it does support ionospheric communication which is great for global communications. This is a band of 27,000 kHz.

Above 30,000 kHz, ionospheric propagation isn't possible, so reliable communication is generally limited to line of sight. Above 30,000,000 kHz, atmospheric attenuation starts becoming a significant problem. So that means a band of 29,970,000 kHz is usable for line of sight radio communications.

This is a very broad categorization, but you can generally see there are not many frequencies that have similar behaviors to a relatively low frequency like 15 MHz, whereas there are many frequencies similar to a high frequency like 1,500 MHz. As such, allocations at lower frequencies must be smaller if one particular user is not to monopolize all frequencies usable for a particular application.

## Answer (score 7, by Kevin Reid AG6YO)

There are some straightforward reasons I can think of which apply to all spectrum allocations, not just amateur radio:


In a lot of cases, the bandwidth of a RF device is relative; if you are using the same physical principles, but change the dimensions/values to double the operating frequencies, everything scales up equally so you have a device with twice the bandwidth. Thus, it is more technologically feasible to use more bandwidth for a single transmission as frequency increases, so there is motivation to make proportionally larger allocations to be able to employ such modes.


From a historical perspective: at any given time after the invention of radio there has been demand for many uses of spectrum *that can be used by the technology of the day.* And as we look back, higher frequencies were less practical, and also the bandwidths of the signals that people wanted (or considered reasonable) to transmit were lower. So, what looks like a reasonable size of pieces to delineate and hand out scales with the technological characteristics.

I don't know to what degree these factors have been *explicitly* considered in allocations, vs. just working with the needs and desires of the time. Answering that would require looking at the history of spectrum allocation and the ITU.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/11797/why-do-the-ham-radio-bands-get-broader-with-increasing-frequency, by koalo, Phil Frost - W8II, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
