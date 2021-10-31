"""
Scenario: 
- We have a valid, DKIM-signed email from DHL. We wanted to see if we can spoof DHL's identity by:
    - Attempt to modify the content that will be rendered on the email client.
    - Avoid invalidating the original DKIM signature.

Findings: 
- Same as dhl emails, this email can't get past the spf check.

Author: Allen Chen
"""
import utils
from email_templates import dr_tampered_template


# For security purposes, security-sensitive stuff like username and password used in the experiment 
# have been hidden in the .env files. Email allenchen@gatech.edu for access/assistance. 
env = utils.Environment("envs/yahoo_to_gmail.env")
env.send(dr_tampered_template)