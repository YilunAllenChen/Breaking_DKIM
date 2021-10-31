"""
Scenario: 
- We have a valid, DKIM-signed email from DHL. We wanted to see if we can spoof DHL's identity by:
    - Attempt to modify the content that will be rendered on the email client.
    - Avoid invalidating the original DKIM signature.

Findings: 
- Google has implemented a mechanism to wrap the original email and append numerous Google-unique attributes 
    like X-Gm-Message-State, X-Google-Smtp-Source and X-Google-DKIM-Signature. All of the original senders' 
    information is also wrapped. For example, if you claim to be DHL in the "from" field, even if the <>-enclosed
    email is from DHL, Google will modify it to be from the gmail address that you are sending this from. That means,
    if you are sending an email from spoofer@gmail.com and claiming in the email that you are DHL Support from 
    DHLSupport@dhl.com, what appears on the receiver's client will be DHL Support <spoofer@gmail.com>. This 
    trivializes the attack scheme because victim can easily tell where the email came from.

Author: Allen Chen
"""
import utils
from email_templates import original_dhl_email


# For security purposes, security-sensitive stuff like username and password used in the experiment 
# have been hidden in the .env files. Email allenchen@gatech.edu for access/assistance. 
env = utils.Environment("envs/gmail_to_gmail.env")
env.send(original_dhl_email)