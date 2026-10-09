# How to make a 1:2 UnUn

*Tags: antenna-construction, transmission-line, transformer · score 4*

## Question

Does anyone have a drawing or instructions on how to make a 1:2 unun like the one in the picture below ?

I searched this question on this site and on the internet with no luck.

## Answer (score 4, by webmarc)

I found this at this page by PA0ROB, which you should absolutely check out. He's focused on higher ratio ununs, but shows the general design principles that you can use to make a 2:1.

One of the key principles is that **the impedance transformation is the square of the turn/winding ratio**, so you're looking to wind a 1.4:1 ratio (since 1.4 * 1.4 ~ 2).

With the ratio math out of the way, now you can focus on translating that to physical windings using the above page as a template.

Hope this is helpful!

## Answer (score 2, by EdvinW)

@webmarc mentioned the ratio 1:1.4, which is an approximation of 1 to the square root of 2, which is approximately equal to 1.4142135..., but how do you approximate this infinite number with a finite number of turns?

@Andrew mentioned the ratio 10:14, which is good, but there are other numbers of turns that could be handy to know.

If you want as few turns as possible, you could go with the ratio 3:2. (3/2)² = 2.25, so you end up with a 1:2.25 transformer which is sort of close and might be good enough for some applications.

6:4 is the same ratio as 3:2, but with higher numbers, but if you want more turns you might as well go with 7:5. This ratio is significantly closer, and (7/5)² = 1.96.

If you want an even closer approximation, the only better approximation with less than 70 turns is 17:12, with (17/12)² ≈ 2.007.

I can't see any reason anyone would need a more accurate approximation than that, since in practice other factors like the precise way you mount the wire on the toroid or how tightly you wind the turns most likely will affect the result more.

If you want more turns, simply use a multiple of one of the suggested numbers!

Hope this helps someone!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20756/how-to-make-a-1-2-unun, by Andrew, webmarc, EdvinW. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
