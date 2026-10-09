# Do you need a radio licence to use ZigBee/Xbee?

*Tags: legal, license, united-kingdom · score 6*

## Question

I want to make a application with my Raspberry Pi along with a XBee module. I am going to use it in public places and in my own home.

The question is, do I need a radio licence (UK) to use the XBee in my home and/or in public places? I want to know this before I even buy a XBee (won't be until later). When this is in public it will be a two-way communication between me and my friend.

**Edit:**

People complaniing that my friend is wrong and needs to do his test again don't need to any more. He didn't hear that I was talking about the zigbee/xbee he just thought it was transmitting data via FM radio waves. Sorry about the confusion.

## Answer (score 2, by Scott Earle)

According to Wikipedia (which is never wrong?), these devices implement IEEE 802.15.4, which defines among other things the frequencies upon which they operate.

http://en.wikipedia.org/wiki/IEEE_802.15.4

From that page, there are three radio bands those devices can use: 868-868.6MHz (Europe only), 902-928MHz (North America only) and 2400–2483.5MHz (Worldwide).

The IEEE 802.15.4 standard is licence-free.

As long as the device is not set to use the North America-only band, you should be good to go.

Do note that the 2400MHz band has quite a few other legitimate (also licence-free) users, such as IEEE 802.11 in various guises (WiFi), Bluetooth, and microwave ovens - in a 'noisy' environment you might want to try using the 868MHz band, if you have that option on your devices.

## Answer (score 2, by Virendra Kumar)

If I am not wrong, XBee works at 2.4 GHz, which is a free band used worldwide. You do not need a license to use this frequency.

However, there are some other frequencies which need a license. I would still recommend you to search the country-specific frequencies free to use.

http://en.wikipedia.org/wiki/ISM_band

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3729/do-you-need-a-radio-licence-to-use-zigbee-xbee, by iProgram, Scott Earle, Virendra Kumar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
