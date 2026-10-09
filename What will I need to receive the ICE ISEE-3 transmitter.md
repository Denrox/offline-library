# What will I need to receive the ICE/ISEE-3 transmitter?

*Tags: antenna, satellites, frequency · score 8*

## Question

The ICE/ISEE-3 spacecraft, launched in 1979, is due to pass by the earth in August, 2014. It was commanded to power down completely years ago, but it appears to have failed to do so, and while it could be re-tasked to perform another mission studying the sun, the equipment to command it was retired in 1999, and no one appears to be interested in funding a new mission.

It is still transmitting, though, and one article suggests

I wonder if ham radio operators will be able to pick up its carrier signal -- it's meaningless, I guess, but it feels like an honorable thing to do, a kind of salute to the venerable ship as it passes by.

- What is the frequency, modulation, and polarization of its signal?
- What will I need to receive it, in terms of how sensitive a receiver or antenna system will be required as it passes?
- When is the 24 hour window of time when it is nearest the earth going to occur?

## Answer (score 4, by Adam Davis)

When is the 24 hour window of time when it is nearest the earth going to occur?

The last fix NASA had on it was in 2008, 6 years ago. The position and velocity at that time have been entered into the JPL Horizons software so we can predict its future location with as much accuracy as can be provided by very old data.

On August 9th, 2014 at 19:12UTC, the spacecraft is predicted to be as close to Detroit Michigan as it will ever be this year, at 0.002729086 AU, which is just over 408,000 kilometers away.

However this is expected to change somewhat as the spacecraft nears earth and better information is collected about its location, direction, and speed.

To find this same information for your specific location, go to the HORIZONS Web-Interface, and set up the parameters as follows:

```
Current Settings
Ephemeris Type [change] :    OBSERVER
Target Body [change] :    ISEE-3_ICE [-111]
Observer Location [change] :    Detroit, MI ( 83°02'57.1''W, 42°19'48.0''N )
Time Span [change] :    Start=2014-08-09, Stop=2014-08-10, Step=1 m
Table Settings [change] :    defaults
Display/Output [change] :    default (formatted HTML)

```

When searching for the Target Body you can simply enter -111 and it will find the ISEE-3_ICE spacecraft. Change Observer Location to your location.

Click Generate Ephemeris to request the information, and it will provide a lot of information, one part of which is a table of data similar to the following:

```
**
Date__(UT)__HR:MN     R.A._(ICRF/J2000.0)_DEC  APmag  S-brt            delta      deldot    S-O-T /r    S-T-O
**
 2014-Aug-09 19:08 *   15 47 41.30 -33 18 20.8   n.a.   n.a. 0.00272908956976  -0.0036236 104.7734 /T  75.0775
 2014-Aug-09 19:09 *   15 47 46.27 -33 18 35.3   n.a.   n.a. 0.00272908828363  -0.0027886 104.7905 /T  75.0604
 2014-Aug-09 19:10 *   15 47 51.23 -33 18 49.8   n.a.   n.a. 0.00272908733324  -0.0019495 104.8075 /T  75.0433
 2014-Aug-09 19:11 *   15 47 56.20 -33 19 04.3   n.a.   n.a. 0.00272908672019  -0.0011066 104.8246 /T  75.0263
 2014-Aug-09 19:12 *   15 48 01.15 -33 19 18.8   n.a.   n.a. 0.00272908644605  -0.0002596 104.8417 /T  75.0092
 2014-Aug-09 19:13 *   15 48 06.11 -33 19 33.3   n.a.   n.a. 0.00272908651242   0.0005912 104.8587 /T  74.9922
 2014-Aug-09 19:14 *   15 48 11.07 -33 19 47.7   n.a.   n.a. 0.00272908692087   0.0014460 104.8757 /T  74.9752
 2014-Aug-09 19:15 *   15 48 16.02 -33 20 02.1   n.a.   n.a. 0.00272908767299   0.0023048 104.8927 /T  74.9582
 2014-Aug-09 19:16 *   15 48 20.96 -33 20 16.5   n.a.   n.a. 0.00272908877035   0.0031675 104.9097 /T  74.9412
 2014-Aug-09 19:17 *   15 48 25.91 -33 20 30.9   n.a.   n.a. 0.00272909021455   0.0040341 104.9267 /T  74.9242
 2014-Aug-09 19:18 *   15 48 30.85 -33 20 45.3   n.a.   n.a. 0.00272909200714   0.0049046 104.9437 /T  74.9073

```

The column that provides the distance to the target is delta, in Astronomical Units, which is about the distance between the Earth and Sun. An easy method to find the closest location is to copy this table into a spreadsheet program and find the minimum value of that column. The deldot is the speed of the spacecraft relative to your location, if negative it is traveling towards you, positive and it's traveling away from you. Due to the rotation of the earth, you may find that there is more than one 'pass' that brings you as close as you'll ever be to this spacecraft, so you can't rely on that alone to tell you the single closest moment of approach, but you can look at the transitions from negative to positive to give you the two closest moments.

Once you have the closest delta, you can use an online converter to do the math for you: 0.00272908644605au in km is 408,266 kilometers.

There is an explanation of this table's other values after the table which would help one to know where to point their antenna, consult your local astronomer for help with these.

## Answer (score 2, by PearsonArtPhoto)

From a specifications document, here's the transponder info:

```
Transponder A: 2090.66 MHz RHCP uplink, command or ranging
2270.40 MHz RHCP downlink, telemetry or ranging

Transponder B: 2041.95 MHz LHCP uplink, command
2217.50 MHz LHCP downlink, telemetry

```

In addition a transmitter/receiver on those frequencies (Tricky), you'd need a reasonably large dish for transmitting/receiving, and the appropriate way to modulate/demodulate the signal. The polarization is circular, left hand. This is in the high bands, pretty close to the Amateur 13cm band.

The day of closest approach is August 10, not sure exactly when the "24 hour window" will start. Obviously the higher gain, the further away communication will happen.

If one was going to do something useful, however, one would need to act sooner than later. And that would require an enormous dish.

I wouldn't be surprised if a few hams hear the spacecraft pass by Earth, but for right now, hearing it is limited to world class EME stations. I suspect quite a few people will hear it as time goes on, and some might even have the ability (But not authority) to transmit before too long. Hopefully something can happen!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1556/what-will-i-need-to-receive-the-ice-isee-3-transmitter, by Adam Davis, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
