# How would operating a ham radio affect other wireless devices in my house?

*Tags: rfi, internet · score 6*

## Question

I am interested in getting into ham radio however one of my concerns is could a ham radio affect current wireless communications in my house. I am particularly concerned when it comes to WiFi signals. Where I would likely put a radio, I currently have my computer which connects via WiFi to my router.

I am concerned that if I set up a radio with an antenna on the roof above me, I could create interference for my already spotty WiFi signal. Is this a potential risk?

## Accepted answer (score 8, by Paul)

Well, mostly **no** but **yes** it is possible for the antenna to have an effect.

**No**. I get more interference from wifi than interference to wifi.

In the computer adjacent to my ham station, I have had lockups but the network does not drop. It is not wifi related. I assume the lockups are from RF entering on a supposedly shielded cable like a USB mouse or keyboard cable. It happens rarely now that RF-blocking clip on toroids are on the shields of these cables.

Interference from a D-Link to the HF radio receiver was only partially reduced by wrapping the D-Link in Alumnium foil (except for the antenna, of course) and adding toroids to the ethernet and power lines. Routers can be noisy and some comparison shopping or additional internet questions may be in order.

**Yes** Any large metal object around your house, an antenna, a refrigerator, a metal table, your car in the garage, metal such as steel studs in the walls or floors ... will reflect the microwaves from your wifi. The level of wifi signal at a particular spot is affected by these reflections. This doesn't have anything to do with talking on the ham radio, we are just talking about microwave reflections off of passive metal objects.

As far as talking on the ham radio goes, the frequency for Wifi is 2.4Ghz or 5Ghz, which is quite different from the frequencies for most ham radio 1.8 - 432 Mhz. So they don't typically interfere. Also, interference temporarily slows down Wifi, it doesn't typically stop wifi unless somehow the router stops operating. The transmission protocol of Wifi immediately resends information that was missed due to any reason (weak signal, interference from neighbors' wifi, etc) without action by the user.

If you have ancient 1980s era 49 Mhz cordless phones or 49 Mhz baby monitors, get rid of those. Some amplified speakers -- like computer speakers -- may receive you when you talk. This does not indicate any fault, and is normal. It is the speakers that are the problem.

If you share your living situation with apartment neighbors or a home with a family or significant other, perception can be more important than fact. Perhaps strengthen the wifi first, and then worry about ham radio.

That being said, a variety of wifi routers and wifi antennas can be had for around 100 US dollars, and often less, that, by trial and error, might improve your existing signal levels. The typical $30 wifi router does not have a very powerful transmitter and you might pay attention to the output power (usually in milliwatts) if you upgrade it.

Some people build focused wifi antennas out of various food cans or flashlights to obtain a gain in signal. The construction of these wifi antennas is more of a do-it-yourself hobby among wifi hobbyists than necessitated by anything about ham radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1259/how-would-operating-a-ham-radio-affect-other-wireless-devices-in-my-house, by Rob Rose, Paul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
