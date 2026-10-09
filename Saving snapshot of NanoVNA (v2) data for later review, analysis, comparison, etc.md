# Saving snapshot of NanoVNA (v2) data for later review, analysis, comparison, etc

*Tags: nanovna · score 3*

## Question

I have a NanoVNA (v2), and I'm using it with vna-qt. I want to capture the raw data from a sweep for posterity, so that I can someday compare different antenna variants for things like SWR, resonance, etc. I'm pretty sure vna-qt itself can't load captured data and display it, but if I at least HAVE a copy of the raw sweep data saved somewhere, I can cross THAT particular bridge later & either find some other program that can, or maybe write my own program to do it.

But first... I need to figure out how to capture an save a sweep's raw data to a file. How can I do this? I've tried the various capture & export options under the "S Parameters" menu, but they all seem to either work only once, or hang the app completely when I try using them, and as far as I can tell, the app's official documentation says *nothing whatsoever* about *anything* under the "S Parameters" menu.

## Accepted answer (score 3, by hotpaw2)

When I want to look at the raw data, I simply use a serial terminal application to connect to my nanoVNA at 9600 baud. Then type "frequencies" to get the current list of sweep frequencies. Then type "data" to get the current list of IQ parameters from the last sweep. Then cut-and-paste the terminal's text output into a spreadsheet, where I can graph/analyze/compare/export/etc. the data any way I want.

You can type "help" into the nanoVNA's console for a longer list of interesting commands.

If you connect to a nanoVNA's serial console via python or Basic (et.al.) you can also script a sequence of sweep commands and data downloads.

## Answer (score 4, by Brian K1LI)

Looks like you have to use NanoVNASaver.

This software connects to a NanoVNA and extracts the data for display on a computer, and for saving to Touchstone files.

Download it from github.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18208/saving-snapshot-of-nanovna-v2-data-for-later-review-analysis-comparison-etc, by Bitbang3r, hotpaw2, Brian K1LI. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
