# How to stop interference on shortwave radio when connecting to a computer

*Tags: hf, receiver, rfi, tecsun · score 6*

## Question

I have a Tecsun PL-600 and when I can receive clear signals, and they come through just fine on headphones, and through the speaker. If I'm trying to receive RTTY or fax, when I connect the radio to my computer the signal becomes inaudible because a huge amount of interference comes through. It only happens when connecting the radio to the computer, so I assume it's something to do with interference going into the radio through the audio cable. But I have no clue if that's even possible.

Is there any way to stop the interference that happens and what is causing it?

Here's a signal recorded with my phones microphone, using the radio's speaker. The signal is coming through very loud and clear. Here's when I have the radio plugged into the computer and I used the computer to record the audio directly through the input. Be warned that both the audio clips are quite loud, especially the one with the noise.

## Accepted answer (score 3, by Kevin Reid AG6YO)

I listened to your samples and I can say that I've never heard interference that sounded like wind on a microphone before. It doesn't sound like typical RFI, but it still could be. It doesn't sound like clipping either.

Regardless, some things worth trying (including those already mentioned in other answers, to be complete) are:


**Change the antenna**; in particular, use an external antenna which is either **balanced** (dipole) and has a balun, or is **grounded** (actual earth ground at the spot, not electrical service ground) at the feed point. This helps prevent conducted noise from your equipment from being received.

(If you set up a outdoor antenna, grounded or otherwise, then I recommend either disconnecting it whenever there may be a thunderstorm, or doing further research on effective ground systems. This is a nontrivial problem.)


**Improving *or removing* equipment grounding**, where by the latter I mean **running on batteries instead of AC adapter**. Removing grounding may be useful if you have a *ground loop* problem rather than an RFI problem per se. First, if you live in an older building, make sure that the electrical outlets are actually grounded. Then, try these four configurations — just to be complete:

 1. Computer and radio grounded. (Ideally, this would be best, but depending on the equipment it could result in ground loop noise.)

Use a multimeter to confirm that the radio's power adapter has continuity between the AC earth pin and the (-) terminal of the DC plug (identified by the symbol on the radio's input and possibly on the adapter itself). If it's not grounded, you could try replacing it with one that is, but there might be something “interesting” about the radio circuit and I'd instead think about grounding at the antenna jack instead.

 1.

Computer and radio ungrounded, running off battery power. (This requires a laptop computer or similar, of course.) If you get less noise here, then it could be a ground loop or it could be noise from the AC power adapter of one or both devices.

 2.

Computer grounded, radio ungrounded.

 3.

Computer ungrounded, radio grounded. This is likely to be the worst case, but if it *doesn't* add more noise, then your problem is something else.


**Use a different audio interface.** Get a decent quality USB audio interface/sound card (different words for the same thing) and use its input instead. (Make sure it has a line-level input, not a microphone input.)


**Use an isolation device** — which could be an optical isolator, as already mentioned, or a 1:1 transformer (“audio isolation transformer”) — in the audio line. I note that some of the designs in that PDF do not isolate ground, which may or may not be a good idea.

## Answer (score 2, by Everett)

Have you considered placing an analog optical isolator in line?

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/5245/how-to-stop-interference-on-shortwave-radio-when-connecting-to-a-computer, by smithy212000, Kevin Reid AG6YO, Everett. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
