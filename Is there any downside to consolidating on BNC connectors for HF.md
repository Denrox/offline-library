# Is there any downside to consolidating on BNC connectors for HF?

*Tags: antenna, connectors · score 7*

## Question

I'm new to ham and quickly finding that the new and old equipment I'm accumulating at an alarming rate has an equally alarming array of connectors:

- UHF PL-259
- BNC
- SMA
- Type N

Is there any downside to consolidating on BNC as my main connector and getting adapters to go from the other 3 types to BNC? My main use purposes are: SDR, QRP on HF (including SOTA), UHF/VHF FM and DMR. I doubt I'll ever set up a full power HF base station.

## Answer (score 6, by Marcus Müller)

## PL-259

I'd really stay the hell away from PL-259. Undefined wave impedance, different manufacturer conventions, adapter stock of either decades of unknown storage (potentially in some moldy military box) or cheapest-supplier production are the main sources… It's a good thing that connector is becoming less common. It's something that you really don't want to deal with above ca 30 MHz.

## connector comparison

As long as all your cabling/connector systems use the same impedance, why not. BNC is a cheap and robust connector.

It certainly isn't known to make the highest-quality connections when compared to SMA or Type-N; however, as said, it's mechanically usually less flimsy then SMA connectors, and you need none of the higher frequency range you can reach with SMA.

There's good things to be said about Type-N: It's what's typical for measurement equipment, and many low- to medium-power mobile basestation systems use it. It's a very reliable connector, it makes connections that are typically more resilient to humidity and vibration, it's mechanically more exact and thus lower in reflections.

You buy these advantages with increased cost and complicated unscrewing and screwing.

Clearly, I'd prefer Type-N at the output of a 100W amplifier. For my receiver, I frankly wouldn't care if we're actually talking about HF.

Of all the acceptable connectors, BNC is definitely the one having the lowest frequency range. So, if you later decide you're into UHF/microwave, bad news, you need to switch back to SMA or Type-N.

That being said, this is all about *what you'd typically expect* when buying connectors of these types. Amphenol RF sells BNC connectors that are specified to work with 0.2 dB insertion loss and -55 dB leakage at up to 3 GHz. But you'd pay more for one of these than for your average Type-N. At the same time, there's cheap crummy Type-N connectors that simply don't mate well and have loose mechanical dimensioning, so that their property is well below what you'd see in medium quality BNC installations.

After all, this boils down to: Get the datasheet or a feeling for the quality/precision for what you're buying. Compare your most likely solutions for insertion loss and leakage – and compare that to what your application needs. Got a 2 W PA? Well, nevermind those 0.7 dB insertion loss – they won't hurt anyone, but you lose a few milliwatt in power. Got 2 kW? Maybe you want to know how much energy is converted to heat or reflected back at your ampl.

## conclusion

If you want to keep the option for higher frequencies, don't need much power / voltage capability, go for SMA. It's medium-priced.

If you want the most reliable connections or need to handle much power, go for Type-N. (attention: 50 Ω and 75 Ω variants exist!)

As a compromise up to 4 GHz, BNC is nice and cheap. Watch out – BNC exists in 75 Ω and 50 Ω versions. Don't buy anything where you don't know which one of these you get. Note that the 50Ω cabling ones go higher in frequency, and as a rule of thumb, price, quality and whether you want to do UHF/VHF with them are correlated.

## Answer (score 4, by Walter Underwood K6WRU)

I avoid UHF connectors as much as possible. My shack is all Type N outdoors (weatherproof) and all BNC indoors.

UHF connectors work fine for HF and even above that. But I hate connectors where you have to wiggle and retighten, then they still leak. Just a poor design.

I've never seen UHF connectors on current professional broadcast gear.

UHF connectors don't have a "real spec" because the military and commercial gear doesn't use them. The best we have is the Amphenol spec, but that only covers Amphenol connectors.

Check the specs for each type. You'll notice that the specs for Type N and BNC are much longer, because they have specs for things like contact resistance. Also, note the peak voltage ratings. UHF is 500 V, BNC is 500 V, Type N is 1500 V.

UHF: https://www.amphenolrf.com/connectors/uhf.html  
BNC: https://www.amphenolrf.com/connectors/bnc.html  
Type N: https://www.amphenolrf.com/connectors/n-type.html

Finally, Oak Hills Research makes a BNC panel socket that fits in a UHF panel hole. Very handy. I used that to build the Oak Hills dummy load kit with a BNC connector. The connector is on their parts page: http://www.ohr.com/parts.htm

## Answer (score 2, by sm5bsz)

Connectors do cause a lot of problems. Avoid them as much as you can outdoors. Use a soldering iron to make permanent connections where you do not need to connect and disconnect. (Antenna stacking cables for example.) Outdoors waterproofing is essential. When I do T connections or connect a 70 ohm cable to a 50 ohm one for impedance transformation after a T I first solder thin copper foil to make a continous screen. I keep a reasonable distance with teflon insulators to keep the impedance right. (trivial up to about 500 MHz.) Then, with epoxy and wowen glassfibre I make the connection mechanically strong and to some extent water tight. Then, very important, I use self vulcanizing tape to cover the joint as well as a couple of cm of the outer jacket of the cables. This provides perfect water proofing. Finally it is necessary to protect the self vulcanizing tape with PVC tape. Make it at least 3 layers if you want more than 10 years lifetime.

For indoor usage, BNC is excellent. You have to be aware of two problems however. Firstly there are computer grade BNC connectors.. They are TOTALLY USELESS for radio. The screen does not connect properly. You would get intermodulation and poor isolation from local noise.

The standard BNC connectors for radio as well as the N connectors have a too low contact pressure for the screen. This results in pick-up of local interference (computer switch power etc.) as well as in intermodulation. I have shown this in a couple of videos and Internet pages: http://sm5bsz.com/lir/nfprec/nfprec.htm Look under the header "connectors." In this video you can see something about IM3 produced in connectors: https://www.youtube.com/watch?v=Cy7mbpvBwsg

You can mate a N male with a BNC female, BUT DO NEVER DO THAT!! The diameter of the N center pin is larger and you might bent the center connector of the BNC for a too low contact pressure.

SMA connectors are critical. Must be mounted correctly and cleaned properly http://www.sm5bsz.com/lir/loss/1296/cleaning/propanol.htm Just using them without cleaning can cause all sorts of problems. I do not remember where, but i think problems have occured in one of my videos.

Conclusion:

BNC is fine. N-connectors behave exactly like BNC with respect to contact pressure. UHF connectors are excellent on frequencies below 200 MHz. Beware that some of them come with poor dielectric. You need teflon or the most common brown material which I do not know exactly what it is. There are UHF connectors with  
plexiglass (acryl) dielectric and also PVC. They are VERY lossy. The UHF connectors provide a better connection than BNC or N because of the much larger contact area. Use adjustable pliers to tighten firmly. Make sure that the UHF connector is rotated into the correct position.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10431/is-there-any-downside-to-consolidating-on-bnc-connectors-for-hf, by RoboKaren, Marcus Müller, Walter Underwood K6WRU, sm5bsz. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
