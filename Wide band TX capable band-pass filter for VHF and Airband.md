# Wide band TX capable band-pass filter for VHF and Airband

*Tags: vhf, rfi, filter, airband · score 5*

## Question

I want to share the same antenna for VHF (TX/RX 144-148 MHz) and for Airband RX-only (116-136 MHz).

I live on a very congested area where filter is a must, so I'm looking for the best solution for my needs:

- Wide bandwidth (~30 MHz)
- Transmit capable (> 20W power handle with low return loss/SWR)

Currently I use a DIY helical filter for TX and a low-power LC filter for airband, but switching them everytime is very combersome. I like the high "Q" of the helical filter, but its bandwidth is very limited (~5 MHz) and I believe they cant be streteched to cover such bandwidth.

My primary source of interference are strong FM stations in the neighborhood, so I need a high Q, sharp filter with a good degree of attenuation between 108 and 116 MHz.

Any advice in the best filter design? My simulations shows a LC band-pass filter (Butterworth/Chebyshev) would meet my "sharpness" requirements, but they tend to have high return loss (SWR) as well, which could compromise my TX requiriments.

I have some soldering skills and a NanoVNA, tuning the helical filter wasn't a big deal.

**Edit**

I finally had time to build a LC filter, looks like it's still the best option to go.

First attempt was building a band-pass filter, but it showed to by tricky to tune. Then I went by a highpass + lowpass 5th-order Elliptic as calculated by https://rf-tools.com/lc-filter/. to allow individual tuning.

The results can be seen on thes imgur post: https://i.sstatic.net/IbhgP.jpg

The overall results are:

- -11dB on 110Mhz (very important to attenuate strong FM station on 107Mhz)
- -40dB on FM band
- 1,5dB insertion loss beteen 117-150Mhz
- SWR < 1:1,5 between 130-150Mhz

Since I had no high voltage variable capacitors in hand, I had to find the correct capacitor values using low voltage ones, then replacing by fixed value 1KV ceramic capacitor. As you might imagine that was a very time consuming exercise. The good thing is that there is no moving parts on the filter.

Sharpness on the lower end is good. On the upper side I didn't push too much the sharpness, since looks like there is a tradeoff between sharpness and return loss. I wanted good SWR and the upper band is not a big source of interference, so a left it a bit soft.

Results are very good. Identical noise compared to a commercial airband filter I had in hand, but extended to 150Mhz. Completely blank airband spectrum, no sign of FM stations spurs.

I wont post schematic or component values because this is a trial and error process. If you want to build something like this, you must have a VNA. Take the values calculated by rf-tools.com as a starting point then tweak to suit your needs.

## Answer (score 2, by glen_geek)

The basic idea is a high-pass filter to separate FM broadcast from Aircraft band. You need quite a wide passband, including aircraft, up to top of 2M ham band. So start with a 5-element high pass of the form:  
  
Then add some traps to take out more of the FM broadcast band, without impacting the passband. Somewhat Chebyshev-like. If you've got some tools like VNA, it can be hand-tweaked. I did the tweaking in LTSPICE, but probably gave up too soon:

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15936/wide-band-tx-capable-band-pass-filter-for-vhf-and-airband, by Aldoir, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
