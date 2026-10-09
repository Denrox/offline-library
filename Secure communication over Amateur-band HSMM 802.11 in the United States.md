# Secure communication over Amateur-band HSMM / 802.11 in the United States

*Tags: united-states, legal, security, hsmm · score 6*

## Question

I'm quite interested in 802.11 over amateur radio frequencies; however, all I have done at this point is reading (I don't have a ham license yet). The [conventional wisdom (espoused in this ham.SE answer) is that you cannot encrypt radio communications at all](Encrypted%20traffic%20and%20amateur%20radio.md). This limitation seems to fly in the face of normal countermeasures used to secure data transfers through the internet.

So encryption is off the table; however, that still leaves issues such as authentication and data integrity. I have read that CRAM-MD5 hashes are sometimes used as part of data services implemented over 802.11 ham radio, because CRAM-MD5 hashes are allowed under the FCC rules. The contents of messages signed with CRAM-MD5 are always visible; yet, the authorship of the message can be verified (because CRAM-MD5 works in the same way that PGP does). As best I can tell, using CRAM-MD5 leaves you vulnerable because:

- It does not perform mutual authentication (i.e. the client can't verify the server's identity)
- It's possible to run off-line dictionary attacks against captured hashes (although the underlying HMAC-MD5 hash doesn't have the same vulnerabilities as MD5).

The bigger concern to me is a man in the middle attack, since CRAM-MD5 offers no mutual authentication between client and server. This kind of vulnerability is also the kind of dynamic that makes PEAP worse than no 802.11 authentication (since PEAP doesn't enforce mutual authentication between the wifi client and RADIUS server, like EAP-TLS does). It has been shown that weak PEAP clients freely offer their password hashes to a wifi AP masquerading the same SSID as the real AP. My concern with 802.11 over ham frequencies is determining that I'm giving my password / data to the right endpoint on the other side (and not an attacker).

### Questions

- Is there another authentication scheme besides CRAM-MD5, that is both legal in the US and performs mutual authentication?
- If I wanted to implement an authenticated HTTP service over ham radio, is there another authentication scheme that I should consider besides CRAM-MD5?

## Accepted answer (score 7, by Amber)

I'd say your best bet is to avoid handing over your hashed password entirely. Instead, use a zero-knowledge authentication scheme; see this security.SE question for more details. Zero Knowledge Authentication will make it so that it doesn't matter who you "give" your response to - even if a malicious server requests authentication (or intercepts other authentication), it doesn't actually learn anything about your password.

If you incorporate the response to the zero-knowledge auth as part of the public-key signed request, you should be able to formulate a system that both (a) is signed by the client, and (b) does not reveal information to 3rd parties that would allow them to forge future requests, since the zero-knowledge challenge response would form a nonce.

As far as verifying the server goes, a public key signature should suffice.

*(Previous response, before OP clarified...)*

IANAL, but...

There is a difference between *encryption* and *authentication*. The former requires no one to be able to tell what data is being passed; the latter requires no one to be able to produce something that is accepted as legitimate without some (non-public) knowledge.

For instance, public-key based signatures allow for authentication of a message's sender without obscuring the contents of the message.

As long as you're okay with the content of your requests being *visible* but not *forgeable*, you could probably use such a public key system without running afoul of the FCC regs.

If, on the other hand, you don't want anyone to be able to see what's in your requests and responses, you're out of luck.

Again, IANAL.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/172/secure-communication-over-amateur-band-hsmm-802-11-in-the-united-states, by Mike Pennington, Amber. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
