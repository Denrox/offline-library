# How can I tell if a call sign is valid?

*Tags: callsign · score 14*

## Question

Many different countries have different callsign formats. The US call signs typically fit into a very well defined category, but there are exceptions even there. I'm looking for a way to tell if a call sign is a real call sign, that works with international call signs. I'm looking for the full call sign, including after a '/'. I don't care if the call sign is actually assigned to a user, just if it is possible to assign the call to a user. I'm looking for rules as to what would be considered valid. A very general sense is okay too. I don't care if I filter something that could be a call sign, but isn't actually assigned, like 1S prefix calls, but I do want to make sure I get special edge cases, like W100AW.

From what I can tell, the format that is valid appears to include a prefix, which can include up to 1 number and always includes 1 or 2 letters, followed by a number identifier, followed by 1-3 letters. An additional part of the call sign can be included before or after the call that can include a lot of things, including a /AE,/AG,/KH6 (Or other prefix), and possibly other things as well, which I'm not really certain of. I'm looking for something like this, but preferably more detailed.

Basically, I'm trying to tell if a callsign is likely to be real, so I can check to see if I have an invalid call sign in my logging program.

## Accepted answer (score 14, by Adam Davis)

Callsigns, per ITU regulations, consist of a prefix and a suffix. The prefix must be obtained from this table:

Table of International Call Sign Series (Appendix 42 to the RR)

And is assigned on a per-country basis. The suffix is then determined by that country's internal radio regulations, and there is no standard that will make this easy for you. You'll need to research each country's regulation and standard and include hundreds of different rules if you need to determine validity to that degree.

However, you can eliminate a lot of bad callsigns simply by verifying that the prefix is valid, using the above list.

The general guidelines on the formation of a whole callsign, including what the suffix may contain, are fairly well explained in this wikipedia article:

ITU prefix (amateur stations)

There are rare exceptions, but generally you start with the country prefix, add a numeral, then add a suffix of between 1 and 4 alphanumeric characters. The last character has to be a letter, not a number, but otherwise there's no regulation internationally.

## Answer (score 3, by Tim Makins)

If you check out the resources provided by Alex Shovkoplyas, VE3NEA in http://www.dxatlas.com/Dev/ you will find a variety of examples of callsign parsing. His prefix list contains REGEX matches for each country, but be aware that he uses HIS OWN syntax for callsign matching:

The 'Mask' field in PREFIX.LST is used for callsign resolution. The following meta symbols are used in the mask:

'@' - any letter '#' - any digit '?' - any character (letter or digit) [AC] - A or C [A-C] - A, B, or C. [AC-E] - A, C, D, or E. '.' - no characters are allowed after this simbol. Example: '??#@@.' matches all calls with 2-letter suffixes.

His symbols MUST be substituted for other types, to use the mask with other languages:Javascript, VB.Net, PHP, etc.

You can also find REGEX strings in the AD1C Country Files.

## Answer (score 3, by PearsonArtPhoto)

Starting with Adam's answer, I did a bit of research into the matter. Using a list of LOTW call signs, I tried the following regular expression \d?[a-zA-Z]{1,2}\d{1,4}[a-zA-Z]{1,4}, which simply says a number can optionally start, followed by 1 or 2 letters, followed by 1-4 numbers, and 1-4 letters. I'm filtering out any extra parts (Stuff before and after a /. Given this, I still failed on the following call signs:

```
4D71/N0NM
4X130RISHON
9N38
AX3GAMES
BV100
DA2MORSE
DB50FIRAC
DL50FRANCE
FBC5AGB
FBC5CWU
FBC5LMJ
FBC5NOD
FBC5YJ
FBC6HQP
GB50RSARS
HA80MRASZ
HB9STEVE
HG5FIRAC
HG80MRASZ
II050SCOUT
IP1METEO
J42004A
J42004Q
LM1814
LM2T70Y
LM9L40Y
LM9L40Y/P
OEM2BZL
OEM3SGU
OEM3SGU/3
OEM6CLD
OEM8CIQ
OM2011GOOOLY
ON1000NOTGER
ON70REDSTAR
PA09SHAPE
PA65VERON
PA90CORUS
PG50RNARS
PG540BUFFALO
S55CERKNO
TM380
TX9
TYA11
U5ARTEK/A
V6T1
VI2AJ2010
VI2FG30
VI4WIP50
VU3DJQF1
VX31763
WD4
XUF2B
YI9B4E
YO1000LEANY
ZL4RUGBY
ZS9MADIBA

```

So I guess there isn't a standard definition, but you should be able to recognize most of them with a similar pattern, and just be aware that there are others out there as well.

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/1352/how-can-i-tell-if-a-call-sign-is-valid, by PearsonArtPhoto, Adam Davis, Tim Makins. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
