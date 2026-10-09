# How to avoid Bluetooth intereference?

*Tags: hf, rfi · score 4*

## Question

I'm thinking about dropping a bluetooth module into my Softrock receiver so I can use it with my computers and portable devices wirelessly.

The receiver runs from 1.8MHz to 30MHz, and the bluetooth transceiver operates in the 2.4GHz band.

Will I need to add shielding or take any special measures to prevent the bluetooth device from causing noise problems with the receiver?

## Accepted answer (score 1, by cj5)

I don't think you need to worry too much about the bluetooth causing direct electromagnetic interference to a receiver operating in the HF bands. There are probably a lot more things to be concerned with, like harmonic interference from the bluetooth device, or electronic adapters, consumer products, and such, but I have never heard or experienced either (http://www.popularmechanics.com/technology/how-to/tips/how-to-fight-rf-interference-with-your-gadgets).

If you have the technical chops, this guy (http://kd0ar.blogspot.com/2010/04/cell-phone-interference-on-softrock.html), uses a softrock and was receiving interference from his cellphone. If you manage to do what he did, maybe you could get the same results. RF chokes really do work. They're everywhere in my house, and have signigicantly reduced household and common device RFI.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1190/how-to-avoid-bluetooth-intereference, by Adam Davis, cj5. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
