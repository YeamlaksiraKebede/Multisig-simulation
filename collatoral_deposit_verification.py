from bitcointx.core.script import CScript, OP_CHECKSIG, OP_SWAP

def create_collateral_deposit_script(borrower_sig, lender_sig, oracle_pubkey):
    script = CScript([borrower_sig, lender_sig, oracle_pubkey, OP_CHECKSIG, OP_SWAP, OP_CHECKSIG])
    return script

if __name__ == "__main__":
    borrower_sig = bytes.fromhex('30440220568ccf55b7eb27498d91081a4a2a54dc51ad5b022039862918e22889b34f129044598482d5403d670b404f58')
    lender_sig = bytes.fromhex('3045022100ebb75177dff45018d726bcfbcba370a86ab3978639243e8bdb12692702205d60b97be588edd53ee052d1d09c895eb4e12f0f26')
    oracle_pubkey = bytes.fromhex('022e55b827e58d2ff8cf0d8b4b98ad85d76e3a72253490d84d6798043fb01f77')

    collateral_script = create_collateral_deposit_script(borrower_sig, lender_sig, oracle_pubkey)
    print("Collateral deposit script:", collateral_script.hex())

