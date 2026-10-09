# World Geodetic System

The **World Geodetic System** (**WGS**) is a standard used in cartography, geodesy, and [satellite navigation](Satellite%20navigation.md), including GPS. The current version, **WGS 84**, defines an Earth-centered, Earth-fixed coordinate system and a geodetic datum, and also describes the associated Earth Gravitational Model (EGM) and World Magnetic Model (WMM). The standard is published and maintained by the United States National Geospatial-Intelligence Agency.

### Definition

The coordinate origin of WGS 84 is meant to be located at the Earth's center of mass; the uncertainty is believed to be less than 2 cm.

The WGS 84 meridian of zero longitude is the IERS Reference Meridian, 5.3 arc seconds or 102 metres (335 ft) east of the Greenwich meridian at the latitude of the Royal Observatory. (This is related to the fact that the perpendicular to the local equipotential surface of the gravity field at Greenwich does not point exactly through the Earth's center of mass, but rather "misses west" of the center of mass by about 102 meters.) The longitude positions on WGS 84 agree with those on the older North American Datum 1927 at roughly 85° longitude west, in the east-central United States.

The WGS 84 datum surface is an oblate spheroid with equatorial radius a = 6378137 m at the equator and flattening f = 1⁄298.257223563. The refined value of the WGS 84 gravitational constant (mass of Earth's atmosphere included) is GM = 3.986004418×10 m/s. The angular velocity of the Earth is defined to be ω = 72.92115×10 rad/s.

This leads to several computed parameters such as the polar semi-minor axis b, which equals *a* × (1 − *f*) = 6356752.3142 m, and the first eccentricity squared, *e* = 6.69437999014×10.

### Updates and new standards

The original standardization document for WGS 84 was Technical Report 8350.2, published in September 1987 by the Defense Mapping Agency (which later became the National Imagery and Mapping Agency). New editions were published in September 1991 and July 1997; the latter edition was amended twice, in January 2000 and June 2004. The standardization document was revised again and published in July 2014 by the National Geospatial-Intelligence Agency as NGA.STND.0036. These updates provide refined descriptions of the Earth and realizations of the system for higher precision.

The original WGS84 model had an absolute accuracy of 1–2 meters. WGS84 (G730) first incorporated GPS observations, taking the accuracy down to 10 cm/component rms. All following revisions including WGS84 (G873) and WGS84 (G1150) also used GPS.

WGS 84 (G1762) is the sixth update to the WGS reference frame.

WGS 84 has most recently been updated to use the reference frame **G2296**, which was released on 7 January 2024 as an update to G2139, now aligned to both the ITRF2020, the most recent ITRF realization, and the IGS20, the frame used by the International GNSS Service (IGS). G2139 was aligned with the IGb14 realization of the International Terrestrial Reference Frame (ITRF) 2014 and uses the new IGS Antex standard.

Updates to the original geoid for WGS 84 are now published as a separate Earth Gravitational Model (EGM), with improved resolution and accuracy. Likewise, the World Magnetic Model (WMM) is updated separately. The current version of WGS 84 uses EGM2008 and WMM2025.

Solution for Earth orientation parameters consistent with ITRF2014 is also needed (IERS EOP 14C04).

### Identifiers

Components of WGS 84 are identified by codes in the EPSG Geodetic Parameter Dataset:

- EPSG:4326 – 2D coordinate reference system (CRS)
- EPSG:4979 – 3D CRS
- EPSG:4978 – geocentric 3D CRS
- EPSG:7030 – reference ellipsoid
- EPSG:6326 – horizontal datum

---

*Source: Wikipedia, World Geodetic System (https://en.wikipedia.org/wiki/World_Geodetic_System), by Wikipedia contributors, CC BY-SA 4.0.*
