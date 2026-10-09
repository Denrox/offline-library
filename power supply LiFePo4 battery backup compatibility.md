# power supply / LiFePo4 battery backup compatibility

*Tags: power-supply, battery-charging · score 3*

## Question

I want to create a battery backup for my radios. Initially I'm thinking of using an Epic PWRgate and a LiFePo4 battery, so the battery is charged by the same power supply that's running the radios. The LiFePo4 batteries require a charge voltage of 14.4v. Radio gear all appears to require 13.8v±15% (11.7-15.8v), so no problem with raising the voltage there. My current power supply isn't adjustable though, and the few I've found that are have a big knob on the front which seems too easy to bump and end up damaging something.

Is there a better way to go about this? Or another precaution I can take to prevent an incorrect voltage from starting a fire?

## Answer (score 2, by hobbs - KC2G)

One thing that works, though it may be a bit silly: use the "Solar" input of the Epic PWRgate instead of the "Power" input.

The PWRgate's output voltage will come from the battery or from the "Power" input, whichever is higher. If you don't connect "Power", then it will always be coming from the battery. The "Solar" input is regulated down (by an MPPT DC-DC converter) to charge the battery. And the solar input will tolerate up to 30V. So if you take one of those power supplies with the knob on the front and turn it all the way up (generally that makes 16 or 17 volts) it will be fine, and your radio will still see a max of 14.4V or so. Even a 24V fixed supply would probably be alright.

The one caveat that I can think of for this: when using the "Power" input, the PWRgate can pass up to 40A safely. But the solar charge controller tops out at 10A. You can still draw more than that, but it will be the battery that supplies the rest of the current. This may or may not suit you, depending on your radios, your duty cycle, and how concerned you are about cycle life on the batteries.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18173/power-supply-lifepo4-battery-backup-compatibility, by Brad Mace, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
