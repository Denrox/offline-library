# does the shape of an antenna ground plane matter?

*Tags: antenna, antenna-theory, counterpoise · score 5*

## Question

I would like to test a tranceiver setup I created before I mount it in my car. In my backyard, there's a length strip of metal; 10m in length, 10cm wide. Now I wonder if I can use that as a ground plane for an antenna.

Is it important for an antenna ground plane that it is round? Or will an irregular shape (or even long strip) work as well? (...as long as the size of the surface is big enough?).

## Accepted answer (score 5, by Kevin Reid AG6YO)

We use irregularly-shaped ground planes all the time — car roofs, and metal boxes, and all sorts of things.

However, [the difference between](When%20and%20why%20does%20the%20size%20of%20a%20ground%20plane%20or%20radials%20matter.md) a *ground plane* and an *antenna with two elements* is in the fact that a ground plane (or set of radials) allows the current to *spread out*. As it has been explained to me, this is the key property which means the size of a ground plane does not much matter — the more the current can spread out, the lower the impedance presented to the feed point. (Ideally it would be 0 Ω, a perfect ground that accepts any amount of current and stays at 0 V, as measured relative to your vehicle chassis or whatever.)

- If you mount your antenna on one end of the long strip, you are not using a ground plane antenna, but an “L” antenna.
- If you mount your antenna in the middle of the long strip, it is *a little bit more like* a ground plane antenna, or an antenna with 2 "radials".
- If you cut your long strip into two pieces, cross them, and put the antenna in the middle, that's even more like a full ground plane (4 radials).

Now, this doesn't mean that your antenna will work *better* this way. Rather, it will work *more like it would with a full ground plane* — your test will be more realistic. But in the end, there is no substitute for testing and tuning the antenna in its final installation location.

## Answer (score 2, by user10489)

It depends entirely on what you are testing.

If you just want to see if it works, there is a minimum size to the ground plane. What you are describing sounds way too small, but that depends on the frequency, so I can't really tell with the information supplied.

The "ground plane" is really just the other half of a dipole needed by a monopole. So it needs to be at least a quarter wave long to work, shorter if it's spread out like radials. For just testing if it is going to work, the shape doesn't matter a lot. Rule of thumb is that the ground plane has to be at least as big as the monopole.

However, the shape does have large consequences to the radiation pattern, and the angle between radials and the monopole has a large effect on impedance. So if you are testing effectiveness, radiation pattern and gain, there's no substitute for placing the antenna in its final location.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21186/does-the-shape-of-an-antenna-ground-plane-matter, by Folkert van Heusden, Kevin Reid AG6YO, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
