# VHF Balancing, necessary? Methods?

*Tags: antenna, vhf, balun, equipment-design, yagi · score 3*

## Question

This is a question about power dissipated due to radiation and ohmic heating caused by common mode current in the coaxial shielding, specifically at VHF frequencies.

When a balanced antenna (such as a yagi) is fed with unbalanced feed line (such as coax), common mode current is induced in the shield of the coax. Even with a perfect SWR (no power reflected to transmitter) common mode current results in some of the power delivered to the antenna being radiated by or dissipated in the coax shield, rather than the antenna, reducing the power radiated by the antenna itself.

My question is: in practice, for VHF frequencies, are these losses due to common mode current negligible or can using a balun noticeably decrease losses due to common mode current? For the sake of this discussion, assume a near-perfect SWR (e.g., 1:1.01).

If there is an antenna efficiency reason to use a balun, what are the pros and cons of sleeve baluns vs gamma matches vs other types?

## Answer (score 2, by user10489)

Most antennas don't actually *need* a balun, but the results of not having one might be undesirable.

Without a balun, the feed coax can become part of the antenna, effectively moving your feed point. If the length of the coax is not resonant, the added length of wire will give wrong impedance and thus higher SWR.

Even if it is resonant (and some antennas do this on purpose), it will distort your antenna's radiation pattern. Depending on the layout of the coax, this might manifest as adding a bit of an omni-directional pattern on top of your existing pattern -- which could be good or bad. It may also distort the power going into the antenna; with something like a yagi, this might shift the highest gain lobe off to one side somewhat.

A gamma or delta match can help balance the antenna when fed with coax, but I don't know if it is a complete solution.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20456/vhf-balancing-necessary-methods, by elplatt, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
