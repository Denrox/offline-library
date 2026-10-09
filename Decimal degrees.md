# Decimal degrees

**Decimal degrees** (**DD**) is a notation for expressing [latitude](Latitude.md) and [longitude](Longitude.md) [geographic coordinates](Geographic%20coordinate%20system.md) as decimal fractions of a degree. DD are used in many geographic information systems (GIS), web mapping applications such as OpenStreetMap, and [GPS](Global%20Positioning%20System.md) devices. Decimal degrees are an alternative to using degrees-minutes-seconds (DMS) notation. As with latitude and longitude, the values are bounded by ±90° and ±180° respectively.

Positive latitudes are north of the equator, negative latitudes are south of the equator. Positive longitudes are east of the Prime Meridian; negative longitudes are west of the Prime Meridian. Latitude and longitude are usually expressed in that sequence, latitude before longitude. The abbreviation [dLL] has been used in the scientific literature with locations in texts being identified as a tuple within square brackets, for example [54.5798, -3.5820]. The appropriate decimal places are used, negative values are given using a hyphen-minus character. The designation of a location as, for example [54.1855, -2.9857] means that it is potentially computer searchable and that it can be located by a generally (open) referencing system such as Google Earth or OpenStreetMap. Four decimal places is usually sufficient for most locations, although for some sites, for example surface exposure dating, five or even six decimal places should be used.

The [dLL] format can be used within publications to specify points or features of interest and within remote sensing to identify ground truth locations within Digital Earth and complying within the FAIR data principles. The format can also be used as a starting point for a traverse or transect. With the increase in scientific papers needing to be searched for words, terms, phrases, authors and data, the [dLL] format can be used to link terms to author name (and by ORCID), place-label location and journal or publication.

### Precision

The radius of the semi-major axis of the Earth at the equator is 6,378,137.0 metres (20,925,646.3 ft) resulting in a circumference of 40,075,016.7 metres (131,479,714 ft). The equator is divided into 360 degrees of longitude, so each degree at the equator represents 111,319.5 metres (365,221 ft). As one moves away from the equator towards a pole, however, one degree of longitude is multiplied by the cosine of the latitude, decreasing the distance, approaching zero at the pole. The number of decimal places required for a particular precision at the equator is:

Degree precision versus length
- decimal  
places  decimal  
degrees  DMS  Object that can be *unambiguously* recognized at this scale  N/S or E/W  
at equator  E/W at  
23N/S  E/W at  
45N/S  E/W at  
67N/S
- 0   1.0  1° 00′ 0″  country or large region  111 km  102 km  78.7 km  43.5 km
- 1   0.1  0° 06′ 0″  large city or district  11.1 km  10.2 km  7.87 km  4.35 km
- 2   0.01  0° 00′ 36″  town or village  1.11 km  1.02 km  0.787 km  0.435 km
- 3   0.001  0° 00′ 3.6″  neighborhood, street  111 m  102 m  78.7 m  43.5 m
- 4   0.0001  0° 00′ 0.36″  individual street, large buildings  11.1 m  10.2 m  7.87 m  4.35 m
- 5   0.00001  0° 00′ 0.036″  individual trees, houses  1.11 m  1.02 m  0.787 m  0.435 m
- 6   0.000001  0° 00′ 0.0036″  individual humans  111 mm  102 mm  78.7 mm  43.5 mm
- 7   0.0000001  0° 00′ 0.00036″  practical limit of commercial surveying  11.1 mm  10.2 mm  7.87 mm  4.35 mm
- 8   0.00000001   0° 00′ 0.000036″   specialized surveying  1.11 mm  1.02 mm  0.787 mm  0.435 mm

A value in decimal degrees to a precision of 4 decimal places is precise to 11.1 metres (36 ft) at the equator. A value in decimal degrees to 5 decimal places is precise to 1.11 metres (3 ft 8 in) at the equator. Elevation also introduces a small error: at 6,378 metres (20,925 ft) elevation, the radius and surface distance is increased by 0.001 or 0.1%. Because the earth is not flat, the precision of the longitude part of the coordinates increases the further from the equator you get. The precision of the latitude part does not increase so much, more strictly however, a meridian arc length per 1 second depends on the latitude at the point in question. The discrepancy of 1 second meridian arc length between equator and pole is about 0.3 metres (1 ft 0 in) because the earth is an oblate spheroid.

### Example

A DMS value is converted to decimal degrees using the formula:

$$
\mathrm{D}_\text{dec} = \mathrm{D} + \frac{\mathrm{M}}{60} + \frac{\mathrm{S}}{3600}
$$

For instance, the decimal degree representation for  
38° 53′ 23″ N, 77° 00′ 32″ W

(the location of the United States Capitol) is  
38.8897°, −77.0089°

In most systems, such as OpenStreetMap, the degree symbols are omitted, reducing the representation to  
38.8897, −77.0089

To calculate the D, M and S components, the following formulas can be used:

$$
\begin{align} \mathrm{D} &= \operatorname{trunc}(\mathrm{D}_\text{dec},0) \\ \mathrm{M} &= \operatorname{trunc}(60 \times |\mathrm{D}_\text{dec} - \mathrm{D}|,0) \\ \mathrm{S} &= 3600 \times |\mathrm{D}_\text{dec} - \mathrm{D}| - 60 \times \mathrm{M} \end{align}
$$

where $$\mathrm{\left\vert D_{dec} - D \right\vert}$$ is the absolute value of $$\mathrm{ D_{dec} - D }$$ and $$\mathrm{trunc}$$ is the truncation function. Note that with this formula only $$\mathrm{D}$$ can be negative and only $$\mathrm{S}$$ may have a fractional value.

---

*Source: Wikipedia, Decimal degrees (https://en.wikipedia.org/wiki/Decimal_degrees), by Wikipedia contributors, CC BY-SA 4.0.*
