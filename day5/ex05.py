'''Assignment 5: Stateful Ledger Scope Machine (LEGB Scopes & Closures)
Scenario
You are developing a stateful balance ledger tracker that tracks account state history. 
To satisfy strict architecture requirements, you must manage this state without defining 
any classes (class keyword is prohibited). Instead, you must use closures, nested functions, 
and Python scoping variables.'''


AUDIT_TRANSACTION_COUNT = 0
def create_bank_account(owner_name, initial_balance):
    balance=float(initial_balance)
    history_list=[f"Account created with {initial_balance}"]
    
    
    def deposit(amount):       
        global AUDIT_TRANSACTION_COUNT
        nonlocal balance
        balance+=amount
        history_list.append(f"deposit {amount}")
        AUDIT_TRANSACTION_COUNT+=1
    
    def withdraw(amount):
        global AUDIT_TRANSACTION_COUNT
        nonlocal balance
    
        if balance>=amount:
                balance-=amount
                history_list.append(f"withdraw {amount}")
                AUDIT_TRANSACTION_COUNT+=1
        else:
            raise ValueError("Insufficient Balance")

    def get_statement():
        return(owner_name, balance, history_list.copy())

    return {
    "deposit": deposit,
    "withdraw": withdraw,
    "get_statement": get_statement
}

def main():   
    acc = create_bank_account("Arham", 1000.0)
    acc["deposit"](500)
    acc["withdraw"](200)
    print("Statement:", acc["get_statement"]())
    print("Final Audit Count:", AUDIT_TRANSACTION_COUNT)
main()