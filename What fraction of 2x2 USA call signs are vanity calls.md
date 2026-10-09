# What fraction of 2x2 USA call signs are vanity calls?

*Tags: united-states, callsign · score 8*

## Question

I found out a while back that, as things currently stand with the FCC, if you take and pass all three license class exams in the same sitting, you get a so-called "two by two" or 2x2 call -- two letter prefix, region/district number, and two letter suffix. Regularly issued Technician and General licenses at this time are 2x3. In the past, there have been times when call signs would change with license upgrades (for instance, when N was inserted in a Novice licensee's call, then replaced with the then-current second prefix letter when they upgraded), but upgrading to Extra class doesn't now, as far as I can see, result in snipping a letter out of your call.

It is also still possible to request a new call on license upgrade, though only Advanced (no longer offered, but still renewed) and Extra are eligible for 2x2 calls. This will get a serially assigned call.

However, there's another way to get a 2x2 call: buy it (though apparently the FCC dropped the fees for vanity call applications). Any licensee in the USA can apply for a so-called "vanity" call, which can be any currently valid (for their license class) format call not currently issued (1x2, 2x2, 2x1, 1x3, etc.).

Which brings up the curiosity question: about what fraction of 2x2 call signs in the USA are vanity calls, as opposed to originally issued in that format? Is this information even public?

## Answer (score 9, by natevw - AF7TB)

According to my calculations, about **20%** of active 2x2 callsigns in the FCC's amateur radio service database are vanity callsigns.

For comparison…

- 75% of active 1x2 ham licenses
- nearly 50% of active 2x1 licenses
- only 3.5% of active 2x3 licenses

…are vanity callsigns.

If you'd like to check my work or make further refinements, I determined these stats using a Python script available at https://gist.github.com/natevw/3ddfe7aef454c345f68464048ad52ee2 against the ftp://wirelessftp.fcc.gov/pub/uls/complete/l_amat.zip file downloaded on 2019 September 4.

Note that as @rclocher3 points out in his answer, two of your question's premises regarding vanity callsigns are a bit off:

- *any* class licensee can request a vanity callsign, not just General and Extra
- but only *Extra* (or Advanced) class licensees can request most 2x2 callsigns

The last point requires a bit of qualification: there are some regions like Alaska, Hawaii, and other US possessions which generate 2x2 patterns within **Group C** and therefore would be available to Technician and General class — that said, unless I'm mistaken you *would* need a mailing address within the region to be eligible. See https://www.fcc.gov/amateur-call-sign-systems for more details of all the callsign groups corresponding to the license classes. (Note that the script used for the stats above does **not** distinguish between callsign *groups*, only the raw letter/number *pattern*.)

## Answer (score 5, by rclocher3)

An amateur licensee of any class can request a vanity call sign. Also, only Amateur Extra operators are eligible for 1x2 or 2x1 call signs; only Advanced and Amateur Extra operators are eligible for 2x2 call signs. See US Title 47 CFR §97.19 and the FCC's Amateur Call Sign Systems page.

Whether a current call sign is sequentially-issued or vanity is easy to see in the FCC's Universal Licensing System (ULS) database: if the service is "HA", the call sign was sequentially issued; if "HV", it's a vanity call.

The fraction of 2x2 call signs that are vanity is public information, since the ULS is public information. To answer it would require downloading the entire database (instructions on how to do so are here) and then analyzing the data. Several organizations, such as qrz.com, have already downloaded the data, so you might ask one of them.

## Answer (score 4, by Phil Frost - W8II)

natevw has already answered the primary question, but there are some secondary points in your question to address.

Although passing the Extra exam doesn't immediately grant you a new call, you do become eligible to request a new one, which will be a 2x2 and sequentially allocated just as it would be for a first-time ham that tested straight to Extra.

It's also possible to request a new call if you move to a region subject to a different numbering scheme.

In the past this was mandatory, but now it's optional.

Finally, vanity calls are now free. The FCC determined they spent more money administering the fees than they made from them, so they just dropped the fee.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/15262/what-fraction-of-2x2-usa-call-signs-are-vanity-calls, by Zeiss Ikon, natevw - AF7TB, rclocher3, Phil Frost - W8II. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
