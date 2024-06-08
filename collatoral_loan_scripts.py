from hashlib import sha256
from bit import Key, PrivateKeyTestnet

# Load keys
with open('keys.txt', 'r') as f:
    keys = f.read().splitlines()

borrower_key = PrivateKeyTestnet(keys[0].split(': ')[1])
lender_key = PrivateKeyTestnet(keys[1].split(': ')[1])
oracle_pubkey = keys[5].split(': ')[1]
lender_pubkey = keys[4].split(': ')[1]

# Helper function to sign messages
def sign_message(key, message):
    message_bytes = message.encode('utf-8')
    return key.sign(message_bytes).hex()

# Collateral Deposit Verification Script
borrower_sig = sign_message(borrower_key, 'message')
lender_sig = sign_message(lender_key, 'message')
collateral_script = f"{borrower_sig} {lender_sig} {oracle_pubkey} OP_CHECKSIG OP_SWAP OP_CHECKSIG"
print(f"Collateral Script: {collateral_script}")

# Loan Funding Verification Script
lender_signature = sign_message(lender_key, 'loan message')
loan_funding_script = f"{lender_signature} {lender_pubkey} OP_CHECKSIG"
print(f"Loan Funding Script: {loan_funding_script}")


