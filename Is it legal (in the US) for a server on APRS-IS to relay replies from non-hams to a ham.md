# Is it legal (in the US) for a server on APRS-IS to relay replies from non-hams to a ham?

*Tags: united-states, legal, aprs · score 6*

## Question

I've heard two sides to this. On one hand, sites that allow you to send messages into the APRS-IS network, for relay over RF, demand you enter a call, as "only licensed hams may cause a message to be relayed over HF". On the other hand, gateways like SMSGTE and EMAIL will allow non-licensed hams to send messages over HF to a ham, generally when they're replying to a message sent by that ham. The system I'm designing is somewhere in the middle - incoming APRS messages from a certain call sign are posted to a Twitter account. Then, replies and mentions are relayed back to the ham, provided the ham has pre-approved the Twitter user that sent that reply or mention. So, given that this gateway server is a "good citizen", with conservative rate limits, blocks against spam, etc, it is legal, in the US, for it to relay the replies, mentions and DMs as described?

## Accepted answer (score 8, by PearsonArtPhoto)

What you are referring to is known as "Third Party Communications". Here is the blurb from the FCC on third party communications:

Section 97.115 of the Commission's Rules, 47 C.F.R. §97.115, authorizes an amateur station regulated by the FCC to transmit a message from its control operator (first party) to another amateur station control operator (second party) on behalf of another person (third party). No amateur station, however, shall transmit messages for a third party to any station within the jurisdiction of any foreign government whose administration has not made arrangements with the United States to allow amateur stations to be used for transmitting international communications on behalf of third parties.

The following countries have made the necessary arrangements with the United States to permit an amateur station regulated by the FCC to exchange messages for a third party with amateur stations in: Antigua and Barbuda, Argentina, Australia, Belize, Bolivia, Bosnia-Herzegovina, Brazil, Canada, Chile, Colombia, Federal Islamic Republic of Comoros, Costa Rica, Cuba, Dominica, Dominican Republic, Ecuador, El Salvador, The Gambia, Ghana, Grenada, Guatemala, Guyana, Haiti, Honduras, Israel, Jamaica, Jordan, Liberia, Republic of the Marshall Islands, Mexico, Federated States of Micronesia, Nicaragua, Panama, Paraguay, Peru, Philippines, St. Christopher and Nevis, St. Lucia, St. Vincent and the Grenadines, Sierra Leone, South Africa, Swaziland, Trinidad and Tobago, Turkey, United Kingdom (special event stations with call sign prefix GB followed by a number other than 3), Uruguay, and Venezuela. The United Nations also has arrangements with the United States to permit an amateur station regulated by the FCC to exchange messages for a third party with amateur stations 4U1ITU in Geneva, Switzerland, and 4U1VIC in Vienna, Austria.

No amateur station regulated by the FCC shall transmit messages for a third party to any amateur station located within the jurisdiction of any foreign government not listed above. This prohibition does not apply to a message for any third party who is eligible to be the control operator of the station.

Bottom line, it's only legal to send a third party message to certain countries. It is perfectly legal if you are keeping it to within the United States, and it's risky to do so outside of the US, unless you know exactly where it's going.

I'm not a lawyer, but I would believe the system you described to be legal if the messages were coming from authorized countries, otherwise it would not be considered legal.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5017/is-it-legal-in-the-us-for-a-server-on-aprs-is-to-relay-replies-from-non-hams-t, by Chris, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
