# What's a cost-effective way to boost the range of my cheap 2m/70cm handheld?

*Tags: antenna, vhf, uhf, ht, uv-5r · score 29*

## Question

I'm a very casual/beginner level ham and as such have mostly avoided committing too much in the way of financial resources - I have a UV-5R for a personal radio, anything else I do I've used others' radios.

I don't mind the 5R's interface; I'm familiar enough with it now that it doesn't really bother me. That said, it'd be nice to give it a little boost without spending a bunch of money and/or buying a new radio. I typically operate at home, so mobility isn't required (though being able to pack it up to have along when traveling wouldn't hurt, either).

What kinds of low-cost options are there that could help improve its range (and/or SNR)?

## Accepted answer (score 17, by Dinesh Cyanam)

A homemade "rat-tail" ground plane costs 35 cents each to make. A crimp on eyelet to fit your antenna's connector, a string of speaker wire about 19-20 inches long and a little heat shrink tubing to dress it up and done. Soldering the the wire to the connector instead of crimping it will be a better option.

Go here for some details about the "Rat-Tail" ground plane: http://www.hamuniverse.com/htantennamod.html

## Answer (score 17, by Rob T.)

There have been a number of good answers already, though I think there are a few additional points worth sharing. Answers would also be more relevant if we knew what situation(s) you were coming up short range wise.

For portable use (out in the field):

1. The stock Baofeng rubber duck antenna has been shown to be a poor performer. All of the stock rubber duck antennas tend to be a compromise and not perform very well, but the stock, stiff, short baofeng antenna seems to perform worse than others.
2. An antenna that is physically close to the right wave length (1/4 wave, 1/2 wave, or 5/8th wave) on the frequency you want to operate on will perform better (have less signal loss) than a shorter antenna. While it's inconvenient to carry around, a 14-15 inch "gain" antenna can help in many cases where a 4-8 inch stock duck can't be heard.
3. The standard rubber duck antennas are 1/4 wave, which are half of a 1/2 wave dipole, oriented vertically. Your body is making up the other half, the ground plane. The rat tail suggestions are good ones, which are providing a better ground plane to complete the other half of the antenna.
4. Get the radio off your belt! If you are using the headset with the radio attached to your belt, your body is absorbing much of the signal. Bring the radio up to your mouth when transmitting.
5. Make sure your battery is fully charged. Your radio is only putting out the rated power when it is getting the design voltage. The lower the voltage from your battery, the less your power output (in watts) will be. Several graphs of power vs. battery voltage have been published for the Baofeng and the similar Wouxun online and in the Yahoo groups.

For use in a car:

1. Get your antenna OUTSIDE of the car. The body of the car will absorb much of the signal. A magnetic mount antenna can be a good non-permanent solution. Make sure you've got enough metal in the roof and that the antenna is as close to the center of the roof as you can.
2. Power the radio from the car to ensure you are getting the full output power your radio is capable of. Use a 12 volt battery eliminator.

For use indoors:

1. Get your antenna outside, especially if you are using 2 meters. The shorter 70cm waves have a much easier time getting through window openings than the longer 2 meter waves. There are many simple choices that don't involve trying to put a large antenna on a roof. A magnetic mount antenna for a car placed on a window air conditioner works well.
2. Use 70 cm where possible instead of 2 meters if it's appropriate for your area.
3. Use a power supply to make sure you a getting full output power.

General:

1. Height and Line of Sight are your friend.
2. 2 meters and 70 cm perform differently and have different advantages depending upon the surrounding terrain. It's good to know which one to use. 70cm is better in urban areas. 2 meters will give you longer distance propagation in open areas.

Important General Tip: **The pin inside the SMA antenna connector will eventually break!** The connector is rated by design for approximately 500 connection cycles. If you use one antenna and rarely disconnect it you'll be fine. If you change antennas frequently, consider using a low profile BNC adapter where the base sits on top of the radio and isn't completely dependent on the SMA jack for all of its mechanical strength.

## Answer (score 6, by Paul)

If you don't need mobility, purchase an inexpensive directional 4 element Yagi antenna for 2m and operate it in vertical polarization, that is with the prongs of the yagi pointing up and down. You can sometimes find these small Yagi antennas used for ~$20-30. But note this will only help you for 2m, and should not be used on 70cm. For 70cm you can get a 70cm antenna, or perhaps find an antenna designed for both bands. This will add cost, however.

One warning about external antennas: convert from big coax down to smaller coax and a BNC or SMA plug near the HT instead of using the big coax with an adapter; a PL259 to BNC/SMA adapter may tear the bnc/sma plug from the wiring or circuit board of an HT.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/23/what-s-a-cost-effective-way-to-boost-the-range-of-my-cheap-2m-70cm-handheld, by Amber, Dinesh Cyanam, Rob T., Paul. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
