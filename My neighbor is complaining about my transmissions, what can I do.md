# My neighbor is complaining about my transmissions, what can I do?

*Tags: rfi, procedure · score 10*

## Question

My neighbor has indicated that they can hear noise from their computer amplified speakers when I'm transmitting. We've done a few tests and it does appear that it's my transmitter that's causing the noise.

I've performed some testing and determined that I'm well within my operating limits. The transmissions are clean, within power limits, etc. There is nothing I can do on my end to resolve the problem, other than cease transmission.

My neighbor is unwilling to replace his speakers with a more noise resistant set, though he may be willing to allow minor modifications if it doesn't otherwise affect performance.

What should I try that should help remove, or at least reduce, the noise on the speakers?

## Accepted answer (score 10, by VU2NHW)

Wikipedia writes to say

By the regulation, the FCC DoC certification mark is mandatory for devices classified under part 15 (IT equipment like computers, switched-mode power supplies, monitors etc., television receivers, cable system devices, low-power transmitters, un-licensed personal communication devices) and part 18 (industrial, scientific, and medical (ISM) devices that emit RF radiation) of the FCC regulations.

The subject is covered in some depth on hamuniverse.com which writes to say (free-form edit applied by me)

Rectification and overload are both **problems with the design of the affected equipment**, and after decades of investigation, the FCC knows this.

In your case, the issue & onus lies upon the manufacturer of the equipment **experiencing interference**.

Having made that clear to the neighbour, you might try introducing a low-pass filter (also mentioned in the article on hamuniverse referenced above)

Another alternative (+: dump a load of ferrite beads over their speaker cables. More detailed reading is listed at this site

## Answer (score 3, by Glenn W9IQ)

I disagree with part of the answer given by VU2NHW:

In your case, the issue & onus lies upon the manufacturer of the equipment experiencing interference.

This is not what the FCC regulations say (assuming we are talking about US jurisdiction). Part 15 clearly puts the issue in the hands of the consumer. The only recourse the consumer has with the manufacturer is through tort law, not federal regulations. However, the consumer can use part 15 to help qualify them as an aggrieved party to allow tort proceedings if the consumer chooses to pursue this course.

There is also case law that reasonably blocks a neighbor ftom attempting tort actions against the ham. This may not stop a filing necessarily, but it should normally bring the matter to a swift and favorable conclusion for the ham.

In these situations of neighbor complaints, the ham is advised to make sure their signal is clean (spectrum analyzer screen shots) and that they have conducted and logged any necessary RF exposure assessments. Keeping a basic log showing the time going on and off the air, the band, mode, and output power is also helpful. If the FCC then makes an inquiry, the ham can show sound due diligence and will be exonerated by the FCC. The FCC will then send a brochure and letter to the consumer advising them that the ham is operating legally and the problem is with the consumer's electronics.

We all want to be good neighbors and help them with their interference problems. But before getting out your toroids and tools, carefully consider the litigious conditions that surround us and weigh this in your decision as to what course of action you will take.

Edit:

Computer speakers are notorious for being affected by nearby EM energy. The most effective remediation is the application of toroid cores on the speaker and power leads to the speaker boxes. Depending on the length of the wires, a toroid on each end of the wire may be warranted. Toroid cores of type 31 material are generally the most effective. Get large enough cores to allow connectors to pass through the hole in the center. Make multiple turns of cable on each core as the EM choking goes up as the number of turns squared.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1034/my-neighbor-is-complaining-about-my-transmissions-what-can-i-do, by Adam Davis, VU2NHW, Glenn W9IQ. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
