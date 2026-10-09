# How can one convert from Lat/Long to Grid Square?

*Tags: location, maidenhead-locator · score 29*

## Question

I see that many contests, awards, and other items, use Grid Squares as a means to identify where one is. How can one figure out what one's grid square is, given lat/long?

## Accepted answer (score 29, by PearsonArtPhoto)

First of all, if you don't want to do any math, then check out a grid square map, such as this one.

There is an excellent process at this page, and additional resources from ARRL. Essentially, Grid Squares contain 3 pairs, the first and last letters, and the middle numbers. Longitude is always the first, followed by latitude, for each pair. For simplicity, let's assume that West and South are negative lat/long, as is a common convention. For example purposes, I'm going to use 32.123 W, 14.321 N. The key thing is to do the following.:

**Longitude**

1. Add 180 to the longitude, and take the integer value /20, and add one. Then figure out which letter of the alphabet that corresponds to, usually written in upper case. The example will be 147.877/20=7. Adding one will give the 8th letter of the alphabet, or H. Note 7.877 is remaining.
2. Take the remainder of what is left, and divide by 2, rounding down. This is the number, no conversion required. The example will give a value of 3. Note 1.877 is remaining.
3. Take the remainder that is left, and multiply by 12, and add one. Round down to the nearest integer.. This is the letter of the alphabet, usually written in lower case. The example gives a value of 22+1=23. This will be the letter w.

**Latitude**

1. Add 90 to the longitude, and take the integer value /10, and add one. Then figure out which letter of the alphabet that corresponds to, usually written in upper case. The example will be 104.321/10=10. Adding one will give the 11th letter of the alphabet, or K. Note 4.321 is remaining.
2. Take the remainder of what is left, and round down. This is the number, no conversion required. The example will give a value of 4. Note 0.321 is remaining.
3. Take the remainder that is left, and multiply by 24, and add one. Round down to the nearest integer.. This is the letter of the alphabet, usually written in lower case. The example gives a value of 7+1=8. This will be the letter h.

Putting them together by pairs, and alternating first longitude then latitude, gives the grid square for 32.123 W, 14.321 N to be HK34wh.

## Answer (score 9, by Walter Underwood K6WRU)

If you'd like to do it yourself, you can use this Python program I wrote.

```
# -*- coding: utf-8 -*-

import sys

# Convert latitude and longitude to Maidenhead grid locators.
#
# Arguments are in signed decimal latitude and longitude. For example,
# the location of my QTH Palo Alto, CA is: 37.429167, -122.138056 or
# in degrees, minutes, and seconds: 37° 24' 49" N 122° 6' 26" W

upper = 'ABCDEFGHIJKLMNOPQRSTUVWX'
lower = 'abcdefghijklmnopqrstuvwx'

def to_grid(dec_lat, dec_lon):
if not (-180<=dec_lon<180):
sys.stderr.write('longitude must be -180<=lon<180, given %f\n'%dec_lon)
sys.exit(32)
if not (-90<=dec_lat<90):
sys.stderr.write('latitude must be -90<=lat<90, given %f\n'%dec_lat)
sys.exit(33) # can't handle north pole, sorry, [A-R]

adj_lat = dec_lat + 90.0
adj_lon = dec_lon + 180.0

grid_lat_sq = upper[int(adj_lat/10)];
grid_lon_sq = upper[int(adj_lon/20)];

grid_lat_field = str(int(adj_lat%10))
grid_lon_field = str(int((adj_lon/2)%10))

adj_lat_remainder = (adj_lat - int(adj_lat)) * 60
adj_lon_remainder = ((adj_lon) - int(adj_lon/2)*2) * 60

grid_lat_subsq = lower[int(adj_lat_remainder/2.5)]
grid_lon_subsq = lower[int(adj_lon_remainder/5)]

return grid_lon_sq + grid_lat_sq + grid_lon_field + grid_lat_field + grid_lon_subsq + grid_lat_subsq

def usage():
print 'This script takes two arguments, decimal latitude and longitude.'
print 'Example for Newington, Connecticut (W1AW):'
print 'python maidenhead.py 41.714775 -72.727260'
print 'returns: FN31pr'

def test():
# First four test examples are from "Conversion Between Geodetic and Grid Locator Systems",
# by Edmund T. Tyson N5JTY QST January 1989
test_data = (
('Munich', (48.14666,11.60833), 'JN58td'),
('Montevideo', (-34.91,-56.21166), 'GF15vc'),
('Washington, DC', (38.92,-77.065), 'FM18lw'),
('Wellington', (-41.28333,174.745), 'RE78ir'),
('Newington, CT (W1AW)', (41.714775,-72.727260), 'FN31pr'),
('Palo Alto (K6WRU)', (37.413708,-122.1073236), 'CM87wj'),
)
print 'Running self test\n'
passed = True
for name,latlon,grid in test_data:
print 'Testing %s at %f %f:'%(name,latlon[0],latlon[1])
test_grid = to_grid(latlon[0], latlon[1])
if test_grid != grid:
print 'Failed '+test_grid+' should be '+grid
passed = False
else:
print 'Passed '+test_grid
print ''
if passed: print 'Passed!'
else: print 'Failed!'

def main(argv=None):
if argv is None: argv = sys.argv
if len(argv) != 3:
usage()
print ''
test()
else:
print to_grid(float(argv[1]),float(argv[2]))

main()

```

## Answer (score 7, by Ossi Väänänen)

My first post in SO. Here's a C version... made this for an Arduino project.

```
void calcLocator(char *dst, double lat, double lon) {
int o1, o2, o3;
int a1, a2, a3;
double remainder;
// longitude
remainder = lon + 180.0;
o1 = (int)(remainder / 20.0);
remainder = remainder - (double)o1 * 20.0;
o2 = (int)(remainder / 2.0);
remainder = remainder - 2.0 * (double)o2;
o3 = (int)(12.0 * remainder);

// latitude
remainder = lat + 90.0;
a1 = (int)(remainder / 10.0);
remainder = remainder - (double)a1 * 10.0;
a2 = (int)(remainder);
remainder = remainder - (double)a2;
a3 = (int)(24.0 * remainder);
dst[0] = (char)o1 + 'A';
dst[1] = (char)a1 + 'A';
dst[2] = (char)o2 + '0';
dst[3] = (char)a2 + '0';
dst[4] = (char)o3 + 'A';
dst[5] = (char)a3 + 'A';
dst[6] = (char)0;
}

```

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/221/how-can-one-convert-from-lat-long-to-grid-square, by PearsonArtPhoto, Walter Underwood K6WRU, Ossi Väänänen. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
