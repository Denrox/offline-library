# Setting up an HF Schedule

*Tags: hf, propagation · score 3*

## Question

I want to make a contact with a ham who is far away (>10,000km). How would I intelligently plan a scheduled contact to maximize possible success?

Assumptions:

- Both stations have optimized their configuration for each band (maximum power, good antenna, capable of trying both long and short path azimuths)
- Both stations are capable of multiple HF bands, without a requirement that it be on one specific band (e.g. I don't need this contact just for a 80m phone award)
- I want to maximize the signal to noise ratio
- We have an accurate time reference for coordination (e.g. GPS clock)
- We are trying to make a voice (SSB) contact
- We can have written correspondence

How should I select a time, band, and frequency to maximize the chance for success? Is there any procedure or protocol that would help?

## Answer (score 4, by tomnexus)

This is actually quite a standard question that any non-hobby HF user will have, so there is good software to help.

I recommend starting with VOACAP online to make predictions for the best bands and times to try. VOACAP makes a prediction based on the typical conditions at a particular sunspot number, not the exact conditions right now. It is really for planning, equipment selection, frequency choice when setting up an HF link. You can download it to run on your computer, but the web version is really easy to use.

Then there is great real-time information available from WSPRnet, which plots propagation right now. Have a look around and see how it works, you can quite easily try a particular band and time window. You can also run a listening station yourself without too much trouble, to see what you can hear. WSPR is even more sensitive than CW, so it works long before phone. If you're anywhere near a large population centre though, there will be plenty of users close enough to you.

## Answer (score 2, by Phil Frost - W8II)

1. Eliminate all times and bands which are not acceptable.
2. [Select a band appropriate for the time of day and seasonal sunspot activity](Which%20HF%20bands%20are%20best%20during%20the%20day%20and%20which%20are%20better%20at%20night.md). It's pretty easy to scout which bands might be good: if you can hear other stations in similar areas at similar times, it's good. Tools you can use in this endeavor are beacons and [receivers streaming to the internet](Is%20there%20a%20way%20to%20listen%20to%20live%20HF%20communications%20using%20the%20internet.md). There are even projects which perform this experiment constantly and publish the results.
3. (optional) Make alternate plans in case your primary plans don't work out, involving different bands, at different times.
4. Hope for the best, then repeat until it works.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/3568/setting-up-an-hf-schedule, by W5VO, tomnexus, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
