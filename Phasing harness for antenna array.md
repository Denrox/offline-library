# Phasing harness for antenna array

*Tags: antenna, feed-line, phased-array, antenna-system · score 10*

## Question

I understand that certain antenna designs (particularly phased arrays) require feeding each radiating element with a certain number of degrees of phase separation in order to achieve a desired radiation pattern or beamwidth.

I found this 2-meter phased array [pdf] article which goes fairly in-depth into the design and theory but glances over the exact details involved in computing the coax lengths for the phasing harness:

The antenna design in the article proposes using a T-connector with a 22" length of coax going to one antenna and a 16" length of coax going to the other antenna to (supposedly) achieve 135-degrees of phase separation.

So my question is... is there a general method or formula for computing these phasing line lengths? (Are the values shown in the article even correct?)

## Answer (score 4, by Adam Davis)

There is, but it depends on the characteristics of the cable and the frequency of interest. There are online calculators that can do the work for you. For instance the two lengths of your cable have the following attenuation (almost none for RG-58) and phase delay. The phase delay is noticeably different, but as I haven't evaluated the antenna design I don't know if it's correct.

The calculator: http://www.mogami.com/e/cad/coax-freq.html

Phase delay and attenuation for the 16" section:

http://www.mogami.com/cgi-bin/uncgi.cgi/cad/coax-freq.cgi?Opt1=Linear&Opt2=yes&Start=144&Stop=148&Len=.4064&Rs=0&Cs=0&Rr=0&Cr=0&Name=RG-58%2FU

Phase delay and attenuation for the 22" section:

http://www.mogami.com/cgi-bin/uncgi.cgi/cad/coax-freq.cgi?Opt1=Linear&Opt2=yes&Start=144&Stop=148&Len=.5588&Rs=0&Cs=0&Rr=0&Cr=0&Name=RG-58%2FU

There is a reasonably comprehensive document that covers the calculations necessary for this here:

http://ve2azx.net/technical/CoaxialCableDelay.pdf

This should give you more exact numbers if you need a particular solution.

## Answer (score 2, by Lonney)

The Christman feed system using 84 and 71 degree lines is an example in ON4UN's Low Band DXing book where 1/4 wave ground mounted verticals are used. The line lengths are calculated from feed line impedance and driving impedance of each antenna in the array.

If the antenna configuration is changed so does the driving impedance, and the phase shift will no longer be 90 degrees. As a result the pattern degrades with a loss of front to back ratio and reduced forward gain. I explored this recently with EZNEC models in Phased Arrays - Christman Feed System.

I'm not aware of a convenient calculator for the Christman feed system. However Roy Lewallen W7EL has a similar feed system called current forcing and wrote an application called Arrayfeed1 that will calculate the line lengths if you know the driving impedances. This you can find by modeling the antenna system EZNEC with two sources then look at the Source Data for the values to plug into Arrayfeed1. You can then use the transmission lines function with the calculated line lengths in EZNEC to see that it works. I worked through an exercise in doing this here Phased Arrays - Lewallen's Simple Feed.

Lastly when building you need to use an antenna analyzer to measure the VF of the coax you have and use that figure in the calculations, the VF can vary between manufactures and manufacturing runs compared to the published VF.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/256/phasing-harness-for-antenna-array, by Craig, Adam Davis, Lonney. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
