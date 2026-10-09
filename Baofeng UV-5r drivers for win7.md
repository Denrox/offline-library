# Baofeng UV-5r drivers for win7

*Tags: baofeng · score 3*

## Question

I've been fighting to get chirp working with my father's baofeng radios. The only computer that he has access to has Win 7 installed. The manufacturer drivers won't work with win7. I tried using the profilic drivers (did the whole install, etc.) and haven't had any success.

Chirp is giving the following error message: could not open port : [Error 3] The system cannot find the path specified.

Any help is appreciated.

## Answer (score 4, by 9F48)

Drivers are not required for the radio, but for the USB cable, as it has to provide a serial port via USB.

A long workaround could be:

- Download a Linux distro that can run from a USB drive in persistent mode, like Ubuntu.
- Download and install CHIRP on Linux.
- Let Linux handle it for you.

I'm saying this because in my case it worked right away on Linux without any problem.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5138/baofeng-uv-5r-drivers-for-win7, by Urge, 9F48. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
