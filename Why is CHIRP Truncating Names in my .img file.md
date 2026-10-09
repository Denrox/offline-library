# Why is CHIRP Truncating Names in my .img file?

*Tags: radio-programming, chirp · score 3*

## Question

I have a problem when I am importing a .csv file into an .img file in CHIRP where the memory location names are being truncated in a strange way.

In the .csv file, the display properly:

And when the .csv file is opened in CHIRP:

However when I import the .csv file into the .img file, the names get truncated:

I can't for the life of me figure out why.

The .img file is from a Yaesu FT-60

Any ideas?

Thanks!

## Accepted answer (score 6, by hobbs - KC2G)

1.

The memory name display (and storage) on the FT-60 is only 6 characters. Your names will be truncated to that length no matter what.

2.

The names use a limited (LCD-friendly) character set that doesn't include any lowercase letters. The Chirp driver for the FT-60 replaces any out-of-charset characters with spaces. Probably it would be better if it turned lowercase letters into uppercase letters instead of spaces, but... it doesn't. Feature request time!

Meanwhile you should go through your CSV file and give all of the stations 6-character names using only uppercase letters, numbers, punctuation, and space.

If you noticed that there are some lowercase "o"s in your file, and I said there are no lowercase letters — good eye! "o" and "u" are actually in the character set. I think they're meant to be *shapes* on the FT-60, rather than letters, but in any case Chirp does map them to those two letters. Make of it what you will :)

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/18834/why-is-chirp-truncating-names-in-my-img-file, by Tikhon, hobbs - KC2G. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
