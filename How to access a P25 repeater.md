# How to access a P25 repeater?

*Tags: repeater, p25 · score 5*

## Question

Are there any special instructions for accessing a P25 repeater? What makes it different from a CTCSS/PL-tone-encoded repeater? What special features does a radio need to access it?

## Accepted answer (score 4, by WPrecht)

P25 is a suite of standards for digital radio communications. P25 is intended to facilitate interoperability between different public safety agencies during emergencies and/or joint operations. Note that this is a North American standard (and a few other places), Europe has a similar but imcompatible standard called TETRA.

A radio needs to be specially designed for P25 use. The public safety agencies use reallocated TV frequencies in the 700MHz range. Most of the usual suspects make HTs for P25 and a couple make dual band radios for amateur use. Due to the audio quality and extra features, some amateur clubs are setting up P25 repeaters usually on the 70cm band, but some on the 2m band.

P25 repeaters use whats called a NAC (Network Access Code) in place of the PL tone/CTCSS access common to amateur repeaters. This a 12-bit prefix that is attached to every packet (including the digitized voice packets). 12 bits means 4096 possible access codes, quite a lot more room than the previous analog methods. There are a few special codes, a default and an "open" code that will pass all traffic.

To program a radio, you need to use a computer, it's too complex to allow keypad programming.

The commerical / public safety versions also support encryption using DES, triple-DES, and AES though it's not consider all that secure do to implementation flaws. However, it's good enough to meet privacy concerns for first responders.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/973/how-to-access-a-p25-repeater, by Dan, WPrecht. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
