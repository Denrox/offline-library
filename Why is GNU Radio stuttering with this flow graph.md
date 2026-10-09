# Why is GNU Radio "stuttering" with this flow graph?

*Tags: software-defined-radio, gnuradio · score 3*

## Question

I have a GNU Radio Companion flow graph, where I have the following connections:

- 440Hz cosine wave
- throttle block
- audio sink

All of the above blocks use the same sample rate (48KHz).

When I execute this flow graph, I don't get a continuous note, the way I expected. Instead, it pulses on and off, several times per second. Why is this?

How can I make it output a continuous 440Hz tone?

Removing the Throttle block makes it stop cutting in and out, but it sounds even worse when I do this.

I have tried this setup, with and without the Throttle block, at all common sample rates for sound cards.

## Answer (score 2, by 888)

I ended up figuring it out. I had to do three things:

- remove the Throttle block
- enable the "OK to Block" option in the audio sink
- ensure the amplitude of the sine wave is less than 1

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14715/why-is-gnu-radio-stuttering-with-this-flow-graph, by 888. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
