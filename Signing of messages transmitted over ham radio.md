# Signing of messages transmitted over ham radio

*Tags: united-states, legal, encryption · score 7*

## Question

FCC Regulation 97.113 (a) 4 states that:

"messages encoded for the purpose of obscuring their meaning"

Are "Prohibited transmissions", I believe this is the clause that is used to prohibit encryption over ham radios. Are there any other clauses that are used to prohibit encryption.

If not, is "signing" of messages acceptable/legal over ham radios. For example consider the following transmission:

A digitally transmitted message contains:

1. The callsign of the sender.
2. The callsign of the intended recipient
3. The public key of the sender
4. The entire body of the message in plain text.
5. A checksum/signature generated from the private key of the sender and the body of the message.

In this case no encrypted information is sent. Additionally any receiver of the message can verify both the integrity of the message (by validating the signature) and that no additional information has been sent, since the entire signature is used as part of the validation process.

Note: I realize that sending the public key is superfluous, but I didn’t want to get into the details of key exchange protocols as part of this question.

Edit: 3/10/19

Thank you all, for the high quality responses.

As pointed out by others in the comments, I had three concerns:

1. That it would be possible to authenticate the generation of the message (this system cannot detect the retransmission of the message in full).
2. That a third party can verify the message contains no encrypted information.
3. That in the US, the only applicable regulation was 97.113 (a) 4

I had read another article specifically on CRAM-MD5 over amateur radio, however my concern was that any system that uses a shared secret, will require the secret in order to prove that no encrypted information is present (if you don’t know the secret, the checksum might be an encrypted string).

This was the reason I based the question on public/private key crypto and why I included the public key in the transmission - I realize that any receiver that wishes to authenticate the transmission needs to obtain the public key via a secure channel.

However with the message formatted as it is, any receiver that knows the protocol, can verify that the message contains no encrypted data.

I feel all these concerns have been addressed and I have accepted the answer.

## Accepted answer (score 4, by Glenn W9IQ)

Even though signing of a digest uses cryptographic techniques, this is permitted.

The Part 97 regulations regarding obscuring clearly speaks of purpose/intent. The regulation you quoted is the only one that applies to this topic for amateur radio. The FCC has previously commented that encryption is prohibited under this regulation even if the algorithm is well published.

A signed digest is not intended, nor is its purpose, to obscure, rather it is used for authentication, integrity and non-repudiation. It would be wise to publically publish the protocol in order to avoid any misunderstandings. In order to minimize potential legal issues, I recommend that you make certain the digest only uses information derived from the clear text (no new or hidden information, no salting, etc.) and its derivation and the signing technique be based on a publicly available method or standard (e.g. SHA or DSA). Similarly, the public keys should be publicly obtainable from a recognized CA (certificate authority).

Be aware that other countries may not permit this technique so it may not see world wide adaption or use.

While I believe your comment regarding the sending of the public key was simply to clarify your question, in practice this is cryptographically weak and should be avoided.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/12994/signing-of-messages-transmitted-over-ham-radio, by DavidT, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
