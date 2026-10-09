# APT/LRPT images geotagging

*Tags: satellites · score 7*

## Question

I want to extend functionality of some open-source programs which decode APT and LRPT images (wxapt and glrpt). More specifically I want to add possibility to overlay geographical data such as land borders, administrative borders, rivers etc on the resulting images after rectification. The same functionality exists in WXtoIMG software and it works only if you have updated Keplers list. I assume that received APT data (e. g. recorded with GQRX and then processes in Audacity) contains some timestamps (or may be GPS coordinates) and smart programs like WXtoIMG are possible to process this hidden metadata together with TLE data and draw geo objects in overlay.

However I can't find very much info about APT/LRPT protocols. The only thing that I found is that LRPT packets could contain APID 70 data which is satellite's onboard time. Does APT suggests the same data or I should rely on exact computer time and updated TLE?

Another problem is that I can't figure out (yet) how to bind together timestamp info, TLE data and get geographical data for pixels. My suggestion is to find one basis point/pixel on my image which is my ground station (GPS coordinates for ground station are always available) and then, knowing rectified image dimensions and resolution, I could draw geographical data (for example from GADM) in overlay. Is it right approach? I think I can catch moment when satellite transmits image line for my latitude (may be derive it from TLE parameters) but I don't know how to find longitude...

Can anyone suggest something?

**EDIT 1.** Here is my thoughts about how to perform pixel geotagging. Let's assume the following:

Let's take that satellite is passing from South to North at certain angle. It scans Earth surface and sends data as image lines with even interval. So at every time moment $t_i$ we obtain a bunch of image lines, let's say that for time interval $\Delta t = t_{i+1}-t_i$ we have four rows of pixels. This resolution should stay constant during satellite working cycle (I believe it's 4 km/px for NOAA and 1 km/px for Meteor-M series). After image rectification procedure we should get image with even pixel spacing so every pixel shift in image corresponds to the same distance shift in kilometers on Earth surface. Pixels which are nearest to the satellite's pass track projection (dashed red line with "Flight direction" label) will stay (almost) untouched during rectification. Knowing exact timestamps $t_i$ and TLE data we can calculate latitude and longitude of satellite projection on Earth (green pixels on scheme). Then we can calculate latitude and longitude for every pixel in image (orange pixels) with respect to our basis pixels (satellite's projection) and map coordinates to them. After that we just take geographical objects for this area from database and draw borders, rivers etc by just mapping geo coordinates to pixel coordinates. Am i right in these suggestions?

## Answer (score 5, by hobbs - KC2G)

Two resources that might be of use to you:

First, NOAA KLM User's Guide Section 4.2, beginning on page 4-51 (PDF page 225) covers APT. Judging from figure 4.2.2.1, there is no absolute timing or positioning information included in the telemetry data; just some calibration values and the channel ID. The "space and marker" contains a 4-line marker every 1 minute (120 lines). The document doesn't specify what, if anything, the marker is synchronized to, but I would guess that the start of the minute marker corresponds to the start of the UTC minute

Second, there is Spatial Registration of TIROS-N Weather Satellite Data, a thesis from the Air Force Institute of Technology. This states (page 35) "Minute markers are also included in four consecutive lines (two white, two black). While the time of each mark is not specified, limited observation found the start of each minute indistinguishable from the first white line in the four-line sequence", which confirms my guess. This means that you can use the computer clock to *roughly* timestamp the image (so long as the computer is kept within 1 minute of accurate time, which isn't that hard), and use the minute marker from the received signal to refine that timestamp to pixel precision.

I've only scanned the remainder of the thesis, but it looks like it contains all of the math needed to answer your second question — how to transform the satellite ephemeris, the time, and the pixel number within a line to a position on the earth.

## Answer (score 3, by Aleksander Alekseev - R2AUK)

First of all, I would like to applaud your desire to work on this project. I've been using both wxapt and glrpt before and having functionality you've described would be great.

I'm not an expert in APT or LRPT but hopefully some information I have will help you a little. Firstly, there is a free e-book Image Communication on Short Waves by Martin Bruchanov, OK2MNM. If I remember correctly it has some details on APT. Also it worth trying to contact the author. Secondly, not a long time ago Andrew @dernasherbrezon wrote a complete LRPT decoder in Java. His article is in Russian but I believe Google Translate should translate it quite well. Andrew seems to be very interested in decoding images from sattelites in general, it worth trying to e-mail him directly. Also you might find useful the article Decoding digital weather satellite images: the LRPT protocol from Meteor-M2 and the sources it references.

It might happen than nor APT or LRPT has any information that might help to draw a land borders on the image. In this case you can use the location of the receiver and the trajectory of the satellite to approximate which countries should be seen on the image. The information about borders, rivers etc is available in OpenStreetMap. Using edge detection algorithms might help to find shores, although if image contains little but clouds this approach might not work.

In any case I wish you good luck with the project!

## Answer (score 2, by glen_geek)

Overlay mapping to APT images is complicated by at least two factors:


Each scan line (0.25 seconds) is pre-distorted to "approximate" a linear surface rather than a spherical surface


The earth rotates during a satellite pass (perhaps 15 minutes)

In addition to these two factors, some demodulators don't account for doppler shift, which adds a noticeable skew to an image. A Costa's loop AM demodulator phase-locks to the 2400 Hz carrier, which can solve this problem.  
APT predistortion...  
NOAA's NOAA KLM Users Guide shows how each transmitted APT horizontal scan line is pre-distorted so as to "linearize" the resulting image. It is crudely divided into ten segments, but your eye accepts the image to be sorta map-like (figure 4.2.3-1 APT Linearization):  
  
This figure refers to "data points"...these are HRPT 1 km pixels. So at the satellite sub-point in zone 1, each 4 km APT pixel is comprised of four averaged HRPT 1 km pixels.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16163/apt-lrpt-images-geotagging, by Drobot Viktor, hobbs - KC2G, Aleksander Alekseev - R2AUK, glen_geek. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
