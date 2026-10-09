# Beginner listening to a repeater - only hearing one station

*Tags: baofeng, repeater, united-kingdom, repeater-coverage · score 5*

## Question

This morning I tuned in to a repeater about 12km from me (in the UK). I could hear activity, but from only one station. I could tell that there were other stations using that repeater from the comments of the station that I could hear. Why couldn't I hear the other stations? Doesn't the repeater re-transmit the other stations with the same signal strength as the station that I could hear?

## Answer (score 9, by vu2nan)

It is presumed that you were receiving on the 2m band.

It appears that you were listening in, using 'repeater reverse' mode. In other words, you were listening in on the repeater's input frequency rather than on it's output.

On 'reverse', you would hear all the stations within range. In this case only one station would have been within range.

Had you tuned in 600kHz above or below, you would have heard all the stations accessing the repeater, either above or below, depending on whether the repeater input frequency was 600kHz above or below its output frequency.

## Answer (score 4, by SandPiper)

The concept is called "offset". The repeater is listening on one frequency, and is repeating it verbatim in real time on another frequency, but typically at a higher power so more people can hear it further away.

Most repeaters (numbers specific for the US anyway, but the concept applies internationally) have a plus or minus 600 khz offset. This is not a legislated requirement, it just a convention people came to over the years. What this means is that a repeater that transmits at 146.000 MHz with a -6khz offset will be listening at 145.400 MHz.

In practice, what this means is that you were listening on your radio to one of those two frequencies, and thus only hearing half the conversation. If it was the repeater's input frequency (145.400 in my example), then you are listening to whoever was nearby talking directly from their radio to the repeater (and also your radio). However, whoever was talking to him was too far away for your radio to hear directly. If you tried talking back, no one would hear you because they are all listening on 146.000, and they won't even know you're there!

If you were on 146.000 though, you would hear everyone talking on the repeater, but the only people that would hear you are the ones close enough for their radios to pick you up directly. Because you were only hearing half the conversation, I suspect you were monitoring the repeater's input frequency, not the output.

Try using a resource like https://www.repeaterbook.com/ to find the repeater and look up what their offset is. Your radio instruction book should show you how to program it. Best of luck!

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/16733/beginner-listening-to-a-repeater-only-hearing-one-station, by Adam, vu2nan, SandPiper. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
