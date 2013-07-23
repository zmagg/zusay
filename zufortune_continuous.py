import os
import sys

import humbug

client = humbug.Client()

client.call_on_each_message(lambda msg: open("fortunetext", "a")
                .write(msg[u'content'].encode('utf-8') + "\n%"))

os.system("strfile fortunetext fortunetext.dat")
