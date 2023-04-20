import pytest
from account import *

class Test:
    def setup_method(self):
        self.a1 = Account('James')
        self.a2 = Account('Maria')


    def teardown_method(self):
        del self.a1
        del self.a2


    def test_init(self):
        assert self.a1.get_name() == 'James'
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == 'Maria'
        assert self.a2.get_balance() == 0


    def test_deposit(self):
        assert self.a1.deposit(10) is True
        assert self.a1.get_balance() == pytest.approx(10, abs=0.001)
        assert self.a1.deposit(0.5) is True
        assert self.a1.get_balance() == pytest.approx(10.5, abs=0.001)
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == pytest.approx(10.5, abs=0.001)
        assert self.a1.deposit(-10) is False
        assert self.a1.get_balance() == pytest.approx(10.5, abs=0.001)


    def test_withdraw(self):
        assert self.a2.withdraw(30) is False
        self.a2.deposit(20.00)
        assert self.a2.withdraw(10) is True
        assert self.a2.get_balance() == pytest.approx(10, abs=0.001)
        assert self.a2.withdraw(.5) is True
        assert self.a2.get_balance() == pytest.approx(9.5, abs=0.001)
        assert self.a2.withdraw(0) is False
        assert self.a2.get_balance() == pytest.approx(9.5, abs=0.001)
        assert self.a2.withdraw(-10) is False
        assert self.a2.get_balance() == pytest.approx(9.5, abs=0.001)

