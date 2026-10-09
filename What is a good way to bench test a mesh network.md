# What is a good way to bench test a mesh network?

*Tags: mesh-network, microwave · score 8*

## Question

I've been experimenting with some 2.4ghz based mesh networks similar to http://hsmm-mesh.org/. I'd like to have something on the bench where I could simulate roving between nodes, and create hidden nodes and varying signal strengths.

Is there a better solution than a network of coax cables with splitters and attenuators (variable and fixed)? Any pitfalls in this approach (I'm turning the power way down and using a lot of attenuation)? Any suggestions on how to build a setup like this without breaking the bank (the attenuators and splitters get expensive!)?

## Answer (score 8, by Phil Frost - W8II)

You can simulate. The idea is to model your RF channel(s) numerically by adding things like AWGN, multipath, clock skew, and so on. And, you want a way to model a lot of these channels, and twiddle the parameters and see how the system responds.

There are many software libraries out there that will make this easier. I'd suggest GNU Radio. It has blocks that can be chained together to model an RF channel, and blocks to implement most basic digital modulation schemes. It has a graphical interface where you can connect them together, which is good for experimentation, and it also has bindings to several programming languages so you can automate the creation of a complex network of channels and implement your own blocks. It also has blocks to interface to real hardware, like the USRP, or an audio card that can in turn interface to inexpensive SDR platforms like Softrock.

*image source*

If you also want to simulate the OS running the hardware on your nodes, you'll need a somewhat more powerful computer, and a way to programatically create virtual machines. Again, many options, but for an easy start, I'd look at Vagrant. With this, you could conceivably create a handful of virtual nodes, each running virtual RF interfaces implemented by GNU Radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/680/what-is-a-good-way-to-bench-test-a-mesh-network, by K9KRB, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
