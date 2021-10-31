"""
Scenario: 
- We have a valid, DKIM-signed email from DHL. We wanted to see if we can spoof DHL's identity by:
    - Attempt to modify the content that will be rendered on the email client.
    - Avoid invalidating the original DKIM signature.

Findings: 
- Different from Outlook and Yahoo, 163 actually accepts the email and attempted to deliver it. However, Google
    on the receiver side recognizes the spoof and rejected the email.

Author: Allen Chen
"""
import utils
from email_templates import original_dhl_email


# For security purposes, security-sensitive stuff like username and password used in the experiment 
# have been hidden in the .env files. Email allenchen@gatech.edu for access/assistance. 
env = utils.Environment("envs/163_to_gmail.env")
env.send(original_dhl_email)