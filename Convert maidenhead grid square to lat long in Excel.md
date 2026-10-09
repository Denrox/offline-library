# Convert maidenhead grid square to lat/long in Excel?

*Tags: contest, map, maidenhead-locator · score 5*

## Question

I have a list of maidenhead grid squares in an Excel sheet that I want to convert to latitude and longitude. I want to keep it as simple as possible. Does anyone know of a formula to convert from maidenhead to lat/long?

## Answer (score 5, by Richard Ferch)

Assuming for the sake of precision that the particular point in the grid square that you want the exact latitude and longitude for is the midpoint of the 6-character subsquare, this can be done readily with Excel formulas.

If the 6-character grid square data is in cell A1, in a format similar to AA00aa (i.e. upper-case, then digits, then lower-case), the formula for the latitude (based directly on the Python code posted previously) is:

=(CODE(MID(A1,2,1))-65)*10 + VALUE(MID(A1,4,1)) + (CODE(MID(A1,6,1))-97)/24 + 1/48 - 90

and the formula for the longitude is

=(CODE(MID(A1,1,1))-65)*20 + VALUE(MID(A1,3,1))*2 + (CODE(MID(A1,5,1))-97)/12 + 1/24 - 180

If you want the latitude and longitude of the southwest corner of the subsquare, just leave out the + 1/48 and + 1/24 terms. Add error-checking, upper- and lower-case conversion, conversion of four-character squares to six-character by adding 'mm', and other embellishments as you see fit.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6114/convert-maidenhead-grid-square-to-lat-long-in-excel, by user6587, Richard Ferch. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
