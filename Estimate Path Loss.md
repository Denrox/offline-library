# Estimate Path Loss

*Tags: simplex, path-loss · score 3*

## Question

I am wanting to setup a simplex path that is 7KM from base to base in relatively flat ground.

How can I estimate the path loss, and what do the numbers mean when I find them?

I am wanting to do it at the 2 meter band, and there are houses and buildings in between

My latitude is 39.76256409 , longitude is -104.86949757, and my friends latitude is 39.73935726 and longitude is -104.95158389

We will probably use cheap easy-to-build 7db yagis on the roof (3 stories or so) if that will work

## Accepted answer (score 4, by AndrejaKo)

How can I estimate the path loss

The answer seems to be to pick one from a catalog of available path-loss models and apply the formula.

Here, I'd try using the Hata model for urban areas. The model was originally made for portable cellular systems, so it uses a bit different terminology.

The formula is not so complicated:

$$L_{50} =69.55 +26.16 \cdot \log_{10}f -13.82 \cdot \log_{10}h_b -C_h +(44.9-6.55 \cdot \log_{10}h_b) \log_{10}d$$

and for 2 m band the correction factor is

$$ C_h = 8.29(\log_{10}(1.54 \:h_m))^2 - 1.1 $$

and

- $f$ is the frequency in MHz
- $h_{b}$ is the height of the base station antenna in meters
- $h_{m}$ is the height of the mobile station antenna in meters
- $d$ is the distance between the base antenna and mobile receiver antenna in kilometers

what do the numbers mean when I find them?

Basic formula for power at the receiver is:

$$ P_{rx} = P_{tx} - P_L $$

Where:

- $P_{rx}$ is the power received, and
- $P_{tx}$ is the transmit power, and
- $P_{L}$ is all losses (path loss, feedline loss, etc).

The Hata model I've shown here will provide path-loss estimate for 50% of locations on the diameter of the circle with center in the "base station" and radius $d$. I personally, as a rough guide, would just use that number as $P_L$.

Now let's try to calculate the number. I'll take the frequency to be 145.5 MHz, which is a bit below the optimal range for the use of this model. The given height is 3 stories plus roof, so I'll round that to 10 meters.

First, the correction factor:

$$ \begin{align} C_h &= 8.29\left(\log_{10} \left(1.54 \cdot \frac{10 \ \mathrm{m}}{1 \ \mathrm{m}}\right)\right)^2 - 1.1 \\ &= 10.6 \ \mathrm{dB} \end{align} $$

Next, the main formula:

$$ L_{50} =69.55 +26.16 \cdot \log_{10}\left(\frac{145.5 \ \mathrm{MHz}}{1 \ \mathrm{MHz}}\right) -13.82 \cdot \log_{10}\left(\frac{10 \ \mathrm{m}}{1 \ \mathrm{m}}\right) -10.6 +\left(44.9-6.55 \cdot \log_{10}\left(\frac{10 \ \mathrm{m}}{1 \ \mathrm{m}}\right)\right) \log_{10}\left(\frac{7 \ \mathrm{km}}{1 \ \mathrm{km}}\right) $$ $$L_{50}=69.55+56.58-13.82-10.6+38.35 \cdot 0.85 $$ $$L_{50}=134.3 \ \mathrm{dB}$$

So what does this number give us and how is it helpful?

The antennas are given as 7 dB Yagi, so I'll take that to be 7 dBi and I'll assume that you have 10 m of say RG-8 coaxial cable (a calculator gives me 0.5 dB loss for that) and that you're transmitting at 35 W.

The transmitter EIRP would be then:

$$P_{tx} =10 \cdot \log_{10}\left(\frac{35\mathrm W}{1\mathrm W}\right) +7-0.5 =21.94\:\mathrm{dBW} =51.94\:\mathrm{dBm}$$

Our estimate of path loss is 134.3 dB and we have a same Yagi at the receiver plus same coax losses. This gives us received power of: $$P_{rx}=51.94-134.3+7-0.5=-75.86 \ \mathrm{dBm}$$ which should be above S9 at the receiver, if my calculations are correct and the S-meter is properly calibrated.

I hope that my description of the process will let you do your own more exact calculations and help you a bit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1581/estimate-path-loss, by Skyler 440, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
