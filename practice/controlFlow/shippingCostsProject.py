weight = 90
cost = 0
shipping_method = "Ground"
if shipping_method == "Ground":
    # Ground Shipping
    if weight <= 2:
        cost = 1.50 * weight + 20.00
    elif weight > 2 and weight <= 6:
        cost = 3.00 * weight + 20.00
    elif weight > 6 and weight <= 10:
        cost = 4.00 * weight + 20.00
    elif weight > 10:
        cost = 4.75 * weight + 20.00
    else:
        print("Error")
elif shipping_method == "Premium Ground":
    # Premium Ground
    premium_ground_cost = 125.00
elif shipping_method == "Drone":
    # Drone Shipping
    if weight <= 2:
        cost = 4.50 * weight
    elif weight > 2 and weight <= 6:
        cost = 9.00 * weight
    elif weight > 6 and weight <= 10:
        cost = 12.00 * weight
    elif weight > 10:
        cost = 14.25 * weight
    else:
        print("Error")
else:
    print("Error")

print("The total cost of shipping for your package weighing " + str(weight) +
      " pounds, using " + shipping_method + "  shipping is $" + str(cost))
