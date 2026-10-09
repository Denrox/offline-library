# Distance between antenna and radio

*Tags: antenna · score 5*

## Question

I live in a small cottage with an unlevelled terrain. My house was built in the lower part of it (left-side), and in the other half of it there is a hill. On top of the hill there's a fairly good plateau where I would like to have my antennas installed, since the place my house was built seems to be too low (my place is surrounded by hills).

On the top of this plateau, I can see very from a very big distance, and I'll bet that would be the perfect area for my antennas.

What I can't solve is the fact that my antennas would stay just too far apart from my house, where I plan to have my shack put together. There would be necessary a whole lot of cable to reach the antennas -never counted, but as a wild guess - about 350 feet.

The answer I can't seem to find here - and elsewhere - is how much is too much, when it comes down to setting an antenna apart from one's shack? I understand that in order to properly resonate, my entire system, i.e. radio + cable + antenna need to be in harmony and everything has to be thoroughly calculated.

To me it seems that's it's just too much cable and it will definitely affect my overall *transception* quality, if not entirely cripple the entire system.

What are your thoughts on the cable distance? Any workaround for that kind of problem if that is not an option?

I'm still to take some small QRP equipment and run some tests on the lower part of my cottage, to see if that's an option, should the whole placing the antenna on the topmost part option become void.

## Accepted answer (score 7, by Kevin Reid AG6YO)

This isn't nearly as big of an issue as you're thinking.

The answer I can't seem to find here - and elsewhere - is how much is too much, when it comes down to setting an antenna apart from one's shack?

The effect of a longer *feed line* between your transceiver and your antenna is increased *loss* — the signal will be weaker at the destination.


If you are transmitting, this means that less of the power from your final amplifier (whether built into your radio or external) reaches the antenna and radiates. Thus, the consequence of the loss is exactly the same as if your radio had less power output — not anything inherently bad.


If you are receiving, this means that less of the power gathered by your antenna arrives at your receiver. This is problematic if the signal is too weak for the *sensitivity* of your receiver (but that is unlikely for HF operation) or if you have sources of interference near your receiver that are stronger than the signal (this is something you can avoid).

The way loss in a transmission line works is that, at a given frequency, over a given length of the cable, a certain proportion of the energy will be lost (dissipated in heat or leaked out). Since this is a ratio, it is easily expressed in dB. For example, Times Microwave LMR-400 (a model of coaxial cable popular for high-end amateur use) specifies that at 30 MHz (the high frequency end of HF), there will be 0.7 dB of loss in 100 ft of cable.

In order to calculate loss for a particular length, you just multiply it (given that it's in dB).

$$0.7\,\text{dB} \cdot \frac{350\,\text{ft}}{100\,\text{ft}} = 2.45\,\text{dB}$$

So, with this cable you would have 2.45 dB of loss. **That's not bad at all** — compared to the average ham's setup, you'll be more than making up for it with your advantageous antenna location and height (assuming you put up a modest tower).

(If you were operating at higher frequencies — VHF or UHF range, say — cable loss becomes *much* more of a problem. But here, having a clear line of sight from your antenna makes even more of an improvement.)

You can also do better than coax, for HF operation. If you use *ladder line* (two plain wires separated by insulating spacers), you will get less loss at a lower price. The primary disadvantage of ladder line is that it will not work properly if there are nearby conductive objects, but that is not at all a problem for a long outdoor run in open air (not along the ground). It is also not suitable for higher frequencies as the spacing of the wires must be much smaller than the wavelength and consistent.

The above is assuming perfect SWR — that is to say, if you have an antenna that is built for the frequency band you are operating on. If you want to use many different bands with a single antenna, you will need an “antenna tuner”, and depending on the precise relationships there will be more loss in the section of feed line between the antenna and the tuner. You can reduce this problem by installing a remote-controlled/automatic tuner at the antenna end rather than at your transceiver.

I understand that in order to properly resonate, my entire system, i.e. radio + cable + antenna need to be in harmony and everything has to be thoroughly calculated.

This is false. There are badly-designed systems where every part influences the characteristics, but you should avoid that (and they would be nearly impossible to “thoroughly calculate” because you would need more information than you can practically gather and compute for the model). In a properly built system, the only shape and lengths that matter are those of the antenna itself (and its immediate surroundings — which is why you mount an antenna up high to avoid them).

## Answer (score 3, by rclocher3)

My answer builds upon @KevinReidAG6YO's fine answer. Let's assume that you're talking about HF frequencies, and that you do put the antennas on top of the hill (which is what I think you should do), and that you use LMR 400 coaxial cable with 2.45 dB loss at 30 MHz.

There are two situations to consider: receive and transmit. For receive, incoming signals will be attenuated, but the noise will be attenuated also. The signal-to-noise ratio, which is the most important measurement for receiving, will be the same. The gain in your receiver will easily make up for the lost 2.45 dB. So you will receive just as well as if your receiver were directly connected to the antenna.

Transmitting is different. When you transmit, some of your power is lost as heat to the coax, so your signal will be weaker for anyone listening. But how bad is the problem? Receivers have meters calibrated in S-units, and the traditional definition of an S-unit is 6 dB. So if your signal is 2.45 dB weaker than it would be if your transmitter were connected directly to the antenna, people listening will hear a signal 2.45 / 6 ≈ 0.4 S-units weaker than if your transmitter were connected directly to the antenna.

For most purposes, 0.4 S-units is so small a loss that it's not worth worrying about. If you did want to worry about it, you could solve the problem by increasing your output power.

Contesters and DXers would probably say that 2.45 dB is too much loss, but that is because they are already running the maximum legal power (or a bit more, ha ha), and the 2.45 dB will make enough of a difference that some far-away stations won't be able to hear the signal when propagation is difficult.

In fact I know a DXer who has his antennas at the top of the hill about 400 feet / 120 m from his house, and he uses cable-TV "hardline" coaxial cable about 3/4" / 2 cm in diameter to the top of the hill, in order to lower the loss. I understand that the loss of his coaxial cable at HF frequencies is about 1 dB. He has gone to quite a lot of expense and trouble to save himself about 1.5 dB in coaxial cable loss, but he likes to work stations halfway around the world that have very weak signals. If your goal isn't to work stations with very weak signals, then 350 feet of LMR-400 to the top of your hill should suit you very well for HF.

All these coaxial loss calculations assume that the SWR is close to 1:1. If the SWR is higher, then the loss increases very quickly. 2.45 dB might not be much loss, but if your SWR were 10:1, then the loss might be 20 dB. That kind of loss is a real problem. (If you had a 100 W transmitter and 20 dB of loss, then you would be radiating only 1 W.) For that reason, if you put the antennas on top of the hill you would do well to choose antennas that have SWRs close to 1 already, or use a remote antenna tuner that is close to the antenna, so that the SWR on the coax is close to 1:1. If the SWR on the coax is close to 1:1, then you won't need to worry at all whether your coax is a certain multiple of wavelengths at a certain frequency. (If you're curious about why that is, get a copy of the ARRL Antenna Book and read up on transmission lines and Smith charts.)

## Answer (score 2, by Jon Kåre Hellan LA4RT)

If you find the coax losses too high, you could try turning your station into a remote controlled station. A lot of hams do this. They install interfacing equipment at both ends, and control the station from their computer. Remoterig is one brand of interface, and I am sure there are many others. Some radio vendors also supply remote control heads, if you prefer a radio with knobs. You probably also want to control other equipment - antenna switches, antenna tuner, amplifier(?), etc, so check that the interface can handle that.

Strictly speaking, you do not need an IP connection to accomplish this. But I suspect it will be easier to find products which run over IP. In your case, it would be a local network run over wifi or wired Ethernet.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6659/distance-between-antenna-and-radio, by Former User of Mine, Kevin Reid AG6YO, rclocher3, Jon Kåre Hellan LA4RT. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
