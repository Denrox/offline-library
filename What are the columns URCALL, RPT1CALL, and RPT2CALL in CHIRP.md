# What are the columns URCALL, RPT1CALL, and RPT2CALL in CHIRP?

*Tags: radio-programming, chirp · score 4*

## Question

I'm populating a CSV file to import into CHIRP. In the documentation, there's a list of CSV columns. However, that list doesn't cover URCALL, RPT1CALL, and RPT2CALL. Can anyone tell me what those columns are for and how they're used in radios?

## Accepted answer (score 7, by rclocher3)

"MYCALL", "URCALL", "RPT1CALL", and "RPT2CALL" are used to program D-STAR channels in D-STAR-capable radios. Those columns should be left blank for analog FM channels.

- MYCALL is your own call sign, eight characters maximum; "/" and suffixes are allowed, as long as everything fits in eight characters.
- URCALL is ostensibly for the call sign of the station you're trying to call, or "CQCQCQ" for calling any station or to talk on a repeater; URCALL can also be used to hold routing information or linking commands.
- RPT1 ("RPT1CALL" in CHIRP) should be set to the local repeater and module that you're trying to access. (The setting doesn't matter for D-STAR simplex.)
- RPT2 ("RPT2CALL" in CHIRP) designates where you want your signal to be routed on your local repeater; normally RPT2 is set to the call sign of the local repeater, followed by "G". (The setting doesn't matter for D-STAR simplex.)

Exactly how to use D-STAR is beyond the scope of a single answer. There's an article here that goes over the basics.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15666/what-are-the-columns-urcall-rpt1call-and-rpt2call-in-chirp, by watkipet, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
