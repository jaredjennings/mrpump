Mr. Pump is a twitter bot, using tweepy.

To use
------

0. Install Mr. Pump.
1. Set up an account for Mr. Pump on Twitter.
2. Follow Pump's account, and make him follow yours.
3. Visit dev.twitter.com. Log in as your Pump user. Create a new 'application.'
4. Remember that only you are responsible for how you use or abuse Twitter.
5. Get the developer access token for your app.
6. Write a config file; we'll call it golem.ini. (see below.)
7. Run Mr. Pump::

     emet golem.ini

8. Send a direct message to Mr. Pump, e.g. "19 ping."
9. Receive his reply: "927 pong."


What are the numbers in the messages?
.....................................

Just a way to get around Twitter's "Whoops, you already said that!" message. It
appears to be meant to prevent double posting. But when you are talking to
computers you may need to repeat yourself more often than with people.



Config file
-----------

::

    [app]
    # OAuth info needed to log in. You get these two when you register your app -
    key = ABCDEFGHijkl012345MNO
    secret = gr0igh24g8h240gh2rvun92rnuEIIH847fhier00
    
    # (this is the screen name of the bot)
    [mygolem]
    # - and you get these two when you get your developer access token.
    token = 284729478-KANEFIIGRVKNRVO3883474KFKEVDKknvdvdkn993
    secret = prgiIRGJIGkvmvvnkfkKNKRFNKFIFEIV48347fenef
    
    # A name for the instance of the ping chem -
    [ping]
    # For the ping chem, use the 'ping' entry point from the 'mrpump' egg.
    use = egg:mrpump#ping
    
    # A name for the instance of the time chem -
    [time]
    # For this one use the 'time' entry point from the 'time_chem' egg
    use = egg:time_chem#time
    # Any additional config required by this chem
    format = Year %Y month %m day %d
    
    [global]
    # A colon-separated list of directories wherein eggs containing chems are to be
    # found.
    plugin path = /home/me/mrpump-plugins
    # This is the same as the section name above.
    screen name = mygolem
    # Name of a file that Mr. Pump can write in. Gets no larger than 10k.
    cache = /tmp/already_seen
    # How many seconds between checking messages. Don't make Twitter angry.
    check every = 60
    # debug, info, error: minimum level of messages to display. Debug is quite
    # verbose.
    log level = info
    # Names of each section above that configures a chem.
    chems = ping, time
    

Terminology
-----------

<http://en.wikipedia.org/wiki/Golems_(Discworld)>


Making Mr. Pump do cool stuff
-----------------------------

Write a chem and put it in an egg. Then change your configuration to include
it, and restart Mr. Pump. Presto, your new functionality is ready!

In the examples directory there is a time chem. To make it work, go in that
directory, and run ``python setup.py bdist_egg``. Put the egg file
(``dist/*egg``) in a directory that's on the configured ``plugin path``. The
``[time]`` section in the example configuration above will load the time chem.
Now run ``emet``, and DM your bot, ``time``. 
