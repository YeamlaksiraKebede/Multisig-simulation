from bitcointx.core.script import CScript, OP_CHECKSIG

def create_loan_funding_script(lender_signature, lender_pubkey):
    script = CScript([lender_signature, lender_pubkey, OP_CHECKSIG])
    return script

if __name__ == "__main__":
    lender_signature = bytes.fromhex('304402202b0d177b5171a462f09247cfe08a5851426f4af080069206951391602201c454a2950704a1d622e21e4cb307db428909fb3bc01')
    lender_pubkey = bytes.fromhex('024b1b7944b23940767e4e79927c3f140c90d829fd766e2944fb178e0eb3ed17')

    loan_funding_script = create_loan_funding_script(lender_signature, lender_pubkey)
    print("Loan funding script:", loan_funding_script.hex())
