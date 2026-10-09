# What SDR software is available that provides internet control?

*Tags: software-defined-radio, software, remote-control · score 7*

## Question

I plan to use a SoftRock Ensemble RX II to receive HF transmissions. I'd like to be able to use it wherever I am when I have a few minutes, though, so I'm wondering what software exists that would allow me to control the receiver over the internet?

I've seen websdr and it appears to support some of the functions of this receiver, but it also appears to publish itself to the websdr website, allowing others to control the station as well. The worst part is that it doesn't allow full control of the receiver, it appears you have to select the band and center frequency at the computer, and cannot operate those parameters remotely.

While I'd prefer windows, if Linux applications are available that do this I'd be willing to set up a PC just for that purpose.

Also not necessary but desired is that it would work with iOS devices, either via HTML5 and javascript, or with a specific app.

## Answer (score 2, by K7AAY)

OK: Windows host for SoftRock Ensemble RX II, remote control of digital modes - why not an COTS (Cheap Off the Shelf) solution, such as TightVNC or other VNC solutions? Since you are talking about station control, not voice, the lack of voice is not an issue, is it?

It's GPL open source (free as in beer), even cross-platform, and supports Android and anything else which runs Java, which would really give you spur-of-the-moment access. You can even get a Reflector app to allow multiple viewers if you wished.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1046/what-sdr-software-is-available-that-provides-internet-control, by Adam Davis, K7AAY. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
