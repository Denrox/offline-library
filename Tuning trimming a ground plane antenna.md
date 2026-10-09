# Tuning/trimming a ground plane antenna

*Tags: antenna-construction, vhf, vertical-antenna, impedance-matching, measurement · score 6*

## Question

I've built a ground plane antenna with a 19.5" vertical and 4 20" radials. Currently, at 147.135 MHz my SWR is 3:1, clearly not ideal (and even bad for the transmitter!).

I'm reluctant to start snipping radials because I really don't know if the problem is that they are too long or too short. How can I figure this out?

My thought is that I could measure SWR at 142 MHz and again at 149 MHz and that this should tell me, based on the difference, if they are too long or two short or if, possibly, simply changing the radial down angle will help, but I have no idea how to interpret the differences.

## Accepted answer (score 9, by tomnexus)

My trick is instead of cutting, rather *extend* the whip first, and see if the SWR gets better or worse. Extend it 1/2" with a bit of wire wrapped around it and sticking out. If the SWR gets better, then you made it too short in the first place. If it gets worse, you can start trimming.

Remember you should only measure SWR when you are away from the antenna - anyone within 1 or 2 m of the antenna will change the SWR and confuse you as you tune.

You need to bend the radials down at 45 degrees to be able to match it properly. The length of the radials isn't as critical as the length of the whip, rather just bend them up and down.

Lots of small steps is the key, not one big jump. Enjoy the antenna tuning!

## Answer (score 5, by Kevin Reid AG6YO)

If you take SWR measurements at a range of frequencies and plot them (or just watch the SWR reading as you change frequency), you should get a graph with one or more valleys of low SWR.

Ideally, if you find the ratio between the valley's actual position and where you want it to be, and trim or rebuild-bigger the antenna according to that ratio (or rather, the reciprocal of it — note that physical lengths go with *wavelength*, not frequency!), then the resulting antenna will be spot on.

In practice, it won't be exact because you're not building an exactly scaled antenna — your feed-point components and your wire diameter will be staying constant. But you can aim for a little bit too big, then trim it down until the SWR stops dropping.

The above procedure will get you minimum SWR for that antenna design. But remember that you can have a resonant antenna that still has the wrong resistance (i.e. not 50 Ω, assuming you're using normal equipment and coax). Resizing the antenna will *not* change the resistance — you have to change the shape or add a matching network.

The simplest way to figure this out is to use an antenna analyzer that can read out the resistance value. Find that minimum SWR point, then look at the resistance (or the magnitude of the impedance — which is the same here).

You can also tell from the shape of the SWR graph. A matched antenna will have a very sharp valley that hits 1:1 SWR. One with a different resistance will have a broader valley that does *not* ever reach 1:1.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5212/tuning-trimming-a-ground-plane-antenna, by David Hoelzer, tomnexus, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
