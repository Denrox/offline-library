# How do Handheld antennas work without ground?

*Tags: antenna, antenna-theory, ht · score 26*

## Question

Dipoles have the 2 wires going to each leg of the antenna completing the circuit.

Big AM towers use the second wire as a ground plane

But how do handheld rigs transmit and receive with just one wire sticking in the air?

## Answer (score 19, by James NF8I)

Your body acts as the ground when using a handheld radio. By holding the radio, you are capacitively coupled to the radio and make the other leg of the antenna. This is one of the reasons to hold the radio in your hand away from your body while using it, rather than using it while attached to a belt clip. (The other reasons pertain to RF safety.)

Of course, you aren't a very good ground system, so you can improve the efficiency of a handheld's antenna by attaching a counterpoise to the radio to be a better ground. There is a product called a "rat tail" designed for this purpose, but you can easily homebrew your own by attaching any handy piece of wire about a quarter wavelength long to the radio's case.

As noted in a comment: further details about adding your own ground/counterpoise to an HT.

## Answer (score 2, by user10489)

If you are using a monopole antenna, when you hold the radio, your body acts as the image of the antenna to make a full dipole. This works for both transmit and receive.

If you are receiving a strong signal, it doesn't make a lot of difference, but if you have a marginal signal, you will notice that it gets a lot worse if you set the radio down or put it on your backpack. However, if you set it down on a piece of metal, like a metal table, it'll be about as good as when you are holding it, because the radio can capacitively couple to the metal. (It doesn't have to make conductive contact to do this.)

However, if you put an antenna on the radio that is a full dipole, like an end fed half wave whip, a loop, or coax going to a J-pole, you'll find that this matters a lot less.

Similarly, you can add a counterpoise to the monopole and it should help.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/495/how-do-handheld-antennas-work-without-ground, by Skyler 440, James NF8I, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
