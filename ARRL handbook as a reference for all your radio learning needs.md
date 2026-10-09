# ARRL handbook as a reference for all your radio learning needs?

*Tags: antenna-theory, software-defined-radio, electronics, equipment-design, arrl · score 5*

## Question

Looking to take up learning understanding everything from basic electronics to how today's wideband radios work, so that I can build my own radio systems (not just ham radios), and talk radio concepts better. Would ARRL Handbook be a good enough guide to learn from? Or are there any missing pieces to that book which can be done with other sources?

## Accepted answer (score 2, by K7PEH)

You might consider the following two books useful in learning more about radio design and the details of various circuits used in transceivers. These two are not equal in their coverage -- the first considers the electronics of radio technology and the second is more focused on the science and mathematics governing the application of various radio circuits.

First suggestion: The Electronics of Radio, by David B. Rutledge, published by Cambridge.

This book is used by the author as a text book for a radio/electronics course given to undergraduate (mostly) students at Caltech. I also know that it has been taught at other universities too. This book uses a novel approach to teach about radio electronics. It uses a kit, popular at the time of its original publication, The Norcal 40A, a 40-meter CW Transceiver, in presenting the material. Students would put the transceiver together but along the way lab courses (outlined in the book) would be used to perform measurements or tests on various circuit elements in isolation.

Although the Norcal 40A is no longer available (at least the last time I looked it was not available), you can still get a lot out of this book even without building the radio. You can still do many of the suggested "labs" and you can still do most of the problem sets.

After preliminary chapters on electronics and electronic components used in the 40A, the chapters cover: Transmission Lines, Filters, Transformers, Acoustics, Transistor Switches, Transistor Amplifiers, Power Amplifiers, Oscillators, Mixers, Audio Circuits, Noise & Intermodulation, and Antennas & Propagation.

Second Suggestion: The Science of Radio by Paul J. Nahin, published by AIP Press.

I own every book Paul Nahin has written and I have read them all. This one on the Science of Radio is one of my favorites. This book can be used as a text book as well, it has problem sets for each chapter. It also makes use of MATLAB and Electronics Workbench for various lab type exercises. If you do not own a copy of MATLAB, you could probably get by with the trial demo copy. But, then again you don't actually need MATLAB, I did all computation and graphics using Mathematica instead.

This book is a bit more focused on the mathematics of Radio as it gets into the use of Calculus and a few Differential Equations and Fourier Analysis in describing the workings of various radio circuits. This book asks the reader to spend more time working through the mathematical theory as a means of understanding the content. Thus, is is less of an armchair read than the Rutledge book but honestly both require study and a sharp pencil (or, whatever you choose to use).

The chapter headings are not that useful in understanding the content so I have not included them here. Instead, I submit you consider Amazon or other resources on-line that include a detailed table of contents.

A good study of both of these books with dedication to doing the problem sets and lab exercises provides a very good education on radio technology, the electronics used by radios (both transmitters and receivers), and the science & math (or, Engineering) background to know the theory.

## Answer (score 4, by Zeiss Ikon)

The *ARRL Handbook* is a useful reference, but it's just that: a **reference**. It's not written as a text. It's useful for looking up forgotten details of stuff you almost mostly know, but it's not in a good form for learning things like electronics, antenna theory, an the like.

A text aimed at self-study would be much more useful -- one written to be learned from. An updated version of *Elements of Radio* (Marcus and Marcus, last edition 1959) would be just about exactly right; it's a learning text that is intended that the learner build along, working from a basic crystal set receiver up to sophisticated receiving and transmitting circuits. It's even useful for the self-learner, with review questions and circuits that include component values (if not tubes that are still easy to get).

Unfortunately, in 1959, transistors were new and cost as much as tubes, if not more (but were much more delicate); its emphasis was almost entirely on vacuum tubes and there's little if any solid state circuity (I haven't gotten completely through it, because I stopped well along the receiver section, planning to start building the circuits to better understand what was happening). Sure, it's possible to do anything with solid state that a vacuum tube circuit will do (except possibly handling very high power, from hundreds of watts into the kilowatts range), but the conversion isn't at all obvious since tubes generally run on voltage, and transistors mostly on current.

The learning path you describe is hard to follow even in college level courses today -- at a minimum, you'd be looking at a full four-year course in electronic engineering. You'll probably get more satisfaction choosing some intermediate goals and working toward them before committing yourself to go as far as radio can go.

## Answer (score 4, by Mike Waters)

While it is useful to have, **NO** single book contains everything that you want or need to know.

Note that the *ARRL Handbook* is published every year, and each year contains different information. But even if you owned every Handbook that was ever published, inevitably something you want to know will still be missing.

The last Handbook that I bought was because arrl.org advertised it as having a new and featured section about something that I really wanted to learn about. However, after I received it in the mail, there were only a couple of pages about it. I had to use Google to find the information that I wanted.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15314/arrl-handbook-as-a-reference-for-all-your-radio-learning-needs, by eecs, K7PEH, Zeiss Ikon, Mike Waters. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
