# Are hashes (such as md5) legal in the US

*Tags: united-states, digital-modes, fcc, remote-control, encryption · score 11*

## Question

If I were to implement a remote computer control system using amateur radio, would using hashes (such as md5, sha-*, etc...) for authentication be permissible under the United States rules?

## Accepted answer (score 12, by PearsonArtPhoto)

Yes, they are. Generally speaking, authentication is legal, obfuscating is not legal. So you could do a cryptographically signed hash that would be legal in the United States to transmit over Amateur Radio.

It's worth mentioning that there is some debate as to how legal a cryptographically signed hash would be. I believe it would be legal, so long as it was a signature, intended to ensure that the message came from a particular person.

MD5 type hashes are definitely legal, they merely provide a signature of data already sent, and are used to ensure the data that was sent is correct.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5259/are-hashes-such-as-md5-legal-in-the-us, by W8AWT, PearsonArtPhoto. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
