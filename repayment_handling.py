from bitcointx.core.script import CScript, OP_IF, OP_ELSE, OP_ENDIF, OP_SHA256, OP_EQUALVERIFY, OP_CHECKLOCKTIMEVERIFY, OP_DROP, OP_CHECKSIG

def create_repayment_script(borrower_signature, borrower_pubkey, preimage, expected_hash, repayment_due_date):
    script = CScript([
        borrower_signature, borrower_pubkey, preimage,
        OP_IF,
            OP_SHA256, expected_hash, OP_EQUALVERIFY, borrower_pubkey, OP_CHECKSIG,
        OP_ELSE,
            repayment_due_date, OP_CHECKLOCKTIMEVERIFY, OP_DROP, borrower_pubkey, OP_CHECKSIG,
        OP_ENDIF
    ])
    return script

if __name__ == "__main__":
    borrower_signature = bytes.fromhex('3045022100f06e67fb7e9e51d9fc198d822b5ab167474df824d0cc0c1823eb48b502206b7720cf999fdc55d45128226e8f02d36ed5b523e9')
    borrower_pubkey = bytes.fromhex('02a122107bfb02cd6f4b1c8eb417638716217e127f6d43938dfb79ebb1972d64')
    preimage = bytes.fromhex('...')  # Replace with actual preimage
    expected_hash = bytes.fromhex('...')  # Replace with actual hash
    repayment_due_date = 1625097600  # Replace with actual lock time

    repayment_script = create_repayment_script(borrower_signature, borrower_pubkey, preimage, expected_hash, repayment_due_date)
    print("Repayment script:", repayment_script.hex())
