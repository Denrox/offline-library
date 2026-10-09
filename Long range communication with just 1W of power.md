# Long range communication with just 1W of power?

*Tags: software-defined-radio, hf, transmitter, india, wspr · score 7*

## Question

Is it possible, and how can I setup communication between stations 1000km apart from each other by using just 1W of transmission power?

By communication, I mean:

- It can be text based
- It can be very slow. It's okay if I receive a small message in few hours of time.

What are the limitations:

- I don't have an amateur license
- I can use only 27MHz CB radio band
- Maximum radiated power can't be more than 1W
- Many busy cities will be between the two stations, not just plain fields and seas.

What I have/can do:

- Use a directional antenna
- I like DIY
- I am planning to receive using an RTL-SDR
- I can use open-source software to decode signals and/or can write a script to do so, too.

I am from India and here is the latest I could find for CB radio band. Also, it seems I could use 5W of power, but no external antenna and no mention of data transfer policy.

I was amazed how far WSPR signals can go with very little power. Trying to achieve something like that. Not just beacons, but actual communication.

If anything I asked doesn't make sense, I'll keep on editing the question as per the community's feedback, to be more specific.

## Answer (score 5, by Glenn W9IQ)

At 27 MHz and a distance of 1000 km, propagation will be the main determinant of the possibility of communications. Propagation will primarily be a factor of time of day and the sun spot conditions. You can get a fairly accurate estimate by using propagation prediction sites such as VOACAP.

If your interest is exchanging messages between stations, one of the best weak signal modes is FT8 which is part of the free WSJT-X software. A similar, derivative work is JS8CALL.

Take care, however, to check your local regulations to see if data modes are permitted on these frequencies. This would not be allowed in the US, for example.

With that being said, why don't you and your friend become ham radio operators? The effort and expense to get a license in India is not very much. For a restricted grade license you don't even need to know morse code. It will give you the option for more power and many more frequencies, some of which are more suitable to reliable communications.

.

## Answer (score 2, by Aleksander Alekseev - R2AUK)

I would say, your task is a challenging one, but not unsolvable. 27 MHz CB radio band should work similar to 10m amateur radio band.

I suggest to start with simple experiments. For instance, solder a simple oscillator. In my experience Clapp oscillator is quite simple to solder, see schematic in this article https://eax.me/clapp-oscillator/ . Then add a 555 timer to turn it on and off. Now you have a simple CW beacon.

Then use the beacon on transmitting side and RTL-SDR on receiving side. Experiment with antennas, power, observe the propagation during different time. If you receive a beacon, even a wery weak signal, *now* you can start experimenting with different modes.

Also I would like to note that in some countries it's illegal to use a directional antenna in CB.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12650/long-range-communication-with-just-1w-of-power, by Akshit Mehra, Glenn W9IQ, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
