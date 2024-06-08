# key_generation.py
from bit import PrivateKeyTestnet

# Generate private keys for borrower, lender, and oracle
borrower_key = PrivateKeyTestnet()
lender_key = PrivateKeyTestnet()
oracle_key = PrivateKeyTestnet()

# Public keys
borrower_pubkey = borrower_key.public_key.hex()
lender_pubkey = lender_key.public_key.hex()
oracle_pubkey = oracle_key.public_key.hex()

# Save keys to a file (optional)
with open('keys.txt', 'w') as f:
    f.write(f"Borrower Private Key: {borrower_key.to_wif()}\n")
    f.write(f"Lender Private Key: {lender_key.to_wif()}\n")
    f.write(f"Oracle Private Key: {oracle_key.to_wif()}\n")
    f.write(f"Borrower Public Key: {borrower_pubkey}\n")
    f.write(f"Lender Public Key: {lender_pubkey}\n")
    f.write(f"Oracle Public Key: {oracle_pubkey}\n")

print(f"Borrower Public Key: {borrower_pubkey}")
print(f"Lender Public Key: {lender_pubkey}")
print(f"Oracle Public Key: {oracle_pubkey}")
