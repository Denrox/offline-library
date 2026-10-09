# What were the reasons why ATIS identification was introduced?

*Tags: vhf, history · score 3*

## Question

I am just about to make my inland waterways’ marine VHF radio license in Germany. In Germany, all inland marine VHF radios must be equipped with an ATIS transmitter, which basically sends the stations’ call sign digitally by frequency shift keying when releasing the PTT, on the same channel as the voice transmission.

Unlike DSC used in international shipping, the ATIS codes are not decoded on the receiving units and can neither be used by other ships to identify the sender, nor there is a way to call a ship or land station, if its ATIS number would be known. I have no idea if anybody can or does decode these digital transmissions, and with which benefit. To my eyes, the system only has drawbacks, mainly you need additional circuits inside your maritime radio, and the “noise” it causes, or even more circuits, called “ATIS killer”, to suppress that noise on the receiving side. (I searched for, but I didn’t either find a smart phone app that uses its microphone to decode the ATIS signal, if the onboard units can’t. There is such for weather fax, that was why I started digging for it.)

I was searching for the reasons why ATIS was introduced for inland waterways’ marine VHF, but I was not able to find anything informative. What were the reasons why those countries introduced the ATIS system for inland waterways’ marine VHF radio? What problem should it solve, and did it actually solve it?

## Answer (score 4, by Glenn W9IQ)

ATIS simply provides automatic identification of the vessel transmission. This is helpful in eliminating the requirement for the typically non professional ship radio operator to manually identify. It also effectively shortens transmission time allowing better utilization of crowded channels while ensuring easy identification of the ship and transmitter. This is particularly helpful with authenticating distress, interfering, or unlawful calls.

ATIS is a subset of DSC (Digital Select Calling) with a format specifier of 121. Thus any standard DSC decoder on the receive channel can read the ship identification information. ATIS data is only sent on the transmitting channel (unlike full DSC on channel 70) and only upon key release with an ~285 ms data burst. Because the data sent is only an index to the ship identification, the 'Belgisch Instituut voor Postdiensten en Telecommunicatie' database must be accessed to resolve the actual vessel name.

The data packet is sent with 1200 baud FSK using 1.3 kHz and 2.1 kHz tones. Because the tones are in the normal audio passband and because the data transmission is quite short, fully blocking of the data audio is difficult without applying a digital delay to the audio channel. If you wish to homebrew a decoder instead of simply blocking the packet, the DSC message format is well documented.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9650/what-were-the-reasons-why-atis-identification-was-introduced, by Matthias Ronge, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
