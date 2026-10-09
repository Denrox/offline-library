# Yagi vs Parabolic Dish for 2.4GHz Campus Wifi from 1,800ft away?

*Tags: united-states, antenna-theory, wifi, yagi, range · score 5*

## Question

My apt balcony is 1,812 feet exactly from my campus's Wifi access point behind a triple pane, brick, 4th floor building window. There is a clear line of sight. I was interested in seeing if I could use a Yagi or a Dish to connect to it.

I ran this project idea past a campus network administrator and he said there wouldn't be any concern by the campus.

As the apartment is restricted to slow, overpriced Comcast internet. (Mentioning as this factors into the cost-benefit analysis of my setup)

What would be the better antenna to try using? Is this even worth the electrical cost of keeping this broadcasting?

## Accepted answer (score 6, by Glenn W9IQ)

You can make a first order approximation by using typical WiFi ranges in combination with two free space path loss calculations.

802.11b/g has a typical indoor range of 150 feet. By calculating the difference in FSPL between 150 feet and 1812 feet, the approximate antenna gain requirement can be determined. Using an on-line FSPL calculator, we find 73 dB vs 95 dB of loss respectively for 0 dBi antennas. So your antenna must have at least 95 dB - 73dB = 22 dBi of gain.

This is a first order approximation that assumes the stock WiFi antennas have 0 dBi of gain, the normal working range is 150 feet, the window coatings do not present any additional losses, and there are no other attenuating effects in the path. Given all of this, adding another 6 dB of antenna gain (28 dBi total) for good margin would put you at a reasonable starting point.

An antenna such as this one would meet the requirement. Don't forget adapter cables and keep them as short as possible as these too will introduce losses.

Regarding the power usage requirements, here is a nice site that catalogs the power required for various WiFi access points. Based on this data, a budget of 15 watts would be generous. If you leave it on 24x7, it would use 15 watts * 24 hours per day * 365 days per year = 131.4 kilowatt-hours per year. According to Electricity Local, your residential electric rate is 0.0984 dollars per kilowatt-hour. This puts your worst case operating cost at $12.93 annually. That is well within the budget of even the most frugal grad student!

## Answer (score 6, by Phil Frost - W8II)

Depends on the particular Yagi or dish. Look for a published gain. Beware of low-quality manufacturers that publish erroneous data. Higher gain will correlate with higher probability of working. Point-to-point links of 1812 feet are easily accomplished, with a clear line of sight.

I think you'll have 4 potential issues:

- Attenuation by the building will have to be overcome by antenna gain. 1812 isn't so far, so that may be feasible. You might want to calculate a [link budget](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md) to estimate how much gain you'll need.
- Interference from other sources is another concern. A higher gain antenna will have a narrower beam, reducing interference.
- The hidden node problem. That you're using such a directional antenna makes it likely you will not hear other devices on the same AP. Your campus network administrator might have a change of heart after you get the project up and running.
- Regulations may limit antenna gain and/or power you can legally use.

In my area, electricity costs about \$0.13 per kilowatt-hour. Comcast is \$80/mo. That means for the price of Comcast for a month, I can purchase 615 kWh of energy. There are about 720 hours in a month, so roughly speaking, I'd have to burn 1,000 watts every hour of the month to keep pace with the price of Comcast. Electrical cost of a WiFi radio will be orders of magnitude less than that.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12779/yagi-vs-parabolic-dish-for-2-4ghz-campus-wifi-from-1800ft-away, by Gabriel Fair, Glenn W9IQ, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
