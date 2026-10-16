# Prosigns for Morse code

**Procedural signs** or **prosigns** are shorthand signals used in [Morse code](Morse%20code.md) telegraphy, for the purpose of simplifying and standardizing procedural protocols for landline and radio communication. The procedural signs are distinct from conventional [Morse code abbreviations](Morse%20code%20abbreviations.md), which consist mainly of [brevity codes](Brevity%20code.md) that convey messages to other parties with greater speed and accuracy. However, some codes are used *both* as prosigns and as single letters or punctuation marks, and for those there is an ambiguity even in context since they are not distinct.

### Overview

In the broader sense prosigns are just standardised parts of short form radio protocol, and can include any abbreviation. Examples would be **K** for "okay, heard you, continue" or **R** for "message, received". In a more restricted sense, "prosign" refers to something analogous to the nonprinting control characters in teleprinter and computer character sets, such as Baudot and ASCII. Different from abbreviations, those are universally recognizable across language barriers as distinct and well-defined symbols.

At the coding level, prosigns admit any form the Morse code can take, unlike abbreviations which have to be sent as a sequence of individual letters, like ordinary text. On the other hand, most prosigns codes are much longer than typical codes for letters and numbers. They are individual and indivisible code points within the broader Morse code, fully at par with basic letters and numbers.

The development of prosigns began in the 1860s for wired telegraphy. Since telegraphy preceded voice communications by several decades, many of the much older Morse prosigns have acquired precisely equivalent pro*words* for use in more recent voice protocols.

Not all prosigns used by telegraphers are standard: There are regional and community-specific variations of the coding convention used in certain radio networks to manage transmission and formatting of messages, and many unofficial prosign conventions exist; some of which might be redundant or ambiguous. One typical example of something which is not an officially recognized prosign, but is yet fairly often used in Europe, is one or two freely timed dits at the end of a message,  **II**   or  ▄ ▄   ▄ ▄ ; it is equivalent to the proword *OUT*, meaning "I'm done; go ahead". However the *official* prosign with the same meaning is **AR**, or  ▄ ▄▄▄ ▄ ▄▄▄ ▄ , which takes a little longer to send.

#### Representation in printed material

Even though represented as strings of letters, prosigns are rendered without the intercharacter commas or pauses that would occur between the letters shown, if the representation were (mistakenly) sent as a sequence of letters: In printed material describing their meaning and use, prosigns are shown either as a sequence of dots and dashes for the sound of a telegraph, or by an overlined sequence of letters from the International Morse Code, which when sent *without* the usual spacing, sounds like the prosign symbol.

The best-known example of the convention is the standard distress call preamble: **SOS**. As a prosign it is not really composed of the three separate letters *S*, *O*, and *S*, (in International Morse:  ▄ ▄ ▄   ▄▄▄ ▄▄▄ ▄▄▄   ▄ ▄ ▄ ) but is run together as a single symbol  ▄ ▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ▄ , which is a sign in its own right.

### Notation and representations

There are at least three methods used to represent Morse prosign symbols:

1. Unique dot/dash sequences, e.g.  ▄▄▄ ▄ ▄ ▄ ▄▄▄
2. Unique audible sounds, e.g. *dah di di di dah*
3. Non-unique printed or written overlined character groups, e.g. **BT**

Although some of the prosigns as-written appear to be simply two adjacent letters, *most* prosigns are transmitted as digraphs that have ***no*** pauses between the patterns that represent the "combined" letters, and are most commonly written with a single bar over the merged letters (if more than one single character) to indicate this. The only difference between what is transmitted for the Morse code prosign vs. the separate letter signs is the presence or absence of an inter-letter space between the two "dit" / "dah" sequences. Although the difference in the transmission is subtle, the difference in meaning is significant:  
For example, the unofficial prosign **AA** ( ▄ ▄▄▄ ▄ ▄▄▄ ) indicates that the receiving Morse operator should begin a new line, but the two separate letter sign or abbreviation **AA** ( ▄ ▄▄▄  ▄ ▄▄▄ ) indicates the voice procedure words *ALL AFTER*, used to indicate what part of the previously transmitted message needs to be re-transmitted.

Because no letter boundaries are transmitted with the codes counted as *prosigns*, their representation by two letters is usually arbitrary, and may be done in multiple equivalent ways. Normally, one particular form is used by convention, but some prosigns have multiple forms in common use:  
For example, **AA** ( ▄ ▄▄▄ + ▄ ▄▄▄ ) is exactly equivalent to **EK** ( ▄ + ▄▄▄ ▄ ▄▄▄ ) and **RT** ( ▄ ▄▄▄ ▄ + ▄▄▄ ).  
Although the well-known calling prosign for emergency messages **SOS** is always represented by the three letters "SOS", it *could* just as well be written **VZE** ( ▄ ▄ ▄ ▄▄▄ + ▄▄▄ ▄▄▄ ▄ ▄ + ▄ ), **VGI** ( ▄ ▄ ▄ ▄▄▄ + ▄▄▄ ▄▄▄ ▄ + ▄ ▄ ), or even **3B** ( ▄ ▄ ▄ ▄▄▄ ▄▄▄ + ▄▄▄ ▄ ▄ ▄ ); all of these render the same single code  ▄ ▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ▄ .

Many Morse code prosigns do not have written or printed textual character representations in the original source information, even if they do represent characters in other contexts. For example, when embedded in text the Morse code sequence  ▄▄▄ ▄ ▄ ▄ ▄▄▄  represents the "double hyphen" character (normally "**=**", but also "**– –**"). When the same code appears alone it indicates the action of spacing down two lines on a page in order to create the white space indicating the start of a new paragraph or new section in a message heading. When used as a prosign, there is no actual written or printed character representation or symbol for a new paragraph (i.e. no symbol corresponding to "¶"), other than the two-line white space itself.

Some prosigns are in unofficial use for special characters in languages other than English, for example **AA** is used unofficially for both the "next line" prosign and for "**Ä**", neither of which is in the international standard. Other prosigns are officially designated for both characters and prosigns, such as **AR** equiv. "**+**", which marks the end of a message. Some genuinely have only one use, such as **CT** or the equivalent **KA** ( ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ), the International Morse prosign that marks the start of a new transmission or new message.

### International Morse code

The procedure signs below are compiled from the official specification for Morse Code, ITU-R M.1677, International Morse Code, while others are defined the International Radio Regulations for Mobile Maritime Service, including ITU-R M.1170, ITU-R M.1172, and the Maritime International Code of Signals, with a few details of their use appearing in ACP 131, which otherwise defines operating signals, not procedure signals.

#### Prosigns

The following table of prosigns includes **K** and **R**, which could be considered either abbreviations (for "okay, go ahead", and for "received") or prosigns that are also letters. All of the rest of the symbols are not letters, but in some cases are also used as punctuation.

General-use procedure signs
- Prosign   Matching voice procedure word   Code symbol   Reference   Explanation
- **AA**   *UNKNOWN STATION*    ▄ ▄▄▄ ▄ ▄▄▄       This meaning is ***only*** used for directional signal lights. It has no official use in radio telegraphy, where it is *unofficially* used to represent an accented letter **Ä** or **Á**, or the prosign for "next line", and then only when it is embedded inside a heading section in amateur traffic.
- **R**   *ROGER*    ▄ ▄▄▄ ▄       Means the last transmission has been received, but does *not* necessarily indicate the message was understood or will be complied with.  
- **K**   *OVER*    ▄▄▄ ▄ ▄▄▄       Invitation to transmit after terminating the call signal. (e.g.  ▄ ▄▄▄ ▄ ▄▄▄ ▄  ▄▄▄ ▄ ▄▄▄ ).  
- **AR**   *OUT*    ▄ ▄▄▄ ▄ ▄▄▄ ▄       End of transmission / End of message / End of telegram.  
(Same as **EC** "end copy", and character [ **+** ].)  
- **AS**   *WAIT*    ▄ ▄▄▄ ▄ ▄ ▄       "I must pause for a few minutes." Also means "I am engaged in a contact with another station (that you might not hear); please wait quietly."  
- **ASAR**   *WAIT* *OUT*    ▄ ▄▄▄ ▄ ▄ ▄  
▄ ▄▄▄ ▄ ▄▄▄ ▄       I must pause for more than a few minutes.
- **VE**   *VERIFIED*    ▄ ▄ ▄ ▄▄▄ ▄       Message is verified.  
- [ **?** ]   *SAY AGAIN?*    ▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄       When standing alone, a note of interrogation or request for repetition of the immediate prior transmission that was not understood. When [ **?** ] is placed *after* a coded signal, modifies the code to be a question or request.  
- **INT**   *INTERROGATIVE*    ▄ ▄ ▄▄▄ ▄ ▄▄▄       Military replacement for the [ **?** ] prosign; equivalent to Spanish [[ **¿** ] punctuation mark](https://en.wikipedia.org/wiki/%C2%BF). When placed *before* a signal, modifies the signal to be a question/request.
- **HH** ...   *CORRECTION*    ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄       Preceding text was in error. The following is the corrected text. (Same as **IIII** or **EEEEEEEE**.)  
- **HHAR**   *DISREGARD THIS TRANSMISSION* *OUT*    ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄  
▄ ▄▄▄ ▄ ▄▄▄ ▄       The entire message just sent is in error, disregard it. (Same as **EEEEEEEEAR**.)
- **BT**   *BREAK*    ▄▄▄ ▄ ▄ ▄ ▄▄▄       Start new section of message.  
Same as character [ **=** ] or rarely [ **– –** ] .
- **KA**   *ATTENTION*    ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄       Message begins / Start of work / New message  
(Starting signal that precedes every transmission session. Sometimes written as **CT**.)  
- **SK**   *OUT*    ▄ ▄ ▄ ▄▄▄ ▄ ▄▄▄       End of contact / End of work / Line is now free / Frequency no longer in use  
(Ending signal that follows every transmission session. Occasionally written **VA**.)  
Also used as shorthand to describe a "Silent Key", i.e. a radio operator who has passed away.

#### Abbreviations for message handling

The following table lists standard abbreviations used for organizing radiotelegraph traffic, however none of them are actual prosigns, despite their similar purpose. All are strictly used as normal strings of one to several letters, never as digraph symbols, and have standard meanings used for the management of sending and receiving messages. Dots following indicate that in use, the abbreviation is always followed by more information.

General-use abbreviations and letter-codes
- Abbrev.   Matching voice procedure word   Code symbol   Reference   Explanation
- **DE** ...   *[THIS IS] FROM*    ▄▄▄ ▄ ▄   ▄       Used to precede the name or other identification of the station sending the transmission ([Morse abbreviation](Morse%20code%20abbreviations.md)).
- **NIL**   *NOTHING HEARD*    ▄▄▄ ▄   ▄ ▄   ▄ ▄▄▄ ▄ ▄       General-purpose response to any request or inquiry for which the answer is "nothing" or "none" or "not available" ([Morse abbr.](Morse%20code%20abbreviations.md)). Also means "I have no messages for you."
- **CL**   *CLOSING*    ▄▄▄ ▄ ▄▄▄ ▄   ▄ ▄▄▄ ▄ ▄       Announcing station shutdown ([Morse abbr.](Morse%20code%20abbreviations.md)).
- **CQ**   *CALLING*    ▄▄▄ ▄ ▄▄▄ ▄   ▄▄▄ ▄▄▄ ▄ ▄▄▄       General call to any station ([Morse abbr.](Morse%20code%20abbreviations.md)).
- **CP** ... ...   *CALLING FOR*    ▄▄▄ ▄ ▄▄▄ ▄   ▄ ▄▄▄ ▄▄▄ ▄       Specific call to two or more named stations ([Morse abbr.](Morse%20code%20abbreviations.md)).
- **CS** ...   *CALLING STATION*    ▄▄▄ ▄ ▄▄▄ ▄   ▄ ▄ ▄       Specific call to exactly one named station ([Morse abbr.](Morse%20code%20abbreviations.md)).
- **CS ?**   *WHO ?*    ▄▄▄ ▄ ▄▄▄ ▄   ▄ ▄ ▄   ▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄       What is the name or identity signal of your station? ([Morse abbr.](Morse%20code%20abbreviations.md)) In many contexts, the question mark is optional.
- **WA** ...   *WORD AFTER*    ▄ ▄▄▄ ▄▄▄   ▄ ▄▄▄       ([Morse abbr.](Morse%20code%20abbreviations.md))
- **WB** ...   *WORD BEFORE*    ▄ ▄▄▄ ▄▄▄   ▄▄▄ ▄ ▄ ▄       ([Morse abbr.](Morse%20code%20abbreviations.md))
- **AA** ...   *ALL AFTER*    ▄ ▄▄▄   ▄ ▄▄▄       The portion of the message to which I refer is all that follows the text ... ([Morse abbr.](Morse%20code%20abbreviations.md))
- **AB** ...   *ALL BEFORE*    ▄ ▄▄▄   ▄▄▄ ▄ ▄ ▄       The portion of the message to which I refer is all that precedes the text ... ([Morse abbr.](Morse%20code%20abbreviations.md))
- **BN** ... ...   *ALL BETWEEN*    ▄▄▄ ▄ ▄ ▄   ▄▄▄ ▄       The portion of the message to which I refer is all that falls between ... and ... ([Morse abbr.](Morse%20code%20abbreviations.md))
- **C**   *CORRECT* / *YES* / *AFFIRMATIVE* / *CONFIRM*    ▄▄▄ ▄ ▄▄▄ ▄       Answer to prior question is "yes". ([Morse abbr.](Morse%20code%20abbreviations.md))
- **N**   *NO* / *NEGATIVE*    ▄▄▄ ▄       Answer to prior question is "no". ([Morse abbr.](Morse%20code%20abbreviations.md))
- **ZWF** ...   *WRONG*    ▄▄▄ ▄▄▄ ▄ ▄  ▄ ▄▄▄ ▄▄▄  ▄ ▄ ▄▄▄ ▄       Your last transmission was wrong. The correct version is ...
- **QTR ?**   *REQUEST TIME CHECK*    ▄▄▄ ▄▄▄ ▄ ▄▄▄  ▄▄▄  ▄ ▄▄▄ ▄  
▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄       Time-check request. / What is the correct time?  
(Time is always UTC, unless explicitly requested otherwise, e.g. **QTR** **HST** **?**)
- **QTR** ...   *TIME IS*    ▄▄▄ ▄▄▄ ▄ ▄▄▄   ▄▄▄   ▄ ▄▄▄ ▄       The following is the correct time in HHMM 24 hour format  
(The time is always in UTC, except in rare cases when it is followed by a 3 letter time zone abrv., e.g. **PST**.)
- **BK**   *BREAK-IN*    ▄▄▄ ▄ ▄ ▄   ▄▄▄ ▄ ▄▄▄       Signal used to interrupt a transmission already in progress ([Morse abbr.](Morse%20code%20abbreviations.md)). NATO nets use **AX**. Some military networks use  ▄▄▄▄▄▄▄▄▄▄▄  ≈ **TTTT** instead.
- **CFM**   *CONFIRM* / *I ACKNOWLEDGE*    ▄▄▄ ▄ ▄▄▄ ▄   ▄ ▄ ▄▄▄ ▄   ▄▄▄ ▄▄▄       Message received ([Morse abbr.](Morse%20code%20abbreviations.md)). (Same as **R**.)
- **WX** ...   *WEATHER IS*    ▄ ▄▄▄ ▄▄▄   ▄▄▄ ▄ ▄ ▄▄▄       Weather report follows ([Morse abbr.](Morse%20code%20abbreviations.md)).
- **INTERCO**   *INTERCO*

(*in-tur-ko*)

▄ ▄   ▄▄▄ ▄   ▄▄▄   ▄   ▄ ▄▄▄ ▄  
▄▄▄ ▄ ▄▄▄ ▄   ▄▄▄ ▄▄▄ ▄▄▄       Groups of abbreviations from the *International Code of Signals* follow ([Morse abbr.](Morse%20code%20abbreviations.md)).

### Amateur radio National Traffic System

For the special purpose of exchanging ARRL Radiograms during National Traffic System nets, the following prosigns and signals can be used, most of which are an exact match with ITU-R and Combined Communications Electronics Board (military) standards; a few have no equivalent in any other definition of Morse code procedure signals or abbreviations.

Table of Morse code prosigns and useful [Morse code abbreviations](Morse%20code%20abbreviations.md)
- Prosign   Code symbol   Meaning   Comments   Verbalization   As text
- **AA**    ▄ ▄▄▄ ▄ ▄▄▄    Start new line   Space down one line; typewritten as Carriage Return, Line Feed (CR-LF). Only used instead of **BT** in ARRL batched messages, where **BT** would prematurely start a pending next section. Also written **RT**.   *di dah di dah*   **Ä**, **Á**
- **AR**    ▄ ▄▄▄ ▄ ▄▄▄ ▄    Message separator, start new message / telegram.   New Page, space down several lines. Decoder software may show [ **+** ]. Alternative for "Break" in conversational Morse. Also written **RN**.   *di dah di dah dit*   [ **+** ]
- **AS**    ▄ ▄▄▄ ▄ ▄ ▄    Wait   Respond with: **SN**, or characters "**R**" (Received) or "**C**" (Confirmed).   *di dah di di dit*   [ **&** ]
- **BT**    ▄▄▄ ▄ ▄ ▄ ▄▄▄    Start new section / paragraph   Space down two lines; typewritten CR-LF-LF. Decoder software may show [ **=** ].   *dah di di di dah*   [ **=** ], [ **– –** ]
- **CT**    ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄    Start of  
transmission  
Start of new  
message   Attention commencing transmission. Also written **KA**.   *dah di dah di dah*
- **HH** ...    ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄    Error /  
correction   Always followed by correct text. Equivalent to both **IIII** and **EEEEEEEE** . Sometimes transcribed as "???".   *di di di di di di di dit*
- **K**    ▄▄▄ ▄ ▄▄▄    Invitation for any station to transmit   Lone alphabetic character "**K**" at the end of a transmission.   *dah di dah*   **K**
- **X**    ▄▄▄ ▄ ▄ ▄▄▄    Full stop   Lone alphabetic character "**X**" surrounded by word spaces.  
Substitute for period **AAA** in ARRL batched messages.   *dah di di dah*   **X**
- [ **?** ]    ▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄    Please say  
again   Lone question mark "**?**" from the receiving station in response to a transmission; possibly followed by **AA** ... or **AB** ... .   *di di dah dah di dit*   [ **?** ]
- **KN**    ▄▄▄ ▄ ▄▄▄ ▄▄▄ ▄    Invitation for  
named station  
to transmit   Go ahead, specific named station. Decoder software may show equivalent character [ **(** ].   *dah di dah dah dit*   [ **(** ]
- **NJ**    ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄    Shift to Wabun code   Shift from [Morse code](Morse%20code.md) to Wabun code Kana characters. Also written **XM**.   *dah di di dah dah dah*
- **SK**    ▄ ▄ ▄ ▄▄▄ ▄ ▄▄▄    End of work /  
End of contact  
/ Frequency no longer in use   Also written **VA**.   *di di di dah di dah*
- **SN**    ▄ ▄ ▄ ▄▄▄ ▄    Understood / verify / verified   Message received and checks okay. Alternatively shift from Wabun to Morse code. "**SN?**" verification requested. Also written **VE**.   *di di di dah dit*   **Š**, **Ś**
- **SOS**    ▄ ▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ▄    Start of a distress signal   Only used by the original distressed station, and only for imminent danger to life or property. (listen)   *di di di dah dah dah di di dit*
- **DDD**    ▄▄▄ ▄ ▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄ ▄    Start of a  
distress signal relayed from another station   Used to forward a copy of a received "**SOS**".   *dah di di dah di di dah di dit*
- **BK**    ▄▄▄ ▄ ▄ ▄  ▄▄▄ ▄ ▄▄▄    Break in  
conversation   [Morse abbreviation](Morse%20code%20abbreviations.md) for "back-to you" ([Morse abbr.](Morse%20code%20abbreviations.md)). In conversational Morse some use any of **AR**, **BT**, **KN**, or "**K**" instead.   *dah di di dit* *dah di dah*    **BK**
- **CL**    ▄▄▄ ▄ ▄▄▄ ▄  ▄ ▄▄▄ ▄ ▄    Closing down   Abbreviation for "closing station" ([Morse abbr.](Morse%20code%20abbreviations.md)).   *dah di dah dit* *di dah di dit*    **CL**

### Obsolete prosigns

Historical Morse code prosigns
- Prosign   Matching voice procedure word   Former code symbol   Explanation   Reference
- **CQD**   Distress call    ▄▄▄ ▄ ▄▄▄ ▄   ▄▄▄ ▄▄▄ ▄ ▄▄▄   ▄▄▄ ▄ ▄    Obsolete code used to call all stations during distress (see **CQ**). Replaced by **SOS** in 1906 (see above).
- **VE**   General call    ▄ ▄ ▄ ▄▄▄ ▄    Code re-used for "Message verified" or "Message understood" (see **SN** above). Replaced by **CQ** (see above).   1937 Royal Navy Signal Card
- **NNNNN**   Answering sign    ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄    Dropped.
- **ii**     Separative sign break    ▄ ▄   ▄ ▄    Generally replaced by **BT**, although it is still used in MARS CW operations, and other military standards.  
Later re-used for both a "ditto" mark and to represent the warning "I repeat" before a duplicated transmission.
- **EEEEE**   Error    ▄ ▄ ▄ ▄ ▄    Exactly five dits (code for digit **5**). Replaced by **HH** (exactly eight dits, **EEEEEEEE**).
- **RRRRR**   Receipt sign   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   Replaced by **R**.
- **É** (printed as e)   Further message sign    ▄ ▄ ▄▄▄ ▄ ▄    Re-purposed original ITU symbol for **É** not used in English.

---

*Source: Wikipedia, Prosigns for Morse code (https://en.wikipedia.org/wiki/Prosigns_for_Morse_code), by Wikipedia contributors, CC BY-SA 4.0.*
