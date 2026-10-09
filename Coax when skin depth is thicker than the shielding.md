# Coax when skin depth is thicker than the shielding

*Tags: coaxial-cable · score 3*

## Question

Considering coax cable's operation is based on skin effect and shild current flowing on the inner side of the shield how does it work when the skin depth for a given frequency is more than the foil thickness?

I suppose (maybe I'm wrong) coax shielding foil or braid thickness e.g. of a low power thin cable like RG59 may be around 200 microns (https://www.farnell.com/datasheets/2095749.pdf) and according to https://en.wikipedia.org/wiki/Skin_effect for aluminum or copper shield the skin depth at e.g. 100KHz would be 269 microns $$\delta \approx 503 {1\over{\sqrt{\mu_r\times f\times\sigma }}} = 503 {1\over{\sqrt{1\times10^5\times3.5\times 10^7}}} \approx 269\times 10^{-6}$$

So the shield is thinner than the skin depth.

Does it mean there's a lower frequency limit for coax cables determined by the shield thickness?

## Accepted answer (score 4, by tomnexus)

Yes, exactly!

It's not an actual hard low limit, just the shielding effectiveness of the cable starts to drop as the current is no longer confined to the "inside" but flows in the bulk of the copper.

Skin depth is the depth at which the current has dropped to $1/e$ of the value at the surface. Because of the way the integral works, you can calculate the *effective impedance* of a *thick conductor* by assuming all the current flows in one skin depth. But the current actually penetrates much deeper. For example at 4 skin depths there is $1/{e^4}$ or 2% of the current. Even at 10 skin depths the current is -87 dB of the surface; this is a big number but not very impressive shielding.

References to shielding effectiveness at low frequencies are quite hard to find, try also searching for "transfer impedance" which is the Voltage (per metre) developed on the outside of the coax for every Amp of current flowing in it. It's best illustrated by this simple diagram of how it is measured (from (1):  
Here the current is applied to the ouside and measured on the inside (so that you pick up less interference from the environment). They simply apply a known RF current to the bulk cable, and measure the RF voltage developed in the coax.

Here is a graph of the transfer impedance measured on a braided cable (from (2)):  
Notable features of this graph are:

- as the frequency increases, the transfer impedance goes down for a while, so the shielding effectiveness gets better. This is because of the skin effect - as the skin depth gets smaller, less and less of the current *inside* the coax is getting to the *outside*.
- but at some point it turns and starts going up again. This is leakage *through* the braid, because it's woven and not a perfect metal cylinder, as the wavelength gets shorter more and more of the current is visible on the outside again.
- the mess above 100 MHz is probably resonance in the measurement setup, when the cables approach $\lambda/2$
- of course at DC, the transfer impedance is simply the DC resistance of the cable (braid) itself so this is the limit at low frequencies or DC. You can see from the graph it is $0.08 \Omega/m$.

So at frequencies where the shield thickness is less than a few skin depths, the coax still works fine, but it will leak or transfer some of the signal from inside to outside. Whether this is a problem or not depends on the application.

Further reading:


This article has a graph of some results on a braided cable.


This MSc Dissertation[PDF] has tons more detail about transfer impedance and the design of coaxial cables and braids.

(1) A. Fourie, O. Givati, and A. Clark, "Simple technique for the measurement of the transfer impedance of variable length coaxial interconnecting leads," IEEE Transactions on Electromagnetic Compatibility, vol. 40, pp. 163-166, May 1998. (no open access, sorry)

(2) Sensitivity of Shielded Cable Transfer Impedance Measurement to Triaxial Cell Diameter Oskari Leppaaho, Frederic Lafon, Priscila Fernandez-Lopez, Marine Stojanovic, Richard Perdriau, Mohammed Ramdani Link

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21868/coax-when-skin-depth-is-thicker-than-the-shielding, by axk, tomnexus. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
