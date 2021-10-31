"""
Scenario: 
- We have a valid, DKIM-signed email from DHL. We wanted to see if we can spoof DHL's identity by:
    - Attempt to modify the content that will be rendered on the email client.
    - Avoid invalidating the original DKIM signature.

Findings: 
- Yahoo prevents this email from going out due to SPF policy. The address we are sending from (outlook) does
    not match the one in the FROM field, which is DHL. This works similarly to Outlook.

Author: Allen Chen
"""
import utils
from email_templates import original_dhl_email


# For security purposes, security-sensitive stuff like username and password used in the experiment 
# have been hidden in the .env files. Email allenchen@gatech.edu for access/assistance. 
env = utils.Environment("envs/yahoo_to_gmail.env")
env.send(original_dhl_email)