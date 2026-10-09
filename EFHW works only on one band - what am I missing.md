# EFHW works only on one band - what am I missing?

*Tags: antenna, hf, wire-antenna, end-fed-antenna · score 5*

## Question

I tried to build a multiband EFHW antenna as described in articles by PA3HHO, PD7MMA, G0KYA and many others. I decided to start with a short 40/20/(15?)/10 meters version without any loading coils. Surprisingly, no matter what I tried I didn't manage to make the antenna work on more than one band. I was hoping someone could explain where my mistake was.

I used FT240-31 ferrite core for 64:1 (and later - 49:1) transformer, about 18 meters of wire (П274М, Russian equivalent of British D10 - I've used it many times before for long wires, dipoles and delta loops) and 2 meters of RG58 as a feed line and counterpoise at the same time. The second end of the cable was connected to a 1:1 balun. The antenna was installed in inverted-L configuration on a 10 meters long fishing rod.

Here is a photo of a transformer and 100 pF capacitor:

I easily got SWR from 1.5:1 to 1:1 on 40m. However the best I could get on 20m is 4:1:

I tried to get rid of the capacitor, to change it value with a variable capacitor, to change the 64:1 transformer to the 49:1 one, to change the length of the antenna, etc. Currently I spend three weekends on this project. No matter what I tried I get a single band antenna.

It looks like I'm missing something. Maybe the loading coil is not optional in this antenna, maybe it's important to use mix 43 (not 31) as other authors did, maybe something else. What would you do to make the antenna work on 2+ bands?

## Accepted answer (score 5, by Aleksander Alekseev - R2AUK)

Eventually I managed to make the antenna work on more than one band. I used a modeller (CocoaNEC) to approximately determine the impedance on each band of interest for my antenna configuration (inverted-V on a 10m long fishing rod). The impedance was about 2450 Ohm. Thus I rewinded the transformer to 1:49. Also I used a 1:1 balun (8 turns of RG58 on FT240-31 core) to eliminate any common mode current. Using a variable capacitor I've found a capacitance (138 pF in my case) that gives the best SWR plot:

No counterpoise was needed since it's role was played by the coax in the 1:1 balun. Then I replaced a variable capacitor with a constant NP0 capacitors. You can find a little more details here. The article is in Russian, but Google Translate should manage.

The antenna was tested on all band where it has SWR < 3: from 80m to 15m. QSOs were made on all these band. However, subjectively the overall performance of the antenna is not great comparing to the performance of a regular dipole. I wouldn't recommend trying to repeat it, at least definitelyly not with cores I've used.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15018/efhw-works-only-on-one-band-what-am-i-missing, by Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
