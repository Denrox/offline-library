# Calculating satellite passes without an internet tracker?

*Tags: satellites, software, software-development · score 5*

## Question

**Situation:**

You want to know when a satellite will pass in order to receive an image transmission or to work an amateur satellite. However, you cannot access internet for whatever reason, and therefore can't simply look up a pass prediction chart or live tracker.

**Question:**

Can you/how would you calculate approximately where a satellite would be at any given time, or calculate when the next pass would be? Do satellites always follow a scheduled path to repeat and cycle through? What basic orbit information should I collect about each satellite I need beforehand?

Is the satellite always *actively* kept in this exact timing, or does it slowly "drift" from its scheduled path? I ask this because if it does drift, this would eventually make any planning useless without direct connection to the satellite, if that makes any sense.

A simple path/time map (like below) would be best, but (offline) software also works.

Edit - Do the satellites transmit data about their position that I would be able to receive and decode?

## Accepted answer (score 8, by tomnexus)

The simplest might be to use an app.

On Android, Heavens Above, a product of the 25-year-old website of the same name, stores the orbital elements of the satellites of interest, and does the pass calculations on your phone.

The app uses the GPS to find your location. It likes to get fresh elements from the Internet on startup, but it caches them, so as long as you download them before you leave, for radio amateur purposes they will be fine for a week or more.

W1ANT satellite tracker is designed specifically for amateur satellite operation.

See this Wikipedia entry for a solid summary of desktop and web software available.

Satellites do drift away from simple orbits, and almost none of them maintain them deliberately (Starlink does, with ion thrusters). Perturbations from the changing solar wind, atmosphere, the moon's gravity, and non-ideal shape of the earth result in the keplerian elements getting stale. It depends on how accurately you need the position - for a visual pass, 100 km accuracy is probably good enough. For pointing a small dish, 10 km. For GNSS you need to know their position to better than about 50 m for them to be useful, the operator updates the almanac of orbital elements every few hours.

Most satellites don't transmit their position, you need an external database. They are tracked daily by the US military and others, by a combination of radar and optical systems, and the updated elements are published on Celestrak and elsewhere. GNSS satellites are different, because position is at the heart of what they do, and you need to be able to use them without another data connection, they do broadcast their position all the time.

There are many hobbyists that track down satellites and determine their orbits, even unpublished military satellites.

Finally - here is a method from 1958 do allow computing of a pass just with pencil, paper and a slide rule. (remember, we've been in orbit longer than we've had integrated circuits).  
Some beautiful diagrams from the paper:

## Answer (score 3, by user10489)

To track the satellites, you need the Keplerian TLE orbital coefficients. Once you have those, you can track the sats without internet access. The TLE's are accurate enough for about a week. The TLE file format is standardized and works with nearly all the tracking software, and most software either downloads them on command or can import from a file.

As already mentioned, sats like GPS and GNSS continuously broadcast their orbital parameters. I believe GPS updates them every 6 hours or something, based on ground station data uploaded to the GPS network. (In other words, the data is not exactly live, it doesn't change that fast.)

However, other sats don't broadcast their positions.

So there are three ways you could do this:

1.

(easiest) Download the TLE's for the sats you want to track ahead of time when you do have internet. Hopefully you'll be able to update them a week or two later.

2.

(the hard way) Use the stale TLE to guess where the sat is and use visual or radio methods to track it and measure the drift. This might have to be done daily or the drift will be great enough to make it hard to find.

3.

There is an amateur radio digital HF net that broadcasts a number of static files, including the current TLE's for popular satellites. I believe the net is daily (or weekly) and runs for a few hours. Software like fldigi along with one of its accessory programs can listen to the broadcast and save the files. There may be other radio sources (including a satellite network) for this information as well.

Some resources are:

- https://www.amsat.org/keplerian-elements-resources/
- https://www.kc4mcq.us/?page_id=24816
- http://www.arrl.org/digital-transmissions

---

*Source: Amateur Radio Q&A (Stack Exchange), https://ham.stackexchange.com/questions/17633/calculating-satellite-passes-without-an-internet-tracker, by Galaxy, tomnexus, user10489. CC BY-SA 4.0 (posts before May 2018: CC BY-SA 3.0), Stack Exchange.*
