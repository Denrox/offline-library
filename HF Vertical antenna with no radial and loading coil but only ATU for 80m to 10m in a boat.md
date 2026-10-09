# HF Vertical antenna with no radial and loading coil but only ATU for 80m to 10m in a boat

*Tags: antenna, hf, vertical-antenna, antenna-tuner, radial · score 3*

## Question

I am new to HF antenna designs. I want to build an antenna for my fishing boat. My question is - if I use an ATU (like the ATU-100) and a 10m aluminium pipe as an antenna and fix it with a mast, will that work to transmit and receive in multiple bands from 80-10 metres?

I see people use radials and caps and loading coils. I can't use radials in a boat. A loading coil is possible. But If i have an ATU is a loading coil necessary?

Also I saw vertical antennas that use different diameter pipes where the diameter decreases as the height increases. Those antenna use ATU. What is the reason for that and should I do it?

If I build a vertical antenna for the 80m band with 10m height and with radials and loading coils for my garden will that work ok on the 40m and 20m bands? Considering if I don't adjust the loading coil ratio?

What should I be considering when setting up an 80-10m antenna in a boat?

## Accepted answer (score 7, by tomnexus)

On boats the traditional solution is to use the backstay as the radiator, with an insulator near the top, another near the bottom, and an insulated wire running to the tuner. The water serves as the ground. No radials are required. With the tall mast and the conductive seawater you will have quite an efficient antenna. There is lots of information about this on the Internet if you look around.

**For the whip antenna:**  
For power boats without a tall mast you will need to install a vertical whip antenna. There are formidible mechanical engineering challenges to making a long vertical mast, especially on small boats. Guying will help a lot. Making the tip very light will also help, perhaps using a 108" whip to reduce wind resistance there.

A freestanding whip is usually done as a fibreglass tube with wire inside it, as this is strong and light and allows a smooth taper. Metal will certainly work if you can manage the fatigue and corrosion issues.

See for example this 10 m tall antenna from Comrod, 22 kg, which mounts on 6 M12 bolts and deflects 5 metres at the tip in 55 m/s wind. Or this 29 foot metal antenna from Valcom. The key here is that they are quite flexible so aren't so easily damaged by boat pitching and strong wind. They also may include lead shot dampers inside to reduce resonances from engine vibrations.  
There is no electrical benefit to tapering the antenna, in fact a fat cylinder is slightly better as an antenna, but the mechanical considerations are more important.

**For ground** you can connect to any metal part that is exposed to the sea water - perhaps your anode, rudder parts or any underwater hull penetration. It should ideally be fairly close to the mounting point of the antenna.

**Now about the ATU:**  
You will definitely need an antenna tuner to use the whip over 80-10m. It should be mounted near the ground, with the live wire running up to the antenna well away from other metal objects.

Not all tuners will work at 3.5 MHz on this short whip. Tuners have a maximum inductance, and this limits their low frequency operation with short antennas, which need a lot of inductance to match.  
The ATU-100 has 8.5 uH of inductance, at 3.5 MHz this is only j180 ohms, but a 10 metre monopole has a reactance of about -300 ohms. So the ATU-100 cannot tune a 10 metre whip at 3.5 MHz, it will stop working below about 4.2 MHz. For this length whip, you need to look for a tuner that has a maximum inductance of at least 14 uH. The SGC-237 and SGC-230 have this much. The Icom AH-4 says "3.5 MHz to 54 MHz (with a long wire antenna, 7 m; 23 ft or longer)" so it will work.

As an aside, to counter the rumours of "my ATU tunes my 108" whip fine from 1.8-30" I can tell you about the SGC-235 which is rated for 500 W (PEP), but specifies a minimum antenna length of 50 feet at 3.3 MHz and 300 feet at 1.8 MHz. I used it with a 5 metre whip antenna and found that it would sometimes find a tuning solution at 1.8 MHz, but it was deliberately adding some capacitance to the output, which massively reduced its efficiency (so it looked matched). The solution was unstable and it would start hunting again as soon as the coils warmed up a bit. On a boat there is much less ground loss to smooth over the difficulty of tuning the whip. So it is important to operate the ATU within its specified antenna length.

**No loading coil is necessary** if you have the right ATU, and it will almost certainly make the antenna more difficult to match. The problem is that an inductor big enough to make a difference to the impedance down at 3.5 MHz (say 8 uH) will be far too big at 30 MHz. If you are willing to switch the coil in and out manually for 80 m, it might help you use a smaller tuner.

A final note about tuners is that they almost all overstate their power handling capability. At low frequencies the antenna radiation resistance is low and a lot of of the power is dissipated in the tuner. They will assume a very low duty cycle. 100 W PEP means 50 W average while you are speaking, 25 W if you leave gaps between your words, and 10 W if you take turns. A 100-watt rated tuner can realistically dissipate an average of 10 W in its coils, but not the whole 100 W. They will work for normal SSB conversation, but don't plan to use them for long overs at 100 W on FT8 or PSK31. I've seen a continuous kilowatt-rated tuner, it was a 18" metal cube with large fans inside and outside to cool the coils. Apparently it still burned out regularly.

Please watch out for power lines with your new tall antenna. I knew a sailor that was killed when his mast touched a power line, it had drooped close to the water for some reason.

## Answer (score 2, by Richard Fry)

RE: ***What should I be considering when setting up an 80-10m antenna in a boat?***

In addition to the ones already posted here earlier by tomnexus, it may be wise to consider the fields that can be present around the relatively small area of a typical small, sea-going boat with a transmit system in use.

E-M fields can be very high near a radiating antenna. They may be a health issue, and/or affect the operation of nearby electrical devices.

The graphic below is a illustration of this, for the conditions stated there.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21450/hf-vertical-antenna-with-no-radial-and-loading-coil-but-only-atu-for-80m-to-10, by Asif Rahman, tomnexus, Richard Fry. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
