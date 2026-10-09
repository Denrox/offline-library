# RF Bridge Problem - K6BEZ Antenna Analyzer

*Tags: hf, diy, measurement, swr-meter · score 6*

## Question

This question regards erroneous SWR measurements of K6BEZ antenna analyzer (links gone from Internet now) design from 2013 using Arduino and AD9850 DDS modules. There have been many variations of it by other people over the years. Good details to make it work right seem hard to find. Here is my circuit for just the bridge section (the FWD and REV go out to the Arduino).

While testing it for SWR with resistors, it only reads correctly at 50 ohms. 100 ohms and 25 ohms both measure about 1.3 SWR and should be 2:1. I believe the problem is the way the bridge drives the op amps. The op amp circuit and onward work fine and calculate the SWR properly if I simulate the supposed bridge detector output using DC voltages. Although the 300mV DDS wave is rather low, the 1N5817 diodes have only 134mV forward voltage drop. Two helpful resources I used to check the bridge operation, were:

1.

Wideband SWR meter, using an identical bridge and analog meters (which I built), and

2.

[Adapting an Antenna Coupler](Adapting%20an%20antenna%20coupler.md).

Below are photos showing my wiring to mount the RF components as close together as possible.

Below is a graph of SWR on a 20-meter dipole. I monitored the Arduino on the PC serial COM port, capturing its text file output of the SWR at 100 frequency points between 4-30 MHz. Then I graphed the data in Excel.

The analyzer does seem to show something meaningful but but the valleys are too wide. The red line at 14.250 MHz is where I measured the lowest SWR (resonance?) using the Wideband SWR meter (mentioned above) and it was a sharp dip, unlike the graph from the Arduino analyzer.

Any **comments or suggestions** would be much appreciated.

## Answer (score 8, by Peter Buxton)

(See updated information further down)

I found an article to address the problems all in one place in **QST, September 2019**. The author addresses the same problems in the question, and explains his fixes for a similar bridge-circuit-based Arduino analyzer originally published in QST, November 2017. I realize I am a newcomer and many have already figured out fixes, but their information is so scattered, so the above article was great.

After days of searching and hitting dozens of dead links, I have dug up some meaningful and linkable documents on the history and evolution of AD9850 Antenna Analyzers. It has been very time-consuming, but educational to find and organize all these as bookmarks and I want to share what I found.

NJQRP DDS Daughtercard Kit, site last updated in 2005, is the earliest mention I've found of a DDS measuring project, although in their page they link to AARL publication - Original DDSVFO Article by Curtis Pruess WB2V, QEX 1997, which was a PIC/AD9850 VFO, essentially the same circuit as an analyzer but without the RF bridge. The daughtercard version, however, included an RF amplifier for the DDS, addressing the low output level even at that time.

DDS-60 Kit from the AmQRP is a current web page with a 2014 upgraded version of the same daughtercard, with history and lots of detail about the daughtercard evolution.

Related to the above daughter cards is WØPCE "Sweep Gen" - Automated DDS Sweep Generator Measurement System that had a dead link to original article by Sam Green, WØPCE (in QEX for Nov-Dec 2008) but which by searching I found mention of a version II in QEX September/October 2012.

I couldn't find mention of early DDS projects used for an antenna analyzer until 2013. The first one seems to be Beric Dunn's K6BEZ Antenna Analyzer. After that, many other analyzers seem to be offshoots of his, including some using the Si5351 DDS. Beric's version did not use an RF amplifier, which I believe is one key problem prompting me to post my question.

Another related project is The Poor Ham's Scalar Network Analyzer (PHSNA) by Nick Kennedy—WA5BDU from 2014. It uses DDS, and also an AD8307 log detector (which I've read can be used instead of the diodes as an improved detector in the bridge.)

In conclusion, a website with files originating from 2016, Antenna Analyzer for Ham Bands by Jack Purdum (W8TEE), Farrukh Zia (K2ZIA) is their project that they published in QST, November 2017. Lots of documentation here! This one uses a nearly identical bridge circuit that Beric's did, but includes an RF amplifier for the DDS. This seems to be the most sophisticated and documented source of all, especially with the mods and customizing mentioned in QST, September 2019.

**3/12/2020 Update**

It's disappointing to report that I can't make this project work accurately, when others claim to have made theirs work. I've tried every suggested modification that I've found: correcting DDS generator output filter impedance, add a MAR-65M MMIC to boost DDS output, tested with various diodes, germanium and Schottky, in the bridge and added in the op-amp feedback to correct below diode threshold voltage, etc. I've hand-matched the resistors and diodes use in the bridge. Below is the current schematic. Note: the FWD and REV outputs go to MCP6002 op-amps as in the schematic in the posted question.

I've made special code tests to check FWD and REV amplitudes coming from the bridge at individual frequencies (prior to the SWR calculation formula). The formula used in the code to calculate SWR is VSWR = (FWD + REV) / (FWD - REV). Below are four different test load results of the Arduino output on the COM port, graphed in Excel showing SWR with A/D units that go into the formula:

Each different load strangely has its own unique characteristic, but they are repeatably the same every time I test them. The red circles show the correct SWR and the A/D units calculate properly in the formula. All modifications I mentioned above don't change the basic patterns of SWR calculated for each resistor; they only affect the absolute RF levels involved, but the proportions stay basically the same going into the formula, thus the same SWR numbers coming out.

One thing I have noticed is that the high-frequency end of the RF sine wave has an average DC offset of about +50 mV after AC-coupling at the bridge, so that may indicate distortion, if that matters. Regardless of the wrong SWR readings, the resonant point of any dipole I've tried is detected and matches up with that of a NanoVNA and also an MFJ noise bridge. While researching on this site, I noticed in an answer of a somewhat related post, [Antenna tuning while receiving](Antenna%20tuning%20while%20receiving.md), that this type of bridge doesn't really measure SWR.

I've also considered that my breadboarded construction may cause errors, but I've seen worse on the Internet that claim to work, and besides, it isn't really that high a frequency spectrum I'm working with.

**Last update - 3/16/2020**

I suspected the metal film resistors causing a lot of problems at high frequencies, since I believe they are spiral-trimmed and therefore inductive. I made a whole new bridge using SMT resistors, capacitors, and Schottky diodes (BAT-54A). That made the measurements much more consistent and nearly level on the charts (and exactly level for 50 ohms).

Now, all parts are as close together as possible and in a logical layout and there is a grounded backplane. The resistors all measure exactly the same on my ohmmeter. The diodes are in a dual package, so probably closely matched. Also I made a section with SMT load resistors to use for tests, since my others were the metal film type. I used pin jumpers to switch between test loads and antenna.

So I got some positive results. Now, a 50 ohm resistor measures exactly 1.000 SWR from 1 MHz to 30 MHz. The single problem that still exists is that at 25, 100, and 150 ohms, the SWR is not what it should be. However it is close, and more important, they chart very close to one value from 1 MHz to 30 MHz. So 25 ohms measures 1.52 to 1.41 (should be 2.0), 100 ohms is 1.54 to 1.39 (should be 2.0), and 150 ohms is 2.27 to 2.02 (should be 3.0). I'm willing to live with that as long as 50 ohms is 1:1 as it is now. It is very much improved (less erratic) compared to the charts I posted above recently before switching to SMT.

I also left space on the PCB to add capacitors successively as a test. C1 and C2 attached to the diodes are 1 nF in the schematic. I wondered if that value was correct so I first tested the new PCB with those, then I added 10 nF, and finally, 100 nF in parallel and with any of those values, the results were essentially the same, so that answered my question on that.

To check one more area, I tested the FWD and REV op-amp sections with DC from 0 to +5V and both channels' outputs tracked the inputs within a few millivolts with a gain of 1 so it seems that isn't part of the problem. As I mentioned before, the code calculating the SWR from the FWD and REV is correct, so I can't think of any other reasons for the SWR readings being off. The analyzer works very well finding the SWR dip on antennas, so I think it's now working as well as I can make it work.

So my answer now is that SMT parts on a PCB are much better than the discreet parts I had tacked together for an RF bridge.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15626/rf-bridge-problem-k6bez-antenna-analyzer, by Peter Buxton. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
