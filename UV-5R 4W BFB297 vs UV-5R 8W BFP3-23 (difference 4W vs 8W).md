# UV-5R 4W BFB297 vs UV-5R 8W BFP3-23 (difference 4W vs 8W)

*Tags: baofeng, equipment, uv-5r · score 6*

## Question

How big difference will it be between UV-5R 4W & newer UV-5R 8W (difference between 4W & 8W), in real life use 1 on 1 HT. In SAME conditions, how much different distance / range will we get? (simple example)

So I want to buy two HTs and change stock antennas with Nagoya NA-701, and major things that I want to use them for are:


Rare occasions use and for about 8-10 hours top max until it will be near charger;


will not use 8W all the time, just in case when other HT is out of reach with 4W (between two ski resorts, one car start the trip few minutes before other one..);


mountain - skiing, to get friends locations, to meet up;


while travelling by car, with friends (few km separated);

I read A LOT of topics 4W vs 8W, and most of people say it's too small difference, few are saying with hard evidence that it's a big difference (Link added).. here are some quotes (for helping other people that read this):


some say that thay don't want 8W radiation around their head for too long.


5W vs 8W won't make more than a "mosquito-fart" difference in signal.


Range depends on antenna height and terrain. Those few extra Watts won't do much, if anything, but they will drain battery faster.


Don’t forget – gaining one lousy extra s-point would require 4x the original power output, which means that the UV-5R would have to deliver 16 Watts. That’s technically not possible.


(some forum talk about UV5R & F8HP) With 4W and the 701 antenna, best I could do was 10 miles, but with the 8W and 701, I can stand in that same spot and reach repeaters and simplex 16 miles away. The disclaimer with my location is little elevation difference, but surrounded by thick pine tree forest.

I hope that you will help me, and that this thread will help others while still there are not so much info & tests about "UV-5R 8W"

**To simplify**, here's the example situation:

Talk between two same HTs (4W to 4W or 8W to 8W), with line-of-sight (**mountain to valley or mountain to another mountain**) that means no earth curving, could we produce a situation when 4W to 4W is not enough and in same spots 8W to 8W will work?

And approximately what would be a difference in KM / Mile? or would it be more likely in Meters maybe?

Because I'm not interested in repeater just in one on one HT use, and use of 8W would only be when other HT is out of reach with 4W, also I would use 8W just to set meeting point... so in that kind of use, I don't need to worry about "Brain radiation" or whatever.

That is what I'm looking for here, in real life, will that work or not and what would be the difference in distance for the same spots if it works.

I'm new to radios / frequencies / dBs and all that comes to it, but thinking would it be good to spend little more $ for 4W more (for future needs) or it's a waste of money.

## Accepted answer (score 5, by Phil Frost - W8II)

4W to 8W is a doubling of power, or a 3dB increase. That's 3dB you can add to your [link budget](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md). Provided of course that the limiting factor is the other station hearing you, not the other way around.

Let's say with 4W you can be heard up to 10 miles away. In idealized conditions (no terrain in the way, no interference, etc) 8W increases your range to 14.1 miles.

Why? According to the inverse square law, irradiance is inversely proportional to the square of the distance.

$$ \text{irradiance} \propto {1 \over \text{distance}^2} $$

That means multiplying the distance by $x$ will require an increase of $x^2$ in EIRP to maintain the same irradiance, which can be made by increasing transmitter power or antenna gain.

We must also consider the radio horizon. Even if there are no hills in the way, the curvature of the Earth will get in the way at some distance. The horizon (in miles) for a station at some height (in feet) is approximated by:

$$ \text{horizon} = 1.41 \sqrt{\text{height}} $$

For height in meters and horizon distance in kilometers, change the constant to 4.12.

This approximation takes into account the shape of a perfectly round Earth, and a "bonus" to account for atmospheric bending of the signal. It doesn't account for trees, buildings, or hills.

Let's say your HT is 4 feet high. Your horizon is $1.41\sqrt{4} = 2.82$ miles. And the repeater is on a 50 foot tower: $1.41\sqrt{50} = 9.97$ miles. The horizons add, so beyond about 12.8 miles you no longer have a line of sight, and adding more power won't do much to increase range.

## Answer (score 5, by Glenn W9IQ)

The exact answer is given by the Friis equation. If you double the power, your range will increase by 1.413 times whatever it was before doubling the power if you change nothing else. This assumes you do not violate line of sight rules and that there are no additional obstructions in the longer path.

You could get this same effect by doubling the gain of one of the antennas.

On the other hand, if you doubled the gain of both antennas and left the power as it was (4 watts), your distance is nearly doubled and you do not have the additional battery drain. The extra distance is because you are increasing the effective transmit power and the effective receive gain.

## Answer (score 3, by MoTLD)

Of your quoted testimonials, the one I'd put the least credence in is the 10 miles at 4w and 16 miles at 8W, because I'm not sure what they mean by the "elevation difference" disclaimer; at these frequencies even a small difference in location, especially in elevation, can make much more difference than doubling wattage. The rest seem pretty much spot on.

4W vs 8W is slightly more than mosquito-fart difference, but not much. Most of the time it will just be a waste of battery. If the price difference means you can get the 4W plus a better antenna instead of the 8W, that's what I'd do. If you can afford both, get the 8W radio *and* a better antenna. Options are good to have even if you seldom use them, and those extra few dB might make the difference one day. You can always transmit at medium or low power when battery life matters.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7585/uv-5r-4w-bfb297-vs-uv-5r-8w-bfp3-23-difference-4w-vs-8w, by SxOne, Phil Frost - W8II, Glenn W9IQ, MoTLD. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
