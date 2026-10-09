# How to obtain raw data for Global Real Time foF2 Map

*Tags: hf, propagation, map · score 5*

## Question

Note!!!!: I am not looking for help with how make a map using Google Maps API (that part is done). I need help with finding data.

I am building a shortwave radio/HF listening log book online, and it uses Google Maps for the plotting of receiving and transmitting stations when logs are made. I wanted to add a layer for real-time critical frequencies to the map, like the one provided by the Australian Space Weather Agency http://www.ips.gov.au/HF_Systems/6/5 (which is an image file). Is there data anywhere that provides plot points for this map?

## Answer (score 4, by Adam Davis)

The map projection used in the mentioned webpage is a cylindrical map projection, with the degrees latitude and longitude marked off on the left and bottom edges. Each 10 degrees latitude is about 24 pixels, and each degree longitude is about 27 pixels. It shouldn't be too hard to take each pixel and convert it to a latitude and longitude from this data. Then you'd use the google API to change the latitude and longitude back to the google's projection, which is a variant of the mercator projection. The projections are different, so you can't simply overlay this image on a google map and expect it to match. You'll have to collect the data points in terms of lat/lon pairs, then place them on the google projection using google's tools.

It's reasonably obvious that they are extrapolating this map from limited data, though - the curves and contours suggest that there are only a handful of data points which they then process to generate the map. They themselves suggest this is the case in the text on that page explaining where they get the data from. It appears they don't release their aggregated data in any other form than the map, though. You have two options - contact them and see if they will publish the hourly data in a way you can easily gather it, or go to the sites they list as their sources of data and collect the data yourself.

Neither option is particularly easy, but one or the other should work.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/962/how-to-obtain-raw-data-for-global-real-time-fof2-map, by cj5, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
