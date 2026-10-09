# Will 2 ferrite beads taped side by side perform the same as a single-piece binocular core?

*Tags: antenna, ferrite, transformer · score 6*

## Question

I intend to make a beverage antenna and have quite a few spare ferrite beads of various mixes. If you look up binocular core ferrite on amazon you will see they are a single chunk piece of ferrite with 2 holes side by side bored through it. Is there anything special to it being one piece? Do the same RF physics apply to taped adjacent beads? Thanks kindly.

Ref blog article: Blogger using taped ferrites

## Answer (score 2, by Marcus Müller)

Is there anything special to it being one piece?

Yes! Let me elaborate below.

Do the same RF physics apply to taped adjacent beads?

Only for some applications, not for others.

When I look at the photo of how the core is used in the blog post that you refer to:

We can see that the currents in the windings are flowing in a horizontal circle. Right-hand rule tells us that thus the magnetic field is vertical in the middle of that circle! And knowing magnetic fields always form a closed loop, they would come out of the middle of that wire loop, and make a "donut" (where the windings all lie in the dough). So much for basic electronmagnets.

Now, the ferrites are *not* air. They are a material that has a high $\mu_r$, meaning that it is much "nicer" for the magnetic field to follow the shape of the ferrite.

That's pretty OK in this case: our "air core donut" simply gets two sides that contain a lot of field strength (left and right in the photo) where there is actual core material. That's awesome– the magnetic field just forms a circle in each of the two hollow cylinders. There's not "no field at all" at the far and close end of the cylinders, but it's so much less that you can usually neglect it, compared to how much of the power is actually in the ferrite.

So, in this configuration, the "bridge" between the two "tunnels" simply doesn't matter; tape away!

However, one might be tempted to wire a transformer/balun differently, much like "textbook transformers" are usually built: primary side wound around the left core, secondary side wound around the right core. Would be cool if you could just re-wind (or exchange) one side if one finds out, for example, that the antenna matching is slightly off and 3 windings less on the secondary side would be better. Much easier than unwinding your whole balun just to be able to do that!

It would be a bad idea, however. Remember that due to the higher $\mu_r$, the magnetic fields will much prefer to go through the ferrite than through air. There will not be much magnetic field that goes through the other core, so the transformer/balun will not transport energy from one side to the other, making it simply look like two independent inductors instead.

Now, that seems like an easy mistake to avoid. Why then sell these binoculars instead of two hollow things, which saves material?

The answer is probably that the binocular shape is easy to produce and solves the issue of holding the two tunnels in place for anything to be wound through both. Wasting a bit of not-that-expensive-anymore material might be cheaper than adding an extra fabrication step to glue these two together!

Also mote that due to thermal and saturation reasons, it's desirable that the two cylinders are a bit thicker in the center of the electrical winding – because thicker means that the magnetic field spreads out a bit more, reducing the maximum field strength. So, the ideal shape would be a bit of like a "thickish $\infty$"; but saving that little about which is the difference between the "flattop binocular" and the "thickish $\infty$" really only pays if your core material is expensive, or your core is so large that producing it in one piece is complicated.

tl;dr:

So, the trick here is visualizing, based on where the current loop lies, which path the magnetic loop must take. If it can be all in the ferrite materials (such as in your blog post), it's all fine. If not, you might be in trouble, and will probably not get around simulating your electromagnetic system to know whether it can do what you want it to do.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22771/will-2-ferrite-beads-taped-side-by-side-perform-the-same-as-a-single-piece-bin, by BBQ-Man, Marcus Müller. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
