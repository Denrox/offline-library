# Help implementing FT8 crc check in Rust

*Tags: ft8 · score 3*

## Question

I'm playing around with implementing portions of the FT8 protocol in Rust. I'm having trouble with the CRC algorithm.

Here is my not yet working attempt: https://gist.github.com/JohnRudolfLewis/696c538c97a5b49d95b32c85a853b2d4

Using https://github.com/vk3jpk/ft8-notes/blob/master/Transmit.ipynb as a reference, I have implemented a single test, and it is not currently passing. Clearly, the crc crate is not calculating the crc in the same way as vk3jpk's code.

If anyone with knowledge of the crc crate in Rust and also how FT8 calculates crc, and can point out the error in my implementation... it would be much appreciated.

73 de N0YPR

## Accepted answer (score 4, by JohnRudolfLewis)

I had also reached out the the author (VK3JPK) of the paper that I was referencing in order to write this code. He pointed out what turned out to be my error.

You specify your message using a 128-bit integer which I suspect will be converted by Rust into 16 bytes NOT 12. You may need to drop 4 of these bytes before passing them onto CRC library function so that it will infer the appropriate message length.

I've updated the gist with a working example.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/22571/help-implementing-ft8-crc-check-in-rust, by JohnRudolfLewis. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
