# Can you think of any reason my NanoVNA says my antenna has 1.2 SWR while my radio says it has off the scale SWR?

*Tags: antenna, impedance-matching, swr-meter, nanovna, mchf · score 3*

## Question

My radio is an mcHF kit that I just finished soldering up. It receives fine, but when I went to transmit it's giving off the scale SWR. I rechecked my antenna with my NanoVNA, and it shows 1.2 SWR at the same frequency. I would say there's a fault in my radio but when the radio is connected to a dummy load it shows 1.1 SWR. I'm going to retrace all the solder joints on the kit in case I've connected something wrong, but I thought I'd post here in case someone has hints on what to look for.

## Answer (score 2, by hobbs - KC2G)

Perhaps your radio is way off-frequency, do you have any way to test that? A dummy load should be flat across a wide frequency range, so you get a nice low reading whatever frequency you TX at. But the antenna isn't, so if your radio and your NanoVNA are working at different frequencies, it would explain the drastically different readings.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20420/can-you-think-of-any-reason-my-nanovna-says-my-antenna-has-1-2-swr-while-my-ra, by rcx935, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
