#!/usr/bin/env python

from acme import Employee

filename = "data.txt"

with open(filename) as f:
    content = f.read().splitlines()

for line in content:
    employee = Employee(line)
    print(employee.pay())