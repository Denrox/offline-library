# How much current can Baofeng UV-5R provide on +V pin?

*Tags: baofeng, audio-interface · score 10*

## Question

I noticed that the [pinout](What%27s%20the%20pinout%20for%20Kenwood%202.5mm%20TRS%203.5%20mm%20TRS%20connector.md) for cheap Baofeng connectors has +V available. I'm interested in powering some electronics directly from this connector.

When unloaded, this seems to have about 3.3V on it, but when I try to power my load (an ESP32), the voltage drops to 0.8V.

How much current can this pin actually provide without significant voltage drop? Or, what does the voltage/current curve look like?

## Accepted answer (score 11, by Evan Krall)

- With no load, I measure 3.17V
- With 100kΩ load, 2.91V
- With 10kΩ load, 1.59V
- With 1kΩ load, 0.29V

The math works out to a 10kΩ series resistance between +V and ground.

As such the maximum power that can be drawn is at 1.59V/10kΩ load, or 0.25mW max power. Short circuit current would be about 0.3mA.

## Answer (score 9, by Phil Frost - W8II)

I would first measure the current draw of your ESP32 to rule out a fault there.

The +V pin on the Baofeng microphone connection is probably intended to bias an electret microphone. These are essentially a capacitor, with sound pressure changing the spacing between the plates and thus the voltage. They contain a FET buffer since the capacitor could not drive a cable directly. The buffer requires power, but very little: the bias current is probably far less than 1 mA.

Thus it's quite likely the +V pin is unable to supply even a small current. Adding a series resistance on such a pin would have no impact to the intended use of biasing a microphone, but is a cheap and effective way to protect the radio from all kinds of faults that could happen on such a connector.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14619/how-much-current-can-baofeng-uv-5r-provide-on-v-pin, by Evan Krall, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
