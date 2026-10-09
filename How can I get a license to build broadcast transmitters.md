# How can I get a license to build broadcast transmitters?

*Tags: united-states, legal, license, fcc, testing · score 5*

## Question

I am in the United States.

The title pretty much says it all. I am really into to building transmitters. It's even more fun for me than using them. I really have a lot of skills and would like to sell my own broadcast transmitters. Yes, I have a spectrum analyzer and can check to make sure they comply with specifications.

I understand that there is compliance testing that would have to be done (IE the transmitter would need to be sent to a lab for specification testing, etc.). This part I am pretty sure on, however I have no idea whether I need a license to build such transmitters or can I just contact some testing house and if it passes, I have a licensed transmitter. Is it that simple or do I need other licenses?

Also, the name of any testing facilities would be appreciated, but that is outside the scope of the question.

## Answer (score 4, by Scott Earle)

As implied in other comments and answers, this sounds like it would be legal to do (we’re all assuming you’re in the USA, given the fcc tag), since all you are doing is building equipment.

However, if you want to sell the equipment once you have built it, that is going to be more difficult.

I would ask you the question - why *broadcast* equipment specifically? You say in a comment that you really want to build high-quality exciters, and not multi-kilowatt behemoths.

My suggestion to you would be to get an amateur radio licence (not difficult, especially if you’re already ‘into’ electronics and have an interest in radio) and build high-quality *amateur* radio transmitters/amplifiers/etc. - that way, you could test them out yourself, use them in your own shack, and even sell them to other amateurs. There is no type-approval (as such) for amateur radio equipment, although the usual checks for spurious and out-of-band emissions that you mention would have to be done.

It could be the start of a business - there are a few small companies that specialise in amateur radio transmitters and amplifiers already, but more are always welcome. Especially those that are made in the USA.

Plus it would have the advantage that you would be able to get experience in building equipment across a huge range of frequencies, not just the usual broadcast frequencies currently in use.

## Answer (score 4, by rclocher3)

No license is required to build broadcast transmitters in the United States. To get approval to sell your transmitters in the US, you would most likely need FCC authorization. The process to get that authorization is covered by 47 CFR part 2, and is summarized on this FCC web page. I'll summarize further:

1. Determine FCC Rules that Apply. Determine if device is a Radio Frequency (RF) device subject to the FCC rules.
2. Equipment Authorization Procedures. If a device is subject to FCC rules, determine the specific type of equipment authorization that applies to the device. Devices subject to the rules require either the Supplier’s Declaration of Conformity (SDoC) procedure, or the Certification procedure.
3. Compliance Testing. SDoC-procedure devices don't need to be tested by an FCC-recognized accredited testing laboratory, but thorough records must be kept. For Certification-procedure devices, an FCC-recognized and accredited testing laboratory must be used. There is a search form for accredited testing laboratories here.
4. Approval. Finalize the approval process based on the applicable approval procedure. For the SDoC procedure, the manufacturer warrants that the devices comply with the rules, keeps all the applicable records, and prepares a compliance information statement to be supplied with the product at the time of marketing. For the Certification procedure, the responsible party must apply for an FCC Registration Number (FRN). Then the responsible party must apply for a Grantee Code by applying at the Grantee Registration website. Then the responsible party files an application for a grant of certification with a Telecommunication Certification Body (TCB), which is a third party designated by the FCC. Assuming all goes well, the TCB then issues a grant of certification on the FCC Equipment Authorization Electronic System (EAS) database.
5. Label/Manual/Record Retention. Label the product and provide the required customer information, and keep all the records mandated by law.
6. Manufacture/Import/Market. Finally you get to sell stuff!
7. Modifications to Approved Products. Changes to your product design may require additional approval, which is covered by a separate process.

So there you have it. Designing a product you'd like to sell is just the beginning.

## Answer (score 2, by Zeiss Ikon)

Building doesn't require a license (though if you're planning to do it commercially, as seems to be the case, you may need to meet government safety standards, especially for the high voltages required on the finals). Actually transmitting *would* require a license of some sort -- not an amateur license, because you're almost certainly talking about building hardware that won't work in the amateur bands and will exceed the legal power limits (1.5 kW for most bands) for amateurs.

A dummy load and sufficient shielding might ensure you don't radiate enough power to need a license, but that's a hard thing to test without actually applying the power. Otherwise, you're asking someone (albeit a skilled and trained someone) to test a previously untested high power, high voltage device for you. This will not be cheap. It may not even be possible. Companies that build transmitters for broadcasters typically have their own testing facilities and engineers; for that reason, you may not find anyone with the qualifications and equipment to can/will do the testing you want.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/13326/how-can-i-get-a-license-to-build-broadcast-transmitters, by Synaps3, Scott Earle, rclocher3, Zeiss Ikon. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
