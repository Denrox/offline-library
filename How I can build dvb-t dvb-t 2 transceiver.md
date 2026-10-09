# How I can build dvb-t/dvb-t 2 transceiver?

*Tags: software-defined-radio, gnuradio · score 3*

## Question

I need dvbt2 transreceiver. I tried gnuradio with https://github.com/BogdanDIA/gr-dvbt. The "apps/dvbt_tx.grc" is working. But, video cannot transfer flexibly.

On gnuradio flow, I adjust multiple const value, and **tx gain** of limeSDR-mini sink.

Anyway, video transfer is not good.

- How I can convert **video.mp4** to **adv8dvbt34.ts**?
- Why "multiple const" used before LimeSdr sink?
- How do I transfer videos flexibly?
- Is there dvbt/dvbt-2 receiver?

## Answer (score 4, by Marcus Müller)

Is there dvbt/dvbt-2 receiver?

Yes and no: T2 reception is too computationally hard so far. It's work in progress, but it's almost certain that your average PC can't decode full standard T2 rates in real time on its CPU. The channel coding is just too involved.

Transmission is always computationally easier.

See gnuradio/gr-dtv/ example flowgraphs.

Why "multiple const" used before LimeSdr sink?

To adjust the amplitude – that's what the multiplication with a constant does.

How I can convert video.mp4 to adv8dvbt34.ts?

FFMPEG can be used to convert video file containers to MPEG transport streams. You need to *exactly* use the same bit rate as your DTV transmission chain uses for the transport stream.

How do I transfer videos flexibly?

Stretch multiple times daily and make sure to train hard so that you'll be the most flexible user of GNU Radio in existence.

No seriously, "flexibly" doesn't tell me anything about what you need.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12856/how-i-can-build-dvb-t-dvb-t-2-transceiver, by John, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
