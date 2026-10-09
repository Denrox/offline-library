# Polarisation loss Dipole antennas

*Tags: antenna, dipole · score 3*

## Question

For a school assignment I need to calculate a link budget between two half wave dipole antennas, but I am stuck at calculating the polarisation losses in the antennas. the antennas are ideal and matched. The antennas are 6 KM apart, the signal strengt Ps = 10 W, frequency f= 100 MHz, angle between the antennas is 50 degree and the max Gain of the antennas is 2,13dB.

I have to calculate the link budget between S and E3. What the teacher did the following to get the Gains with polarisation loss:

Gs3 = 10log (10^2,13 * (sin^3(90+50))^2 ) = -1,707dBi

G3s = 10log(sin^2(90-50) ) = - 1,707dBi

The problem is that I am not getting these numbers when I use these formulas and different now I am seriously confused about how I am supposed to calculate this.

I do know that the original formula for polarisation loss in dB is: 20 log( Cos^2(a)). But even when I use this formula I am not getting the same numbers as what the teacher gave us.

## Answer (score 2, by tomnexus)

I think I can decide the intent of the formula. It's wrong, as you've written it.  
I assume the drawing is a flat 2D picture of three antennas in space, not a perspective view of three antennas on the earth's surface.

In this case I can see what you're trying to do:

Gain of a dipole is 2.13 dBi.

The radiation pattern of a dipole can be approximated by $\sin^2(\theta)$.

So you could say $10\log_{10}(10^{2.13/10} \sin^2(90-\alpha))$.  
Or better, $2.13 + 20\log_{10}(\sin(90-\alpha))$.  
Equals $2.13 - 3.8 = - 1.73$.

This is simply the gain of dipoleE3 *in the direction of dipoleS*.  
Wikipedia has a good page with this picture:  
There is no polarisation loss as they're in the same vertical plane. Your formula for that does look correct, but for dipoles not in the same horizontal plane, to find the angle a you might need some tricky trigonometry.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6845/polarisation-loss-dipole-antennas, by MarkerDave, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
