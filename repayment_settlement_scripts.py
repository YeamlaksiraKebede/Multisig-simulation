# repayment_settlement_scripts.py
from hashlib import sha256
from bit import Key, PrivateKeyTestnet

# Load keys
with open('keys.txt', 'r') as f:
    keys = f.read().splitlines()

borrower_key = PrivateKeyTestnet(keys[0].split(': ')[1])
lender_key = PrivateKeyTestnet(keys[1].split(': ')[1])
oracle_key = PrivateKeyTestnet(keys[2].split(': ')[1])
borrower_pubkey = keys[3].split(': ')[1]
lender_pubkey = keys[4].split(': ')[1]
oracle_pubkey = keys[5].split(': ')[1]

# Helper function to sign messages
def sign_message(key, message):
    message_bytes = message.encode('utf-8')
    return key.sign(message_bytes).hex()

# Repayment Handling Script
preimage = "secret"
expected_hash = sha256(preimage.encode()).hexdigest()
repayment_due_date = 1700000000  # Example timestamp for lock time
repayment_script = f"""
{sign_message(borrower_key, 'repayment message')} {borrower_pubkey} {preimage}
OP_IF
    OP_SHA256
    {expected_hash} OP_EQUALVERIFY
    {borrower_pubkey} OP_CHECKSIG
OP_ELSE
    {repayment_due_date} OP_CHECKLOCKTIMEVERIFY OP_DROP
    {borrower_pubkey} OP_CHECKSIG
OP_ENDIF
"""
print(f"Repayment Script: {repayment_script}")

# Contract Settlement Script
contract_settlement_script = f"""
OP_IF
    {sign_message(borrower_key, 'settlement message')} {sign_message(oracle_key, 'settlement message')} 2 {borrower_pubkey} {oracle_pubkey} OP_CHECKSIGADD OP_CHECKSIGADD 2 OP_NUMEQUAL
OP_ELSE
    {sign_message(lender_key, 'settlement message')} {sign_message(oracle_key, 'settlement message')} 2 {lender_pubkey} {oracle_pubkey} OP_CHECKSIGADD OP_CHECKSIGADD 2 OP_NUMEQUAL
OP_ENDIF
"""
print(f"Contract Settlement Script: {contract_settlement_script}")
