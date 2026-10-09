# Yaesu VX-7R clock is running very fast

*Tags: ht, yaesu · score 8*

## Question

I just noticed the clock on my Yaesu VX-7R is running *very* fast. I noticed this a few days ago, where it would be days ahead. I would reset the time to the second and then, again, hours or days ahead.

I'm not sure when this started happening, or if it has always been this way. The unit was purchased new a few years ago. I guess I never had the clock on the display at all, but I've recently tweaked the settings to show the clock on the main display at all times.

Finally, today I set it and saw that it was running *minutes* fast. It would be 2-3 minutes ahead after only one minute of actual wallclock time.

One hint on an old forum suggested doing a **Microprocessor Resetting** as per the instructions in the manual, but this did not change the behaviour.

## Accepted answer (score 9)

Original poster and answerer here. This Answer is incorrect. Once the clock starts doing this a full battery reset will only help for shorter and shorter increments. The correct answer is to replace the battery, as per [https://ham.stackexchange.com/a/21914]

Self-answering because I did not find this anywhere else, though in retrospect it was sort of obvious. I thought that putting it here might make this more accessible to future internet spelunkers.

Even though a **Microprocessor Resetting** (VX-7R manual, p.80) did not work as I previously mentioned, it occurred to me that some non-volatile settings might be maintained across a reset.

So, I pulled the battery and let it sit for a minute or so before replacing the battery. Then I did a [4] [BAND] [V/M] reset and set the clock to the correct time. It's been keeping accurate time since.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20439/yaesu-vx-7r-clock-is-running-very-fast, by . CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
