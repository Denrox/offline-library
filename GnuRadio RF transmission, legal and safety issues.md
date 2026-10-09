# GnuRadio RF transmission, legal and safety issues

*Tags: united-states, legal, frequency, gnuradio, usrp · score 6*

## Question

I'm trying to run some transmit/receive RF examples that I found online using GNU Radio with USRP B200. I read and heard about some cautions in terms of transmitted frequencies here in the USA which made me slow down! What is the legal frequency signals that I can transmit in the USA as a hobbyist or a student? Kind of, I felt lost while looking at the following USA Frequency Allocations Chart:

Assuming I know what is my ISM band allocation value, where I should input this value, I mean which block?

The other issue is the safety issue. I don't want to fry my tools, so how and where I should set the power? Again, which block I should be looking at?

Any hints, clues, or recommended resources would be highly appreciated.

## Answer (score 6, by user10489)

The frequency allocation chart is really more artistic than informative. You can not and should not use that as a guide for selecting a frequency. There is too much information to fit on the chart, and as much as is there anyway, it's not surprising you feel lost looking at it. (That may be part of the intention of the chart.)

There are multiple bands where unlicensed transmissions are allowed. These are covered in **Part 95** and **Part 15**. You can also build transmitters under **Part 97**, but this requires a license. You should read and understand the relevant sections before you start building a transmitter.

**Part 15** has a section covering low power transmitters in the ISM bands. You can select any ISM band, but you must follow the rules governing the specific bands. Generally, the maximum allowed power in these bands is low enough that you won't hurt anything or damage equipment. Several ISM bands have rules specifically allowing experimental use in controlled conditions.

**Part 95** covers FRS, CB, and similar bands. These allow higher power than Part 15, but also only allow transmitters that are type accepted. This excludes you building a radio (unless you are a manufacturer and are seeking FCC type acceptance) or modifying an existing radio. So while part 95 allows unlicensed transmission, it doesn't allow unlicensed radios.

**Part 97** covers amateur radio. You can build or modify radios for these frequencies and use significant power on those radios. However, you must have an amateur radio license to transmit. The license requires you to take a knowledge based exam. The exam covers safety of transmitters and safe RF radiation exposure limits, basic electronic knowledge needed to build radios and use them without damaging them, legal requirements for when, where, and what you are allowed to transmit and on what frequencies. As part of studying for the exam, you should read all of Part 97 as well as studying other material. When you do build a radio, it is your responsibility to make sure the radio functions properly, including checking its output on a spectrum analyzer to make sure it is not transmitting on unintended frequencies (and adding filters if it does). It is your responsibility to do an environmental study of your radio and antenna system to make sure RF radiation is safe for you and your neighbors. The amateur radio literature covers how to protect yourself and your radio while transmitting.

If you are intending on building radios, you should get an amateur radio license even if you only intend on transmitting in ISM bands, because the knowledge for the license will help you significantly, and if you are learning to build radios, you already have a good start on learning that material.

If you are building a radio in GNU Radio, you have to realize that SDR radios typically emit lots of unintended parasitic frequencies. To legally transmit with one (even under part 15), you **must** add hardware filters at the radio output to attenuate these extra frequencies. The filters must be specific to the band you are intending to use. Some SDRs may have band filters built into them already, but most don't.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14863/gnuradio-rf-transmission-legal-and-safety-issues, by Hadad, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
