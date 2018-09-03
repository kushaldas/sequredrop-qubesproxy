from sdqubes import (
    login,
    get_all_sources,
    get_source,
    delete_source,
    get_submissions,
    add_star,
    get_submission,
    flag_source,
    get_current_user
)
from sdqubes import get_all_submissions, delete_submission
from pprint import pprint
import pyotp
import json

t = pyotp.TOTP("JHCOGO7VCER3EJ4L")
token = login(
    "journalist", "correct horse battery staple profanity oil chewy", str(t.now())
)

print(token)

# token = '{"expiration": "2018-09-03T21:45:21.458861Z", "token": "eyJhbGciOiJIUzI1NiIsImV4cCI6MTUzNjAxMTEyMSwiaWF0IjoxNTM1OTgyMzIxfQ.eyJpZCI6MX0.X9U-WuN0PGAD9BLI09c48WfSBEqtg2gyfS4hYjyO_Mw"}'

sources = get_all_sources(token)
print("Length is {}".format(len(sources)))
# pprint(sources)

s = sources[0]

pprint(flag_source(token, s.uuid))
# pprint(add_star(token, s.uuid))
# pprint(get_source(token, s.uuid))

# print("deleting source")
# pprint(delete_source(token, sources[0].uuid))


sources = get_all_sources(token)
#submissions = get_submissions(token, sources[0].uuid)
# pprint(submissions)

# s2 = get_submission(token, submissions[0].uuid, sources[0].uuid)

# pprint((s2.uuid, submissions[0].uuid))

# pprint(delete_submission(token, submissions[0].uuid, s.uuid))
# sss = get_all_submissions(token)
# pprint(sss)
pprint(get_current_user(token))
