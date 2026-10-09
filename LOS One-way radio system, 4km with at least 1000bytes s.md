# LOS One-way radio system, 4km with at least 1000bytes/s

*Tags: digital-modes, equipment-design · score 5*

## Question

In order to track skydivers/BASE-jumpers with flysight I am looking for a one-way radio system to transmit the location data. System needs the following specifications:

```
Frequency:          Not important, preferable legal (Europe)
Bandwidth           1000 bytes per second (at least)
Range:              4000 meters
Line of Sight       Yes
Latency             As little as possible
Mobile Coverage     Not available
Transmitter
 - Location      Air
 - Movement      Moving, up to 200 km/h horizontal groundspeed
vertical distance: closing towards receiver during operation
 - Interface     USB or serial
 - Weight        As little as possible
 - Size          As small as possible
Receiver
 - Location      Ground
 - Movement      Stationary during operation, movable by car
 - Interface     Not important, what ever works
 - Weight        Not important, movable by car
 - Size          Not important, movable by car

```

Any suggestions?

## Accepted answer (score 4, by BenSwayne)

There are a number of commercially available RF data modems that operate within the amateur radio spectrum for hobby use particularly with RC (remote controlled) hobby aircraft. However, I believe your specific ITU Region imposes additional output power limitations which will make this challenging at 4 km distance.

The RFD900 developed by an Australian company is sold in the USA by jDrones for hobby RC use and will support ranges up to 40km and data rates up to 250 kbps! However please note these specs are inversely related and subject to the limitations of your antenna system and the environment (more speed closer, slower data rate further away). Line of sight open air 4 km should be no problem at all with the data rates you are talking about.

This particular model outputs 1 watt in the 902 Mhz to 928 Mhz frequency range otherwise known as the 33cm band in ITU Region 2 (Americas). However, it appears this band is not allocated in Europe (ITU Region 1) and may exceed your maximum output power limits - so you may not be able to use this specific model of hobby radio modem in your location. This is simply the only one I know because I am in Canada.

For Europe you should look for a comparable model in the 70cm (433 Mhz) band such as the PipX (only 100 mw). However the additional limitation on output power may limit operational range.

In that case you may need to look into building an antenna tracker for use with a highly directional antenna such as a yagi. This involves transmitting the GPS co-ordinates down the link and having the antenna tracker point the antenna straight at the target. This may be somewhat experimental if you are moving at 200 km/h - I think you will need to custom build your antenna tracker, perhaps taking into account the average falling speed and any latency in the motor controller and anticipating the targets future position.

Eitherway, experimentation is part of the hobby of amateur radio! So if you do decide to take this on, publish your project progress somewhere for all to enjoy.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1862/los-one-way-radio-system-4km-with-at-least-1000bytes-s, by wittrup, BenSwayne. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
