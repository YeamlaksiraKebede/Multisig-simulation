# multisig_script_creation.py
with open('keys.txt', 'r') as f:
    keys = f.read().splitlines()

borrower_pubkey = keys[3].split(': ')[1]
lender_pubkey = keys[4].split(': ')[1]
oracle_pubkey = keys[5].split(': ')[1]

# Create multisig address
multisig_script = f"{borrower_pubkey} {lender_pubkey} {oracle_pubkey} OP_CHECKSIGADD OP_CHECKSIGADD 2 OP_NUMEQUAL"
print(f"Multisig Script: {multisig_script}")
