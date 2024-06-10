from bitcointx.core.script import CScript, OP_CHECKSIGADD, OP_NUMEQUAL

def create_multisig_script(borrower_pubkey, lender_pubkey, oracle_pubkey):
    script = CScript([borrower_pubkey, lender_pubkey, oracle_pubkey, OP_CHECKSIGADD, OP_CHECKSIGADD, 2, OP_NUMEQUAL])
    return script

if __name__ == "__main__":
    borrower_pubkey = bytes.fromhex('02a122107bfb02cd6f4b1c8eb417638716217e127f6d43938dfb79ebb1972d64')
    lender_pubkey = bytes.fromhex('024b1b7944b23940767e4e79927c3f140c90d829fd766e2944fb178e0eb3ed17')
    oracle_pubkey = bytes.fromhex('022e55b827e58d2ff8cf0d8b4b98ad85d76e3a72253490d84d6798043fb01f77')

    multisig_script = create_multisig_script(borrower_pubkey, lender_pubkey, oracle_pubkey)
    print("Multisig script:", multisig_script.hex())
