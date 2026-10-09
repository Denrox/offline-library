# Stealth HF station setup advice

*Tags: hf, antenna-system, magnetic-loop · score 10*

## Question

I need some advice on setting up my first HF station in a somewhat restricted townhouse community. If I had a detached house with a backyard I’d probably already have everything setup. But with this townhouse I keep second guessing what to do.

Townhouse Specs:

- Freehold (I can attach things to the outside. But wish to remain discreet.)
- 4 story
- No back yard
- Deck is located above the car garage
- There is a small balcony outside the 4th floor master bedroom
- No attic
- No basement

Known:

- Radio: ICOM IC-7300
- Power Supply: Astron RS-35M

Need help:

- Antenna
- Grounding (no place to install ground rod(s))

The magnetic loop keeps coming up in my research for situations like this. And I have also read some of the SGC documentation for their Smart Tuners. If I understand correctly I could using a SG-237 and do the following without the need for a earth or counterpoise. Based on any of these I should be able to do some variation with my outdoor space (deck and balcony),

- Center Feed (page 12)
- Loop (page 13)
- Apartment Loop (page 22)
- Portable Loaded Loop (page 23)

Do you think going with a magnetic loop like those from MFJ is a better option that doing one of the many wire antenna options with a SG-237? People seem to like MFJ magnetic loops other than some quality control issues and learning to turn it. The reviews of the SG-237 are also positive.

## Answer (score 3, by Kevin Reid AG6YO)

The design of antenna called a magnetic loop has the disadvantage that it has a very narrow bandwidth, and the frequency is set by a variable capacitor mounted on the antenna. This means that changing frequencies requires you to go to the antenna and turn a knob. If your operating position is not next to the loop, this is very inconvenient.

The loops in the Smartuner document you link are not that antenna design (there is no inner loop). But they do have a similar property of placing a tuning element at the feed point of the loop — just this one is automatically controlled, which will be much more convenient, but more expensive.

However, as non-resonant antenna systems go, a tuner at the feed point is the best possible configuration for minimizing loss. If you think you can fit it in your space, that would be an excellent choice.

In any case, you do **not** need a RF ground for any kind of loop antenna to function properly. If you look at the instructions, the “ground” terminal of the tuner is in fact to be connected to the other half of the antenna — it's just that in vertical/“end-fed” designs the ground is the other half, but in any loop it's the other end of the loop wire.

Depending on whether the tuner incorporates a proper balun (I can't tell) you may want to add a choke at the input to the tuner. This prevents the feed line from becoming unintentionally part of the antenna and radiating your transmit power (all the way back to your operating position and causing interference, computer crashes, or shocks in the worst case).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7664/stealth-hf-station-setup-advice, by ifletch, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
