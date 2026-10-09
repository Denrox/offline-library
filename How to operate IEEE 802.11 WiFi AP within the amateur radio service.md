# How to operate IEEE 802.11 WiFi AP within the amateur radio service?

*Tags: united-states, legal, wifi · score 14*

## Question

How can I properly use my ham radio license to operate an IEEE 802.11 WiFi access point within the US amateur radio service, rather than the US "part 15" regulations for unlicensed transmissions?

## Accepted answer (score 12, by user)

IANAL, but based on my limited knowledge of US amateur radio regulations:

- Disable all encryption, as encrypted communications are not allowed within the amateur radio service. Yes, WEP counts as encryption, too. So does HTTPS, SSH or SMTP with STARTTLS. One of the few things you can allow is plain-text HTTP.
- Set the network SSID to your call sign. This should be enough to identify the transmissions.
- Force select a channel which is within the boundaries of the amateur radio band.

This *should* put you within the limits of the amateur radio service and allow you to operate the access point under the regulations relevant to amateur radio.

## Answer (score 4, by Joseph)

All the info you could ever want is being provided on this website..http://hsmm-mesh.org/ They are using WRT54G routers for ham band wifi usage. There is a great community for support and lots of documentation..Type "ham mesh net" into your favorite search engine and you will find many answers.

## Answer (score 3, by dcaswell)

In 2006 the ARRL dropped its support for changing the rules to allow digital encryption. The rationale for their decision is that it was already legal.

Their reasoning comes for the following FCC rule:

*Part 97 : Sec. 97.105 Control operator duties (a) The control operator must ensure the immediate proper operation of the station, regardless of the type of control.*

The ARRL interprets this rule to mean that encryption to ensure the integrity and control of one's operations is legal.

This document explains the entire rationale.

In the United States no Control Operator has ever faced any disciplinary action for encrypting their WIFI transmissions as long as the encryption mode (but not the key) is public.

The article has lots of cautions, for example: Every control operator is still responsible for periodically transmitting their call-sign. It recommends you use your wifi-SSID for that purpose.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6/how-to-operate-ieee-802-11-wifi-ap-within-the-amateur-radio-service, by David Anastasio, user, Joseph, dcaswell. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
