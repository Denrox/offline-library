# Why am I receiving a local tv channel on a CMB frequency

*Tags: receiver, propagation, vhf, rfi, baofeng · score 3*

## Question

I am using a simple Baofeng H6 dual band radio and I programmed weather channels. Well, on frequency 161.77500 I am actually picking up WGN, a local tv network. This frequency should be reserved to transmitting weather, no? Why can I be picking a TV signal in this frequency?

## Answer (score 3, by hobbs - KC2G)

161.775 isn't a frequency reserved for weather broadcasts in the US, no. CMB is a Canadian service; the same allocation doesn't exist in the US. NOAA All Hazards Weather Radio stations are on channels from 162.400 to 162.550 MHz.

According to RadioReference, WGN-TV has an IFB channel at 161.74875 and a remote audio channel at 161.77250. These are channels that broadcasters use "in the back-end" for studio monitoring and for transmitting audio over short distances; they aren't part of the actual broadcast product, but anyone with a narrowband FM receiver capable of tuning those frequencies can listen in. You're probably hearing the latter one — a small tuning error doesn't affect an FM signal very much.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17923/why-am-i-receiving-a-local-tv-channel-on-a-cmb-frequency, by fiacobelli, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
