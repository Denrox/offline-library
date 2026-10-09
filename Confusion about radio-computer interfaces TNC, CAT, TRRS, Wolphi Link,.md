# Confusion about radio-computer interfaces: TNC, CAT, TRRS, Wolphi Link, ...?

*Tags: digital-modes, audio-interface, computer-aided-transceiver · score 9*

## Question

This is probably a very simple and stupid question, but I'm getting more confused over time. Perhaps it is a matter of terminology, but a unified resource differentiating and explaining the different interfaces to connect radio with computer (desktop, Mac, mobile phone, GPS devices, etc.) would be very helpful.

To start: I have assembled a home-brew cable to connect Kenwood radios with Android/iPhone. The cable has a 3.5 mm audio (in and out) at one end and Kenwood style audio double-jack at the other end. I understand this as a TRRS cable. I've also worked with a programming cable that has USB at one end and Kenwood style audio jack at the other end.

I've read about TNCs, CAT cables and Wolphi Link interfaces. What is the advantage of one over the other? I want to interface my radio with my smartphone as well as my computer. Both have a 3.5mm audio jack and the computer has a USB interface too. I'd also like to connect the radio to some GPS device, and possibly other devices. I'd also like to program the radio from a computer/phone. I have Yaesu and Kenwood phones.

What cables/interfaces should I use? Can I use just one type of cable for different tasks (digital+packet operations and programming), or do I need a different cable for each task?

## Accepted answer (score 11, by AndrejaKo)

First of all, don't feel to overwhelmed! This can be a bit confusing at the start, but once you understand the pattern and historical development, things will get a bit simpler.

So fist of all, you're confusing connectors and cable purposes. Some cable types for certain purposes have common connectors, but in general, be sure to differentiate between the two.

So let's start with the TRRS cable. TRRS is a a connector type, the one used by smart-phones for headphones, with tip, two rings and sleeve. The Kenwood connector has two TRS (tip-ring-sleeve) connectors.

Radios using Kenwood connector usually implement a serial port via the Kenwood connector. This serial port is usually used to program frequencies and set the settings for the cable. The USB cable you have will have a USB to serial port chip inside and will use that serial port to communicate with the radio. The other alternative is to use a Kenwood to serial cable that can be used with a real serial port.

The same Kenwood connector also implements connection for external loudspeaker-microphone combinations with push-to-talk buttons. There are TRRS to Kenwood cables that can be used with smart-phones to transfer audio from the radio to the smart-phone and from the smart-phone to the radio. Usually, that's done for purposes of "digital modes" or for "packet radio". Basically, the phone acts as an old-school fax modem and generates audio that is then transmitted by the radio. In this case, usually the radio is set to VOX (voice activated) mode, so that the phone just needs to send audio to the radio. A better solution is to use external hardware to key the radio, but implementing this with a phone can be a bit complicated, so most people don't do it.

Next, you mentioned TNC and CAT.

So let's go back in time a bit, before the smart phones, in the era of analog telephone modems. Back then, if you wanted to send and receive data over audio lines, you needed an external device to do that. This device would be connected to a computer via a serial port and on the other hand have audio connection over the telephone jack. In Internet world, such devices got the name "analog modems, "fax modems" or just "modems", but in amateur radio world, they got name Terminal Node Controller. The TNC, in addition to doing modulation/demodulation, would also do a bit of packet processing. So the device would go between your computer (or even just dumb serial terminal!) and your radio and supply radio with suitable audio that would carry the data.

Fast forward a couple of decades and now we have computers (and telephones!) that can do all the work of a TNC in software and only need the audio connection to the radio. The name TNC however stuck and the cable used to connect the TNC to the radio is called TNC cable.

Note that in usual TNC operation, you set up the radio more-or-less manually and the TNC only receives audio, keys up the radio and sends audio to the radio.

Then we have CAT and CI-IV(old radios)/CI-V(newer radios). The CAT stands for computer aided tuning and CI-V is Communications Interface 5 (4 was the older version) and is the name used by Icom for CAT.  
Basically, the idea here is to remotely control the operation of the radio itself. So the radio has a serial port, you sit in front of a computer connected to the radio and select frequency, mode and other settings of the radio. Keep in mind that this is just settings for the radio and carries no audio signal on its own. Depending on the commands implemented by the radio, you might be able to do the "programming" of the radio as well.

So if you want to do digital modes on a relatively new radio, you need two cables: A "TNC" cable and a CAT cable, one to carry data and the other to carry audio. Some newer radios solve this by having just one USB cable: The radio shows up as a composite USB device consisting of a USB to serial converter and a sound card. You just send the instructions using the serial port and audio using the sound card and that's it.

Now about the Wolphi Link. This is what they call an "interface". It's a realization of a TNC (more or less) cable. On one side, you have the 6-pin connector for the radio, then you have the interface itself and on the other side, you have audio connection for the phone. The interface is there to provide some isolation between the radio and the phone, since it can happen that you have RF going over the TNC cable. The device also claims to be able to generate the key signal for the radio, which can be more reliable than just using VOX and will work with VOX-less radios as well.

About the GPS part... There's no sense in connecting a GPS to a dumb radio, pretty much in the same way it's senseless to connect an egg to a radio. On the other hand, with some "smarter" radios, you have a TNC inside of the radio and some radios even have full APRS support (marine radios also have GPS connection for digital selective calling). In this case, it does make sense to connect a GPS receiver to the radio, but from "subsystem" point of view, you're connecting the GPS to the TNC/computer inside of the radio. You'll usually do this using serial port as well or by connecting radio with its own proprietary GPS receiver. If you however want the phone or computer to be the TNC, then you need to connect the GPS to the computer or use phone's GPS.

In this answer, I left out the part about software on the phone/computer that's going to drive the radio itself, since I believe that this side of the story is a bit too complicated to be fitted in this answer.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6766/confusion-about-radio-computer-interfaces-tnc-cat-trrs-wolphi-link, by hamster, AndrejaKo. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
