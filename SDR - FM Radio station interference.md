# SDR - FM Radio station interference

*Tags: rtl-sdr · score 6*

## Question

I want to learn about software defined radio and how wireless transmission work in general.

So I started messing around with SDRSharp and a little antenna I bought.

I figured I would start looking at known frequencies like local radio stations. Some I can get to come in clear by messing with the digital noise reduction but this station (one of the strongest in my area) has a ton of background noise that I can't seem to filter.

Any ideas?

## Accepted answer (score 6, by Juancho)

The interfering harmonics are spaced at around 15.5 kHz. Do you have an old (CRT) TV set nearby? That may be the source, since TV line frequency is 15.625 Hz.

If not, look for other interfering electronics, such as compact fluorescent lights or other switched-mode power supplies (your own PC?).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2063/sdr-fm-radio-station-interference, by DotNetRussell, Juancho. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
