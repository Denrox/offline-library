# Learning morse, but I can't write fast enough?

*Tags: morse-code · score 8*

## Question

EDIT below with collected thoughts so far...

I've been learning morse lately, and thought I was doing tolerably well until I learned that doing this at 5 wpm/15 Farnsworth, is evidently considered essentially pointless. So, now I'm trying at 20 wpm, except that I can't write anywhere near fast enough (I seem to peak out around 5 wpm!) I've tried saying what I recognize aloud and audio recording that to verify afterwards, but interferes with my hearing the next character. I've also tried typing, but if I miss anything at all I'm out of sequence. Does anyone know if there's a trainer (software) that lets you type what you think you heard and in doing so keeps track of when you typed and therefore doesn't lose sync with what character you're trying to respond to? Perhaps there's something else going on but I can handle the 20 wpm for K+M "in my head" for about 5 characters--after that, I can't remember what I've heard, so I can't validate it. Any attempt to get the characters "out of my head" so far has screwed me up completely. Am I missing something? Any suggestions? I'm tempted to write a trainer from scratch that allows me to type as it goes, but I'd rather spend the time learning morse than writing something, particularly if that something already exists, or would perhaps be ineffective anyway.

At this point, and in very large measure based on comments and proposed answers, I'm making progress. I'll outline the things that have worked and what hasn't, and what I think might help more if I could find a way to try it:

1.

I have managed to get to a point where typing is better than writing. Fortunately I "mostly touch-type" so I'm pretty fast at this compared with hunt-and-peck two finger typing. Your situation, naturally, might differ.

2.

I'm really having to practice keeping up, even when I want to spend time because "that letter is on the tip of my tongue". Trying to get the last letter transcribed in that situation simply results in missing the next five or so. I have to practice letting it go if it's not "right there".

3.

It's necessary to practice the transcription, not just the recognizing of the characters. Sadly, annoyingly even, this is part of the game and trying to bypass it was kidding myself.

4.

A significant part of my "I can't write fast enough" was in fact simply that I wasn't (and of course still am not) recognizing the morse instantly.

5.

As I've built a bit more actual "instant recognition" it actually feels different from the feeling of identifying the dits and dahs. The same thing has also allowed me to survive a small backlog in what I'm copying. Not much, but certainly one character, perhaps two, and the next word-pause let's me (sometimes :) catch up with the copying.

6.

If I have time to mentally replay the sound, I'm not learning to recognize the morse, but to look it up. That's what people mean about learning slow being a waste of time. It has to be recognition, and that does mean that I'm going to miss a ton at first. Fortunately, it seems that once the brain has discovered that these sounds can be recognized and has started to do so, it becomes easier.

7.

I am copying this into a plain-text editor, but I currently have to do the validation "by hand". The Unix diff tool only works line at a time, so is useless for this. Similarly the cmp tool doesn't "resynch", and if you miss a character, or add an extra, it will report everything from there on as wrong.

8.

In order to force recognition of the whole sound, and prevent a separation of the dits and dahs, I'm finding that listening to 20 "dit-rate" ("20 Farnsworth", in other words) and spewing them at 8 wpm seems to work. You might need more if your brain is able to pull out the individual sounds in the spacing that leaves. I'm noticing that for many of the letters that I've now learned to recognize at this speed, I have them instantly and the gap is almost boring, for the ones I'm learning, the gap is necessary.

9.

I still suspect that the principles of "perceptual learning" (which is how, for example, people learn to determine the sex of baby chicks) would be well placed here, but I'm not really interested in writing the software to do this when what's happening now does seem to be producing results.

10.

I'm staying away from anything with actual words in since it's important to me to be able to copy callsigns and other cryptic stuff. No doubt it'll be way easier to handle natural English text, but I don't want that to trick me into thinking I'm better than I am.

11.

The trainers I'm using right now are: http://aa9pw.com/ and G4FON trainer

The first of these creates random groups of five characters though it has some other modes. It doesn't show you the text until you ask it to. It's web-based too, which has advantages.

The second is a windows program, but works out of the box under Linux/wine (there's a slight tendency to jiggle the tone timing, but that's actually perhaps helpful, since it, along with a bunch of other configurable features like noise, channel interference and more, somewhat simulates hand-sent code with imperfections).

## Answer (score 5, by rclocher3)

Not being able to write the letters down fast enough for the Morse code that you're hearing is a problem that's as old as Morse code. I have a few suggestions:

- Write faster. Try cursive, skip dotting the i's and crossing the t's, or come up with your own shorthand substitutes for the more troublesome characters.
- Use a "mill" (that's the old telegrapher slang for a typewriter). These days people use computers more often than typewriters, of course. I don't know what is generating the Morse code that you're hearing, but if it's software generating the code, couldn't you type into a text editor window as you listen?
- Learn to "throw away the pencil", i.e. translate the Morse characters into letters, and the letters into words, and the words into meaning in your head without writing it down. This only works for meaningful text, such as a QSO or the ARRL practice recordings. It's an intermediate technique that probably won't help most beginners, unfortunately. I learned it when I was up to about 12 wpm, and I found it easier to learn the faster the code got.
- The old-time professional telegraphers recommended learning to "copy behind", to have a buffer of the dits and dahs in your head. I haven't been able to do this for longer than a second or two. Some of the old-timers could allegedly do this for as long as a minute at a time.

Some general tips:


Missing the next five characters while you're trying to recognize one tricky character is a universal problem. If you can, try and skip tough characters when the code is a bit too fast for you. Write "-" or something. In a real QSO, you miss characters all the time because of static bursts and fading, so being able to carry on with imperfect copy is a great skill to have. In a real QSO you can fill in the missing character from context, or request a "fill" (a repeat of the missing information).


Trying to copy Morse code that's a bit too fast is the fastest way to improve your copying speed. However, one should also practice copying at comfortable speeds to solidify recently-learned skills.


In my opinion, one should practice copying call signs, numbers, and text with real words. I don't see much value in practicing random five-character groups once one has solidly learned all the characters. Practicing with real text teaches one to recognize words directly, which is much faster and easier than trying to piece together every word from individual characters. For instance, anyone who has ever spent much time tuning across the CW portions of the bands can recognize "CQ" at any speed, whether or not they know Morse code. Learning to copy whole words will also automatically help you lengthen your mental buffer of undecyphered characters, which is a good thing.


My favorite software for practicing call signs and numbers is MorseRunner, which simulates a Morse code contest. It's fun! Other trainers for practicing call signs also exist.

Learning to copy Morse code can be a difficult skill to learn at first, but like any skill, regular practice will help.

## Answer (score 4, by henryflower)

"Does anyone know if there's a trainer (software) that lets you type what you think you heard and in doing so keeps track of when you typed and therefore doesn't lose sync with what character you're trying to respond to?"

I believe K9OX's Fully Automatic Morse Code Teaching Machine does that. LCWO also comes with an implementation of that idea.

## Answer (score 4, by Peter Bagyinszki)

There are videos on Youtube that play the morse first and then the meaning in spoken English. For me, this was the most comfortable method of learning.

For example: Top 180 QSO Elements

Full playlist for 20 wpm: 20 wpm

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20296/learning-morse-but-i-can-t-write-fast-enough, by Toby Eggitt, rclocher3, henryflower, Peter Bagyinszki. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
