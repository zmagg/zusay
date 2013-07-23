"""
zufortune.py is a short script that dumps the maximum possible Zulip messages, as allowed by the Zulip API, into a local file in the format expected for files as inputs to the Unix fortune command.
It also ensures that there are no message duplicates in the file from previous runs. It then updates the generated fortune binary file.
"""
import os
import sys

import humbug

client = humbug.Client()

id_msg  = client.get_messages({"last" : 0})

#hack to get max ID read supported by humbug
message_id = int(id_msg['msg'].split("Minimum valid is")[1]
                .split("!")[0].split()[0])

try:
    last_run_id_msg = open(".last_run", "r").readline()
except IOError:
    last_run_id_msg = 0

# use last run if later than greatest read supported.
if int(last_run_id_msg) > message_id:
    message_id = int(last_run_id_msg)

messages = client.get_messages({"last" : message_id})

message_string = ""
msg_contents = messages.values()[1])
for msg in msg_contents:
    message_string += msg['content'].encode('utf-8') + "\n%\n"

# write fortune file and update .dat file
open ("fortunetext", "a").write(message_string)
os.system("strfile fortunetext fortunetext.dat")

# update last_run
open(".last_run", "w").write(str(msg_contents.pop()['id']))
