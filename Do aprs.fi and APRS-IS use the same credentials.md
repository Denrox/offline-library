# Do aprs.fi and APRS-IS use the same credentials?

*Tags: aprs, software · score 7*

## Question

I have an account/profile on aprs.fi, and now I am trying to use APRSdroid, which requested my credentials. Can I use the password from aprs.fi for it?

I am unable to register/submit my application through TQSL because my country is not on the list. I will investigate that in more detail, but at this point I just wonder if aprs.fi and APRS-IS are the same thing, because I read that the former pulls data from the latter.

## Answer (score 8, by oh7lzb)

**The aprs.fi passwords can not be used when logging in to the APRS-IS servers. aprs.fi and APRS-IS are two different things.**

The APRS-IS network consists of roughly a hundred servers distributed around the world, run by a large team of volunteer server operators. APRS-IS requires the use of the passcode number for logging in and sending data to the APRS-IS network. APRSdroid and most other APRS applications connect to the APRS-IS for sending and receiving APRS data. APRSdroid simply gives your passcode to an APRS-IS server when logging in. The passcode is a static number calculated from the callsign, and it cannot be changed.

If you're using APRSdroid, you can get a passcode from the APRSdroid team. It may take a short while for them to respond, as explained on the FAQ.

Some APRS-IS servers also accept TLS/SSL connections, as an experimental feature, in which case you can use an amateur radio certificate, together with your private RSA key, to log in. The TQSL app can be used to request such a certificate from the ARRL Logbook Of The World.

aprs.fi is a web site, which connects to the APRS-IS network just like APRSdroid itself does, collects APRS data, and stores it in a large database. aprs.fi has its own user database, with usernames and passwords. Each aprs.fi user may choose their own password, and it can also be changed afterwards.

## Answer (score 5, by W8AWT)

To get a passcode for the APRS-IS on APRSdroid you do not necessarily have to contact the APRSdroid Developer team. You can use any one of several APRS-IS passcode generators available on the web as web based or Windows based applications . Just enter your callsign, press enter and a APRSIS passcode will appear with which you can login to the APRS-IS in APRSdroid.

Here is a list of just a few web based APRSIS passcode generators:

- APRS Passcode Generator - Magicbug
- KF5JWC.us-APRS passcode generator
- APRS Callpass - George Smart's Wiki

Here is a list of a few downloadable Windows based applications:

- APRS-IS Passcode Generator - EagleFlint | Soar (Needs to be installed to run.)
- N8ZAK's APRS Passcode Generator (Portable Windows command line application)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3819/do-aprs-fi-and-aprs-is-use-the-same-credentials, by harayz, oh7lzb, W8AWT. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
