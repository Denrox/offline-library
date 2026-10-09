# Using threaded rod for VHF radials

*Tags: antenna-construction, vhf, radial · score 3*

## Question

I've been thinking about building a VHF antenna using stainless threaded rod for the ground plane's radials to mate with a hub I already have. My theory is that will make life easier than trying to put threads on stainless round bar myself.

But I know that RF travels along the skin of the conductor, and presumably the distance that electrons have to travel will be longer because of all those threads.

Does threading make any difference in terms of radial length?

## Accepted answer (score 5, by tomnexus)

I was about to say it would have no impact - In my experience thread has no effect. I've used threaded rod all over antennas though not usually for the whole element. But scratching a bit found this excellent application note which describes how surface roughness in the copper on PCB traces matters to attenuation. They say that the roughness starts to matter *when the size of the surface features becomes similar to the skin depth*. So in your case it would definitely have this effect.

Whether the modest increase in resistance will matter to you depends on the antenna design. A base inductor of a short whip carries a lot of current, every ohm counts. For the ground radial, four in parallel, I'd say even if you get 10 ohms each, it wouldn't matter to the antenna.

Stainless steel has a much higher resistance than copper or aluminium, but again it probably won't have a large effect on the antenna performance. You can work it out, with a skin effect calculator, for both types of wire, but even several ohms in series with the feedpoint won't change the gain or VSWR very much.

Using stainless steel instead of copper, brass or aluminium, will have a much bigger effect than the threads.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20950/using-threaded-rod-for-vhf-radials, by user3486184, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
