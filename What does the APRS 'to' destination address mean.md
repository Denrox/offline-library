# What does the APRS 'to'/destination address mean?

*Tags: aprs · score 4*

## Question

I'm looking at incoming packets. Here's the beginning of a few messages:

```
KF7WXW-9>TU3RTW,WIDE1-1,WIDE2-1:`2D<..
KX5ONE-9>T5SRPV,WIDE1-1,WIDE2-1:`2E0..
KX5ONE-9>T5SRSV,WIDE1-1,WIDE2-1:`2E ..

```

So, what to the Txxxxx labels mean? The APRS spec talks about the destination addresses (pg13). Is it related to the MIC-E encoding (pg44)? If so, please break down the encoding in your answer.

## Accepted answer (score 3, by rclocher3)

The Txxxxx labels are the Mic-E encoded Destination field. Let's take the first example, TU3RTW. If we look up the latitude digits from the table, we get 453247. Then there is the other information encoded in the six digits. The first three digits give the message code. T gives 1 (standard), U gives 1 (standard), and 3 gives 0. So that's standard message code 110, which means "en route". Moving on, R in the 4th digit (rather than 2) means North. The T in the 5th digit means +100° longitude. The W in the 6th digit means West.

To sum up, we have a station "en route" at 45° 32.47' North latitude. Also the station is in the western hemisphere, somewhere west of the 100° West longitude line. (The rest of the longitude is encoded in the Information field of the message.)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5968/what-does-the-aprs-to-destination-address-mean, by 300D7309EF17, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
