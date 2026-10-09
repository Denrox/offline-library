# Installing GNU radio on android

*Tags: gnuradio, mobile · score 3*

## Question

I want to install this miracle program on my smartphone in order to get more mobility.

I found such a solution exists: https://github.com/bastibl/gnuradio-android

However, I could not do everything as indicated in that article. As I understand it, you need to create an installation file yourself, which can only then be installed as an application. But isn't there still a ready-made installation file? I am not good at programming, so nothing works. I understand that maybe I wrote in the wrong area, but suddenly one of you wondered this question and found an easier installation solution. I will be glad to any answer, thanks!

I also saw a video where the GNU radio companion is also opened^ https://www.youtube.com/watch?v=DfCjLYp-apY

## Answer (score 4)

*I know this is old, but if anyone comes across this one it might be useful to have some idea what is going on.*

This GitHub project is not a way to put "GNU Radio on Android". Mostly because GNU Radio isn't an application; rather, is a framework used to create programs that do radio things. If you run the GNU Radio Companion it shows you the parts of those radio things as recognizable block diagrams, but at the end of the day a GNU Radio application is one or more Python, native, and UI modules compiled and linked together to make a radio thing.

What this project does is provide a turnkey build-and-deploy system to host or assist Android Studio development for the purpose of *compiling and packaging* GNU Radio applications that can be subsequently installed onto Android devices. It looks like there are sample applications ready for deploying, but the idea is that you would be creating your own GNU Radio application that does what you want it to do on your hardware.

It appears to replace most of the boring hacking necessary to set up Android Studio so that it compiles, assembles, and packages Android applications that "wrap" GNU Radio processing so you can run those applications on Android. It looks like it takes some of the pain away around device handling for USB SDR hardware, as well.

So, there is nothing for it but to learn how to get this development system working based on the documentation, and to learn how to create and run Android applications on your connected Android devices.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18089/installing-gnu-radio-on-android, by Антон. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
