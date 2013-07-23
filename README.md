Toy project that to create fortune files from <a href="http://www.zulip.com/">Zulip</a> messages. 

Files included:
* zufortune.py dumps the latest zulip messages into a file to formatted to be used with the UNIX command fortune. It then updates the fortune binary in the same script. Can be used wonderfully in combination with a cron job to grab the newest ~350 messages every N minutes.
* zufortune\_continuous.py uses the polling Humbug client to get all next messages and dump them to the fortune file. It then updates the fortune binary in the same script.
* cowputer.cow is the Hacker School logo as ascii art to be passed into cowsay.

<a href="http://www.zulip.com/">Zulip</a> (formerly known as Humbug) is a chatroom used at Hacker School (and other places). Zusay uses the Zulip API to dump messages from Zulip into a correctly formmated fortune file for usage with the Unix fortune command for fun and profit. 

Example usage:

Download and setup the <a href="https://zulip.com/api/">Zulip API bindings</a>.

Download fortune and cowsay. (available on brew for OSX, and apt-get for Debian\*)

Set up your ~/.humbugrc as described above or pass in your API key manually to the program. 

Run zufortune.py.

Run

fortune -s fortunetext | cowsay

and giggle. 

Optional usage:

cp cowputer.cow to wherever your cow files are located.
On OSX & brew, mine were located at /usr/local/Cellar/cowsay/3.03/share/cows


/ Ha that was very informative, thank \

\ you.                                /

 ------------------------------------- 

 \      :::::::::::::

  \     ::         ::

        :: Made at ::

        ::         ::

        :::::::::::::

             ::

        Hacker School

        :::::::::::::


(this was a real fortune generated!!)
