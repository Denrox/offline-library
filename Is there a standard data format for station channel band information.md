# Is there a standard data format for station/channel/band information?

*Tags: software · score 7*

## Question

Does there exist a *de facto* standard data (file) format, or even several common formats, for representing information about radio stations, channels, and/or bands? I am writing software which would like to be able to make use of such data sets where they exist.

To clarify the sort of data sets I care about, the minimum information such a file would need to contain is a list of frequencies; useful associated information would be name or callsign, mode/protocol, and geographic coordinates. An example of a data set I would like to be able to obtain and process would be a list of amateur radio repeaters for a given location.

My research so far has found data sets provided in the following forms:

- Not-completely-regular HTML tables on web pages (e.g. ARRL Band Plan)
- Columnar text files of no standard layout
- CSV files used by CHIRP, a tool for configuring radios

This last has been somewhat useful, in that it is relatively well-defined and the first two can often be semi-automatically converted into CSV files, but I would like to know if there is something common that I simply haven't learned the right terminology to find or recognize.

## Answer (score 2, by Adam Davis)

No such universal standard exists currently. RepeaterBook, Radioreference, and RFinder have differing format they use for transmitters and repeaters which you may find nominally useful.

The FCC maintains databases of TV, Radio, and other licensed transmitters and their locations in the US. You may find their format interesting, though I doubt you'd want to adopt it for your purposes. I expect other countries have similar databases for their radio licensees.

Several manufacturers have developed different formats for their radios, though they are probably more limited than what you want as they are meant to be programmed into the radio, but they usually include at minimum location, frequency information, and station ID.

CHIRP accepts a number of formats, and converts between many of them. I'd suggest working with the CHIRP team to develop a standard that could be used as default.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/633/is-there-a-standard-data-format-for-station-channel-band-information, by Kevin Reid AG6YO, Adam Davis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
