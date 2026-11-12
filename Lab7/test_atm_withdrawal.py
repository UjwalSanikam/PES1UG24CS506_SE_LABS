from hypothesis import given, strategies as st

from atm_withdrawal import average_withdrawal, mask_card, notes_needed

arbitrary_input = st.text() | st.none() | st.integers() | st.binary()
whole_amounts = st.integers(min_value=0, max_value=10**18)
card_groups = st.text(alphabet="0123456789", min_size=4, max_size=4)


@given(arbitrary_input)
def test_notes_needed_no_crash(value):
    result = notes_needed(value)
    assert result is None or type(result) is int and result >= 0


@given(arbitrary_input)
def test_mask_card_no_crash(value):
    result = mask_card(value)
    if result is not None:
        assert isinstance(value, str)
        groups = value.split()
        assert len(groups) == 4
        assert all(len(group) == 4 and group.isascii() and group.isdigit()
                   for group in groups)
        assert result == "XXXX XXXX XXXX " + groups[-1]


@given(arbitrary_input)
def test_average_withdrawal_no_crash(value):
    result = average_withdrawal(value)
    assert result is None or type(result) is int and result >= 0


@given(whole_amounts, st.booleans())
def test_notes_needed_counts_full_notes(amount, grouped):
    formatted = f"{amount:,}" if grouped else str(amount)
    assert notes_needed(f" {formatted} ") == amount // 100


@given(st.tuples(card_groups, card_groups, card_groups, card_groups))
def test_mask_card_preserves_only_last_group(groups):
    assert mask_card("  ".join(groups)) == f"XXXX XXXX XXXX {groups[-1]}"


@given(st.lists(whole_amounts, min_size=1, max_size=20))
def test_average_withdrawal_rounds_down(amounts):
    assert average_withdrawal(", ".join(map(str, amounts))) == sum(amounts) // len(amounts)


@given(whole_amounts)
def test_malformed_withdrawal_fields_are_rejected(amount):
    assert notes_needed(f"{amount},") is None
    assert notes_needed(f"-{amount}") is None
    assert average_withdrawal(f"{amount},") is None
    assert average_withdrawal(f"{amount},-{amount}") is None


@given(st.lists(card_groups, min_size=5, max_size=8))
def test_mask_card_rejects_extra_groups(groups):
    assert mask_card(" ".join(groups)) is None
