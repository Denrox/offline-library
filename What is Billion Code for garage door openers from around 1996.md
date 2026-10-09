# What is "Billion Code" for garage door openers from around 1996?

*Tags: software-defined-radio, digital-modes · score 6*

## Question

I've been trying to "hack" my garage door using an SDR (LimeSDR) for a high school physics project, and I have run into a snag.

When I look at the signal and demodulate it using ASK in Ultimate Radio Hacker (URH), I seem to be getting a signal that makes no sense.

I get.

10011001101110001011100010111011100110011 [Pause: 70854 samples] 1110001000100010001001101110011001101110001 [Pause: 78094 samples] 10011001101110001011100010111011100110011 [Pause: 74099 samples] 1110001000100010001001101110011001101110001 [Pause: 78071 samples] 10011001101110001011100010111011100110011 [Pause: 74078 samples] 1110001000100010001001101110011001101110001 [Pause: 78096 samples] 10011001101110001011100010111011100110011 [Pause: 74111 samples] 1110001000100010001001101110011001101110001 [Pause: 66865 samples]

...but the dip switch on my Garage door clicker is set to 010100010101.....

Confusing, right?

Well, so now I figure out that my garage door clicker is meant to work with many different types of garages, from rolling code to dip switch. So I look up whether my garage door opener uses a rolling code or dip switches, and I find out that since it was made in 1996 and it is a model 2000SD Chamberlain Green Button, it uses something called "Billion Code".

I can't seem to find out any details on what this is and I desperately need your help.

## Accepted answer (score 6, by Glenn W9IQ)

The billon code refers to a generation of transmitters that could transmit up to ~3.5 billion different codes. Although there were a large number of codes possible, the transmitter always transmitted the same code each time the button was pressed, unlike more modern versions where the code changes each time the button is pushed (a rolling code).

The DIP switch on your remote could either be that it is facilitating a dual standard remote (e.g. an earlier standard) or the DIP switch selects on of ~ 4096 different codes out of the ~3.5 billion possible. I would guess based on your decoded output stream that it is the former.

So, you have already decoded the fixed bit strings that your transmitter puts out. You can see that it consistently repeats. Now you simply recreate that bit stream in your SDR transmitter and you can open the door using your SDR.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10198/what-is-billion-code-for-garage-door-openers-from-around-1996, by Ben Newhall, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
