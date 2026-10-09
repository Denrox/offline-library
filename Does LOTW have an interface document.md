# Does LOTW have an interface document?

*Tags: logging, lotw, software-development · score 8*

## Question

I want to be able to sign my own LOTW entries, without using the provided library (My application is pure Java). Is there a document that explains in enough detail how to do this, assuming of course that I'm provided with a certificate (.tq8 I believe)?

## Accepted answer (score 4, by PearsonArtPhoto)

After looking through things for quite some time, and asking around, I was able to find the following, assuming that I can get a copy of the signed certificate from somewhere. There is some more information at this blog article, and this GitHub site.

1. The log file is done in a format called GAbbI (Global Amateur Interchange). This file format is similar to ADIF, but not quite identical.
2. The signature is performed using X.509 certificate handling.
3. The station data is a field in the GAbbI format.
4. The file is then gzipped, and uploaded to ARRL.

Bottom line is, following the specification given through the linked site is the best bet to getting this to work. X.509 is a standard library, and the GAbbI format is close enough to ADIF that it should be relatively easy to parse through.

A few things to note that are different from the GAbbI spec:

- All of the data for signing is upper case.
- The order of fields for the signed data is: CA_PROVINCE, CQZ, GRIDSQUARE, IOTA, ITUZ, US_COUNTY, US_STATE, BAND, BAND_RX, CALL, FREQ, FREQ_RX, MODE, PROP_MODE, QSO_DATE, QSO_TIME, SAT_NAME. Note that station comes first, then QSO data.
- There are several undocumented fields, including CA_PROVINCE, US_STATE, SIGNDATA, and SIGN_LOTW_V1.0. SIGNDATA is the data signed for the LOTW signature, SIGN_LOTW_V1.0 is the LOTW signature itself. CA__PROVINCE and US_STATE are the Canadian Province and US state.
- SIGN_LOTW_V1.0 has a :6 after the number of digits. I suspect this is related to the base 64 output.
- The max space per row is actually 64, not 72 as specified.
- The character count includes line breaks, and if there is any line breaks, it also counts the last line break. For a single line, it doesn't count the final line break.
- The signature is signed as SHA1withRSA.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1492/does-lotw-have-an-interface-document, by PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
