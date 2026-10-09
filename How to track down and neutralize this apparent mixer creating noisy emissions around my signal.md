# How to track down and neutralize this apparent mixer creating noisy emissions around my signal?

*Tags: rtl-sdr, noise, mixer · score 4*

## Question

When I transmit, it there seems to be something mixing and reflecting my signal. For example, when I transmit on 14.300 MHz, I see signals above my transmitted signal at at 14.500, 14.700, 14.900, etc. and below my signal at 14.100, 13.900, 13.700, and so on. I tested on another frequency in twenty meters and saw the same pattern, with both tests radiating signals with frequencies "reflected" around 14.400 MHz.

This sounds like some issue with my signal getting unintentionally mixed with some other signal. The weirdest thing is that I still see at least the primary reflection---e.g. the 14.500 MHz signal when I transmit on 14.300 MHz---when I'm using a dummy load.

I even see noise signals being reflected around this 14.400 MHz point. What could possibly be doing this, and how can I track it down?

Some information about my system:

- I am watching the spectrum using an RTL-SDR, with SDR# software
- Rig is an Icom IC-718
- Antenna is a dipole cut for 20 meters, run around the interior perimeter of my shack
- Antenna is connected to the radio with 12ft of DXE400MAX coax
- Transmission line has a common-mode choke wound into the receiver end of the coax
- There is a 1:1 current balun is at the antenna side
- The following points are all bonded together, however they are only bonded to the AC ground since I am in a third-floor apartment:

 - The transmission line shield at the antenna end
 - The transceiver (ICOM IC-728)
 - The power distribution bar (MFJ-1129)
 - The power strip this is all powered by (an MFJ-4230MV)

## Accepted answer (score 5, by Rosa)

This is caused by the RTL-SDR I was using to view my signal. Here's a quote from the guide at https://www.rtl-sdr.com/rtl-sdr-blog-v-3-dongles-user-guide/:

Note that this feature makes use of direct sampling and so aliasing will occur. The RTL-SDR samples at 28.8 MHz, thus you may see mirrors of strong signals from 0 - 14.4 MHz while tuning to 14.4 - 28.8 MHz and the other way around as well. To remove these images you need to use a low pass filter for 0 - 14.4 MHz, and a high pass filter for 14.4 - 28.8 MHz, or simply filter your band of interest.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17115/how-to-track-down-and-neutralize-this-apparent-mixer-creating-noisy-emissions-, by Rosa. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
