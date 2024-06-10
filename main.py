import bitcointx as btc


btc.select_chain_params("bitcoin/regtest")

from bitcointx.wallet import CCoinKey
from bitcointx.core import COutPoint, CTxIn, CTxOut, CMutableTransaction, CTxInWitness, b2x, lx, CTxWitness
from bitcointx.core.script import CScript, OP_ADD, OP_1, OP_2, OP_4, OP_5, OP_EQUAL, TaprootScriptTree, CScriptWitness
from bitcointx.wallet import P2TRCoinAddress, P2WPKHBitcoinRegtestAddress
from binascii import hexlify, unhexlify

# Importing custom scripts
from multisig_address_creation import create_multisig_script
from collatoral_deposit_verification import create_collateral_deposit_script
from loan_funding_verification import create_loan_funding_script
from repayment_handling import create_repayment_script

# Define the public keys for the multisig address creation
borrower_pubkey = bytes.fromhex('02a122107bfb02cd6f4b1c8eb417638716217e127f6d43938dfb79ebb1972d64')
lender_pubkey = bytes.fromhex('024b1b7944b23940767e4e79927c3f140c90d829fd766e2944fb178e0eb3ed17')
oracle_pubkey = bytes.fromhex('022e55b827e58d2ff8cf0d8b4b98ad85d76e3a72253490d84d6798043fb01f77')

# Create multisig address
multisig_script = create_multisig_script(borrower_pubkey, lender_pubkey, oracle_pubkey)

# bitcointx will build a tree of branches and leaves
script_a = CScript([OP_1, OP_ADD, OP_2, OP_EQUAL], name="a")
script_b = CScript([OP_2, OP_ADD, OP_4, OP_EQUAL], name="b")
script_c = CScript([OP_1, OP_ADD, OP_5, OP_EQUAL], name="c")

tree = TaprootScriptTree([script_a, script_b, script_c])

# Create a provably unspendable public key in order to
# make the coins spendable ONLY using the script path
internal_pubkey = CCoinKey.from_secret_bytes(unhexlify("50929b74c1a04954b78b4b6035e97a5e078a5a0f28ec96d547bfee9ace803ac0")).xonly_pub
tree.set_internal_pubkey(internal_pubkey)
addr = P2TRCoinAddress.from_script_tree(tree)
print("Send 0.01 BTC to the following address: {}".format(addr))
# prints: Send 0.01 BTC to the following address: bcrt1p6zvv97wg8j0hec7uhatuaqtqksj88wqk0xqq8q98fr9zt4ecy4hqwgv6k2

# Example transaction creation
outpoint = COutPoint(lx('02bf783d1dcf1b7a7c2cf7d2f1baf29e07b578b1b1e7ee5d0488d6c8e4eacb60'), 0)
txin = CTxIn(outpoint)
txout = CTxOut(1000000, multisig_script)
tx = CMutableTransaction([txin], [txout])

tx_hex = b2x(tx.serialize())
print("Transaction hex:", tx_hex)
