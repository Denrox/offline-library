# How do I design a dual band LPDA antenna?

*Tags: antenna, antenna-theory, antenna-construction · score 4*

## Question

Im not sure if this is the best place to ask a question like this but its the best place i could find.

My goal is to build a dual band antenna similar to this one. That covers 694-1000MHz and 1500-3000MHz.

In theory the design seems fairly simple its just a high frequency antenna on the end of a low frequency antenna sharing the same core. Here is an image of a similar antenna where you can clearly see this

So borrowing from a diagram i found here The design seems to be as "simple" as this


The only issue with this design is that *"Zterm"* measurement.

 1. As far as I can tell the rails need to be terminated a specific distance from the last element.
 2. The way I suspect they get around this is maybe Zterm does not have to be a specific value but instead some multiple of the target wavelength or something?
 3. If that's the case then you could just design the high frequency antenna with a large enough Zterm to fit in the low frequency antenna behind it.
 4. The problem is I have no idea if thats how it actually works and if it is how to calculate the what Zterm values would work for the high frequency antenna.
 5. And then there's the possibility that simply slapping a low frequency antenna behind it would cause them to interfere with each other.

So i am here hoping someone a little more knowledgeable than me would be happy to share their knowledge. It would be really nice to be able to build something like this prof scratch considering the price of the commercial versions.

## Accepted answer (score 6, by tomnexus)

You're on the right track, just cut the middle out of an LPDA and see what happens.

The benefit of this design is that by eliminating the middle section of the antenna, you can get *slightly* more gain in the bands of interest, for the same boom length. Or you can achieve a small shortening of the boom. It's ideal for dual-band cellular antennas, where the bit from 1 GHz - 1.7 GHz is (was) not really required. Doing this makes a mess in the middle frequencies, (the transitions can be improved by tweaking).

Its die-cast successor, the LPDA-44, shows a gain graph like this:  
  
So you can see the hole between the bands.

You should definitely simulate this one before you build. I did all of these in NEC-2, nothing fancy, then built and tested a few prototypes to decide on the exact number of elements needed at the front. You will need to write a custom program to generate the structure with the middle missing, and link up all the segments correctly. Here's a site with an example of a suitable simple NEC LPDA model.

Don't try to make a gap-LPDA like this without simulating it in detail - if you're not going to simulate (or copy one) then you're probably better off with a simple LPDA - they're so forgiving it will almost certainly work first time. Trying this without simulation will probably be lower performance than just making a continuous LPDA.

Termination of the boom is not really required on high gain / pointy LPDAs. Shorter fatter ones have many weird dips in gain when the boom and the longer elements resonate mysteriously, and sometimes the only way to improve this is with a resistor. In this case we short circuited it 1/4 wave from the back, which makes it mechanically strong, and prevents static build-up. You can also leave it open-circuit.

Here are a few more pictures of it, if you want to study the lengths.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14950/how-do-i-design-a-dual-band-lpda-antenna, by brandon3055, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
