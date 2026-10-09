# Repairing a Tecsun PL-660

*Tags: receiver, equipment-troubleshooting, repair, tecsun · score 3*

## Question

Two years ago, my father and I both received a Tecsun PL-660 radio as a Christmas gift. We both have had good experiences with our radios and generally enjoyed them until they recently both stopped working. I should mention my radio has been at my house in Arizona for the last 2 years, while my Dad's radio has been in Pennsylvania. So they have been in completely different/isolated environments.

My Dad's radio died first and seemed to be completely bricked. There was no on-screen display at all, and no combination of batteries or wall warts was going to get that radio to do *anything*. It was a doorstop.

About a month later, my radio starting flashing the display and blinking a "Lo battery" message. Changing the batteries and/or using the wall adapter did not improve the situation at all. The radio simply will not turn on.

Now, some cursory googling has shown a lot of people have had problems with this model of radio, and for the price they generally give up and get a new one. However, we generally take good care of our gear and the radios were gifts so we decided to see if we could do anything...

After taking apart my Dad's radio, I noticed there is a small button battery welded to the main board. Reading the battery in place showed it to be completely flat. So we did some surgery and 'popped' the battery off the board. We did some guessing as to the correct voltage, but putting 4.5v from an external set of AA's was enough to bring my Dad's previously dead radio back to life. Almost.

The display (computer?) has come back to life, we can turn on the radio and selecting different bands works. The radio will tune and looks like it should be working. However, we still have NO audio at the speaker or the headphone jack. The on-screen signal strength meter is completely flat, and the internal display 'backlight' will not illuminate.

I could theorize we had two separate issues, and we only fixed one of them by repairing the flat battery - or maybe we flexed/broke something when removing the original button battery from the board.

So the crux of my question is for some input of what else we might check? I don't have access to the second radio at the moment, so there is no way to find out if the battery repair is enough to bring the second radio back to life. Until I can do that test, I figure we can continue to tinker with the radio we do have. But what should we chase? Obviously we aren't going to get into replacing surface mount IC's etc. So I'm fishing. Any ideas?

**Update**

I have not pursued trying to fix this radio any further than I described in my original post. However, I did do some research on the net and found some additional resources I thought might aid anyone else trying to repair their radio.

First, I found this blog post regarding ESD repair to a Tecsun 600, which might be similar in design to the 660:

Repairing the Tecsun PL-600 after electrostatic discharge (ESD)

I was also able to locate schematics for the PL-600 and PL-660 radios - both printed in (what I am guessing is) Chinese. I no longer can locate the URLs for those, but they can hopefully be found with some Googling...

Finally, I remember reading *someplace* that there is a 3.5v (I think?) voltage regulator on the radio mainboard, that frequently goes bad. I think it was a surface mount component, and that is beyond my skill level to replace - so I never pursued it further. I've never even looked for the component to see if I could locate it. I'm mainly mentioning it because there was renewed interest in my original question, and if someone does manage to repair their radio, it would be interesting to know if that is indeed the culprit or if it's something completely different going on.

I still have hope of eventually fixing these radios, but it is far down on my list of projects.

## Answer (score 6, by vincenzo)

I signed up here just to reply to this great (the only one I could find on the internet) question/experience that helped me with an identical problem. I was so close to giving up when I read this thread and went to examine the component that looks like a coin battery (as the original poster described)  and having owned a sucking hakko soldering gun, i managed to remove it from the board (you'll have to remove the metal shield under the board first, which makes it even harder, but a piece of cake for an expert like me). I then soldered two tiny wires to it's pins and connected to a power supply that I started at 1.0v and incremented 0.1v at a time. The radio's dead screen came to life at 2v and everything was normal. The screen was on even with no AA batteries, but the "low battery" symbol was blinking and the radio won't turn on until the AA's were installed. This component looks like two small coin batteries stacked over one another. Upon further investigation, I discovered that it is actually a very small super capacitor of .22F and 5.5v that is relatively expensive (around $10 a pop). I put a 2200uf that i had and the screen came on for only a second. I'm not sure if supercaps (very high capacitance electrolytics) can be tested just like a regular cap and if they have a short life time but i'm still researching and would love to hear from others (especially the original poster from 4 years ago!). It could be that tecsun put very bad quality component there purposely to sell more radios!!! that's for them to answer.

## Answer (score 5, by SDsolar)

Tecsun is very similar to Baofeng in that anybody selling them expects a certain number of DOAs and other failures. They already know that QA on those rigs is directly reflected in the price.

In the past I have had good success with getting vendors of like this to replace the radio body (no battery or antenna) simply by writing to them.

I have gotten two Baofeng radio bodies shipped to me (no return necessary) and returned a Tecsun entirely this way.

On eBay they always appreciate it if you do not use the return option - instead just send them a message. That way they will hope you can still give them positive feedback and their selling reputation doesn't take a hit.

Your question is about how to repair it: My answer is that the best repair is replacement.

Give it a try. Send them a message.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/9459/repairing-a-tecsun-pl-660, by Geo..., vincenzo, SDsolar. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
