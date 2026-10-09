# How different is Q-factor of SMD inductor from regular one?

*Tags: equipment-design, inductor · score 5*

## Question

I am trying to figure out if it is possible to replace inductors like this  wound by 0.1mm (diameter) copper wire with multilayer 0805 SMD inductors. Those are supposed to be used inside band-pass filters. Right now there are 2 coils but I am thinking if it is worth using SMD inductors + trimmer capacitors there. The main goal is to reduce footprint on the board. I want to make cheap mobile rig so am looking for ways to make it lightweight and compact.

## Accepted answer (score 8, by tomnexus)

SMD chip inductors, compared to larger ones, will generally have:

- lower Q
- higher DC resistance
- higher SRF
- lower DC saturation current, if they're ferrite cored

But read the datasheet and see if they'll work for your application. Often the higher SRF, smaller size and lower cost are the most important factors.

For filter design trade-off, I'd suggest:  
First design the filter with ideal components.  
Then simulate it again with real inductor resistance and Q. (Choose inductors that have SRF several times your operating frequency). Adjust inductance to bring the filter back into tune.  
Compare performance to the ideal filter.

This will give you an idea of the additional losses in the filter due to the small components.

For simulations, if you don't already have a tool, I recommend QUCS. It's old and slightly cranky, but it's free and can do almost anything. Others might know better free software.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10484/how-different-is-q-factor-of-smd-inductor-from-regular-one, by k1zmt, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
