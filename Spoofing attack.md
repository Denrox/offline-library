# Spoofing attack

In the context of information security, and especially network security, a **spoofing attack** is a situation in which a person or program successfully identifies as another by falsifying data, to gain an illegitimate advantage.

### Internet

#### Spoofing and TCP/IP

Many of the protocols in the TCP/IP suite do not provide mechanisms for authenticating the source or destination of a message, leaving them vulnerable to spoofing attacks when extra precautions are not taken by applications to verify the identity of the sending or receiving host. IP spoofing and ARP spoofing in particular may be used to leverage man-in-the-middle attacks against hosts on a computer network. Spoofing attacks which take advantage of TCP/IP suite protocols may be mitigated with the use of firewalls capable of deep packet inspection or by taking measures to verify the identity of the sender or recipient of a message.

#### Domain name spoofing

The term 'Domain name spoofing' (or simply though less accurately, 'Domain spoofing') is used generically to describe one or more of a class of phishing attacks that depend on falsifying or misrepresenting an internet domain name. These are designed to persuade unsuspecting users into visiting a web site other than that intended, or opening an email that is not in reality from the address shown (or apparently shown). Although website and email spoofing attacks are more widely known, any service that relies on domain name resolution may be compromised.

#### Referrer spoofing

Some websites, especially pornographic paysites, allow access to their materials only from certain approved (login-) pages. This is enforced by checking the referrer header of the HTTP request. This referrer header, however, can be changed (known as "referrer spoofing" or "Ref-tar spoofing"), allowing users to gain unauthorized access to the materials.

#### Poisoning of file-sharing networks

"Spoofing" can also refer to copyright holders placing distorted or unlistenable versions of works on file-sharing networks.

#### E-mail address spoofing

The sender information shown in e-mails (the From: field) can be spoofed easily. This technique is commonly used by spammers to hide the origin of their e-mails and leads to problems such as misdirected bounces (i.e. e-mail spam backscatter).

E-mail address spoofing is done in quite the same way as writing a forged return address using snail mail. As long as the letter fits the protocol, (i.e. stamp, postal code) the Simple Mail Transfer Protocol (SMTP) will send the message. It can be done using a mail server with telnet.

#### Geolocation

Geolocation spoofing occurs when a user applies technologies to make their device appear to be located somewhere other than where it is actually located. The most common geolocation spoofing is through the use of a Virtual Private Network (VPN) or DNS Proxy in order for the user to appear to be located in a different country, state or territory other than where they are actually located. According to a study by GlobalWebIndex, 49% of global VPN users utilize VPNs primarily to access territorially restricted entertainment content. This type of geolocation spoofing is also referred to as geo-piracy, since the user is illicitly accessing copyrighted materials via geolocation spoofing technology. Another example of geolocation spoofing occurred when an online poker player in California used geolocation spoofing techniques to play online poker in New Jersey, in contravention of both California and New Jersey state law. Forensic geolocation evidence proved the geolocation spoofing and the player forfeited more than $90,000 in winnings.

### Telephony

#### Caller ID spoofing

Public telephone networks often provide caller ID information, which includes the caller's number and sometimes the caller's name, with each call. However, some technologies (especially in Voice over IP (VoIP) networks) allow callers to forge caller ID information and present false names and numbers. Gateways between networks that allow such spoofing and other public networks then forward that false information. Since spoofed calls can originate from other countries, the laws in the receiver's country may not apply to the caller. This limits laws' effectiveness against the use of spoofed caller ID information to further a scam.

### Satellite navigation spoofing

In global navigation satellite systems (GNSS), a spoofing attack attempts to deceive a GNSS receiver by broadcasting fake GPS or other GNSS signals, structured to resemble a set of normal GNSS signals, or by rebroadcasting genuine signals captured elsewhere or at a different time. GNSS spoofing is a more sophisticated and deceptive practice than GNSS jamming, which merely blocks affected devices from being able to use GNSS systems at all.

Spoofing attacks are generally hard to detect as adversaries generate counterfeit signals. These spoofed signals are challenging to recognize from legitimate signals, thus confusing ships' calculation of positioning, navigation, and timing (PNT). This means that spoofed signals may be modified in such a way as to cause the receiver to estimate its position to be somewhere other than where it actually is, or to be located where it is but at a different time, as determined by the attacker. One common form of a GNSS spoofing attack, commonly termed a carry-off attack, begins by broadcasting signals synchronized with the genuine signals observed by the target receiver. The power of the counterfeit signals is then gradually increased and drawn away from the genuine signals.

Even though GPS and other GNSS networks are among the most relied upon navigational systems, they have demonstrated critical vulnerabilities towards spoofing attacks. GNSS satellite signals have been shown to be vulnerable due to the signals' being relatively weak on Earth's surface. A reliance on GNSS could result in the loss of life, environmental contamination, navigation accidents, and financial costs. However, since 80% of global trade is moved through shipping companies, relying upon GNSS systems for navigation remains unavoidable.

As of 2022, all public-access GNSS systems, such as the US GPS, Russia's GLONASS, China's BeiDou, and Europe's Galileo constellation, are vulnerable to this technique. In order to mitigate some of the vulnerabilities the GNSS systems face concerning spoofing attacks, the use of more than one navigational system at once is recommended. In 2025, Galileo deployed a feature that allows supporting receivers to differentiate between real and forged signals using cryptography.

The term GPS spoofing may refer either to a GNSS spoofing attack or to a distinct phenomenon more accurately known as AIS spoofing or *first-party spoofing*, in which a vessel or aircraft deliberately broadcasts false information about its own position via AIS signals, despite its crew knowing its correct position.

### Voice spoofing

Information technology plays an increasingly large role in today's world, and different authentication methods are used for restricting access to informational resources, including voice biometrics. Examples of using speaker recognition systems include internet banking systems, customer identification during a call to a call center, as well as passive identification of a possible criminal using a preset "blacklist".

Technologies related to the synthesis and modeling of speech are developing very quickly, allowing one to create voice recordings almost indistinguishable from real ones. Such services are called text-to-speech (TTS) or style transfer services. The first one aimed at creating a new person. The second one aimed at identifies as another in voice identification systems.

A large number of scientists are busy developing algorithms that would be able to distinguish the synthesized voice of the machine from the real one. On the other hand, these algorithms need to be thoroughly tested to make sure that the system really works. Prior work has demonstrated that feature design and masking-based augmentation play an important role in improving spoofed speech detection performance. More recently, approaches that integrate trainable feature extractors with strong and diverse audio augmentation strategies have shown improved robustness, highlighting the importance of jointly learning representations while exposing the model to a wide range of artifacts and signal distortions.

### Facial recognition spoofing

Facial recognition technology is widely employed in various areas, including immigration checks and phone security, as well as on popular platforms like Airbnb and Uber to verify individuals' identities. However, the increased usage has rendered the system more susceptible to attacks, given the widespread integration of facial recognition systems in society. Some online sources and tutorials detail methods for tricking facial recognition systems through practices known as face spoofing or presentation attacks, which can pose risks in terms of unauthorized access. To mitigate these dangers, measures such as liveness checks (verifying blinking), deep learning, and specialized cameras like 3D cameras have been introduced to prevent facial recognition spoofing. It is important to implement comprehensive security procedures like these to protect against face spoofing attempts and uphold the overall security and integrity of systems relying on facial recognition authentication.

---

*Source: Wikipedia, Spoofing attack (https://en.wikipedia.org/wiki/Spoofing_attack), by Wikipedia contributors, CC BY-SA 4.0.*
