# What is the difference between RIT and XIT?

*Tags: transceiver, jargon, vfo, split-frequency · score 6*

## Question

What is the difference between RIT and XIT? When would one use one and not the other for split (or other) HF operation? When would one need both? Which one is more useful for a transceiver to have if it only had one?

## Answer (score 4, by Scott Earle)

Modern radios that have RIT and XIT typically also have a button that you can use to listen on your transmit frequency. This means that if you use XIT or RIT, then you can listen on your transmit frequency (rather than on your receive frequency) to check conditions on there.

The typical use case for RIT is if you are calling CQ and you start to get a pileup, so you shift to listening “up” or “down”. If you say “UP 5” then you would shift the RIT up 5kHz and listen to people calling there. You would occasionally listen on your transmit frequency to make sure conditions there are still OK and you don’t have too many people ignoring the UP instructions (if you do, you can send “UP” several times in the hope that they get the hint).

For most of us though, we are on the opposite side of this pileup. And this is where XIT is useful: We set our VFO to the DX’s transmit frequency, and tune XIT up 5kHz. Then while the DX station is running through a bunch of people calling we use the “listen on my transmit frequency” button to determine exactly where the station currently being worked is. Then we listen to the DX and as soon as the current contact is completed we know where the last contact was transmitting, and we can call right away on exactly the same frequency. This can greatly improve our chances of being heard by the DX. Or we can listen to several contacts in succession, and find a pattern in where the DX is listening - for example, slowly working stations on higher and higher offsets, then returning to UP 5, and repeating. Working out patterns in a pileup can almost guarantee that even with a smaller station, we can break through the pileup.

The final part of the question asks which is more useful if you could have only XIT or RIT. I say that depends on which side of the pileup you usually sit. If you’re the DX listening up, you want RIT. If you spend a lot of time trying to break pileups, you want XIT and a “listen on my transmit” button.

## Answer (score 4, by hobbs - KC2G)

RIT means that your VFO frequency will be offset from your dial frequency (usually by a relatively small amount) while you are receiving. XIT means that your VFO frequency will be offset from your dial frequency while you are transmitting.

So a dial frequency of 7125 kHz and a RIT of +1000Hz will accomplish exactly the same thing as a dial frequency of 7126 kHz and an XIT of -1000Hz (that is, receive on 7126 and transmit on 7125), but the controls you use to get there are different.

As [this linked answer](How%20is%20clarifier%20control%20helpful.md) mentions, RIT can be used to clear up an SSB QSO partner's offset during the QSO without inducing them to "chase you up the band". It's also useful for "listening up" when operating split CW — you leave your dial at your transmit frequency, and spin the RIT up a kHz or two to listen for responses. I don't know of any good use of XIT, and I have never used it myself. It seems less convenient in every way, to me.

## Answer (score 3)

While most modern radios are vary accurate in regards to frequency, not all radios are. Our signals get garbled with the transmitting frequency of one radio is not the same as the receiving frequency of the other.

By slightly adjusting the receiver frequency with RIT, you can sometimes get better reception of a station that is transmitting slightly off frequency. Your transmitting frequency for not change when adjusting RIT.

While less common you can also slightly adjust your transmit frequency with XIT so the receiving station can hear you better. Adjusting XIT does not change your receiving frequency.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17081/what-is-the-difference-between-rit-and-xit, by hotpaw2, Scott Earle, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
