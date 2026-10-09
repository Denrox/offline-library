# How Could Superheterodyne Receiver Ever Work?

*Tags: receiver, equipment-design, mixer, superheterodyne · score 9*

## Question

I am surprised how the Superheterodyne Receiver still works and is still in use after coming to realise the impact of Image Frequencies on its performance. Basically, I'm curious how engineers make such an architecture work despite the affect made by Image Frequencies at multiplication stage of Super Heterodyne Architecture. I illustrate the affect of Image Frequencies using the following diagram.

As seen, It seems our intelligence on right hand side can be destroyed by the Image Frequencies (whole band of it) standing to the left side to the LO once both signals go through the mixer. I think this is an unavoidable scenario because making Band Pass Filters to eliminate signals close to the left hand side of LO is not practical.

Imagine a busy band such as 868MHz. The complete spectrum is busy and filled with **very closely spaced outpowerful transmissions**. In such cases, I can be certain that there will definitely be powerful signals to the left of my LO. Hence, the resulting down converted difference frequency band will always represent both bands to surrounding the LO. This can be more clearly seen by the figure below.

I am very interested to know how engineers despite this phenomena still make excellent use of this architecture. What am I missing?

Please note that I am fully aware that this problem is eliminated in the later Homodyne architecture. But I would like to make my question very specific to this architecture.

Thanks for your answer/s.

## Accepted answer (score 14, by Phil Frost - W8II)

The answer is simple: filtering.

For example, let's say the desired signal is at 800 MHz, and the intermediate frequency (IF) is chosen to be 100 MHz. Mixing the 800 MHz signal with a 900 MHz local oscillator (LO) would get the signal into the desired 100 MHz IF, because 900 - 800 = 100.

But also the image frequency of 1000 MHz would end up at the IF, because 1000 - 900 = 100.

The solution is simple: add a filter between the antenna and the mixer such that there are no signals at 1000 MHz.

The designer can select the IF to make this easier. A higher frequency IF moves the image frequency farther away, making the image frequency easier to reject. However this also makes it more difficult to obtain a sharp band-pass filter at the IF, since the fractional bandwidth will be smaller. This is one of the reasons for the superheterodyne design: a high first IF makes image rejection easier, while a lower frequency second IF makes a sharp channel filter easier.

The designer can also put the LO above or below the target frequency, which may place the image frequency such that it avoids broadcast bands which are likely to contain strong interference, etc.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10472/how-could-superheterodyne-receiver-ever-work, by Denis, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
