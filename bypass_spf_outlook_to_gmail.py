"""
Scenario: 
- We have a valid, DKIM-signed email from DHL. We wanted to see if we can spoof DHL's identity by:
    - Attempt to modify the content that will be rendered on the email client.
    - Avoid invalidating the original DKIM signature.
- We have made modifications to the email: we have added an additional FROM field that complies with the SPF record. However,
    presumably this should invalidates DKIM, or invalidates RFC 5322. 

Findings: 
- Email was rejected immediately at send-time as it cannot get pass the SPF check still, probably because of compliance to RFC 5322.

Author: Allen Chen
"""
import utils
from email_templates import tampered_dhl_email_bypass_spf


# For security purposes, security-sensitive stuff like username and password used in the experiment 
# have been hidden in the .env files. Email allenchen@gatech.edu for access/assistance. 
env = utils.Environment("envs/yahoo_to_gmail.env")
env.send(tampered_dhl_email_bypass_spf)