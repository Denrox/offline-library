# Linux APRS client

*Tags: aprs, software, linux, tnc · score 3*

## Question

I have an old PK-232 packet TNC which is spitting out APRS data from 144.390 to the serial port. I have confirmed this with minicom and see all sorts of data with lat long etc.

I would like to view this on a map. I have centos 5 linux.

Are there any linux APRS clients that will take data from the serial port, and put it on a map or something?

## Accepted answer (score 8, by Paul V)

Xastir is most likely what you want. http://xastir.org/index.php/Major_Features#SUPPORTED_TNC.27s:_DARN_NEAR_EVERYTHING.21

YACC - Yet Another APRS Client is also a newer choice. I have not personally tried it. http://www.ka2ddo.org/ka2ddo/YAAC.html

## Answer (score 4, by captcha)

You could use Aprx or Direwolf and configure the client as a Receive-only iGate. You can then assist in sending some directly received data to APRS-IS (the Internet side of APRS) and see the data appear on sites like www.aprs.fi

You will need a password to be able to log to aprsis but this is trivial once you have a callsign and google for aprs password calculator.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2294/linux-aprs-client, by Skyler 440, Paul V, captcha. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
