class Account:
    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self.transactions: list[int] = []

    @property
    def balance(self) -> int:
        return self.amount + sum(self.transactions)

    def handle_transaction(self, transaction_amount: int):
        if self.balance + transaction_amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self.transactions.append(transaction_amount)
        return f"New balance: {self.balance}"

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        return self.handle_transaction(amount)

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self.transactions)

    def __getitem__(self, index):
        return self.transactions[index]

    def __reversed__(self):
        return reversed(self.transactions)

    def __gt__(self, other: 'Account'):
        return self.balance >= other.balance

    def __ge__(self, other: 'Account'):
        return self.balance >= other.balance

    def __eq__(self, other: 'Account'):
        return self.balance == other.balance

    def __add__(self, other: 'Account'):
        new_owner = f"Account({self.owner}&{other.owner})"
        new_amount = self.amount + other.amount
        new_account = Account(new_owner, new_amount)
        new_account._transactions = self.transactions + other._transactions
        return new_account