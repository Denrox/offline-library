# How can I find the input port for downloading my radio information?

*Tags: radio-programming, uv-5r · score 3*

## Question

I am trying to download my Baofeng UV-5R into CHIRP for the first time and it is asking what port to pull information from. How can I find what to input here since it isn't automatically updating/ what do I need to fix to get it to automatically input?

## Accepted answer (score 3, by rclocher3)

The program is asking you which serial port you're using to connect to the radio. If CHIRP's list is empty, then you probably have no serial ports because the drivers for the virtual serial port chip in your cable aren't installed, or your cable or virtual serial port chip just isn't working.

If CHIRP isn't picking a serial port for you automatically, but there are some in the list, then you may have more than one serial port or "virtual" serial port in your computer, and your problem is to figure out which one belongs to your cable.

If you have more than one serial port in the list and you're using a USB-to-serial adapter cable, which most people use, then there are ways to find the identifier of the virtual serial port associated with your cable.

- In Windows, pull up the Device Manager and plug and unplug the cable a few times. The serial port associated with your cable will appear and disappear in the Device Manager as you plug and unplug the cable.
- In macOS, open Terminal and enter the command ls /dev/cu.* to list all serial devices, then unplug or plug in the cable, run the command again, and see what appeared or disappeared.
- In Linux, unplug and plug in the cable (once), and run sudo dmesg | less; the output should give you a few clues. If you only have one virtual serial port then the one you're looking for is probably /dev/ttyUSB0 in Linux.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18289/how-can-i-find-the-input-port-for-downloading-my-radio-information, by user19296, rclocher3. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
