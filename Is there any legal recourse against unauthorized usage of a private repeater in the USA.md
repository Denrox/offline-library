# Is there any legal recourse against unauthorized usage of a private repeater in the USA?

*Tags: united-states, legal, repeater · score 13*

## Question

Can the FCC revoke an amateur license for unwelcomed use of another amateur's private/closed repeater system?

It's clear that private repeaters are **allowed**, per 47 CFR 97.205(e):

Limiting the use of a repeater to only certain user stations is permissible.

Someone summarized this here [https://ham.stackexchange.com/a/236/1362](OK%20to%20use%20any%20repeater.md) as saying that an owner "can legally prevent someone from using their repeater", that is, under FCC jurisdiction a ham repeater doesn't have to be available to all hams. A club *may* limit usage to only its members, an individual *may* limit usage to only certain friends/family, a linked system *may* limit access to those who are deemed worthy, etc.

So a repeater operator *may* take measures to limit use of their repeater. Seems they could:

- set up a CTCSS code and try to keep it secret
- leverage some digital protocol with a real authentication scheme
- deploy a sophisticated multi-receiver TDOA triangulation setup able to isolate and thereby retransmit only signals appearing to emanate from certain pre-approved locations
- simply shut down their repeater whenever there's unwanted traffic

All those means of "limiting the use" would be "permissible". But what if they don't work? Or what if the control operator of the repeater doesn't implement any actual physical/technical limitation but simply makes up some rules "limiting" who they want using their repeater?

In what way (and by whom) would such a limit be **enforced**?

I can't find any rule in Part 97 that says anything like "your signals may not be retransmitted by a repeater station unless you have permission from its control operator" or "when a frequency is reserved for the exclusive use of another station, the intentional transmission of CTCSS tones is prohibited on that frequency" or anything.

Say I were to set up a completely open (technically) repeater, but say "I hereby limit the use of this repeater to Eve and Mallory only". If Alice and Bob make a habit of using my repeater anyway (giving priority to emergency traffic, not interfering or profane, simply exchanging messages between licensees…), have *they* broken any specific FCC rule? Does breaking my personal rules "limiting the use of a repeater to only certain user stations" give the FCC grounds to prosecute Alice/Bob for transmitting an otherwise-authorized signal that gets picked up by the repeater I operate?

## Answer (score 13, by natevw - AF7TB)

The short answer seems to be that **yes**, the FCC apparently *does* consider the repeater operator's rules as enforceable. They have in the recent past (e.g. 2013 and 2017) sent out official Warning Letters signed by Enforcement Bureau legal counsel:

The trustees of ____ have requested that you refrain from use of their repeater(s). The request to refrain from use of the repeater was issued as a result of your failure to follow operational rules set forth by the licensee/control operator of the repeater systems for their users. You have failed to comply with the request.

The Commission requires that repeaters be under the supervision of a control operator and not only expects, but requires, that such control operators be responsible for the proper operation of the repeater system. Control operators may take whatever steps they deem appropriate to ensure compliance with the repeater rules, including limiting the repeater use to certain users, converting the repeater to a closed repeater or taking it off the air entirely.

Please be advised that the Commission expects you to abide by the request of the trustee and/or control operator that you stay off of ___ – and any other similar requests to cease operations on any other repeaters by any other repeater licensees, control operators or trustees.

Use of this repeater again after receipt of this letter could subject you to severe penalties, including license revocation, monetary forfeiture (fine) or a modification proceeding to restrict the frequencies upon which you may operate.

What stands out to me is that the letters do *not* cite "failure to follow the rules of the Amateur Radio service" or claim that "control operators may take whatever steps they deem appropriate to ensure compliance with Part 97 regulation"!

Instead, the operators are accused only of being out of compliance with the **repeater** rules; the warning is for "failure to follow operational **rules set forth by […] the repeater systems for their users**" (emphasis added).

The exact basis for this is unclear. What stops someone from setting up shop as a "limited-use repeater" just to boss around others on some random VHF frequency for a while? I would argue that this deputization goes beyond what the rules actually laid out in Part 97 cover!? (But I would only want to argue that here, between you and me on this random website; I would very much *avoid* being in a position where I had to argue this point against the aforementioned FCC legal counsel, in court… :-P)

Regardless, it is clear that the FCC is on record considering a repeater's own rules to have some force of law, at least to the extent that they have threatened severe penalties against operators who would continue to use a repeater after its trustee had asked them to cease.

"Limiting the repeater use to certain users" appears go well beyond technical cat-and-mouse games: if the trustee/operator of a repeater *requests* a person refrain from use of that repeater, the FCC expects compliance with that request.

Letters like these were found via a tip in a commment on [OK to use any repeater?](OK%20to%20use%20any%20repeater.md):

- https://transition.fcc.gov/eb/AmateurActions/files/Chris13_09_23_5360.html
- https://transition.fcc.gov/eb/AmateurActions/files/Barne13_09_23_5359.html

And clicking through found at least two others as recently as 2017:

- https://transition.fcc.gov/eb/AmateurActions/files/DOC-349389A1.html
- https://transition.fcc.gov/eb/AmateurActions/files/DOC-349399A1.html

These all follow roughly the same template as above.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21461/is-there-any-legal-recourse-against-unauthorized-usage-of-a-private-repeater-i, by natevw - AF7TB. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
