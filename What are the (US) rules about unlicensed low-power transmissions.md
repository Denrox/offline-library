# What are the (US) rules about unlicensed low-power transmissions?

*Tags: united-states, legal, rf-power · score 12*

## Question

It is common wisdom that transmissions of any sort (perhaps unidentified, encrypted, in the FM broadcast band, etc.) are permitted if they are sufficiently low power.

**Where are the FCC regulations which permit this**, or **where can I find a well-accepted interpretation of said rules?** People say they are in Part 15, but I read (well, skimmed) Part 15 and found mainly rules about offering equipment for commercial sale. I am specifically interested in permission for DIY or experimental transmitters and transmissions.

I am also interested in how these rules compare to those applying to devices transmitting in the “ISM” bands; is the latter equal or lesser in restriction?

(I am aware that while this question may be *amateur radio*, it is not about *the Amateur Radio Service*; I am asking it here in the hopes that it is a topic of sufficient interest to the community and that the relevant expertise is present.)

## Accepted answer (score 6, by Adam Davis)

### Overview

Title 47 Part 15 defines regulations which cover any device that

1. Radiates RF, whether intentionally, unintentionally, or incidentally
2. Doesn't require an *individual* license for operation

While a device might not require an individual license to be operated, it may still require FCC testing. This applies most strongly to devices made to be sold to others, which is why you see a lot of commercial references. Just because you are not commercializing your device, though, doesn't make you immune to the regulations affecting commercial devices. In fact the only difference between home built devices and commercial devices in this section is that home built devices are not subject to testing, verification, and declaration of conformity. They are otherwise subject to all the same rules.

### Regulation summary for home built, non-commercial, intentionally radiating devices

Here is a list of some (out of many) of the regulations you will have to follow whether your device is commercial or not. Your device must:

1. not cause harmful interference, and must accept any interference caused by other devices that follow the regulations they are subject to. (15.5.b)
2. be disabled upon notice from the FCC that the device is causing harmful interference. (15.5.c)
3. be designed and constructed in accordance with good engineering design and manufacturing practice. (15.15.a)
4. be designed so that any user-operable controls do not allow the device to operate outside the limits of these regulations (15.15.b)
5. be labeled correctly (15.19)
6. be built for personal use, not marketed, not constructed from a kit, and built in quantities of five or less (15.23.a, 15.201b)
7. not transmit more than spurious RF inside restricted bands detailed in 15.205.
8. not conduct emissions onto the AC line, if connected to the AC line, greater than the limits specified in 15.207.

### General RF field limits

For intentional radiators devices must not emit a field strength stronger than specified for the frequency ranges measured at the distance specified:

```
MHz            Field Strength (microvolts per meter)   Measurement distance(meters)
0.009 -   0.490     2400/F(kHz)                           300
0.490 -   1.705   24,000/F(kHz)                            30
1.705 -  30             30                                 30
 30   -  88            100                                  3
 88   - 216            150                                  3
216   - 960            200                                  3
960   -  ∞             500                                  3

```

Unless otherwise specified under Additional Provisions and elsewhere(15.211-15.2xx) any intentional radiator following all other regulations is not restricted to any specific mode, modulation, or transmission scheme. (15.215.a)

Note that most of these bands have additional provisions

## Answer (score 4, by K7AAY)

Page 15 of the FCC's OET63 specifies maximum emission of 100 µV/m measured three meters away, for consistent transmission in the US FM broadcast band, and 250 µV/m if you can keep the bandwidth down to 200KHz or less. That would permit Codec2, FreeDV, Olivia, PSK63, Pactor-I, RTTY, Q15X25 and many other digital modes.

Now, when you're talking about ISM, there are multiple bands available in the US and that link shows the frequencies and permitted bandwidth, which you can match up with the FCC table in the first line about for power limits. If, forex, you're talking about the 902-928 MHz band, you have **26 MHz** to play with and up to **1W** output power for spread-spectrum use, so the answer is a qualified YES, depending on *which* ISM band band you want to use.

Also, the Hobby Broadcaster website may be a useful resource for you as well.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1016/what-are-the-us-rules-about-unlicensed-low-power-transmissions, by Kevin Reid AG6YO, Adam Davis, K7AAY. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
