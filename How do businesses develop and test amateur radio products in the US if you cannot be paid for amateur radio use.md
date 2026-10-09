# How do businesses develop and test amateur radio products in the US if you cannot be paid for amateur radio use?

*Tags: legal, transmitter, fcc, testing, transmission · score 6*

## Question

Certainly there are companies in the US (like Kenwood) that develop HAM products that transmit. For development and QA they would likely need to test the product outside of a Faraday cage.

How can companies test those products in the HAM bands if §97.113 says they can't transmit for commercial purpose?

I didn't see it in the part 97 regs, but are there special exceptions or licenses for developing products to transmit in the Part 97 bands that can be assigned to a corporation?

## Accepted answer (score 8, by user10489)

Two parts to this answer:

First, most testing would be done against dummy loads, looking at the results on spectrum analyzers. Such tests should not propagate.

Secondly, there's a fine line here. As worded, Part 97 prohibits:

(2) Communications for hire or for material compensation, direct or indirect, paid or promised, except as otherwise provided in these rules;

(3) Communications in which the station licensee or control operator has a pecuniary interest [with a number of excpetions that don't apply here]

This doesn't say you can't transmit while being paid. The classic example here would be if I'm working, but I use my amateur radio to call a coworker and ask them if they want to go to lunch. My employer derives no benefit from this transmission.

Similarly, the paragraphs above don't actually say transmission, they say communication. So, if while testing a radio under field conditions, you might have a conversation with someone over the radio, and this conversation might have nothing to do with testing the radio and derive no benefit to my employer, and thus be perfectly legal, while at the same time you get test results during the transmission.

Another example is emergency communications. Someone asked FCC if emergency responders were allowed to use amateur radio. FCC replied with a memo stating that the responder was being paid to help with the emergency, and using the radio to communicate was not commercial content for that purpose. They later revised the commercial exception list (to what is there now) to explicitly include that case, and expanded on limitations for this exception in the regulation.

The original intent of the non-commercial clauses in amateur radio was to prohibit the amateur spectrum from becoming commercialized, which could leave little room for non-commercial use, and at the same time, allow commercial users to bypass rules that require them to pay for their spectrum use. So communications of a commercial nature are are generally prohibited.

The intent wasn't to make it difficult to build and test amateur radio equipment that would later be sold. There are even provisions in the exceptions to allow amateur operators to talk about selling their own equipment over the radio.

I can see a radio manufacturer giving a prototype radio to a ham for testing, and they could use it, say, over a weekend the same way they would normally have used any radio. The employer doesn't control the content of those transmissions and derives no benefit from that content. The tester could then write a report describing issues while using the prototype radio. Technically, they would be paid for the report. This is certainly a fine line, and ripe for abuse, but infrequent and appropriate use shouldn't be an issue, neither violating the letter nor intent of the regulation.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20351/how-do-businesses-develop-and-test-amateur-radio-products-in-the-us-if-you-can, by KJ7LNW, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
