# Why do satellites receive and transmit on different bands?

*Tags: uhf, satellites, vhf · score 11*

## Question

Most satellites I've found transmit on VHF and receive on UHF or vice versa. Why is this? I would think there's enough space on a single band.

## Answer (score 13, by Pete NU9W)

They don't always do that, but the reason for it is simply separating the transmitted RF from the received RF. A ground-based repeater uses a fairly large duplexer to make sure that its transmissions don't feed back into its receiver; with a satellite, size and weight are at a premium, and having two widely separated frequencies requires much less hardware than two closely-spaced frequencies with a duplexer.

## Answer (score 2, by Italic_)

Thinking back, the systems in a hamsat are very similar to a repeater system we had when I staffed a boy scout camp. Like Pete said, it saves you space because duplexers are huge and expensive. We had four business frequencies at our disposal, so we set up one VHF and one UHF in the repeater. It was a two-way system, so you could transmit on the VHF frequency and the repeater will broadcast at UHF, or you could transmit at UHF and the repeater will output VHF.

It was very simply one or two power supplies connected to standard base radios, which fed into each other with an audio cable and an auto-transmit circuit, something like VOX. We stored these radios in a small back room on a shelf. You walk into the repeater room expecting to see a big setup of wires and boxes everywhere, but it was actually just a small PSU box, two small stacked radio boxes, and a couple cables linking the two and the antennas. The whole thing couldn't have taken up more than one or two cubic feet.

It's very space-efficient and cost-efficient. You don't need any sort of computer, nor do you need a duplexer, nor are your radios terribly expensive.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/946/why-do-satellites-receive-and-transmit-on-different-bands, by Skyler 440, Pete NU9W, Italic_. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
