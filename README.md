# Multisig-simulation
Collateral Loan Scripts
This repository contains Python scripts for managing collateralized loans using Bitcoin's scripting capabilities. The scripts are designed to handle various aspects of collateralized lending, including multisig address creation, collateral deposit verification, loan funding verification, repayment handling, and contract settlement.

Features

-Multisig address creation

-Collateral deposit verification

-Loan funding verification

-Repayment handling with time lock enforcement

-Contract settlement based on repayment status


Requirements

1) Python 3.x

2) bit library (for Bitcoin scripting)

3) bitcoinlib library (for Bitcoin-related utilities)

Run the scripts individually:

- multisig_script.py: Generates a multisig address for collateral handling.

- collateral_script.py: Verifies the borrower's collateral deposit.

- loan_funding_script.py: Ensures the lender sends the loan amount to the borrower.

- repayment_script.py: Handles borrower repayments and enforces a time lock for late payments.

- contract_settlement_script.py: Handles the release or claim of the collateral based on repayment status.
