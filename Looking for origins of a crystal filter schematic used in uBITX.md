# Looking for origins of a crystal filter schematic used in uBITX

*Tags: diy, transceiver, electronics, filter · score 4*

## Question

Here is a crystal filter used in uBITX transceiver:

I've never seen such a topology in any other transceiver and decided to invest some time in exploring it. Turned out it's quite interesting. Eight crystals for any frequency from 11 to 12 Mhz and C217-C221 = 82 pF will give you a decent SSB filter with ~200 Ohm impedance and 2000-2300 Hz bandwidth depending on crystals. You can play with given crystals and capacitance value in LTspice to make the bandwidth more or less narrow. It also works with 9 MHz crystals if you change C217-C221 to 120 pF. The impedance in this case is still ~200 Ohm, the frequency response is fine.

I'm curious who invented this topology and/or in which publication it was first described and/or what software calculates filters like this one?

**UPD:** The documentation for uBITX states: "The ladder topology is now enhanced with the improvisation suggested by G3UUR. Paralleling up crystals at two ends of the regular ladder filter of Cohn topology really flattens out the response and even improves the losses." However from this text it's not quite clear if Dr. Dave Gordon-Smith, G3UUR invented this particular topology or maybe he suggested some other improvements in the schematic.

## Accepted answer (score 4, by Aleksander Alekseev - R2AUK)

After a little bit of searching I discovered that this topology is called **QER filter**, where QER stands for Quasi-EquiRipple. This topology is attributed to Dr. Dave Gordon-Smith, G3UUR, who is also well-known for inventing a popular method (the G3UUR method) of measuring crystals. Apparently it was first described in The QRP Quarterly, Spring 2010 under the title "Further Thoughts on Crystal Ladder Filter Design".

As a side note, it's most unfortunate that old issues of The QRP Quarterly don't seem to be available anywhere. I was hoping to read this article.

Links:

- http://ka7exm.net/emrfd/Messages/thread_10742.htm
- https://www.vk2sja.org/piffle/?p=254
- https://www.qrpforum.de/forum/index.php?thread/10139-literatur-zu-g3uurs-qer-quarzfilter-qrp-quarterly-u-arrl-handbook/
- The ARRL Handbook 2011, sections "11.6.2 Crystal Filter Design" and "11.11 Filter Projects"

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17851/looking-for-origins-of-a-crystal-filter-schematic-used-in-ubitx, by Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
