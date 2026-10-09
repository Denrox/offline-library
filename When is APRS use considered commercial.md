# When is APRS use considered commercial?

*Tags: united-states, aprs · score 12*

## Question

I've heard that APRS is only allowed for non-commercial use. I was thinking of a building a weather station that uploads data via APRS (so far, non-commercial). If I then include data from that weather station on a website with advertisements, is it commercial use (and thus not allowed)? If that is not commercial use, what would be an example of commercial use?

## Accepted answer (score 9, by Kevin Reid AG6YO)

There is no rule specific to APRS; the relevant regulations do not care about what mode, protocol, etc. you are using. From §97.113:

§97.113 Prohibited transmissions.

(a) No amateur station shall transmit:

1.

Communications specifically prohibited elsewhere in this part;

2.

**Communications for hire or for material compensation**, direct or indirect, paid or promised, except as otherwise provided in these rules;

3.

Communications in which **the station licensee or control operator has a pecuniary interest**, including communications on behalf of an employer, with the following exceptions:

4.

...

*I am not a lawyer. This is not legal advice. This is speculation based on a layman's understanding. If you actually need a reliable answer, consult a lawyer.*

These rules prohibit what you are proposing, because you are making transmissions which in which you have a pecuniary interest: your site, from which you profit via advertisements, would be of less value if you did not have the weather station transmitting.

On the other hand, if you are only doing one of the two things:


If you have a weather station transmitting and no one's paying you to do it, there is no pecuniary interest, so the transmission is not prohibited.


If you are receiving APRS and displaying the data on a web site, you are not transmitting, so §97.113 does not apply. In fact, the well-known APRS data site aprs.fi contains ads.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/2318/when-is-aprs-use-considered-commercial, by Anssssss, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
