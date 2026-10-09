# Has any computer been hacked over amateur radio digital modes?

*Tags: digital-modes, security, digital · score 7*

## Question

We don't normally worry about security in ham radio, because we can't encrypt our transmissions anyway in the vast majority of cases. Some niche protocols support authentication of messages, but that's it, unless you're controlling satellites. There is nothing except regulations and etiquette stopping me from making contacts using any mode with someone else's call sign, and if I use a digital mode, there's no way for anyone except me and the person I'm impersonating to tell. It is certainly possible for me to eavesdrop on other people's conversations, and this is neither illegal nor unethical.

However, when we use digital modes, our computers are processing arbitrary data from an untrusted source. Since security isn't really a concern for most hams, it's unlikely that ham radio programs such as fldigi and WSJT-X are tested for responses to invalid data; it's quite possible that some ham programs have remote code execution vulnerabilities or similar bugs. There is nothing (again, except regulations and etiquette) stopping a hacker from making transmissions intended to exploit such bugs.

I found a few articles about people hacking their own computers over ham radio for experiments, but have there been any documented cases of a ham radio operators' (or shortwave listener's) computer being compromised over an amateur radio digital mode without the owner's permission?

## Answer (score 6, by user3486184)

I know of at least one app that has been hacked based on data received over the air. Because it was done by an ethical pen tester it didn't adversely affect an unsuspecting party, but nonetheless WinAPRS has had three CVEs opened against it:

- CVE-2022-24700
- CVE-2022-24701
- CVE-2022-24702

The last one (24702) is the most concerning, as it "allows a remote attacker to achieve remote code execution via malicious AX.25 packets over the air." The original developer of WinAPRS no longer has a build environment for the application, so this vulnerability is likely to remain for all WinAPRS users.

Rick Osgood did the original research and filed the vulnerability; his efforts are documented at Hacking Ham Radio: WinAPRS.

## Answer (score 4, by user10489)

There are two aspects to communications security here; security issues surrounding invalid data causing issues, and valid data including a command that is itself an inherent security issue.

Addressing the first issue, most ham protocols are sufficiently simple that invalid data causing a security issue is unlikely. Others, like WSJT-X are actually extremely complicated and most of the design of the protocol is all about detecting and correcting invalid data. To assume that something like WSJT-X is not tested is extremely wrong -- because when you're receiving data from a radio, especially weak signal HF data, the likelyhood of receiving corrupted data is extremely high. All radio data protocols need to be robust in handling corrupted data because amateur radio is all about dealing with noise mixed in with your signal.

One of the common ways to test for this type of security vulnerability is to send random data to the program and see if it crashes. With amateur radio, this happens (literally) naturally. I'm not saying that there are no buggy amateur radio programs. What I'm saying is that they will crash from natural noise and it will likely be noticed long before anyone tries to hack them with invalid data, and that these programs do need to be tested for that or they are not going to function well in a real environment. (Of course, cleverly invalid data rather than just randomly invalid data could still be a big issue.)

As to the second point, if the signal carries valid control data for a control command, this is not a radio issue but an issue with the security of the control system. I think a lot of telemetry control protocols rely on it being highly illegal to send unauthorized communications with huge penalties, and don't think a lot about that type of security. Having said that, FCC part 97 specifically authorizes encryption ("that obscures meaning") for only one purpose -- satellite control.

And, as already covered in the comments, I believe cryptographicly signing a control packet can be designed so that it does not obscure meaning and thus is not illegal. But I believe the use of cryptographic signatures did not exist when the FCC regulations concerning encryption were written, and the regulations have not been updated with this language -- and possibly don't need to be.

## Answer (score 2, by Aleksander Alekseev - R2AUK)

That's an excellent question! It's true that software has bugs and in theory one can hack an SDR transceiver and/or PC over ham radio bands. This is also true for regular (non-amateur) SDR receivers, and not necessarily only SDR.

This being said a modern security world is quite commercialized. People having expertise necessary to implement such an exploit are smart and their services are not cheap. They are also smart enough to make good money without breaking a law.

So unless Yaesu / Kenwood / ICOM will open a bug bounty program I don't think we will see such attacks in any foreseeable future. To my knowledge such attacks were not reported as of today.

People do hack other wireless devices though, like Wi-Fi routers, IoT devices (webcams, robot vacuums, even sex toys). These are cheap and often have literally no security. So even if a manufacturer doesn't have a bug bounty program such devices are a good target to boost the resume of a newcomer to the security world, or just to spent time with fun.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21565/has-any-computer-been-hacked-over-amateur-radio-digital-modes, by Someone, user3486184, user10489, Aleksander Alekseev - R2AUK. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
