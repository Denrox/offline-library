# Is a boom important to a Yagi?

*Tags: antenna-construction, uhf, yagi · score 6*

## Question

I am trying to make a yagi for a 900M. The tinkering starts causally with some 1.2mm welding wire (cut to size based on K7MEM yagi calculator, direct soldering, no special matching as suggested on K7MEM page) glued to a 1mm plastic strip, since I really didn't expect it to work. The result just works much better than a ceramic disk antenna (I need focused, direct, long distance beam in this case). I can read EPC card a lot further away.

But the strip is too flexible so I moved to chopstick + hot glue (for miniature), the halves of driving element is so hard to fix onto the boom. I have to cut broken lead and re-solder the RG178 cable once, re-glued many times.

To solve this issue, I have the following doubts:


Can I ditch the boom just stick them to my pcb casing (Its a plastinc box with 3mm thin walls, the lid is 60mm away from the PCB. I am thinking stick the elements through the sides of the lid. Putting the wire yagi on the casing lid didn't affect the performance much, thus I guess moving it 5mm inward won't make much difference) ?


Or can I use a PCB strip to solder the steel wire to a PCB bar


In both case, as to the gap between the 1/2 halves of the driving element , how big can it go ?


In case a boom is strongly suggested, does a metal boom and non-metal boom make much difference (I mean booms isolated from elements) since all boom options in the DL6WU calculator are metal, while K7MEM include non-metal. I wonder if this has any significance.

PS: ppl might wonder why care to ask since you already have a working yagi with 1mm thin "boom". As you can see, it's a causal test, I don't know what performance to expect, the small circular polarized ceramic disk antenna distant is too close, big ones has a mysterious radiation path at distance - tags have to be moved around to find a readable spot. So,I guess I might be comparing orange to apples, and the test is only successful to my new comer standard.

## Accepted answer (score 4, by tomnexus)

A couple of quick pointers for RFID and antennas in general.

First, read the **free book** "Antennas in Practice" by Clark and Fourie has some excellent background on antennas, yagis, helixes, and includes some reliable yagi designs that you can scale for your frequency.

For RFID you really need **circular polarisation** unless the tag is guaranteed to be in a particular orientation. This naturally leads you to patch antennas, but circular patches are hard to design and tune. You don't want a little 1 inch square ceramic patch - look for a product with a full size patch (150 mm) on a reasonable-size groundplane (300 mm).

You can definitely make a yagi for 900 MHz, but please take these hints:

- Without a way of measuring what you've got, you will be thrashing around in the dark. The read range is one way of measuring performance, but if it's not working well, it doesn't tell you anything about what to do next. If you haven't already, get a \$50 NanoVNA and several metres of thin coax with SMA connectors, from Amazon, Ebay, etc.
- Yagis are quite sensitive beasts, not very forgiving of dimensional errors. Lots of tuning and tweaking to get them to work properly. They;re quite narrow band, so for example, if you tune it for 915 MHz, it won't work at 868. This also means that dimensions need to be within 1% or 2% of perfect, which is just 2 mm at these frequencies.
- Plastics near or touching the elements will "lengthen" them by 10%, for thin plastic, or 20% or more, for thicker plastic or printed circuit board. Unless you have the \$25k/year software, you need to find the factor by experiment.
- Yagi elements lengths need correction for a metal boom too, there's a formula for how much shorter they must be, depending on the thickness of the boom. The boom isn't required, or it can be plastic or wood, but if it's metal it affects the element lengths slightly.

So I'd suggest these steps in getting a yagi made of wires-on-plastic working:

1. Find a working reference design (see the book below for example).
2. Build it in free space, thin plastic or metal boom, and check that it works well.
3. Migrate it to plastic one step at a time. First tune the reflector for best performance, with no directors in place. Start at 90% of the free space length, cut it shorter until you find the best length. Then install the directors, cut them all shorter 1 mm at a time until you find the best length. Then re-tune the reflector. Finally adust the driven element for best VSWR. In all cases, you'll see the "region of best performance" moving up in frequency as you cut.

As you can see you'll need a way of modifying the antenna many many times, so you need a design that supports both comfortable and fast adjustments and testing, but is also close enough to the final product that you don't have to repeat the tuning yet again.

Consider also an axial-mode helical antenna. These are easy to build, give circular polarisation, and with a >50% bandwidth they are extremely forgiving. You can wind some wire onto a piece of PVC pipe, and adjust the part near the connector for best VSWR (on your NanoVNA). There are many designs and tutorials on the web.

The plastic will make the antenna "larger" than its physical size, so get a pipe maybe 20% smaller than the basic calculations require. I've found that if you go to the hardware store and buy all the sizes near what you think you'll need, you get a set of overlapping antennas and can choose the best for your application.

## Answer (score 4, by user10489)

The boom on a yagi is critical. As you've discovered, without it, it falls apart. :-P

Seriously, though, the real function of the boom is to hold the mechanical positions of the elements. It does matter of it is conductive or not -- but this only changes parameters of the geometry, it doesn't affect the performance.

Also, you could make the yagi on the PCB directly with traces and not bother with the wires. (But wires are easier to move around if you aren't modeling it.) Also, the dialectic of the PCB (or the lid or whatever it is near) can affect the tuning a bit, but generally don't have a large effect on performance.

## Answer (score 3, by Escoce)

The boom on a yagi is strictly structural. If you can somehow suspend elements at the right placement and spacing, it will work perfectly. Yagi's alter (focus) the field, not the current.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/21785/is-a-boom-important-to-a-yagi, by Ben, tomnexus, user10489, Escoce. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
