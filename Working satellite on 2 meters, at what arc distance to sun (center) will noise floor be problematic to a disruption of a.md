# Working satellite on 2 meters, at what arc distance to sun (center) will noise floor be problematic to a disruption of a communication path?

*Tags: antenna, satellites, noise, solar · score 4*

## Question

Is there some simple utility, or published set of charts, or suite of formulae, where one can approach the situation by inputting a space weather summary, (sunspots, various indexes, etc), the receive frequency (band), half power beam width and gain of antenna, and arc distance from max gain main lobe vector to the sun disk (using the az el of the rotators), where the noise floor will rise enough to make signal detection unlikely, everything else being equal? Yes, that might be too broad a brush. Please educate my ignorance.

Stated differently: If I am working a satellite or the ISS digipeater with a two meter beam or helical, and the sun is up, and the satellite (ISS) pass comes close to or even transits the sun disk, then at what arc distance to the sun (center?) will the sun likely cause enough RFI to black out the attempted communication with the satellite (ISS), on two meter, 70 cm, 23 cm bands? I understand it will depend on the main lobe of the antenna, and its half power beam width? Let's use as an example, the average 3 element yagi maximized for gain, such that it gives about a 40 degree half power beam width... if those numbers are unrealistic, still, you get the idea of what I am looking for, yes? I'd like an announced expectation of a sun causes comm black out. It already says 'eye protection' when the antenna is pointed within 45 degrees arc distance of the sun. Why? When portable, or in power conserving situations, the rotator(s) might be strong-arm, aligning with a big plywood compass (az) rose on the ground, and an elevation scale, while looking somewhat along the antenna. With az and el announcements every four seconds, strong-arm alignment should be plenty good enough. People are making contacts with less accuracy than that, roadside, on youtube.

I'm thinking there must be some utilities already out there without my re-inventing the wheel, for the sun related noise floor increases. Hopefully source code available, opensource, so I can write them into my python script(s), honoring any licensing terms and conditions of course.

My Antenna handbook is from 1988, and I figure there is a lot more data and experimentation since then, particularly in this context.

I've got a python program using pyephem, that runs continuous, and gives periodic voice announcements of the status of upcoming passes and 'in progress' passes, grabbing TLE updates each day, internet connection dependent at least once per week. It runs on a raspberry pi or an android device (since pyephem is easily installed on either of them). I would like it to also give a caution regarding possible noise floor related black out(s) when the pass is closely aligned with the sun (risen of course). For that, I need this additional RFI noise floor based on the sun/space-weather information, so it can be appropriately coded.

Maybe the EME folks have already worked something like this out? The geostationary commercial bird operators know when there is a higher probability for a blackout, briefly, twice per year, when the orbital position basically transits the sun for certain geographic regions. I am looking to know if for the HAM sats, this would only happen if there is a literal transit, or if it develops into happening as the main lobe of the receive antenna gets within a certain threshold arc distance of the sun.

Comments please if you need more clarification.

**Update 2-23-2020:**

I have selected the post from tomnexus as the answer, but I wish to be clear. Phil Frost - W8II 's post was just as valuable as the answer. As is often the case here, there is not always a *best* answer, but instead, several postings that form the more complete answer for which an OP was hoping. Some of the comments and comment exchanges were also essential toward an *answer* that would give me what I need to form a project decision. If you can, imagine that both these posts have been selected as the answer. If there are more posts that I miss later on, I trust they will be in some way helpful to someone with a similar question(s). Thank you to all the contributors.

## Accepted answer (score 3, by tomnexus)

It depends on the gain of your receive antenna, your system noise temperature, and how much link margin you had in the first place.

The moonbounce (EME) community use Sun Noise as a measure of their system performance, so the sun is certainly detectable by a modest amateur station.

A quick Google search for "sun noise EME 144" yields this interesting result from SM7SJR: *2m noise measurement: 2 x 15 el LFA. Stacked vertically. LNA 0,36dB NF. Aimed at the sun: 5,3dB sun noise.*

So with this fairly large station with a very good preamp, the noise floor rises 5 dB when pointed at the sun. Can your link budget afford this much additional noise?  
If you have no LNA or say one 5-element yagi (6 dB less gain, 10+ dB more system noise) then the sun will only contribute <<1 dB of noise, not enough to worry about. If you have both a small antenna and no fancy pre-amp then you definitely won't be able to detect sun noise. If you can hear the satellite at night, you'll be able to hear it in the day even as it transits the sun.

For detailed, more general predictions, you can look up measurements of the solar flux at your frequency - it depends on the sunspot number. Then with the rest of the system parameters - gain (pattern), noise temperature - you can predict the rise in noise due to the sun in the beam. The sun raises the system temperature depending simply on the pattern of the receive antenna.

There are several EME system calculator programs which can predict sun noise for a particular system. The first many results for "eme calculator sun noise" look useful.

## Answer (score 2, by Phil Frost - W8II)

The answer will depend on many factors. You've not given sufficient information to yield an answer, but the following concepts should help you arrive at your own answer.

Firstly you must start with a link budget. The link budget determines how much power from the transmitter will arrive at the receiver. See [What is a link budget, and how do I make one?](What%20is%20a%20link%20budget%2C%20and%20how%20do%20I%20make%20one.md)

Ultimately it's not the power received that determines whether a signal is decodable or not, but rather the signal to noise ratio. So you will want to evaluate the noise performance of your receiver(s), see [How can I calculate the effects of an LNA, antenna gain, etc. on noise performance?](How%20can%20I%20calculate%20the%20effects%20of%20an%20LNA%2C%20antenna%20gain%2C%20etc.%20on%20noise%20performance.md) Linked in that answer is ITU-R P.372-13 which will give you some estimation of the noise temperature of the sun, sky, and terrestrial noise in various conditions and frequencies.

You'll have to combine all these noise sources, weighted by the sensitivity of the antenna in every direction. That is, an extremely directional antenna will have a noise temperature nearly identical to just the thing it's pointed at, whereas a weakly directional antenna (like a 2 element Yagi) will pick up more noise from the sides, back, and other directions.

Finally compare the estimated signal to noise ratio with the sensitivity of the mode you'll be using, and you should have some estimation of whether communication will work or won't.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16011/working-satellite-on-2-meters-at-what-arc-distance-to-sun-center-will-noise-fl, by always_learning, tomnexus, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
