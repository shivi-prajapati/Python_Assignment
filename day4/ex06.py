'''Assignment 6: Atomic Transaction processing with Log Rollback
Scenario
A bank updates user balances in a database dictionary based on transaction files. 
To ensure accounting consistency, if any single transaction in a batch contains an 
error (such as a negative transfer amount, an unrecognized account number, 
or an overdraft), the entire batch must fail, all accounts must be restored to their 
initial states, and a rollback action must be logged to a text file.'''
import copy
class AccountNotFoundError(Exception):
    pass
class OverdraftError(Exception):
    pass
class InvalidTransactionError(Exception):
    pass

def process_transaction_batch(accounts, batch_list, log_path):
    accounts1=copy.deepcopy(accounts)
    for b in batch_list:
        acc_name=b["acc"]
        if acc_name not in accounts:
            raise AccountNotFoundError(f"Account {acc_name} not found.")
        
        type_name=b["type"]
        if type_name=="withdraw" or type_name=="deposit":
            ...           
        else:
            raise InvalidTransactionError(f"Invalid transaction type {type_name}.")
        amount=b["amt"]
        if amount<=0:
            raise InvalidTransactionError("Transaction amount must be positive.")
           
        balance=accounts1[acc_name]
        if type_name=="withdraw" and balance<amount:
            raise OverdraftError(f"Insufficient funds. Account {acc_name} has balance {balance}, requested {amount}.")
        elif type_name=="withdraw" and balance>=amount:
            accounts1[acc_name]-=amount
        elif type_name=="deposit":
                accounts1[acc_name]+=amount
    accounts.clear() 
    accounts.update(accounts1) 
    print("Batch successful:", accounts)


def main():
    accounts = {"ACC01": 100.0, "ACC02": 50.0}
    log_file = "transactions.log"
    batch_1 = [{"acc": "ACC01", "type": "withdraw", "amt": 30.0},
    {"acc": "ACC02", "type": "deposit", "amt": 20.0}]
    print("*********Batch 1 Started***********")
    try:
        process_transaction_batch(accounts, batch_1, log_file)
    except AccountNotFoundError as e:
        print(e)
    except InvalidTransactionError as e:
            print(e)
    except OverdraftError as e:
            print(e)
    print("**********Batch 2 Started**********")
    batch_2 = [
    {"acc": "ACC01", "type": "deposit", "amt": 50.0},
    {"acc": "ACC02", "type": "withdraw", "amt": 200.0} ]
    try:
        process_transaction_batch(accounts, batch_2, log_file)
    except OverdraftError as e:
        print(f"Caught: {e}")
main()