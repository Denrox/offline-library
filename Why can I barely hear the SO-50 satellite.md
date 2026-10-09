# Why can I barely hear the SO-50 satellite?

*Tags: satellites, uhf · score 3*

## Question

I have a Kenwood TM-V71A dual-band radio that I have attempted to use to listen to the FM repeater on the SO-50 satellite. I'm using a home-made dual-band yagi antenna made out of coat hangers, that I built from these instructions: http://www.amateurradio.bz/4_dollar_satellite_antenna.html

I tested out the antenna by listening to some local repeaters and weather frequencies and it seems to work fine for that. I double-checked that I'm using the right downlink frequency for the satellite, and that I have the correct time and direction info from pass predictions obtained here: http://www.amsat.org/amsat-new/tools/predict/index.php

I haven't even bothered trying to transmit yet, because I can barely get a receive signal from SO-50. When I attempt to listen to a satellite pass, at approximately the halfway point where the satellite is at maximum elevation, I can hear a clear signal for about 5-10 seconds, and then nothing for the rest of the pass. This has happened several times now. On passes with low elevation (less than 20 degrees from horizon), I hear nothing at all. On passes with high elevation (45-70 degrees from horizon), I will get a few seconds of signal, right around the middle of the pass.

So what am I doing wrong? I'm pretty sure I've built the antenna correctly, and have the correct pass times. I started out using the directional information, but now I basically just spin in circles at all different angles, trying to get any signal whatsoever. I also rotate the antenna for different polarizations. The times that I do get a few seconds of signal, it may end up being from the totally wrong direction than what the pass prediction said.

Do I need to be at a much higher elevation than ground-level in my back yard? What else could be going wrong? Are there other satellites that I can try? It seems to me that SO-50 is the only operational FM voice repeater (aside from the ISS, which isn't always in voice mode, if I understand correctly).

Thank you for any help.

EDIT: I had been adjusting for Doppler shift at first, but then left it at the centre frequency, as it did not seem to be making a difference. However, the chart provided by Pete NU9W was very helpful in making me realize the problem. I think my radio isn't sensitive enough to adjust for Doppler shift properly. It will only change the frequency by 25 kHz at a time, and the chart suggests adjusting by 5 kHz at a time. In my case, I can be 5 kHz off centre, or 30 kHz off in either direction. Since 30 kHz is too far off, it would explain why I only hear something in the middle of the pass.

EDIT 2: I figured out how to change the step frequency on my radio to 5 kHz instead of 25 kHz. I will try using this setting and see if I can adjust for Doppler shift better next time.

## Accepted answer (score 4, by Pete NU9W)

It sounds like you're not adjusting for Doppler shift. Just like the sound of a car horn, which is higher pitched when the car is coming toward you than when it's going away, the signal from the satellite is at a higher frequency when it's coming toward you than when it's going away. When the satellite is close to the horizon at the start of the pass it's coming toward you, so the frequency you see is higher; at the end of the pass it's going away, so the frequency is lower. When it's overhead you see it at its actual frequency. You have to adjust for these frequency changes during the pass. Here's a link to a page with suggested frequencies (scroll down).

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5195/why-can-i-barely-hear-the-so-50-satellite, by mikazo, Pete NU9W. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
