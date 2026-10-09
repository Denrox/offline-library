# Can the external VFO input in a Heathkit SB-(100, 101, 102) be used to operate on frequencies outside the radio's normal range?

*Tags: hf, transceiver, modification · score 3*

## Question

I've got a Heathkit SB-102 that I'm working on making operational (problems with transmit, receiver works just fine). This model radio has a 9-pin Molex connector in the back, intended to connect an external auxiliary VFO.

By design, this feature is intended to support "split" operation -- listening on a different frequency from the transmit setting (much more different than the usual 1 KHz offset of the CW setting in this model family). It occurred to me to wonder, however, whether this external frequency input could be used to operate on bands outside the radio's normal complement of 80, 40, 20, 15, and 10m amateur bands. There are a number of other amateur bands available within this freuqency range (30m, for instance, as well as 17m and 12m) as well as bands outside this range that might be within the capability of the hardware (160m and 6m come to mind).

Is it possible to use the external VFO connector on an SB family radio to transmit and receive on amateur bands outside the 80-10m range, or unsupported bands within that range? Would it become possible if a bypass for the internal VFO (aka LMO) were installed, so the "primary" operation was controlled by the external VFO?

## Answer (score 4, by PeterH)

**My answer**

It looks to me like you could probably go further outside the limits of the band you're switched to by using an external VFO with a wider tuning range than the inbuilt LMO (5.0 to 5.5 MHz) but the pass-band tuned circuits will limit the amount you can do this by. I'm fairly sure the WARC bands would be too far away from the original fitted bands to work well or at all.

Off frequency tank circuits can result in unexpected out of spec anode currents or voltages, which can do damage or cause parasitic oscillations, etc. They will at least severely limit the desired signal.

To tune to the other ham bands you would have to add suitable tuned circuits and crystals to the band selector circuits rather than just use a different VFO frequency.

While this is not really difficult, it would require some careful adjustment of inductors and/or capacitors, and correct crystal frequencies to mix the 8.395 to 8.895 MHz signal into/from the desired band (in the 2nd Tx mixer / 1st Rx mixer).

You could probably pull the tuning of the nearest higher band down to the correct tuning for some bands (e.g. 20m setting to work on 30m) by adding suitable high quality caps and/or trimmer caps across the 4 tuned circuits (across C607, C704, C802, C923 for example) through a multi-pole switch when required, simultaneously switching to the appropriate crystal at Y503  
e.g. 18.6MHz xtal would put 10.1MHz operating frequency in the 8.395 to 8.895 pass band at 8.5MHz. The transceiver would certainly be capable of operating either side of the 10.1 to 10.15MHz ham band.

You could possibly use some of the 10m band switch positions for new bands if you don't need all 4. However looking at the circuitry and the wafers of the band selector switch it seems that this could not easily be done without changing the switch wafers a bit (or using relays perhaps?).

The tubes will probably all work ok up to 6m. The 6146 was commonly used as a final in VHF mobile "radiotelephones" fitted to fleet vehicles and operating through commercial repeaters.

**Obscurely related to the question** (but possibly interesting to some):

After reading the comments I feel it is probably ok to add some extra notes about my experience with valves (tubes). Stop reading here if you don't like anything not entirely related to the question.

I initially learnt about electronics as a child, when almost everything electronic used valves or relays. WW2 surplus equipment and old radio receivers were relatively plentiful and could be and were converted to work on ham bands, with a bit of DIY coil winding and tweaking and alignment. A grid dip meter helped. And some trial and error. Easy enough really and lots of fun.

Transistors were still rare, easily destroyed, expensive, mostly germanium, and rather mysterious things.  
By contrast you could still get useful activity out of a valve that you had seen a "flash-over" happen inside of, or had biased badly and had got the anode glowing red hot for a moment (both of which I have done while learning).

I could clearly picture the "electron cloud" around the cathode and the negative electric field around G1 repelling these electrons, preventing most of them from getting past. Once past. they are strongly attracted to the highly positive anode. As G1 becomes less negative, more and more electrons get past it so more anode current flows, which is then seen as voltage across the plate load. Everything fairly high impedance.  
And high voltages everywhere. (Seems you can survive a pretty big shock if it doesn't go past your heart...)

It took a while for me to even begin to understand how bipolar junction transistors actually work, with "electron carriers" and "holes" etc.  
Current at the base rather than voltage.

So looking at the circuit diagram of the SB102 is like going back in time to something that I was quite familiar with once.  
Several thoughts come to mind that I find useful in tracing and understanding valve circuits:

Valves are similar to FETs in operation. The extra grids in tetrodes, pentodes, etc. were added to decrease anode to G1 capacitance and improve linearity but can mostly be ignored when working out what's happening to the signal.  
There are exceptions to this so it's not always true e.g. SB102 V2 and V4 appear to be turned on/off by their G2 voltage.  
It was common to use some of the valves and circuitry in transceivers for both receive and transmit as seen in the 1st IF V3, and the bandpass filter T202, because valves cost a lot more than transistors in both space and (particularly heater) power drain. This can certainly appear to complicate the circuit, and can make understanding the signal path tricky.  
Valves can effectively be removed from the circuit (e.g. between Rx and Tx) by changing the G1 bias or G2 volts (e.g. V5A,V6,V7,V8,V9, or V2,V4).

Hope this helps.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15566/can-the-external-vfo-input-in-a-heathkit-sb-100-101-102-be-used-to-operate-on-, by Zeiss Ikon, PeterH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
