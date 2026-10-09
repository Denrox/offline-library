# Why is the speed of light rounded to 286 Mm in calculations involving frequencies below 30MHz?

*Tags: math, physics · score 10*

## Question

I understand that in order to make the maths simpler, frequency ($f$) is expressed in megahertz (MHz) and the velocity of propagation in free space ($c$) for frequencies above 30 MHz is expressed as and rounded to 300 megameters/second (Mm/s). The actual speed of light is 299,792,458 meters/second, so expressing and rounding this to 300 Mm makes sense.

I'm confused why it is rounded to 286 Mm when $f < 30\ \mathrm{MHz}$. Please explain. An excellent answer will show the maths.

## Accepted answer (score 8, by Adam Davis)

Electrical wave propagation in wire is about 95% to 97% the speed of light. Since wavelength is most commonly used for building antennas, which involve conducting the wave from air into the wire and vice versa, the calculation is adjusted assuming the slower propagation in an unshielded conductor.

However, this 3% to 5% discrepancy is small enough at frequencies above 30 MHz that it is usually ignored for simplicity, and 300 is used instead. For frequencies below 30 MHz it becomes more significant and the adjusted value, *approximately* 95% of 300 Mm, is used instead - about 286 Mm.

\begin{equation} \lambda_{\mathrm{m}} = \frac{(300\ \mathrm{Mm})(0.95\overline{3})}{f_{\mathrm{MHz}}} = \frac{286\ \mathrm{Mm}}{f_{\mathrm{MHz}}} \end{equation}

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/325/why-is-the-speed-of-light-rounded-to-286-mm-in-calculations-involving-frequenc, by Dan, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
