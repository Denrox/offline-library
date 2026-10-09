# Would a ham license allow me to use an uncertified radio on other (non-ham) bands I have permission to use?

*Tags: united-states, legal, license, uv-5r · score 3*

## Question

I just purchased a UV-5R to hopefully integrate into business class radios my company uses. Do I need a technician or other class FCC license to operate these only on the frequencies I already access with the business radios?

If I do need a license then what class would this type of use fall under, it seems to be something that doesn’t qualify entirely under any of the FCC classes as I’ve read them so far.

## Answer (score 11, by natevw - AF7TB)

I just purchased a UV-5R to hopefully integrate into business class radios my company uses.

Unfortunately, this is not likely legal.

Business radio is licensed under the FCC's Part 90 rules; those rules include 47 CFR § 90.203 - Certification required: "[…] each transmitter utilized for operation under this part […] must be of a type which has been certified for use under this part."

That is, unless the FCC has approved your particular radio model for use on business bands, you can't use it there. And they will **not** approve radios where the user can arbitrarily change the frequency. That's based on §90.203(e), which says transmitters "shall not be certified […] if the operator can program and transmit on frequencies other than those programmed […]".

The radio you use on business bands has to be both:

- eligible for Part 90 certification
- have been granted that certification

For example, the UV-82C is a special version of a similar radio to what you have. It has its frequency settings locked out **and** then successfully went through the process to get an FCC-ID approval. As a result, it would be legal to use. It also looks a bit more expensive to buy!

Do I need a technician or other class FCC license to operate these only on the frequencies I already access with the business radios?

A Technician-class license under *would* allow you to operate a UV-5R on the "ham" bands but **not** on the "business" bands. There's no crossover between the Amateur Radio Service ("ham radio", i.e. Part 97 rules) and the Private Land/Mobile Radio Service ("business radio", i.e. Part 90 rules).

Even if you have multiple licenses, each time you use a radio you have to operate completely within **one** of them:

- as a ham licensee you could use that radio on the 2m or 70cm frequencies, but you have to follow that license rules (saying your callsign frequently, not conducting business, etc.) and transmit **only** on frequencies allowed to Technician class operators
- as a business licensee you could use certain other frequencies that hams can't, but unfortunately only using an approved ("certified") radio

This is similar to the situation with [using a Baofeng on FRS or MURS frequencies](Using%20my%20Baofeng%20UV-5R%20to%20talk%20to%20walkie%20talkies.md), where they are technically not allowed due to lack of certification, even if used in an otherwise appropriate manner.

The ham license is fairly unique in allowing non-certified equipment. The trade-off is that you have to both pass a knowledge test to get the license, and also abide by a lot of communication restrictions once you have it. For the other services, they put the burden more on the equipment manufacturer than the end-user.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/14597/would-a-ham-license-allow-me-to-use-an-uncertified-radio-on-other-non-ham-band, by Trevor, natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
