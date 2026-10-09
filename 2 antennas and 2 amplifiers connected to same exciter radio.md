# 2 antennas and 2 amplifiers connected to same exciter radio

*Tags: antenna, 2m-band · score 3*

## Question

Does anyone here have experience connecting one exciter radio to a pair of identical amplifiers each connected to identical cables connected to identical antennas? Let's suppose we are talking about 2m FM and the pair of identical 4 element Yagi beam antennas are stacked vertically at 1 wavelength (WL) apart (center to center spacing). Should I expect the Tx performance of this to be better than that of the same stack fed by only one amplifier (which is the normal way to do it)? What problems could and may arise with the dual amp? If there is a phase difference in them is there an easy way to fix that such as adding a short piece of coax cable to one of the antennas? If that works on Tx, will it possibly mess up the Rx slightly? What are the chances that 2 identical amps (same make same model), will have the same phasing and will work from the same input signal?

To me it seems there is no benefit to doing this on Rx (vs. a normal stack with just 1 amp) but there is a possible 3dB to be gained on Tx. Also, if someone has a pair of identical 100 watt amps and they want to Tx with 200 watts, they wouldn't have to sell their 100 watt amps and then buy a 200 watter. It would be a good conversation piece on the air.

Also what is the best way to test the dual amp setup to make sure it is working? Would a Field Strength (FS) meter suffice? Does it matter much if the stack is side by side vs. one above the other as far as for testing purposes?

Another interesting question is can a comparison be done with the single amp setup simply by powering down the 2nd amp? Suppose the amps are 5W in and 100W out and they are both being "hit" with 5W on their inputs. Then with 1 amp off, it will be about 105 watts (assuming they are in perfect phase) vs. 200W with both amps on (also assuming perfect phase).

## Answer (score 3, by Martin Ewing AA6E)

Combining multiple power amplifiers is a standard technique for generating high power from a number of lower-power components. You feed all amplifiers with the same input (split the input with transformers or other devices) and combine amplifiers through transformers. For example, 4 25 Watt amplifiers will give you an equivalent 100 Watt amplifier. (These would typically be fixed-tuned, broadband amplifiers, run from a single power supply.)

You would run into problems when you try to combine amps that have to be retuned for changes in operating frequency, like many HF SSB linear amps. It would be hard to get the tuning just right, so that all amps are pulling their share of the load. Furthermore, if you run one amp at a lower level (or off) the transformer combiner is likely to push reverse power into that amp, or even into the exciter -- not a great idea.

So making a big amp by combining outputs of smaller amps can work if the smaller amps are well matched and operated under similar conditions. Otherwise, things get tricky.

Using multiple amps to drive multiple antennas should not be a problem if the antennas are not coupled to each other. Two yagis in a stack would be somewhat coupled, but one yagi pointing north and another pointing east would mostly uncoupled.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/4917/2-antennas-and-2-amplifiers-connected-to-same-exciter-radio, by David, Martin Ewing AA6E. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
