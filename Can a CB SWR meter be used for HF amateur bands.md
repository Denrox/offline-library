# Can a CB SWR meter be used for HF amateur bands?

*Tags: antenna, swr-meter · score 4*

## Question

I have a basic CB SWR meter, I can’t see any reason why it can’t be used on other HF bands and be at least indicative of what the SWR is, even if the absolute power measurement is inaccurate. Is this a correct assumption? I also assume that the meter might be useable up to 10m and possible 6m but above that it would introduce problems - too much loss, for example. Is this also correct?

## Accepted answer (score 5, by Glenn W9IQ)

Many hams have re-purposed CB SWR meters but there are so many variations that some caution and testing is warranted.

Many CB meters were not designed to handle the higher power levels of amateur transceivers. A 100 watt transmitter could cause component failures within the meter. While the most likely result is simply the failure of the meter, I wouldn't rule out the possibility of it causing a short across, or open of, the transmission line. Remember that these meters were designed for an unsophisticated, and at times cost sensitive, market. The engineering can be dubious. With that being said, many meters have been used successfully at 100 watts - perhaps due to the SWR meter manufacturer recognizing the propensity for rule breaking power levels deployed on this band.

You can test the SWR accuracy on various bands using lower power and a 50 ohm dummy load - it should show a 1:1 SWR. Then parallel another 50 ohm dummy load (borrow it from a friend or club if you do not have a second one) by using a coaxial tee connector and repeat the SWR test. This time it should show a 2:1 SWR. These tests will give you an indication on which bands the calibration is adequate for your purposes.

If the meter directly reports forward and reflected power, you can further test the meter by reversing the in and out connections and compare the readings.

Using the meter into the VHF and UHF bands is questionable but you can repeat the above tests to qualify the meter on these bands. Make certain your dummy loads are rated for these bands as well in order to make the test results meaningful.

## Answer (score 2, by Mike Waters)

To add to Glenn's excellent advice, *some* "CB" SWR meters **will** handle the legal limit on HF with ease.

For example, I have two or three old Radio Shack meters that will do that. I have compared them with other meters of high quality (such as the wattmeter in my Collins 312B-4) and they are plenty accurate enough from 1.8 to 30 MHz.

Having said that, I always tuned at low power until the line VSWR was low, and afterwards always turned the calibration pot fully CCW to ensure the meter was not destroyed at high power.

## Answer (score 2)

Your assumption is correct. It would definitely be usable for 10m. The basic circuit design can range from simple to complex but for it to work at all there is a minimum design requirement that should provide you with a usable device. I don’t feel that 6m is out of the question. I’d compare the forward power indication of your transmitter’s power meter with that shown by the SWR meter in question and note any tendency for the outboard meter to show meaningfully less forward power. If it does not, you may be safe in assuming that the diodes utilized in the design are operating within their frequency operating range.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10168/can-a-cb-swr-meter-be-used-for-hf-amateur-bands, by MattC, Glenn W9IQ, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
