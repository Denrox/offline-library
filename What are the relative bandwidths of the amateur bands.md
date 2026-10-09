# What are the relative bandwidths of the amateur bands?

*Tags: united-states, hf, bandwidth · score 12*

## Question

While I was operating on 40 m for Field Day, I noticed a higher SWR than when I first set my antenna tuner for the band. This happened, of course, because I was in a different part of the band, but I hadn’t done enough HF operation to expect the result automatically.

80 m is famously so wide that the phone segment of it gets called “75 meters” because the difference matters for antenna design.

I’ve heard that what matters for antenna and electronic design is the relative bandwidth — the ratio of the low and the high ends. I’d like to see what this ratio is for *all* of the amateur bands, and just how much of an outlier 80 m is or isn't.

## Accepted answer (score 11, by Kevin Reid AG6YO)

The usual figure used in this context is, apparently, *fractional bandwidth*, defined as the bandwidth divided by the center frequency, and therefore having a range of 0 to 2.

$$ \text{fractional bandwidth} \,=\, \frac{f_{\text{max}} - f_{\text{min}}}{f_{\text{center}}} \,=\, 2\frac{f_{\text{max}} - f_{\text{min}}}{f_{\text{max}} + f_{\text{min}}} $$

Given that definition, and using the United States band edges, here are the fractional (and absolute) bandwidths of all amateur bands:

This chart was generated using a gnuplot program which can be found in the source of this answer.

## Answer (score 3, by Keith Martineau)

Here is a chart I made. Hope you find it useful. The numbers are approximate and it depends on your exact method of calculation. I use percentages because that information is easier to find or calculate. This chart is the average percentage using the center frequency (I also have numbers related to each band edge). A lot of people quote a "good" or "well designed" or "average" antenna as having about 10% bandwidth, but it varies a LOT with the exact antenna type in use. The "notoriously wide" bands are 160M, 80M, 10M (despite the smaller numbers), and I would add 6M and 70Cm.

```
 160M 10.55%
 80M 13.39%
 60M  1.36%
 40M  4.2%
 30M   .49%
 20M  2.47%
 17M   .55%
 15M  2.12%
 12M   .4%
 10M  5.9%
 6M  7.7%
 2M  2.74%
1.75M  2.7%
 70Cm  6.9%
 33Cm  2.84%
 23Cm  4.73%

```

## Answer (score 2, by Keith Martineau)

The bandwidth is often quoted as a percent of the difference between the "center frequency" and the "band edges" or the difference between the "band edges". Band edge can be defined in several ways (-3Db point, pattern degradation, or some other requirement, to name a few). Because of the mathematical relationship, the lower frequencies (with smaller numbers, in terms of Mhz) are wider due to even a small difference in frequency (at the band edges compared the the center frequency) is a significant percentage of the center frequency so they are at a disadvantage from the beginning. Since 80 Meters has a relatively wide (compared to the center frequency) bandwidth in the USA it is an outlier. Also note that the center frequency method of design is not the best. The geometric mean more closely aligns the results in the band due to the difference between the center frequency and "lower" band edge, compared to the difference between the center frequency and the "upper" band edge. The percentages are NOT the same. Using the geometric mean helps the design work nearer the same at the top and bottom band edges.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5084/what-are-the-relative-bandwidths-of-the-amateur-bands, by Kevin Reid AG6YO, Keith Martineau. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
