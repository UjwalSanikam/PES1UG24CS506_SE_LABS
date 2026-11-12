import re


def _parse_amount(value):
    """Parse a non-negative integer written with ASCII digits."""
    if not value.isascii() or not value.isdecimal():
        return None
    try:
        return int(value)
    except ValueError:
        # Python can limit the length of decimal strings accepted by int().
        return None


def notes_needed(amount):
    """Return the number of full 100-unit notes, or None for invalid input."""
    if not isinstance(amount, str):
        return None
    amount = amount.strip()
    if "," in amount and not re.fullmatch(r"[0-9]{1,3}(,[0-9]{3})+", amount):
        return None
    value = _parse_amount(amount.replace(",", ""))
    return None if value is None else value // 100


def mask_card(card_number):
    """Mask the first three groups of a valid four-group card number."""
    if not isinstance(card_number, str):
        return None
    groups = card_number.split()
    if len(groups) != 4 or any(
        not re.fullmatch(r"[0-9]{4}", group) for group in groups
    ):
        return None
    return "XXXX XXXX XXXX " + groups[-1]


def average_withdrawal(amounts_csv):
    """Return the rounded-down mean of comma-separated whole amounts."""
    if not isinstance(amounts_csv, str):
        return None
    total = 0
    fields = amounts_csv.split(",")
    for field in fields:
        value = _parse_amount(field.strip())
        if value is None:
            return None
        total += value
    return total // len(fields)


def main():
    print("==== Running notes_needed ====")
    user_input = input("Enter an amount (e.g. 2,500): ")
    result = notes_needed(user_input)
    print("Number of 100 Notes:", "Invalid amount" if result is None else result)

    print("\n==== Running mask_card ====")
    user_input = input("Enter a card number (e.g. 1234 5678 9012 3456): ")
    result = mask_card(user_input)
    print("Masked Card:", "Invalid card number" if result is None else result)

    print("\n==== Running average_withdrawal ====")
    user_input = input("Enter withdrawals as CSV (e.g. 500,1000,2000): ")
    result = average_withdrawal(user_input)
    print("Average Withdrawal:", "Invalid withdrawal list" if result is None else result)


if __name__ == "__main__":
    main()
