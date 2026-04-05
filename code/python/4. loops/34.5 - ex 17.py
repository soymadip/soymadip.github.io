"""
ATM Withdrawal Simulator

Imagine you’re building a backend feature for an ATM. Customers can request multiple withdrawals during one session. Your task is to simulate how the system should handle each request based on the account balance.
Tasks:

    Use a while loop to iterate through the list named withdrawals. withdrawal is the list of request withdraws.
    For every withdrawal:

        ✅ If the current balance is enough:
        Subtract the amount.
        Append a success message: "Withdrawn: {amount}"
        ❌ If not enough:
        Append a message: "Insufficient funds for requested amount: {amount}"

    After all withdrawals:
        Append the final balance as: "Remaining Balance: balance"

    Return a list containing all the messages.
"""


# This function will be tested automatically.
# Do not change the function name or parameters.
def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    # Write your code below this line
    result = []
    index = 0

    while index < len(withdrawals):
        amount = withdrawals[index]
        if amount <= balance:
            balance -= amount
            result.append(f"Withdrawn: {amount}")
        else:
            result.append(f"Insufficient funds for requested amount: {amount}")
        index += 1
    result.append(f"Remaining Balance: {balance}")
    return result
