# Tuner at antenna side versus transmitter?

*Tags: feed-line, antenna-tuner · score 8*

## Question

I figure the transmitter has a 50-ohm pure resistive output and that the transmission line is 50-ohm as well. I think it's usually the antenna itself that actually needs to be tuned, yet it sounds like everyone places the tuner at the transmitter side. what are the effects and wouldn't it be better to have the tuner at the antenna? my guess is that the transmitter sees a "perfect" match and will have no complaints but that there are reflections from the antenna port going back and forth between the tuner and the antenna. i think this would create a power bottleneck where the transmitter could put out more power but the tuner/cable/antenna combo can't "absorb" that much power. i would think there are standing waves between tuner and antenna which will make it harder to send more power through as well as cause additional losses.

## Accepted answer (score 9, by Phil Frost - W8II)

There are a lot of topics in this question, so let's take them one at a time.

I figure the transmitter has a 50-ohm pure resistive output

Not necessarily. You're probably arriving at this conclusion based on the maximum power transfer theorem. Which of these circuits delivers more power to the load resistor?

What we *can* say is the manufacturer has designed the transmitter expecting a 50 ohm load, and they've also designed it to minimize their cost, thus maximizing their profit. This means when the load is 50 ohms the transmitter will be able to make its rated power while staying within the ratings of the components of the transmitter, the finals especially. But there won't be much margin for deviation, because that would increase costs.

When the load isn't 50 ohms this might subject the finals to too much current, voltage, or power. If we're lucky this means the radio just reduces power. If we're unlucky the radio doesn't reduce power, and the finals are damaged.

So we want the transmitter to see 50 ohms so it can operate as designed.

I think it's usually the antenna itself that actually needs to be tuned

Usually, but not always. Most radios these days are designed for a 50 ohm load, and 50 ohm coax is very popular. But there is also 75 ohm coax, and there are balanced feedlines between 200 and 600 ohms which are readily available.

Also, not all radios are designed for a 50 ohm load. In particular, older tube radios typically have a variable output network, so they will work with a whole range of loads. And although coax has been around since the mid-19th century, it wasn't really until after WWII that it became available to regular folk. Prior to that the most common feedline was some kind of balanced feedline typically with a higher impedance.

my guess is that the transmitter sees a "perfect" match and will have no complaints but that there are reflections from the antenna port going back and forth between the tuner and the antenna.

This is exactly right. The reflected power from the antenna encounters the tuner, and the tuner (if you've managed to adjust it so the transmitter sees a 1:1 SWR) re-reflects that power back at the antenna. The consequence of these extra reflections is usually (but counter-intuitively, not always!) [additional loss in the feedline](What%20is%20the%20actual%20loss%20in%20a%20feed%20line%20with%20high%20SWR.md).

i think this would create a power bottleneck where the transmitter could put out more power but the tuner/cable/antenna combo can't "absorb" that much power.

Not usually. Under normal circumstances, the feedline and antenna are linear systems, which means waves can be superimposed indefinitely. What happens is that each reflection is independent of what's happening with other reflections at the same time.

However, linearity does break down eventually for just about any real system. To give one example, that additional loss in the feedline causes the feedline to become warmer. At some point it will become warm enough that the dielectric may melt, and the center conductor will short to the shield. Or, the voltage can get high enough to arc through the coax dielectric. It's pretty much impossible to get to this point with 100W and LMR-400, but 2kW and some really terrible RG-58 might. For broadcast stations in the megawatts, it's definitely a concern.

In summary, on purely theoretical grounds it usually is better to put the tuner at the antenna end of the feedline. However this requires making it weatherproof, and having some mechanism to remotely operate it, which makes it more expensive and difficult to install. Those downsides may or may not outweigh the benefit, depending on circumstances and priorities.

## Answer (score 4, by hotpaw2)

I'll add that a tuner is used for tuning, and tuning, for a single or small set of frequencies is often done at the antenna, usually by adding or adjusting a loading coil or adding a capacitive top-load or hat (etc.), usually done during antenna design, construction, or deployment.

However a tuner is used for a wider range of tunings, thus has additional reactive components and switching components that (1) weigh something and (2) are only used in some tunings for some frequencies. Thus a tuner has addition weight, often unneeded, that might involve some difficulty adjusting, maintaining, and hoisting stuff perhaps a hundred feet in the air, far away from the operating point, to an antenna's feedpoint.

But for some field antenna's the answer is both, as the feedpoint for a random wire or an end-fed (e.g. highly off-center fed dipole) and counterpose might be right at the transmitter (in SOTA ops, et.al.). So tuning with a tuner can be done at both the transmitter and the feedpoint, since those two points are colocated.

## Answer (score 4, by user10489)

To make a long story short, if you are using 50 ohm coax with a 50 ohm radio, putting the tuner at the antenna is higher efficiency because it reduces losses in the coax caused by high SWR.

However, putting the tuner at the antenna has some huge disadvantages. It has to be weatherized. It is more prone to damage from lightning. It has to be remotely powered and possibly remotely controlled. If anything goes wrong, you have to pull down your antenna to service it, etc. It's much easier to just put the tuner next to the radio. Manual tuners (that need to be next to the radio) don't even need power.

Having said that, there are a number of antenna designs that integrate a simple cheap tuner into the antenna. These miss most of the disadvantages, and some don't even need to be powered.

However, the losses from SWR in the coax are usually not so bad that you can't operate anyway with a tuner at the radio, as long as you stick to under 100w and realize you might not be getting full power to the antenna. And as another answer pointed out, not all radios or feed lines are 50 ohms, so a remote tuner might not make sense in that case.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/19939/tuner-at-antenna-side-versus-transmitter, by pgibbons, Phil Frost - W8II, hotpaw2, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
