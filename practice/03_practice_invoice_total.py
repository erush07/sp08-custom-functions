'''
OPTIONAL AI GUIDANCE PROMPT:
----------------------------
I am a student in an introductory Python class. I am learning many coding
principles for the very first time. I am going to paste in the instructions to
a practice problem that my professor gave me to try before class. Please be my
kind tutor and walk me through how to solve the problem step by step.

Don't just give me the full solution all at once (unless I later ask for it).
Instead, help me work through it gradually, with clear explanations and small,
easy-to-understand examples. Please use everyday language and explain things
in a simple, friendly way.


INSTRUCTIONS:
-------------
Write a function calculate_total(price, quantity) that returns the product
of price and quantity.
1. Prompt the user or hard-code a price of 12.0 and quantity of 3.
2. Call calculate_total() and store the return value.
3. Print: You owe $36.0 for 3 widgets at $12.0 each.
'''

def calculate_total(price, quantity):
    price = float(input("What is the price of the item? "))
    quantity = float(input("What is the quantiy you are purchaseing of the item? "))
    total = price * quantity
    print(f"You owe {total} for {quantity} widgets at ${price} each.")

calculate_total(12, 3)