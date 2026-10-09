# Can I use APRS over TCPIP without ham license?

*Tags: legal, license, aprs, europe · score 3*

## Question

Simple question, but for me is really important. "Can I use the APRS over TCPIP without a ham license in Europe Union (especially in Austria)?"  
I consider yes, because I am not transmitting with radio, but I am not sure. And if yes, which call sign I can use?

## Accepted answer (score 8, by Phil Frost - W8II)

I don't know Europe's regulations, but in the US under the FCC's jurisdiction, the onus is on the station operator to prevent unauthorized transmissions. An unlicensed individual using APRS on the internet wouldn't be violating any regulation, but the station operator who allows her station to make prohibited transmissions via the internet would be.

Likewise, the FCC does not regulate Winlink, AllStar, IRLP, or any other ham-on-internet activity. They regulate what's transmitted, and hold the station operator accountable.

So while using APRS on the internet without a license may not be illegal per se, it's not allowed by the amateurs who operate the APRS network.

## Answer (score 4, by penguin359)

Contrary to other answers, there are ARPS networks out there that can be used without a Ham license. The key, as @PhilFrost points out, is that your original packet must not make it out to RF. The APRS-IS network is specifically focused on supporting an Internet backbone for APRS that might originate or be destined for RF and so requires a Ham license before sending any packets to it, but there are two other, compatible networks that specifically disallow RF transmission of their data, CWOP and FireNet. Both of them tend to be focused around collecting weather data, but will pass any APRS packets receive to other TCP/IP clients attached to the network. All traffic on APRS-IS is replicated on FireNet which also includes a lot of higher volume NWS messages/alerts.

## Answer (score 4, by Pedja YT9TP)

When you send something to APRS, even via Internet, it eventually may end up retransmitted on ham radio frequencies.

Thus, you are not allowed to use the system if you do not have valid amateur radio license.

APRS network requires you to identify using ham radio call sign which you have only if you have valid license.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/7092/can-i-use-aprs-over-tcpip-without-ham-license, by Bjørson Bjørson, Phil Frost - W8II, penguin359, Pedja YT9TP. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
