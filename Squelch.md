# Squelch

In telecommunications, **squelch** is a circuit function that acts to suppress the audio (or video) output of a receiver in the absence of a strong input signal. Essentially, squelch is a specialized type of noise gate designed to suppress weak signals. Squelch is used in [two-way radios](Two-way%20radio.md) and VHF/UHF [radio scanners](Radio%20scanner.md) to eliminate the sound of noise when the radio is not receiving a desired transmission.

### Squelch

In some designs, the squelch threshold is preset. For example, television squelch settings are usually preset. Receivers in base stations, or [repeaters](Repeater.md) at remote mountain top sites, are usually not adjustable remotely from the control point.

In [two-way radios](Two-way%20radio.md) (also known as radiotelephones), the received signal level required to unsquelch (unmute) the receiver may be fixed or adjustable with a knob or a sequence of button presses. Typically the operator will adjust the control until noise is heard, and then adjust in the opposite direction until the noise is squelched. At this point, a weak signal will unsquelch the receiver and be heard by the operator. Further adjustment will increase the level of signal required to unsquelch the receiver. Some applications have the receiver tied to other equipment that uses the audio muting control voltage, as a "signal present" indication; for example, in a [repeater](Repeater.md) the act of the receiver unmuting will switch on the transmitter. Squelch can be *opened* (turned off), which allows all signals to be heard, including radio frequency noise on the receiving frequency. This can be useful when trying to hear distant or otherwise weak signals, for example in DXing.

**Carrier squelch** is the most simple variant of all. It functions strictly on the signal strength, such as when a television mutes the audio or blanks the video on "empty" channels, or when a [walkie-talkie](Walkie-talkie.md) mutes the audio when no signal is present. Carrier squelch uses receiver Automatic gain control (AGC) to determine the squelch threshold. [Single-sideband modulation](Single-sideband%20modulation.md) (SSB) typically uses carrier squelch.

**Noise squelch** is more reliable than carrier squelch. A noise squelch circuit is noise-operated and can be used in AM or FM receivers, and relies on the receiver quieting in the presence of an AM or FM carrier. To minimize the effects of voice audio on squelch operation, the audio from the receiver's detector is passed through a high-pass filter, typically passing 4,000 Hz (4kHz) and above, leaving only high frequency noise. The squelch control adjusts the gain of an amplifier which varies the level of the noise coming out of the filter.

This noise is rectified, producing a DC voltage when noise is present. The presence of continuous noise on an idle channel creates a DC voltage which turns the receiver audio off. When a signal with little or no noise is received, the noise-derived voltage is reduced and the receiver audio is unmuted.

Noise squelch can be defeated by intermodulation present in the high-pass band. For this reason, many receivers with noise squelch will also use a carrier squelch set at a higher threshold than the noise squelch.

### Tone squelch and selective calling

Tone squelch, or another form of selective calling, is sometimes used to solve interference problems. Where more than one user is on the same channel (*co-channel* users), selective calling addresses a subset of all receivers. Instead of turning on the receiver audio for any signal, the audio turns on only in the presence of the correct selective calling code. This is akin to the use of a lock on a door. A carrier squelch is unlocked and will let any signal in. Selective calling locks out all signals except ones with the correct key to the lock (the correct code).

In non-critical uses, selective calling can also be used to hide the presence of interfering signals such as receiver-produced intermodulation. Receivers with poor specifications—such as inexpensive police scanners or low-cost mobile radios—cannot reject the strong signals present in urban environments. The interference will still be present, and will still degrade system performance, but by using selective calling the user will not have to hear the noises produced by receiving the interference.

Four different techniques are commonly used. Selective calling can be regarded as a form of in-band signaling.

#### CTCSS

CTCSS (Continuous Tone-Coded Squelch System) continuously superimposes any one of about 50 low-pitch audio tones on the transmitted signal, ranging from 67 to 254 Hz. The original tone set was 10, then 32 tones, and has been expanded even further over the years. CTCSS is often called *PL tone* (for *Private Line*, a trademark of Motorola), or simply *tone squelch*. General Electric's implementation of CTCSS is called *Channel Guard* (or *CG*). RCA Corporation used the name *Quiet Channel*, or *QC*. There are many other company-specific names used by radio vendors to describe compatible options. Any CTCSS system that has compatible tones is interchangeable. Old and new radios with CTCSS and radios across manufacturers are compatible. For those PMR446 radios with 38 codes, the codes 0 to 38 are CTCSS Tones:

- **PMR446 CTCSS Privacy Codes**
- **NumberTone HzNumberTone HzNumberTone Hz**
- **0**   Off   **13**    103.5   **26**    162.2
- **1**    67.0   **14**    107.2   **27**    167.9
- **2**    71.9   **15**    110.9   **28**    173.8
- **3**    74.4   **16**    114.8   **29**    179.9
- **4**    77.0   **17**    118.8   **30**    186.2
- **5**    79.7   **18**    123.0   **31**    192.8
- **6**    82.5   **19**    127.3   **32**    203.5
- **7**    85.4   **20**    131.8   **33**    210.7
- **8**    88.5   **21**    136.5   **34**    218.1
- **9**    91.5   **22**    141.3   **35**    225.7
- **10**    94.8   **23**    146.2   **36**    233.6
- **11**    97.4   **24**    151.4   **37**    241.8
- **12**    100.0   **25**    156.7   **38**    250.3

#### SelCall

Selcall (Selective Calling) transmits a burst of up to five in-band audio tones at the beginning of each transmission. This feature (sometimes called "tone burst") is common in European systems. Early systems used one tone (commonly called "Tone Burst"). Several tones were used, the most common being 1,750 Hz, which is still used in European amateur radio repeater systems. The addressing scheme provided by one tone was not enough, so a two-tone system was devised—one tone followed by a second tone (sometimes called a "1+1" system). Motorola later marketed a system called "Quik-Call" that used two simultaneous tones followed by two more simultaneous tones (sometimes called a "2+2" system) that was heavily used by fire department dispatch systems in the US. Later selective call systems used paging system technology that made use of a burst of five sequential tones.

#### DCS

Standard DCS Codes
- *0nn*  *1nn*  *2nn*  *3nn*  *4nn*  *5nn*  *6nn*  *7nn*
- 023  114  205  306  411  503  606  703
- 025  115  223  311  412  506  612  712
- 026  116  226  315  413  516  624  723
- 031  125  243  331  423  532  627  731
- 032  131  244  343  431  546  631  732
- 043  132  245  346  432  565  632  734
- 047  134  251  351  445    654  743
- 051  143  261  364  464    662  754
- 054  152  263  365  465    664
- 065  155  265  371  466
- 071  156  271
- 072  162
- 073  165
- 074  172
- 174

DCS (Digital-Coded Squelch), generically known as *CDCSS* (Continuous Digital-Coded Squelch System), was designed as the digital replacement for CTCSS. In the same way that a single CTCSS tone would be used on an entire group of radios, the same DCS code is used in a group of radios. DCS is also referred to as *Digital Private Line* (or *DPL*), another trademark of Motorola, and likewise, General Electric's implementation of DCS is referred to as *Digital Channel Guard* (or *DCG*). Despite the fact that it is not a tone, DCS is also called *DTCS* (Digital Tone Code Squelch) by [Icom](Icom%20Incorporated.md), and other names by other manufacturers. Radios with DCS options are generally compatible, provided the radio's encoder-decoder will use the same code as radios in the existing system.

DCS adds a 134.4 bit/s (sub-audible) bitstream to the transmitted audio. The code word is a 23-bit Golay (23,12) code which has the ability to detect and correct errors of 3 or fewer bits. The word consists of 12 data bits followed by 11 check bits. The last 3 data bits are a fixed '001', this leaves 9 code bits (512 possibilities) which are conventionally represented as a 3-digit octal number. Note that the first bit transmitted is the LSB, so the code is "backwards" from the transmitted bit order. Only 83 of the 512 possible codes are available, to prevent falsing due to alignment collisions.

DCS codes are standardized by the Telecommunications Industry Association with the following 83 codes being found in their most recent standard, however, some systems use non-standard codes. For those PMR446 radios with 121 codes, the codes 39 to 121 are DCS codes:

**DCS**
- **NumberDCS CodeNumberDCS CodeNumberDCS Code**
- **39**   023   **67**   174   **95**   445
- **40**   025   **68**   205   **96**   464
- **41**   026   **69**   223   **97**   465
- **42**   031   **70**   226   **98**   466
- **43**   032   **71**   243   **99**   503
- **44**   043   **72**   244   **100**   506
- **45**   047   **73**   245   **101**   516
- **46**   051   **74**   251   **102**   532
- **47**   054   **75**   261   **103**   546
- **48**   065   **76**   263   **104**   565
- **49**   071   **77**   265   **105**   606
- **50**   072   **78**   271   **106**   612
- **51**   073   **79**   306   **107**   624
- **52**   074   **80**   311   **108**   627
- **53**   114   **81**   315   **109**   631
- **54**   115   **82**   331   **110**   632
- **55**   116   **83**   343   **111**   654
- **56**   125   **84**   346   **112**   662
- **57**   131   **85**   351   **113**   664
- **58**   132   **86**   364   **114**   703
- **59**   134   **87**   365   **115**   712
- **60**   143   **88**   371   **116**   723
- **61**   152   **89**   411   **117**   731
- **62**   155   **90**   412   **118**   732
- **63**   156   **91**   413   **119**   734
- **64**   162   **92**   423   **120**   743
- **65**   165   **93**   431   **121**   754
- **66**   172   **94**   432

#### XTCSS

XTCSS is the newest signalling technique, and provides 99 codes with the added advantage of "silent operation". XTCSS-fitted radios are purposed to enjoy more privacy and flexibility of operation. XTCSS is implemented as a combination of CTCSS and in-band signalling.

### Uses

Squelch was invented first and is still in wide use in two-way radio. Squelch of any kind is used to indicate loss of signal, which is used to keep commercial and [amateur radio repeaters](Amateur%20radio%20repeater.md) from continually transmitting. Since a carrier squelch receiver cannot tell a valid carrier from a spurious signal (noise, etc.), CTCSS is often used as well, as it avoids false keyups. Use of CTCSS is especially helpful on congested frequencies or on frequency bands prone to skip and during band openings.

Professional wireless microphones use squelch to avoid reproducing noise when the receiver does not receive enough signal from the microphone. Most professional models have adjustable squelch, usually set with front-panel control on the receiver.

---

*Source: Wikipedia, Squelch (https://en.wikipedia.org/wiki/Squelch), by Wikipedia contributors, CC BY-SA 4.0.*
