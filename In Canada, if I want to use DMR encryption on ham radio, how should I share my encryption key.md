# In Canada, if I want to use DMR encryption on ham radio, how should I share my encryption key?

*Tags: legal, canada, dmr, encryption · score 3*

## Question

In Canada, one is permitted to "use a code or cipher that is not secret" on amateur radio.  
(See: https://laws-lois.justice.gc.ca/eng/regulations/sor-96-484/FullText.html under "Communications with Radio Apparatus in the Amateur Radio Service")  
However, the wording of "not secret" is vague, and I couldn't find the definition of "not secret" in the definitions. If I were to use the encryption function of my DMR radio, how should I publicize the encryption key? Would I need to read it over the air (which would not be very convenient, since the key is pretty long)? Or, could I just put it on my website or QRZ page, along with my call sign?

## Accepted answer (score 3)

"Not secret" in this context means the encoding or protocol has been publicly published and is accepted as some kind of established standard. I think there is a question on the exam to this effect.

Of course, DMR uses publicly available algorithms to do what it does. More to the point, ISED specifically says we may "not employ the use of any secret code, or cipher".

So, the encryption built into DMR handhelds is based on algorithms that are both well-established and publicly available, and also trivial to break (at least at the "basic" tier).

None of the security modes in DMR that I just looked at are actually "encryption". They are more of a basic scrambling system based on a shared keys that are rotated in predictable order. At the basic level one could scan all 256 keys and find the one you are using. But, combined with frequency hopping and slot assignment this is considered Good Enough security.

*Perhaps* the 40-bit choose-your-own-key runs afoul of the Regulations in Canada. Certainly many US hams say that it does for them. (And just as many would argue that protecting certain comms has *always* been legal for them, and only if the *purpose* of the encryption was to "obscure" the message would they be contrary to laws regarding their license. I'm no lawyer, but that sounds like an excellent way to lose a legal argument and your license at the same time.)

Though, at the end of the day, given that anyone, private citizen or scary governmental agency, can walk into a shop and buy equipment to crack all your DMR messages sort of makes the whole thing a moot question.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20669/in-canada-if-i-want-to-use-dmr-encryption-on-ham-radio-how-should-i-share-my-e, by Felix An. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
