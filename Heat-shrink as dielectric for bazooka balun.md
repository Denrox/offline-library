# Heat-shrink as dielectric for bazooka balun?

*Tags: antenna-theory, antenna-construction, vhf, balun · score 4*

## Question

I'm intending to make a sleeve balun (aka bazooka) for 2m, but rather than keep the lossy coax jacket as a dielectric (I have some RG58), was considering to remove it and replace it with heat shrink tubing.

I haven't been able to find anything here or via google, and am hopeful that some folks here might have some experience, insight, or resource pointers.

Otherwise I'm just going to try it both ways and measure.

## Accepted answer (score 3, by frkfan)

The spies from CIA had this problem solved long ago. See https://www.cryptomuseum.com/covert/bugs/ec/sleevex/index.htm You need to have the relative dielectric constant between the coax shield and the sleeve equal to the dielectric of the cable. By this you maintain same velocity. Also you want to keep the impedance same, which requires quite a thick layer of polyethylene tube in place of the PVC on the outside of the shield. There is a fine calculator at https://www.pasternack.com/t-calculator-coax-cutoff.aspx Take 2.3 as relative dielectric constant of PE.

There is an article covering every aspect of sleeve baluns at http://www.w8ji.com/sleeve_baluns.htm

If you do not need flexibility, try this http://www.w6nbc.com/articles/2009-07QSTcoaxialdipole.pdf which uses air as dielectric.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17166/heat-shrink-as-dielectric-for-bazooka-balun, by webmarc, frkfan. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
