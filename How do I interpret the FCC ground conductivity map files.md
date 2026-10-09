# How do I interpret the FCC ground conductivity map files?

*Tags: grounding, earth · score 5*

## Question

The FCC has .seq files that show ground conductivity which it makes available for download. Unfortunately, there doesn't appear to be any documentation that comes with the files, or even headers.

I can make an educated guess that there are two longitudes/latitudes for each record, and the last two numbers represent perhaps a range of ground conductivity. What is the meaning of each field? Is there anywhere I can learn more?

## Accepted answer (score 5, by user3486184)

Here are the fields for AM_conductivity_m3.seq_.txt and AM_conductivity_m3hw.seq_.txt files:

```
4001   21.5750  158.2760   21.5840  158.1900    2.00 5000.00

```

Fields, left to right:

1. The number of the line segment.
2. The north latitude of the start of the segment.
3. The west longitude of the start of the segment.
4. The north latitude of the end of the segment.
5. The west longitude of the end of the segment.
6. The immediate ground conductivity east of this segment (north conductivity for exact east-west lines) in mS/m.
7. The immediate ground conductivity west of this segment (south conductivity for exact east-west lines) in mS/m.

I think I also understand the 9999 lines:

```
9999  466.0000   19.0000  160.0000   24.0000  152.00   98.00

```

Fields, left to right:

1. The number 9999 indicates the start of a region.
2. The number of records (excluding the 9999) for that region.
3. The north latitude of the lower left corner of a box bounding the region.
4. The west longitude of the lower left corner of a box bounding the region.
5. The north latitude of the upper right corner of a box bounding the region.
6. The west longitude of the upper right corner of a box bounding the region.
7. The index number of the region (1.00, 2.00, 3.00...etc.). The file AM_conductivity_m3.seq_.txt contains regions 1-97, and the Hawaii file AM_conductivity_m3hw.seq_.txt has region 98.

Just for completeness, 9998:

```
9998    1.0000    1.0000    1.0000    1.0000    1.00    1.00

```

9998 is indeed an end-of-file, with dummy values of 1 in all fields.

Here are the fields for AM_conductivity_r2.seq_.txt file:

```
 11   2  5000.0    1.0  BROCK ISLAND
 77.873115.027  77.905115.060  77.930115.181  77.935115.192  77.942115.126
 77.940115.071    .000   .000    .000   .000    .000   .000    .000   .000

```

1. Region number.
2. Number of following lines containing points for that region.
3. Conductivity on one side of the line defined by the points (mS/m).
4. Conductivity on the other side of the line defined by the points (mS/m).
5. Name of the region.
6. List of points in XX.XXX north latitude, YY.YYY west longitude. (So 77.101120.133 means 77.101 N, 120.133 W.) Points with value .000 should be ignored. Negative values are S or E.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14792/how-do-i-interpret-the-fcc-ground-conductivity-map-files, by user3486184. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
