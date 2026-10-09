# Looking for a morse code decoder that simulates keyboard input

*Tags: morse-code · score 3*

## Question

I know that there are several commercial programs that will decode incoming CW using the computer's sound card, but this is not quite what I need.

The specific requirement that I have is to feed the decoded output (in real time) into a memo/text field in another program running on the same computer. In my mind, the easiest way to do this is to have the decoding program generate keyboard messages directed at the receiving program.

The application is for a museum exhibit that allows people to send messages using Morse Code as input. The audio input quality will be very good (generated on-site with an oscillator and wired (non-radio) connections, so having a known frequency and audio level), but the Morse code timing will be poor as the general public will be using this system.

I'm looking for solutions preferably for Windows.

Does anyone know of any resources or insights that might help with this problem?

## Answer (score 3, by Andrew)

I think I have built exactly what you need for practising morse. I wrote it all up in a blog :-

http://whaley.org.uk/andrew/blog/2017/04/28/morse-code-cw-via-usb/

It's a USB adapter that takes a key at one end and spits out keyboard characters into a computer at the other. It also contains a buzzer which generates the sidetone. It's really cheap and easy to build and will literally take an hour to assemble. It'll work on all computers and even Android devices without any software being installed.

## Answer (score 3, by flickerfly)

The K3NG keyer probably has all the parts you need except writing out to as a keyboard emulator, but some of the Arduino hardware that the K3NG keyer software runs on has the ability to output USB HID to a computer which makes it appear to be a keyboard.

The K3NG keyer might actually fill all your electronic requirements for the users input also.

Info on Arduino as a USB HID Keyboard: https://arduino.stackexchange.com/questions/484/arduino-as-usb-hid

K3NG Keyer: https://github.com/k3ng/k3ng_cw_keyer/wiki

Both the Arduino and the K3NG Keyer have open source communities that would jump in to help out with any problems you run into.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/6513/looking-for-a-morse-code-decoder-that-simulates-keyboard-input, by EBlake, Andrew, flickerfly. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
