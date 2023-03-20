import pytest
from pay.order import LineItem, Order
from pay.payment import pay_order
from pay.processor import PaymentProcessor
from pytest import MonkeyPatch


# use Mock data for inputs - use MonkeyPatch to mock inputs
def test_pay_order(monkeypatch: MonkeyPatch):
    inputs = ["1249190007575069", "12", "2024"]

    def charge_mock(
        self: PaymentProcessor, card: str, month: int, year: int, amount: int
    ) -> None:
        pass

    monkeypatch.setattr(
        "builtins.input", lambda _: inputs.pop(0)
    )  # replace fns in module with something else -> override built in reading system, replace with lambda fn -> return inputs and pop first element at a time

    monkeypatch.setattr(
        PaymentProcessor, "_check_api_key", lambda _: True
    )  # payment processor communicate with server, dont want that.  check_api_method always returns true here

    monkeypatch.setattr(
        PaymentProcessor, "charge", charge_mock
    )  # charge method replace by charge_mock

    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    pay_order(order)  # not charge credit card so mock paymentprocessor


def test_pay_order_invalid(monkeypatch: MonkeyPatch):
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", "12", "2024"]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
        order = Order()
        pay_order(order)
