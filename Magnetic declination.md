# Magnetic declination

**Magnetic declination** (also called **magnetic variation**) is the angle between magnetic north and [true north](True%20north.md) at a particular location on the Earth's surface. The angle can change over time due to polar wandering.

Magnetic north is the direction that the north end of a magnetised [compass](Compass.md) needle points, which corresponds to the direction of the Earth's magnetic field lines. True north is the direction along a meridian towards the geographic North Pole.

Somewhat more formally, Bowditch defines variation as "the angle between the magnetic and geographic meridians at any place, expressed in degrees and minutes east or west to indicate the direction of magnetic north from true north. The angle between magnetic and grid meridians is called grid magnetic angle, grid variation, or grivation."

By convention, declination is positive when magnetic north is east of true north, and negative when it is to the west. *Isogonic lines* are lines on the Earth's surface along which the declination has the same constant value, and lines along which the declination is zero are called *agonic lines*. The lowercase Greek letter δ (delta) is frequently used as the symbol for magnetic declination.

The term *magnetic deviation* is sometimes used loosely to mean the same as magnetic declination, but more correctly it refers to the error in a compass reading induced by nearby metallic objects, such as iron on board a ship or aircraft.

Magnetic declination should not be confused with *magnetic inclination*, also known as magnetic dip, which is the angle that the Earth's magnetic field lines make with the downward side of the horizontal plane.

### Declination change over time and location

Magnetic declination varies both from place to place and with the passage of time. As a traveller cruises the east coast of the United States, for example, the declination varies from 16 degrees west in Maine, to 6 in Florida, to 0 degrees in Louisiana, to 4 degrees east in Texas. The declination at London, UK was zero in early 2020 and fell to one degree west by 2014. Reports of measured magnetic declination for distant locations became commonplace in the 17th century, and Edmund Halley made a map of declination for the Atlantic Ocean in 1700.

In most areas, the spatial variation reflects the irregularities of the flows deep in the Earth; in some areas, deposits of iron ore or magnetite in the Earth's crust may contribute strongly to the declination. Similarly, secular changes to these flows result in slow changes to the field strength and direction at the same point on the Earth.

The magnetic declination in a given area may (most likely will) change slowly over time, possibly as little as 2–2.5 degrees every hundred years or so, depending on where it is measured. For a location close to the pole like Ivujivik, the declination may change by 1 degree every three years. This may be insignificant to most travellers, but can be important if using magnetic bearings from old charts or metes (directions) in old deeds for locating places with any precision.

As an example of how variation changes over time, see the two charts of the same area (western end of Long Island Sound), below, surveyed 124 years apart. The 1884 chart shows a variation of 8 degrees, 20 minutes West. The 2008 chart shows 13 degrees, 15 minutes West.

### Determination

#### Field measurement

The magnetic declination at any particular place can be measured directly by reference to the celestial poles—the points in the heavens around which the stars appear to revolve, which mark the direction of true north and true south. The instrument used to perform this measurement is known as a *declinometer*.

The approximate position of the north celestial pole is indicated by [Polaris](Polaris.md) (the North Star). In the Northern Hemisphere, declination can therefore be approximately determined as the difference between the magnetic bearing and a visual bearing on Polaris. Polaris currently traces a circle 0.73° in radius around the north celestial pole, so this technique is accurate to within a degree. At high latitudes a plumb-bob is helpful to sight Polaris against a reference object close to the horizon, from which its bearing can be taken.

#### Determination from maps

A rough estimate of the local declination (within a few degrees) can be determined from a general isogonic chart of the world or a continent, such as those illustrated above. Isogonic lines are also shown on aeronautical and nautical charts.

Larger-scale local maps may indicate current local declination, often with the aid of a schematic diagram. Unless the area depicted is very small, declination may vary measurably over the extent of the map, so the data may be referred to a specific location on the map. The current rate and direction of change may also be shown, for example in arcminutes per year. The same diagram may show the angle of grid north (the direction of the map's north–south grid lines), which may differ from true north.

On the [topographic maps](Topographic%20map.md) of the U.S. Geological Survey (USGS), for example, a diagram shows the relationship between magnetic north in the area concerned (with an arrow marked "MN") and true north (a vertical line with a five-pointed star at its top), with a label near the angle between the MN arrow and the vertical line, stating the size of the declination and of that angle, in degrees, mils, or both. However, the diagram itself is not an accurate depiction of the stated numerical declination angle, but is intentionally exaggerated by the cartographer for purposes of legibility.

#### Models and software

Worldwide empirical model of the deep flows described above are available for describing and predicting features of the Earth's magnetic field, including the magnetic declination for any given location at any time in a given timespan. One such model is World Magnetic Model (WMM) of the US and UK. It is built with all the information available to the map-makers at the start of the five-year period it is prepared for. It reflects a highly predictable rate of change. For historical data, the IGRF and GUFM models may be used. Tools for using such models include:

- Web apps hosted by the National Geophysical Data Center, a division of the National Oceanic and Atmospheric Administration of the United States.
- C demo program that for WMM by the National Geospatial-Intelligence Agency, along with various other third-party implementations.

The WMM, IGRF, and GUFM models only describe the magnetic field as emitted at the core-mantle boundary. In practice, the magnetic field is also distorted by the Earth crust, the distortion being magnetic anomaly. For more precise estimates, a larger crust-aware model such as the Enhanced Magnetic Model may be used. (See cited page for a comparison of declination contours.)

### Compass declination adjustment

#### Rotating dial compasses

A magnetic compass points to magnetic north, not geographic (true) north. Compasses of the style commonly used for hiking (i.e., baseplate or protractor compass) utilise a dial or bezel which rotates 360 degrees and is independent of the magnetic needle. To manually establish a declination for true north, the bezel is rotated until the desired number of degrees lie between the bezel's designation N (for North) and the direction (east or west) of magnetic north indicated by the polarised tip of the needle (usually painted red). The entire compass is then rotated until the magnetic needle lies within the outlined orienting arrow or box on the bottom of the capsule, and the course heading (in degrees) is displayed at the base of the direction-of-travel arrow on the baseplate. A compass thus adjusted provides a course bearing in relation to true north instead of magnetic north as long as it remains within an area on the same isogonic line.

In the image at the right, the bezel's N has been aligned with the direction indicated by the magnetic end of the compass needle, adjusted for local declination (10 degrees west of magnetic north). The direction-of-travel arrow on the baseplate thus reflects a true north heading.

After determining local declination, a rotating dial compass may be altered to give true north readings by taping or painting a small delta-point or arrowhead on the compass baseplate west or east of magnetic north pointing to true north on the compass bezel. Other compasses of this design utilise an adjustable declination mechanism integrated with the compass bezel, resulting in true north readings each time the needle is aligned with the orienting arrow.

#### Floating magnetic card compasses

Compasses that utilise a floating magnetised dial or card are commonly found in marine compasses and in certain models used for land navigation that feature a lensatic or prismatic sighting system. A floating card compass always gives bearings in relation to magnetic north and cannot be adjusted for declination. True north must be computed by adding or subtracting local magnetic declination. The example on the left demonstrates a typical conversion of a magnetic bearing from a floating card compass to a true bearing by *adding* the magnetic declination. The declination in the example is 14°E (+14°). If, instead, the declination was 14°W (−14°), you would still "add" it to the magnetic bearing to obtain the true bearing: 40°+ (−14°) = 26°.

Conversely, local declination is *subtracted* from a true bearing to obtain a magnetic bearing. With a local declination of 14°E, a true bearing (i.e. obtained from a map) of 54° is converted to a magnetic bearing (for use in the field) by subtracting declination: 54° – 14° = 40°. If the local declination was 14°W (−14°), it is again subtracted from the true bearing to obtain a magnetic bearing: 54°- (−14°) = 68°.

### Navigation

On aircraft or vessels there are three types of [bearing](Bearing%20%28navigation%29.md): true, magnetic, and compass bearing. Compass error is divided into two parts, namely magnetic variation and magnetic deviation, the latter originating from magnetic properties of the vessel or aircraft. Variation and deviation are signed quantities. As discussed above, positive (easterly) *variation* indicates that magnetic north is east of geographic north. Likewise, positive (easterly) *deviation* indicates that the compass needle is east of magnetic north.

Compass, magnetic and true bearings are related by:

$$
\begin{aligned} T &= M + V\\ M &= C + D \end{aligned}
$$

The general equation relating compass and true bearings is

$$
T = C + D + V
$$

Where:

- $$C$$ is Compass bearing
- $$M$$ is Magnetic bearing
- $$T$$ is True bearing
- $$V$$ is magnetic Variation
- $$D$$ is compass Deviation
- $$V<0, D<0$$ for westerly Variation and Deviation
- $$V>0, D>0$$ for easterly Variation and Deviation

For example, if the compass reads 32°, the local magnetic variation is −5.5° (i.e. West) and the deviation is 0.5° (i.e. East), the true bearing will be:

$$
T = 32^\circ + (-5.5^\circ) + 0.5^\circ = 27^\circ
$$

To calculate true bearing from compass bearing (and known deviation and variation):

- Compass bearing + deviation = magnetic bearing
- Magnetic bearing + variation = true bearing

To calculate compass bearing from true bearing (and known deviation and variation):

- True bearing - variation = Magnetic bearing
- Magnetic bearing - deviation = Compass bearing

These rules are often combined with the mnemonic "West is best, East is least"; that is to say, add W declinations when going from True bearings to Magnetic bearings, and subtract E ones.

Another simple way to remember which way to apply the correction for continental USA is:

- For locations east of the agonic line (zero declination), roughly east of the Mississippi: the magnetic bearing is always bigger.
- For locations west of the agonic line (zero declination), roughly west of the Mississippi: the magnetic bearing is always smaller.

Common abbreviations are:

- TC = true course
- V = variation (of the Earth's magnetic field);
- MC = magnetic course (what the course would be in the absence of local deviation)
- D = deviation caused by magnetic material (mostly iron and steel) on the vessel
- CC = compass course

#### Deviation

Magnetic deviation is the angle from a given magnetic bearing to the related bearing mark of the compass. Deviation is positive if a compass bearing mark (e.g., compass north) is right of the related magnetic bearing (e.g., magnetic north) and vice versa. For example, if the boat is aligned to magnetic north and the compass' north mark points 3° more east, deviation is +3°. Deviation varies for every compass in the same location and depends on such factors as the magnetic field of the vessel, wristwatches, etc. The value also varies depending on the orientation of the boat. Magnets and/or iron masses can correct for deviation, so that a particular compass accurately displays magnetic bearings. More commonly, however, a correction card lists errors for the compass, which can then be compensated for arithmetically. Deviation must be added to compass bearing to obtain magnetic bearing.

#### Air navigation

Air navigation is based on magnetic directions thus it is necessary to periodically revise navigational aids to reflect the drift in magnetic declination over time. This requirement applies to VOR beacons, runway numbering, airway labeling, and aircraft vectoring directions given by air traffic control, all of which are based on magnetic direction.

Runways are designated by a number between 01 and 36, which is generally one tenth of the magnetic [azimuth](Azimuth.md) of the runway's heading: a runway numbered 09 points east (90°), runway 18 is south (180°), runway 27 points west (270°) and runway 36 points to the north (360° rather than 0°). However, due to magnetic declination, changes in runway designators have to occur at times to keep their designation in line with the runway's magnetic heading. An exception is made for runways within the Northern Domestic Airspace of Canada; these are numbered relative to true north because proximity to the magnetic North Pole makes the magnetic declination large and changes in it happen at a high pace.

Radionavigation aids located on the ground, such as VORs, are also checked and updated to keep them aligned with magnetic north to allow pilots to use their magnetic compasses for accurate and reliable in-plane navigation.

For simplicity aviation sectional charts are drawn using true north so the entire chart need not be rotated as magnetic declination changes. Instead individual printed elements on the chart (such as VOR compass roses) are updated with each revision of the chart to reflect changes in magnetic declination. For an example refer to the sectional chart slightly west of Winston-Salem, North Carolina in March 2021, magnetic north is 8 degrees west of true north (Note the dashed line marked 8°W).

When plotting a course, some small aircraft pilots may plot a trip using true north on a sectional chart (map), then convert the true north bearings to magnetic north for in-plane navigation using the magnetic compass. These bearings are then converted on a pre-flight plan by adding or subtracting the local variation displayed on a sectional chart.

GPS systems used for aircraft navigation also display directions in terms of magnetic north even though their intrinsic coordinate system is based on true north. This is accomplished by means of lookup tables inside the GPS which account for magnetic declination. If flying under visual flight rules it is acceptable to fly with an outdated GPS declination database however if flying IFR the database must be updated every 28 days per FAA regulation.

As a fail-safe even the most advanced airliner will still have a magnetic compass in the cockpit. When onboard electronics fail, pilots can still rely on the magnetic compass.

---

*Source: Wikipedia, Magnetic declination (https://en.wikipedia.org/wiki/Magnetic_declination), by Wikipedia contributors, CC BY-SA 4.0.*
