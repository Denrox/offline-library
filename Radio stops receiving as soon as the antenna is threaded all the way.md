# Radio stops receiving as soon as the antenna is threaded all the way

*Tags: antenna-system, connectors · score 4*

## Question

Is it normal for the antenna connector of the radio to have 18ohm resistance between the inner socket(signal) and the thread (ground)?

When I connect the antenna, it works fine if only the inner plug makes contact - if the outer metal part of the antenna touches the radio it stops receiving anything.

The radio is a Yaesu FT-747 and the antenna is a Sirtel Santiago 1200

## Answer (score 3, by Terrik)

I did some more testing and it turns out the fault is in the **coax wire**.

It's not a normal cable, it's a vertical magnetic mount and when I use this cable conecting both live and ground it kill all RF signal but it's not shorted.

Thank you for your answers.

## Answer (score 3, by Kevin Reid AG6YO)

Very loosely speaking, you should expect the radio's antenna connector to measure 50 ohms. But that is only true if you are measuring it using an RF signal in the frequency band the radio is expecting, not using the DC output of an ohmmeter, so 18 ohms is entirely reasonable.

The fact that making the shield connection causes you to stop receiving signals is a very good indication that **either the antenna is defective or that it is completely unsuitable for the band you are trying to receive.**

For example, you'd make exactly the same observations if you were to partially plug in a piece of coax with no antenna on the other end. This is because, without the shield connected, the coax might as well be a plain wire, and any old wire stuck in the antenna port will make a receiving antenna of some effectiveness.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/10325/radio-stops-receiving-as-soon-as-the-antenna-is-threaded-all-the-way, by Terrik, Kevin Reid AG6YO. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
