# Lack of understanding in the APRS specification for LoRa

*Tags: aprs, software-development · score 4*

## Question

I try to understand the APRS specification because I want to build my own APRS tracker. I took a look into this document and into this and into this project to get a better understanding. I also checked https://aprs.fi/, but I don´t understand it completely.

So I came up with the following questions:

1. The file LoRa_APRS_Tracker.cpp contains these lines of code

```
LoRa.write('<');
LoRa.write(0xFF);
LoRa.write(0x01);

```

Why do I have to send these characters at the beginning of the message? Where do I find this information in the documentation?

1. In LoRa_APRS_Tracker.cpp the destination is set to APLT00. What does this mean?
2. Is the LoRa protocol different than the regular protocol (because of the smaller bandwidth)? If yes, what does a LoRa message look like?
3. What is the correct interpretation of the iGate message DO2DKH>APLG01,TCPIP*,qAC,T2DENMARK:=4932.12NL01046.65E&LoRa iGATE? I only know that DO2DKH is my callsign and :=4932.12NL01046.65E&LoRa iGATE is the GPS position and a message. But what does the rest mean?

## Accepted answer (score 5, by hobbs - KC2G)

Why do I have to send these characters at the beginning of the message?

It's just an arbitrary header that this group of people used to identify APRS messages, and distinguish them from other packets that might be heard on the same LoRa frequency. The corresponding code in the iGate drops all packets without that header, and the header is stripped before processing the remainder as an APRS message.

Where do I find this information in the documentation?

Nowhere, because it's not part of the APRS spec, it's a LoRa-APRS quirk.

In LoRa_APRS_Tracker.cpp the destination is set to APLT00. What does this mean?

Since APRS is broadcast, it reuses the AX.25 "destination address" field to contain some information about the sender instead. See pages 13-14 of APRS101.PDF. "LT00" is presumably "LoRa Tracker, version 0".

Is the LoRa protocol different than the regular protocol (because of the smaller bandwidth)?

Not really. It *is* different, because of the aforementioned header, and because the stuff that would have been in the AX.25 packet headers ends up encoded as text (in the same format as APRS-IS or a TNC2 would use) in the LoRa payload, but nothing is changed in the APRS payload.

What is the correct interpretation of the iGate message DO2DKH>APLG01,TCPIP*,qAC,T2DENMARK:=4932.12NL01046.65E&LoRa iGATE? I only know that DO2DKH is my callsign and :=4932.12NL01046.65E&LoRa iGATE is the GPS position and a message. But what does the rest mean?

Routing information added by APRS-IS. Basically: "this message has been over the internet" (used to prevent a message from going RF -> internet -> RF -> internet again if it passes multiple iGates), and "it was received directly over the internet from the originator by the server named T2DENMARK". And the TOCALL is APLG01, which indicates the LoRa igate as the origin rather than the tracker.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21571/lack-of-understanding-in-the-aprs-specification-for-lora, by Kampi, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
