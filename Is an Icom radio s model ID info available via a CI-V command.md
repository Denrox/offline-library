# Is an Icom radio’s model ID info available via a CI-V command?

*Tags: icom, software-development, computer-aided-transceiver, icom-ic-7300, ci-v · score 3*

## Question

I have built a prototype device using an Arduino Nano Every which communicates (using CI-V commands) with Icom radios, to augment control of them. Currently I use the default addresses of the “target Radio” (set to 0x94 - 0x97 via jumpers on the custom PCB) to tweak the commands it sends, but it would be useful if the radio’s model could be determined to allow my device to tailor the range of some of the functions it provides e.g. there are 8 Mode options on an IC 7300, but 20 on an R8600. I have not (yet) found a command which yields the Model type. An alternative method could be to use the small differences in the command sets, and probe those, but that may not be unique to each Model. Any suggestions are welcome. Here is my prototype device https://youtu.be/-kn3Pd1ENI8.

## Answer (score 2, by guitarpicva)

ICOM uses "other" CI-V commands to interrogate the radio. If you have any of the radios which use their "Cloning Software" you will notice that there is an "Information" button. This typically will display the serial number of the radio. Some radios give more information. Some such as the current IC-9700 give nothing at all (which may be firmware dependent).

The only way to get this CI-V information is by serial sniffing. What I have found with 5 of the current D-Star radios is that they each have a different "model number" of 4 digits followed by 8 digits of serial number, thus a 12 digit number. There is a special CI-V command based on that 4 digit "model number" to prompt the radio to send back the full serial number.

For example, the ID-5100A sends:

FEFEEEEFE034840000FD

And the ID-4100A sends:

FEFEEEEFE038660000FD

to reply with the full serial number which reads (for ID-5100A):

3484nnnnnnnn, where "nnnnnnnn" is the serial number of the radio.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/20986/is-an-icom-radios-model-id-info-available-via-a-ci-v-command, by anoracknophobia, guitarpicva. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
