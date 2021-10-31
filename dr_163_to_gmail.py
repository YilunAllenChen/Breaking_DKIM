"""
Scenario: 
- We have a valid, DKIM-signed email from a less-securely-configured domain (our own). We wanted to see if we can spoof this domain's identity by:
    - Attempt to modify the content that will be rendered on the email client.
    - Avoid invalidating the original DKIM signature.

Findings: 
- Modified email was delivered successfully and all of the DKIM signatures remain valid. However, the email appears to be coming from "allen@darwinrobotics.org via 163.com".
    The via part really gives away our disguise. Also, the email appears to be sent and signed by 163.com. Further experiments is needed to figure out whether we can get rid
    of the via part, and make the email appear as signed by darwinrobotics.org.
    
Author: Allen Chen
"""
import utils
from email_templates import dr_tampered_template


# For security purposes, security-sensitive stuff like username and password used in the experiment 
# have been hidden in the .env files. Email allenchen@gatech.edu for access/assistance. 
env = utils.Environment("envs/163_to_gmail.env")
env.send(dr_tampered_template)  