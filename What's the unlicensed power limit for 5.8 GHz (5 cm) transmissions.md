# What's the unlicensed power limit for 5.8 GHz (5 cm) transmissions?

*Tags: united-states, fcc, shf · score 5*

## Question

5.8 GHz NTSC video transmitters are popular for FPV (first person view) model aircraft flying. However, because the 5.8 GHz band (5725 to 5875 MHz) is also available for ISM (unlicensed) use, it's not clear to me at what point I need a license to operate a transmitter of some given power. I've seen a table that says I can transmit up to 1 W (30 dBm) with a low-gain (6 dBi) antenna.

Isn't the ham power limit for 1.3 GHz and up 1 W anyways? What does having a ham license do in ISM bands?

For reference:

```
GHz :  5.650       5.725          5.850    5.875      5.925
ISM Band :                |<------ 100 MHz ------>|
ITU Region 1/3 :    |<------------------ 275 MHz ----------------->|
ITU Region   2 :    |<-------- 200 MHz ------->|

```

## Answer (score 5, by Scott Earle)

According to this site, the maximum allowed for non-licensed ("Part 15") equipment is 1W to the antenna, and the maximum EIRP is 4W.

For point-to-point links, the limit is higher, and the site mentions that on 5.8GHz the maximum allowed would be 53dBm EIRP (30dBm transmitted plus 23dBi gain of the antenna), which is 200W EIRP.

For licensed radio amateurs, I could not find any limit other than the 1,500W regular maximum power limit. Restrictions to transmitting as a 'radio ham' on the amateur bands that overlap with the ISM bands are those of the amateur radio licence. This includes the requirement to send an ident every 10 minutes and the end of the transmission in a mode that can be read by any radio amateur, if you transmit anything at all.

The FCC point us at this link for the latest Part 97 regulations (the regulations that govern amateur radio), and looking in there it states that 1,500W is the maximum unless otherwise stated, and there is no other statement indicating a lower power requirement for the higher bands, unless the operator holds a Novice licence.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5273/what-s-the-unlicensed-power-limit-for-5-8-ghz-5-cm-transmissions, by Nick T, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
