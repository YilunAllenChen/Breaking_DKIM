"""
Scenario: 
- We have a valid, DKIM-signed email from DHL. We wanted to see if we can spoof DHL's identity by:
    - Attempt to modify the content that will be rendered on the email client.
    - Avoid invalidating the original DKIM signature.
- We have made modifications to the email: we have added additional Subject, From, Body and such, 
    in the hope that we can make the email appear to be coming from elsewhere while retaining the
    validity of DKIM.

Findings: 
- Email was rejected immediately at send-time as it was marked as spam. This happens on 163 side.

Author: Allen Chen
"""
import utils
from email_templates import tampered_dhl_email


# For security purposes, security-sensitive stuff like username and password used in the experiment 
# have been hidden in the .env files. Email allenchen@gatech.edu for access/assistance. 
env = utils.Environment("envs/163_to_gmail.env")
env.send(tampered_dhl_email)