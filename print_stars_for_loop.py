#!/usr/bin/env python3
start = 1
symbol = "*"
stop_number = 5

def print_symbol(symbol, number):
    for i in range(number):
        print(symbol, end=" ")
    print("\n")

down_counter = stop_number
for x in range(start, 2 * stop_number):
    if x > stop_number:
        down_counter = down_counter - 1
        print_symbol(symbol, down_counter)
    else:
        print_symbol(symbol, x)

