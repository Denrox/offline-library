# How to read ID-51A GPS logger data

*Tags: ht, software, gnss · score 3*

## Question

I own the original Icom ID-51A. I have the GPS logger logging every 5 seconds to the microSD card. How do I view this saved track data on my computer?

For reference, here's one of my logs (I know it looks like I'm going in circles, I was doing GSAR training that weekend): http://www.km4ayu.com/errors/20160320_145218.log

Feel free to download and process that log, and let me know what you did.

Here's the first several lines of content of that file (plaintext - and the whole thing exceeded the character limit, so just download it from that link above if you want more):

```
$GPGGA,205221.743,3320.2409,N,08646.8572,W,1,04,10.5,170.1,M,-29.1,M,,0000*51
$GPGSA,A,3,23,09,08,07,,,,,,,,,11.5,10.5,4.6*36
$GPRMC,205221.743,A,3320.2409,N,08646.8572,W,1.64,49.17,200316,,,A*4D
$GPVTG,49.17,T,,M,1.64,N,3.0,K,A*36
$GPGGA,205222.743,3320.2939,N,08646.7655,W,1,04,7.4,100.0,M,-29.1,M,,0000*64
$GPGSA,A,3,23,09,08,07,,,,,,,,,7.8,7.4,2.6*3D
$GPRMC,205222.743,A,3320.2939,N,08646.7655,W,1.00,49.17,200316,,,A*4B
$GPVTG,49.17,T,,M,1.00,N,1.8,K,A*3E
$GPGGA,205223.743,3320.3039,N,08646.7474,W,1,04,7.4,81.6,M,-29.1,M,,0000*52
$GPGSA,A,3,23,09,08,07,,,,,,,,,7.8,7.4,2.6*3D
$GPRMC,205223.743,A,3320.3039,N,08646.7474,W,2.11,49.25,200316,,,A*41
$GPVTG,49.25,T,,M,2.11,N,3.9,K,A*3F
$GPGGA,205224.743,3320.3077,N,08646.7421,W,1,04,7.4,80.5,M,-29.1,M,,0000*5D
$GPGSA,A,3,23,09,08,07,,,,,,,,,7.8,7.4,2.6*3D
$GPRMC,205224.743,A,3320.3077,N,08646.7421,W,0.24,49.25,200316,,,A*48
$GPVTG,49.25,T,,M,0.24,N,0.4,K,A*35
$GPGGA,205225.743,3320.3062,N,08646.7444,W,1,04,7.4,87.1,M,-29.1,M,,0000*58
$GPGSA,A,3,23,09,08,07,,,,,,,,,7.8,7.4,2.6*3D
$GPRMC,205225.743,A,3320.3062,N,08646.7444,W,0.88,49.25,200316,,,A*48
$GPVTG,49.25,T,,M,0.88,N,1.6,K,A*30
$GPGGA,205226.743,3320.2993,N,08646.7560,W,1,04,7.4,102.4,M,-29.1,M,,0000*63
$GPGSA,A,3,23,09,08,07,,,,,,,,,7.8,7.4,2.6*3D
$GPRMC,205226.743,A,3320.2993,N,08646.7560,W,1.41,48.98,200316,,,A*49
$GPVTG,48.98,T,,M,1.41,N,2.6,K,A*30
$GPGGA,205227.743,3320.2751,N,08646.8022,W,1,05,2.8,116.5,M,-29.1,M,,0000*62
$GPGSA,A,3,23,27,09,08,07,,,,,,,,3.8,2.8,2.6*35
$GPRMC,205227.743,A,3320.2751,N,08646.8022,W,1.68,49.11,200316,,,A*4F
$GPVTG,49.11,T,,M,1.68,N,3.1,K,A*3D
$GPGGA,205228.743,3320.2493,N,08646.8520,W,1,05,2.8,128.0,M,-29.1,M,,0000*6F
$GPGSA,A,3,23,27,09,08,07,,,,,,,,3.8,2.8,2.6*35
$GPRMC,205228.743,A,3320.2493,N,08646.8520,W,0.35,49.11,200316,,,A*43
$GPVTG,49.11,T,,M,0.35,N,0.7,K,A*31
$GPGGA,205229.743,3320.2420,N,08646.8655,W,1,05,2.8,130.5,M,-29.1,M,,0000*6B
$GPGSA,A,3,23,27,09,08,07,,,,,,,,3.8,2.8,2.6*35
$GPRMC,205229.743,A,3320.2420,N,08646.8655,W,0.21,49.11,200316,,,A*4E
$GPVTG,49.11,T,,M,0.21,N,0.4,K,A*37
$GPGGA,205230.743,3320.2406,N,08646.8679,W,1,05,2.8,130.0,M,-29.1,M,,0000*6C
$GPGSA,A,3,23,27,09,08,07,,,,,,,,3.8,2.8,2.6*35
$GPRMC,205230.743,A,3320.2406,N,08646.8679,W,0.73,49.11,200316,,,A*4B
$GPVTG,49.11,T,,M,0.73,N,1.4,K,A*31
$GPGGA,205231.743,3320.2402,N,08646.8685,W,1,05,2.8,132.0,M,-29.1,M,,0000*68
$GPGSA,A,3,23,27,09,08,07,,,,,,,,3.8,2.8,2.6*35
$GPRMC,205231.743,A,3320.2402,N,08646.8685,W,0.29,49.11,200316,,,A*42
$GPVTG,49.11,T,,M,0.29,N,0.5,K,A*3E

```

## Accepted answer (score 5, by Adam Davis)

This is standard NMEA data format. The GPS is configured to provide the following NMEA strings:

- GPGGA, Essential fix data, time, location, quality of fix, altitude
- GPGSA, Dilution of precision and active satellites
- GPRMC, Recommended minimum data: position, velocity, vector, time
- GPVTG, Velocity and vector

You'll notice much of the information is redundant, time occurs in many sentences, so does position. The original design of the NMEA communications standard allowed many devices to connect to one common data bus and listen only for those sentences they need, and provide only those sentences they had available. Some devices didn't calculate vector and velocity, so never provided more than the GGA and GSA sentences. Now almost all GPS units deliver most of the possible GPS sentences, but they are configurable so you can turn some sentences on or off depending on your needs.

The essential NMEA API is sentence based. The $ starts a sentence, and the *xx ends it, with xx being a checksum. Each device has a two letter prefix, GP for GPS units, and a three letter suffix for the sentence type. There are further interesting things about the standard, but they are not necessary to understand your data. See http://www.gpsinformation.org/dale/nmea.htm for more detail, but here's the interpretation of the first four entries, which comprise one data point, of your data:

#### $GPGGA,205221.743,3320.2409,N,08646.8572,W,1,04,10.5,170.1,M,-29.1,M,,0000*51

```
Where:
GGA          Global Positioning System Fix Data
 205221.743   Fix taken at 20:52:21.743 UTC
 3320.2409,N  Latitude 33 deg 20.2409' N
 08646.8572,W Longitude 8 deg 46.8572' W
 1            Fix quality: 0 = invalid
 1 = GPS fix (SPS)
 2 = DGPS fix
 3 = PPS fix
 4 = Real Time Kinematic
 5 = Float RTK
 6 = estimated (dead reckoning) (2.3 feature)
 7 = Manual input mode
 8 = Simulation mode
 04           Number of satellites being tracked
 10.5         Horizontal dilution of position
 170.1,M      Altitude, Meters, above mean sea level
 -29.1,M      Height of geoid (mean sea level) above WGS84 ellipsoid
(empty)      Time in seconds since last DGPS update
 0000         DGPS station ID number
*51          the checksum data, always begins with *

```

#### $GPGSA,A,3,23,09,08,07,,,,,,,,,11.5,10.5,4.6*36

```
Where:
GSA      Satellite status
A        Auto selection of 2D or 3D fix (M = manual)
 3        3D fix - values include: 1 = no fix
 2 = 2D fix
 3 = 3D fix
 23,9,8,7,... PRNs of satellites used for fix (space for 12)
 11.5     PDOP (dilution of precision)
 10.5     Horizontal dilution of precision (HDOP)
 4.6      Vertical dilution of precision (VDOP)
*36      the checksum data, always begins with *

```

#### $GPRMC,205221.743,A,3320.2409,N,08646.8572,W,1.64,49.17,200316,,,A*4D

```
Where:
RMC          Recommended Minimum sentence C
 205221.743   Fix taken at 20:52:21.743 UTC
A            Status A=active or V=Void.
 3320.2409,N  Latitude 33 deg 20.2409' N
 08646.8572,W Longitude 8 deg 46.8572' W
 1.64         Speed over the ground in knots
 49.17        Track angle in degrees True
 200316       Date - 20th of March 2016
(empty),(empty) Magnetic Variation
A            Fix type (NMEA 2.3, not included on older receivers):
A=autonomous
D=differential
E=Estimated
N=Not Valid
S=Simulated
*6A          The checksum data, always begins with *

```

#### $GPVTG,49.17,T,,M,1.64,N,3.0,K,A*36

```
where:
VTG          Track made good and ground speed
 49.17,T      True track made good (degrees)
(empty),M    Magnetic track made good
 1.64,N       Ground speed, knots
 3.0,K        Ground speed, Kilometers per hour
A            Fix type (NMEA 2.3, not included on older receivers):
A=autonomous
D=differential
E=Estimated
N=Not Valid
S=Simulated
*48          Checksum

```

Of course you don't have to use all of these. A quick way to interpret the data is to load it all into excel as comma delimited, then extract the data you need.

Of course many programs support this data directly. For instance, Google Earth imports these files using these instructions, under "Importing GPS Data".

It's a very commonly used GPS data format, so while it may not be immediately obvious, most mapping software will have a way to import and use it.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5957/how-to-read-id-51a-gps-logger-data, by Daniel, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
