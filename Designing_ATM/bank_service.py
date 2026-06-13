
class BankService:

    def __init__(self):
        self.accounts: Dict[int, Account] = {}
        self.cards: Dict[int, Card] = {}
        self.card_to_account_map: Dict[Card, Account] = {}

    def create_account(self, account_number: int, initial_balance: float) -> None:
        account = Account(account_number, initial_balance)
        self.accounts[account_number] = account
        return account

    def create_card(self, card_number: int, pin: int) -> None:
        card = Card(card_number, pin)
        self.cards[card_number] = card
        return card

    def add_card_to_account(self, card: Card, account: Account) -> None:    
        self.card_to_account_map[card] = account
        account.add_card(card.get_card_number(), card)
        
    def autheticate(self, card: Card, pin: int) -> bool:
        return card is not None and card.get_pin() == pin

    def get_balance(self, card: Card) -> float:
        account = self.card_to_account_map[card]
        return account.get_balance() if account is else 0.0

    def deposit(self, card: Card, amount: float) -> None:
        account = self.card_to_account_map[card]
        account.deposit(amount) if account is not None else raise ValueError("Account not found")

    def withdraw(self, card: Card, amount: float) -> None:
        account = self.card_to_account_map[card]
        account.withdraw(amount) if account is not None else raise ValueError("Account not found")

    def get_card(self, card_number: int) -> Card:
        return self.cards[card_number]