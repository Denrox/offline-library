# My radio in the garage is temporarily shutting down the wifi when I key up

*Tags: rfi, wifi · score 4*

## Question

I have a Yaesu FT-101EE, D-104 Mike, MFJ-929 Antenna Tuner, 80-10 OCF Dipole Antenna with a MFJ balun.

When ever I key up for more than a few seconds, the wifi network goes down for a couple of minutes disconnecting any attached devices. A couple of minutes later after transmitting, it wifi network comes back. The router does not turn off or reset, it just seems to shut down the wifi signal.


The NetGear N600 router is in the house, the radio is upstairs in the detached garage. I don't believe any devices are using 5 GHz.


The balun is attached to a 6' horizontal pole attached to the back of the garage, approximately 25' high. The wires run from the balun across the property behind and parallel to the house and garage. There is approximately 8' of coax from the antenna tuner to the balun.


I have been using the 80 meter band.

Any ideas on what I can do to fix this?

## Answer (score 3, by user10489)

Sounds like the router is getting front end overload. Either your OCF dipole is too close to the router, or you are getting common mode current on the coax and it is radiating along the coax.

A balun on the coax in the right place might help if it is common mode current.

## Answer (score 2, by Chris K8NVH)

I agree with user10489's answer but would like to expand a bit on what to do about it. A signal of some sort appears to be interfering with something associated with the router and there does not seem to be enough information to pinpoint an exact cause.

As stated by user10489, adding a balun or common mode choke in the appropriate place(s) on the feed line (see http://audiosystemsgroup.com/RFI-Ham.pdf for far more information than I could possibly describe) would probably help.

A good resource on common mode chokes is http://www.yccc.org/Articles/W1HIS/CommonModeChokesW1HIS2006Apr06.pdf . Far more information than could be described here.

Also, check all of the feedline, tuner, and antenna connections. A bad connection could be the cause of the interfering signal.

Is there an ethernet wire between the wifi router and whatever is upstream of it? If so, place a common mode choke there as well since it could be the upstream device that is having difficulty. In fact, if it is the upstream device, any of the wires attached to it could be acting like an antenna.

Before adding hundreds of € worth of common mode chokes across every wire in your house, check the connections between your radio and antenna and then run the following test:

1. Log in to your N600. Go to the "Status" screen; look for the device ethernet address and also the list of attached devices.
2. Key up on 80 meters. (You are using the full 130 watts on SSB, right?)
3. Observe the changes on the N600. This should give you a clue where to look.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12278/my-radio-in-the-garage-is-temporarily-shutting-down-the-wifi-when-i-key-up, by Roy Kees, user10489, Chris K8NVH. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
