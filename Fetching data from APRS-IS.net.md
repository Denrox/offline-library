# Fetching data from APRS-IS.net

*Tags: aprs · score 3*

## Question

I would like to fetch the data transmitted by a specific radio station from APRS-IS.net servers. I've read the documentation on their site and it is not clear how you would do it, if you are fetching the data instead of transmitting it. It is mentioned to use a callsign and password, but I'm not sure where to get them from.

## Answer (score 2, by q74)

I am using firenet.aprs2.net and euro.aprs2.net for APRS-IS data. If you need to fetch packets you have to connect to a server on a specific port. Usually port 14580 is the one to use. Once a connection is established you are supposed to authorize yourself using your callsign and password. Password is a hash algorithm based on your callsign. Here is an example of how to request packets from a APRS-IS server:

```
user {your_callsign} pass {password_hash} vers {your_software_name} filter r/{latitude}/{longitude}/{range}\n

```

for example: your GPS location is 50.000N by 20.000E and you want to request packets within 200km range, use the following packet filter:

```
... filter /r/50.000/20.000/200

```

Please bear in mind that you need to add LF ("\n") char to the end of your request. If you need more details please contact me via my website http://www.so6agj.pl

73

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15164/fetching-data-from-aprs-is-net, by Daniela, q74. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
