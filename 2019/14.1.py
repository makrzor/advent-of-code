#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

input_data = {}
cost = {"COM": 0}


def calculate_cost(product: str) -> int:
    if product in cost.keys():
        product_cost = cost[product]
    else:
        # TODO:
        product_cost = calculate_cost(input_data[product]) + 1
    return product_cost


for line in input_file:
    (materials, product) = line.strip().split(" => ")
    product = product.split(" ")
    product = dict((product[1], product[0]))
    materials = materials.split(", ")
    for mat in materials:

    input_data[product] = orbited

distances_total = 0
for orbiting in input_data.keys():
    distances_total += calculate_cost(orbiting)

print(distances_total)
