# Upper Frequency Limit for Bouncing Off Ionosphere

*Tags: ionosphere · score 5*

## Question

What is the upper frequency limit for bouncing a signal off the ionosphere?

Context: I have a friend who claims he's getting E layer bounce of several FM stations (88 to 108 MHz) up to 200 miles around Panama City, FL. using a 20-foot discone antenna. This conflicts with the information I've seen (e.g., Figure 3 here: https://solar-center.stanford.edu/SID/science/Ionosphere.pdf).

Is there some other mode of propagation that could account for this?

PS: Here is a map of stations my friend created.

PSS: Update from friend. The range and stability of the contacts above indicate these are ducts. He provided another contact map in which these are certainly sporadic E layer and has confirmed these were short-lived:

Also see this site which has a lot of info on E layer DXing: wtfda.org

## Accepted answer (score 5, by Ryuji AB1WX)

The 200-mile hop distance is one tricky component in your story. Given that the receive station used a discone antenna, I assume the receiver had a high sensitivity comparable to amateur radio 6m or 2m equipment, rather than an FM radio receiver. There is a significant gap in sensitivity (receiver system gain) among different receiver types.

The free space path loss at 100MHz is about 122 to 125 dB at 300 to 400 km hop distance. That is the baseline.

The regular E layer has way too low an electron density to reflect 100MHz at any angle, so that is not a contributor to this path.

When the sporadic E layer emerges, the path loss is comparable to free-space path loss or maybe up to 5 S-unit weaker. Because 300-400km is a short end for Es hop distance, I would expect about 140-160 dB path loss.

Tropospheric ducting is also possible, and probably most frequently seen in southern Florida, and the path loss is about 35 to 60 dB worse than free space. So around 170 dB loss at 300km.

Troposcatter is another possibility, but the path loss is greater, 170 to 220 dB. Troposcatter is a lot more stable and reliable than the two above, but requires much more serious and intentional system engineering.

Diffraction due to the terrain is also possible at about 40 to 80 dB added to the free space path loss. But this will be a mostly permanent path.

So, if the signal was noticeably very strong and that was a very rare event, I tend to think sporadic E is most likely. However, if the signal was weaker, the duct is more likely. If the same receive situation happens rather frequently, duct is more likely than sporadic E in Florida. (Think Bayes inference.)

The normal daytime E layer has a critical frequency (f0E) of about 2 to 7 MHz, and the MUF for a 300km path will not reach higher than 14MHz. (This is for normal E layer; not to be confused with F layer foE and MUF.) On the other hand, the sporadic E layer can have MUF above 6m and sometimes 2m bands.

How about regular daytime F2 layer? The daytime critical frequency (f0F2) may be about 15 to 20 MHz in low latitude region. But F layers are about 300km high, so $\cos \theta \approx 0.9$ at a hop distance of 320km so MUF is only 10% higher than f0F2. Nowhere near 100 MHz. (Just FYI... at a hop distance of 600km, $\cos \theta=1/\sqrt{2}\approx0.71$ so MUF $\approx 1.41$ F0F2. At 3000km, MUF is about 5 times f0F2. So, it is sometimes possible to work 3000 km via F layer during day at 100 MHz, if all conditions line up, but never 300 km, due to the skip distance at 100 MHz being a very long distance.)

Regular E and F layers have electrons due to ionization of gas atoms/molecules due to energized particles and radiations from the sun. On the other hand, sporadic E layer accumulates electron density due to metal ions like Mg+, Fe+, Na+, Ca+, etc. (Notice singly charged ion in E-region environment. Additional ionization in Mg++, Fe++/+++ require a lot more energy (15-16eV) and that is not available... so the metal ions are usually singly charged.) Those ionized particles are concentrated in a laminar structure due to wind shear and the geomagnetic field.

So, emergence of sporadic E layer depends on stable, layered, neutral shear wind covering the area, on top of calm geomagnetic conditions. Those requirements make it "sporadic" or infrequent.

On the other hand, ducts require more simpler conditions and it makes it most likely mechanism in Florida, especially if the signal strength was not super strong relative to expected path loss.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23672/upper-frequency-limit-for-bouncing-off-ionosphere, by Randy, Ryuji AB1WX. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
