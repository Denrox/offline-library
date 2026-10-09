# Spacing between elements on a Yagi antenna

*Tags: antenna, yagi, antenna-theory · score 3*

## Question

Does anyone know what the spacing between elements on a beam antenna should be? I built a 146 MHz 3 element beam following instructions, and the spacing was 16" between the driven element and the reflector and 20" between the driven element and the director. I was just wondering how you determine the proper spacing between elements; is there any set formula you use to determine boom length, element spacing, etc. that you can use to design a yagi? If anyone can tell me, I would really appreciate it.

## Accepted answer (score 8, by Xevious)

It would be nice to think that there is simple formula or algorithm that one could plug the frequency and desired gain into, and out would come the required element spacings.

The reality is that the math is difficult - requiring the solution of many simultaneous equations - and the results may still not absolutely mirror reality due to variations in materials.

Most Yagi-Uda designs are based on empirical methods and often use pre-tested models such as those by the NIST and DL6WU.

The spacing of the reflector and the first director are usually the most critical. Multiple directors usually end up with around 0.4 wavelength spacing. Small amounts of improvement in gain can be obtained by playing with the spacing of the directors - however, it is generally not worth the effort.

If you can obtain a copy of the ARRL Antenna Book, chapter 18 will likely be helpful.

Additionally, the following resources may also be informative:

DLRWU Yagi Design Page

K7MEM VHF/UHF Yagi Design Help

There are a few more that I would like to include, but I do not have enough reputation points.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1782/spacing-between-elements-on-a-yagi-antenna, by Delta1X, Xevious. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
