# Why is IC-7300 transmitting at zero power in "Rig" split mode with WSJT-X and FT8?

*Tags: icom, equipment-troubleshooting, ft8, wsjt-x, icom-ic-7300 · score 3*

## Question

I am successfully running FT8 with WSJT-X on Windows 10 with my IC-7300. I am using IC-7300 as the rig.

On reading the official WSJT-X User Guide (and various YouTube videos, etc.) I see that many places strongly recommend running FT8 in split mode. Since the IC-7300 has two VFOs and supports split mode I chose the "Rig" setting in the WSJT-X settings. When I do so I see the radio shows "SPLIT" on its screen and does use separate receive and transmit frequencies. However, when it transmits it transmits at zero RF power regardless of what I set the RF power to with the Multi knob.

But when I change WSJT-X to "Fake It", which does not use SPLIT mode and instead just makes the radio change frequency to transmit and then makes the radio change it back to receive I see the radio transmitting at the power level I'd expect.

Any idea why I'm seeing my radio sit at zero transmit power in SPLIT mode? I've talked to a couple of friends with IC-7300 radios and they are *not* seeing that happen with them -- they see the radio transmit at expected power.

## Accepted answer (score 2, by QuantumMechanic)

**Short version of the answer:**

VFO B was USB, not USB-D. After manually changing VFO B to USB-D it worked.

**Longer version:**

I went back to testing this again and finally noticed that the mode indicator was changing from USB-D to USB every time the WSJT-X keyed up the radio. Apparently telling WSJT-X to use data mode only ensures the radio is using data mode on VFO A. Thus you apparently have to manually make sure VFO-B is also set to USB-D.

Given that, I think I'll just keep using "Fake It" instead of "Rig". It accomplishes exactly the same thing and I don't have to worry about forgetting to put VFO B in a proper state.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18873/why-is-ic-7300-transmitting-at-zero-power-in-rig-split-mode-with-wsjt-x-and-ft, by QuantumMechanic. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
