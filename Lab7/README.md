# Lab 7 · ATM Withdrawal Fuzz Testing

From this directory, install the test dependencies and run the application
and its property tests:

```sh
python -m pip install -r requirements.txt
python atm_withdrawal.py
python -m pytest test_atm_withdrawal.py
```

The application accepts non-negative whole amounts, card numbers with four
four-digit groups, and comma-separated lists of whole amounts. The three
functions return `None` on invalid input and the CLI shows an error message
for the relevant prompt. Note counts and averages use integer division.

The [lab report](Lab7_Fuzz_Testing_Report.pdf) records the application runs
and the pytest results before and after validation was added. The starter
files came from the assigned
[Lab 7 directory](https://github.com/SETAPESU26/L6_L7_18_atm_withdrawal/tree/3211240985b5070a8838544fcad13e5990c524d2/Lab%207).
