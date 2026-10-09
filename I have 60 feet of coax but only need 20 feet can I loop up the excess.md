# I have 60 feet of coax but only need 20 feet; can I loop up the excess?

*Tags: coaxial-cable · score 7*

## Question

I was given about 60 feet of good cable with connections but only need about 20 feet. Can I loop up the end or do I need to cut and put a new connector on?

## Answer (score 13, by Kevin Reid AG6YO)

There's nothing inherently wrong with “looping up” extra coaxial cable. In fact, a neatly wound coil of coax can function as an air-core choke balun (“ugly balun”) which is useful for some antenna systems when located at the feed point of the antenna.

The only disadvantage is the extra loss in the coax from the extra length. Loss in a coaxial cable, when measured in dB, is **proportional to the length of the cable**. For example, if your 60 feet of cable has 6 dB of loss as used, then you will have 2 dB if you cut it down or replace it with 20 feet of the same cable.

(Note that this means that the lower loss-per-length the coax has, the less valuable it is to trim it to the right length.)

The other factors — how much loss a particular length has — are:

- the type of cable (better quality coax will have less loss since it is designed to), and
- the frequency of the signal (higher frequencies experience more loss).

If you look at the manufacturer's datasheet for the coax (you should be able to look it up from the printing on the side of the cable, if any) will give a table or graph of loss in dB per 100 feet (or some other such standard length) versus frequency. Just multiply/divide to find the actual loss for your length.

But be sure to think about whether you actually care about the loss:


Loss when transmitting means you're wasting that fraction of your transmitter's power — if the current result is adequate for the contacts you want to make, then don't worry about it, but if the loss is significant then improving the coax is overall cheaper and more efficient than getting a bigger amplifier.


Loss when receiving matters *only if* the incoming signal is so weak that the limiting factor is not noise picked up by your antenna but noise internal to your receiver or leaking into it from nearby sources.

If you have or can borrow an **antenna analyzer**, you may be able to use it to measure the actual loss in a piece of coax. Hook it up to the analyzer with the other end *not connected to anything* — this *unterminated* end will reflect the signal back almost perfectly. In this configuration the *return loss* (amount of power not reflected back to the analyzer) the analyzer measures will be equal to twice the loss in the cable (because the signal bounced back, so it went across the entire length of the cable twice).

Since cable loss is frequency-dependent, set the analyzer's frequency to the highest frequency you plan to use (which should have the most loss), or whichever frequency you wish to measure at.

Best to worst test configurations:


If your antenna analyzer directly reports return loss (e.g. the higher-end RigExpert models do) then you can use that value. Remember, the return loss is the coax loss applied to the signal *twice*, so divide the dB value by two.


If you only have a SWR value, you can calculate it from the SWR value using the following formula or any purpose-made calculator:

$$ \mathrm{RL} = 20\log_{10}\left(\frac{\mathrm{VSWR}+1}{\mathrm{VSWR}-1}\right) $$


If your analyzer displays the SWR as infinity or off-scale, the loss is *too low* to measure. To get a better measurement, you would need an **attenuator** inserted in line (at either end); this will increase the loss by a known amount, and therefore reduce the SWR into a measurable range. Then subtract the attenuator's loss from the return loss before dividing by two.


If your only measurement instrument is a transmitter with built in SWR meter, don't do this unless you know it's protected against mismatched loads. You will almost certainly need an attenuator, and it will have to be rated for the output power, and the result may be rather inaccurate as these meters are not intended for precision measurements.

## Answer (score 2, by rclocher3)

That depends on what kind of cable it is, the band you'll be using, what your SWR is, how old the coax is, and how demanding your needs are. If your SWR is less than 2:1, you're using the coax for HF, and you're not concerned about that last dB, then go ahead and try it as-is. If you're talking about the coax to your 2m antenna that you use to talk to the repeater and your signal is normally full-quieting, then go ahead and try it as-is.

If the coax has been out in the weather for ten years or more, or if it's a lot thinner than the coax people usually use, or if the coax is marked "75 Ω", then I'd leave it alone.

If your situation is somewhere in the middle, then give us more details. 73!

## Answer (score 2, by K7PEH)

Unless you are operating VHF and above, abide by the rule of never cutting your coax cable unless you absolutely must for some reason. What you need today may be 20 feet but a new antenna you might put up next may need 40 feet. If you are active in ham radio, especially with HF, you will probably have dozens of antennas over the life of your coax.

Here is a coax attenuation chart showing loss per frequency per cable type. There are dozens of such charts to be found on the Internet via google.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6041/i-have-60-feet-of-coax-but-only-need-20-feet-can-i-loop-up-the-excess, by Dant1316, Kevin Reid AG6YO, rclocher3, K7PEH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
