# How do I make a RF propagation map for a repeater?

*Tags: propagation, repeater, map, repeater-coverage · score 21*

## Question

Let's say I have a repeater. Knowing all of the information about antenna height and gain in each direction, as well as power, how can I create a map similar to this map I saw of a repeater in Illinois?

Free options are always better!

## Accepted answer (score 12, by W8AWT)

Although much of the main page is not written in English, after you login most of the site is and the RMO Repeater coverage map maker is a wonderful and highly customizable tool even for multi-site repeaters.

VA3XPR.Net: Three easy steps to creating RF coverage maps like a pro:

Radio Mobile Online is a radio wave propagation prediction tool created and maintained by Roger Coudé, VE2DBE, which is dedicated for use by the ham radio community. As indicated on the Radio Mobile Online website, it uses digital terrain information and a mathematical model to simulate radio transmissions between two fixed sites or between a fixed site and a mobile. The digital terrain information comprises three databases: ground elevation, land cover, and population density, which combined total 200 GB of information.

To generate an RF coverage map using Radio Mobile Online, all you need to do if follow the three easy steps below.

1. Create an account with Radio Mobile

Go to the Radio Mobile Online website and create a free account. You can do this by providing your name or callsign and email address. Once you enter this information, you will receive your password to enter the site via the email address you provided during registration.

1. Plot your transmitter location

Once you have created your account and logged into Radio Mobile Online, you will now seen a menu on items on the left side of the page. Before we can create any RF coverage maps, we first need to define the location of the transmitter that we want to determine coverage for. To do this, simple select the “New Site” option in the menu.

Create a Site

You will now see a map of the world and a red pin on it. There are two mays to plot your location on map – either by directly entering the latitude and longitude into the fields provided or by iteratively moving the pin on the map and zooming in until you locate the pin on your desired location. You can switch the map to Ssatellite view if you want to see the actual building or tower that you want to set as your transmitter location. Once you have placed the pin at your desired location, click “Submit”

Site map plot

1. Create a RF coverage map

Once you have defined your transmitter location, it is now time time create a RF coverage map for that location. To do this, select the “New Coverage” option in the menu. You will now see a number of data fields that you’ll need to complete with some already containing default values. An explanation of each of these is below.

Centre Site – this is the location of your transmitter. Select your location using the pull down menu.

Antenna Height – this is the height of your antenna above the ground at that specific location. Please note that this is in metres and if you want to convert your height in feet, divide the value by 3.2808 (i.e. 100 ft = 30.48 m).

Antenna Type – this is the type of antenna that you will be using at the transmitter location. Unless you’ll be using an antenna with an offset gain, you should just use the default omnidirectional, or “Omni” setting.

Antenna Azimuth – this is the direction that your antenna will be pointing, with 0° being north. This value is only important if you are using an antenna with an offset gain value, as it would not have any impact for an omnidirectional antenna.

Antenna Tilt – this is the angle of radiation of your antenna with 0° point towards the horizon. Some antennas have a higher gain value point slightly upwards or downwards, so this setting can be used to address this.

Antenna Gain – this is the amount of gain for your specific antenna. To find out the gain value for your antenna, you may need to check the specifications that are published for it by the manufacturer. Please note that the value for this field is in dBi (isotropic) – if your antenna has a dBd (dipole) value, you can covert dBd to dBi by adding 2.15 dBi (i.e. 5 dBd = 7.15 dBi).

Mobile Antenna Height – this is the height of the receiving antenna on the mobile station that will be used to determine your coverage area. Again, please note that this is in metres and if you want to convert your height in feet, divide the value by 3.2808 (i.e. 10 ft = 3.48 m).

Mobile Antenna Gain – this is the gain of the receiving antenna on the mobile station that will be used to determine your coverage area. Please note that the value for this field is in dBi (isotropic) – if your antenna has a dBd (dipole) value, you can covert dBd to dBi by adding 2.15 dBi (i.e. 5 dBd = 7.15 dBi).

Frequency – this is the frequency that your transmitter will use. Radio Mobile Online allows frequencies to be used within amateur radio bands from 10 MHz to 250 GHz.

TX Power – this is the power output of your transmitter in Watts.

TX Line Loss – this is the power loss in your feed line cable between the transmitter and antenna at your transmitter location. The longer the feed line, the higher this value will be. To find the value, you should check with the cable manufactures specification for your feed line and calculate the total loss based upon the length of your cable. For added precision, you can also include the power loss in your connectors as well.

RX Line Loss – this is the signal loss of the feed line for your receiving station in dBi.

RX Threshold – this is the lowest signal level that the coverage map will display. While most radios have better receive sensitivity than this, this value will provide a good indication for coverage for all radios, including older one with less sensitive receivers.

Required Reliability – this figure displays the reliability to which the coverage is likely to experience. For more accurate coverage maps, you can increase this value, however the resulting coverage area will less.

Maximum Range – this value defines the limit of the coverage analysis. If you expect coverage beyond 100 km, then increase this value to show coverage beyond 100 km. Please note that if you want to convert from miles to kms, multiply by 1.6 (i.e. 100 mi = 160 km).

Once you have entered all of this information, Radio Mobile Online will begin generating the RF coverage map for your transmitter location. Depending on the details entered and the time of day to which you have requested the RF coverage map to be generated, it may take anywhere from a few minutes to 20 minutes to produce the coverage map. Once it’s complete, a map will appear displaying your RF coverage area. To save this RF coverage map, click “Add to my coverages”.

One important note for coverage maps being generated in major cities is that Radio Mobile Online does not have building information included in its database, so the coverage maps it produces will not reflect the impact of buildings on the signals proportion. The result of this will be coverage maps that are not representative of the actual signal levels that a users may experience, especially in urban areas.

So there you go – you’re now on your way to creating professional looking RF coverage maps that can be used to determine how good that proposed repeater site will be that can shared with friends or posted online.

## Answer (score 10, by Adam Davis)

SPLAT! is an RF Signal Propagation, Loss, And Terrain analysis tool for the electromagnetic spectrum between 20 MHz and 20 GHz. It is free and open source, and there are builds for Windows and Mac if you don't want to compile from source on linux yourself. I haven't used it, so I can't speak to ease of use, but it should generate propagation maps based on elevation models and RF propagation characteristics. However it will probably not generate nice map imagery as above since it cannot integrate Google maps or a similar mapping source. Perhaps it can output KML files for use with Google Earth.

Two groups have made free simple web interfaces for SPLAT!:

- http://splat.ecok.edu/ecuindex.html (generates image and KML for Google Earth viewing)
- http://splat.wa7uhf.com/ (??? Not responding at the moment)

The image in your question was generated from CloudRF - a web service based largely on SPLAT!. CloudRF does have a web interface for generating such maps, and does have a free trial, which may meet your needs without installing and learning SPLAT!. Since CloudRF is built on SPLAT! and thus subject to the open source license SPLAT! was released under, the server backend is largely opensource. I believe the map shown was generated using the Keyhole Radio package, which is a client side helper that uses Google Earth along with the CloudRF servers to generate such maps from KML files generated by CloudRF.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1921/how-do-i-make-a-rf-propagation-map-for-a-repeater, by Skyler 440, W8AWT, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
