# Is "low loss" cable required for HF?

*Tags: hf, coaxial-cable, feed-line · score 11*

## Question

I use RG-58 for all my HF antennas, since it's light, flexible, convenient, and cheap. And super easy to choke. Whenever I have a problem I just loop a few turns of it on a ferrite core and the problem goes away. Since I operate 100W max and all my antennas are properly matched, I don't think power loss is a concern.

But in a recent discussion I was told by a ham that he "doesn't bother with anything less than RG213". I looked up the specs for the cable I'm using and the loss is 10.5dB every 100m at 50MHz. My interconnects are 10-12m max and for now I only operate 40 and 20m.

I don't see a reason to upgrade my RG58 to something better (LMR400 is what I would go with), but maybe I'm missing something?

I do see a benefit in going with lower loss for VHF and especially UHF and up. But is there a reason, other than pushing kilowatts, to go with lower loss cable?

## Accepted answer (score 10, by rclocher3)

Your question seems as much about psychology as much as technical concerns. We mainly favor the technical questions, but I'll take a stab at the psychological aspects also. All of you, please feel free to disagree with my conclusions!

Coaxial cable is fairly inexpensive for many, compared to our time, even for LMR400. (Your mileage may vary.) For many, it's easier to buy and install the more-expensive coaxial cable and not have to worry about the power loss or the power handling capability and just install the cable once, rather than opting for cheaper cable initially and then deciding to replace it later, after buying an amplifier perhaps.

Of course statements like "I don't bother with anything less than RG213" sound as though they are less about the utility of various grades of cable, and more about how the operator just likes to go with the highest-quality, most-expensive option every time because of the way it makes him or her feel. Or, as @Mast says, perhaps the operator had a bad experience with poorly-made less-expensive coaxial cable once, and is determined to not let that happen again.

If you were a contester, you might be concerned about the ~1 dB loss in your coaxial cable, because every decibel counts to a contester; 1 dB can easily be the difference between getting the rare multiplier or not in a contest. If you're just a casual operator with short coaxial runs and you're not about to buy an amplifier soon, then 1 dB is just one-sixth of an S unit that you'll likely never miss, and I'd say that there's no reason to upgrade your RG-58, and that makes you no less of a ham than the operator with all-RG-213 or better.

## Answer (score 3, by Phil Frost - W8II)

There are two reasons you might want to upgrade coax:

1. lower loss
2. other reasons

"Other reasons" include durability, weather resistance, and absolute maximum ratings. Usually the coax either meets these requirements or it doesn't. If it meets these requirements then you'd only upgrade to reduce loss.

You say your cable has a loss at 50 MHz of 10.5 dB per 100 meters. Do be sure you got this from your specific cable, as not all cable sold as RG-58 is identical. Some of it is quite cheap, and losses are relatively high.

If your longest run is 12 meters, that's a loss of 1.26 dB at 50 MHz. And you don't operate at 50 MHz, so losses are probably half that, so 0.63 dB.

That's nearly nothing. The difference between these two images is 1 dB:

See [How big is a decibel?](How%20big%20is%20a%20decibel.md) for more of this.

In your situation, money is better spent elsewhere. Consider performance improvement per dollar. Money spent upgrading the feedline could instead be spent upgrading the antenna or transmitter. Other ways you might improve performance include:

- Installing more/longer radials under a vertical, reducing ground losses
- Increasing the height of a dipole, reducing ground losses
- Installing a Yagi or other more directive antenna, increasing EIRP and also improving your station's receive performance
- Buying an amplifier or higher power transmitter

A 1 dB improvement in any part of the [link budget](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md) is the same, so spend your money where it yields the biggest improvement per cost. On HF with runs under 100 feet, that area is not usually the feedline unless your point of reference is exceptionally low-quality coax.

## Answer (score 2)

The loses with RG 58 for HF are fairly small unless you have a long run of coax.

The losses are higher for VHF and much higher for UHF, but as most VHF/UHF is short range, often to a repeater, the loss of power usually does not have much of an impact.

Personally I prefer to use LMR400 instead of RG58, as it has lower losses especially on VHF and UFH. It does cost more, but not much more.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16240/is-low-loss-cable-required-for-hf, by hjf, rclocher3, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
