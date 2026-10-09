# HF vertical 1/4w antenna on a tin roof?

*Tags: antenna, vertical-antenna, grounding, dx, 20m-band · score 3*

## Question

I would like to build a 1/4 ~ vertical antenna on my tin roof for a ground plane.

- Does the angle of the roof matter?
- Should the antenna be vertical, or perpendicular to the roof?
- Would it be better if the roof were pointed east /west /north /south?
- Should the roof be grounded?
- Do I connect the shield of the coax to the roof, or add ladder line?
- What is minimum gauge wire for max DX?

I am in Texas. Freq will be 20m. By better I mean DX.

What do I not know I dont know? (about this question!).

## Accepted answer (score 4, by user10489)

If you want a vertical antenna and your roof is slanted, the antenna would not be vertical if it was perpendicular to the roof. :)

It sounds like you are trying to make a ground plane antenna with the roof, which should work well but may need some tweaking to tune it. The angle of the ground plane ("roof") may affect the impedance of the system, but it is probably easier to adjust the antenna than change the angle of the roof.

There is a minimum size for a ground plane to work well. Generally it needs to be about 1/4 of a wavelength in diameter. Larger might be better. If the roof isn't large enough, you could add ground radials to extend it.

There are three kinds of "ground":

- Lightning ground (for which your roof should be grounded)
- Electrical ground (which should have nothing to do with your roof)
- Antenna ground, which is really a misnomer, it's actually the other half of the dipole when paired with a monopole (your vertical antenna).

How you connect the antenna and roof to your feed line (coax or ladder line) depends in part on how you are going to impedance match the antenna system to that feed line. But also, both types of feed line will couple with the roof, so the feed point location and wire path may also affect this decision. Note that there are commercial antennas designed to be used above metal roofs (usually car roofs, but...) If you use one of these, it would typically include a coax connector, in which case you shouldn't worry about how the coax connects to the roof, the antenna mount will handle that.

Wire gauge has little to do with DX. It has a lot more to do with the power (current) you are going to be using. You can put 100w into a surprisingly thin wire and not have any issues. Higher power might need thicker wire, but at 100w, structural integrity of the wire is the deciding factor. 18 gauge or 12 gauge is typical.

As for aiming for DX... what is DX? Is it Argentina? Is it Africa? Is it Europe? Is it Canada? Australia? Japan? (Hint: yes) On a good day, you can get DX from any direction.

And again, it may be tricky to rotate your roof to aim it...so just use it and see what happens!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21682/hf-vertical-1-4w-antenna-on-a-tin-roof, by marc, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
