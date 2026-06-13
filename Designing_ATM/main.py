

def main():

    atm = ATMSystem.get_instance()
    bank_service = atm.get_bank_service()

    account = bank_service.create_account("1234567890", "1234", 1000)
    card = bank_service.create_card(account)

    bank_service.link_card_to_account(card, account)

    print("== ATM System == ")
    atm.insert_card(card)   
    atm.enter_pin(1234)
    atm.select_operation(OperationType.CHECK_BALANCE)
    atm.select_operation(OperationType.WITHDRAW_CASH, 100)
    atm.select_operation(OperationType.DEPOSIT_CASH, 50)
    atm.select_operation(OperationType.CHECK_BALANCE)

    atm.eject_card()

    print(f"Total transactions: {atm.get_transaction_count()}")


if __name__ == "__main__":
    main()

