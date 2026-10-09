# Recommendation for hobbyist flight computer radio antenna

*Tags: antenna, antenna-theory, antenna-construction · score 3*

## Question

I'm a CS college student working on the flight computer of my Rocketry Club's rocket. My flight computer has a 915MHz radio transceiver, and it needs to transmit data to my computer with another radio receiver on the ground. The rocket at the maximum height will be at least 10,000 feet (3048 meters) away from the ground radio, and probably no more than +2,000 feet of that. (Specifically, I'm using an Arduino paired with an Adafruit RFM69HCW @915MHz radio breakout board for both the flight and ground computers)

Both the ground and rocket radios have SMA connectors. I have not yet figured out how to deal with the antenna situation.

I don't know too much about amateur radios and whatnot, so I was wondering if anyone had a suggestion for an antenna that could handle the needed range, and if not, suggestions on what/how to build an antenna for the radios to handle my required range.

Thanks so much in advance!

## Answer (score 2, by rclocher3)

Your project may demand some engineering, I'm afraid. I see that Adafruit quote a range of 500 m with simple wire antennas for those modules, and that range is probably with optimal orientation of the antennas; in other words, the antennas oriented vertically with the antennas separated horizontally. You probably wouldn't be able to put a gain antenna on the rocket, and your antenna orientation may not be so favorable, so you may not even get 500 m.

You might try buying a couple modules, attaching simple wire antennas like in the picture on the Adafruit site, putting a module and antenna in a rocket body, and seeing what kind of range you actually get. Try all sorts of antenna orientations that you might encounter in a real flight. (Hint: you might be better off with the ground antenna a ways away from the launch pad, so you can trade range for a more favorable antenna orientation.) Maybe Adafruit are being very conservative.

If you don't have enough range, then you need to start thinking about your [link budget](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md). In other words, how do you get enough signal strength for a reliable connection. The answer might be more transmitter power, or a directional antenna on the ground. Maybe it would be easier to just store the data, and then process it after you recover the rocket.

If the answer is a better receiving antenna, one could be built very cheaply with solid copper wire on a handheld wooden boom aimed at the rocket. What isn't so cheap is the expertise and test equipment you would need to design and test such an antenna. Perhaps you could join forces with an amateur radio club.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17474/recommendation-for-hobbyist-flight-computer-radio-antenna, by chungmcl, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
