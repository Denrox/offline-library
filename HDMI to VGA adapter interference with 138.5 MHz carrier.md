# HDMI to VGA adapter interference with 138.5 MHz carrier

*Tags: rfi, rtl-sdr · score 3*

## Question

(sorry for my English)

I'm using the HDMI to VGA adapter on my pc, and receiving weather satellites on ~137 MHz with RTL-SDR V3. There was a problem: my VGA adapter creates a powerful signal, who pollutes the 137 MHz band, with carrier wave on 138.5 MHz. This signal receivable anywhere in the house. I tried to use VGA cable with ferrites and shielding, and shielded the VGA adapter with aluminum foil, but it did not give any result. If I connect SDR to another device, I still can receive this signal. The signal disappears when I unplugging VGA adapter or turning off pc. With VGA graphics card (respectively without VGA adapter), there was not any interference. What should I do to mitigate this interference?

## Answer (score 2, by Scott Earle)

It sounds like you have two options:

1. Buy a new HDMI monitor
2. Use a VGA card

You say it was fine when you used a VGA card. So why change?

It sounds like the HDMI-to-VGA adapter is a generator of much noise, especially in the band you need to use. To me, this means you have to remove it from the equation. Either get an HDMI monitor (these are kind of standard these days), or get a display card that has a VGA port. eBay should be full of those. Of course, I would recommend getting a digital monitor, because VGA is old and analogue, where HDMI is digital.

Heck, I remember using VGA cards over thirty years ago.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16170/hdmi-to-vga-adapter-interference-with-138-5-mhz-carrier, by lethanner, Scott Earle. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
