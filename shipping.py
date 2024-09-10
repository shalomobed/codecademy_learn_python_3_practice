weight = 41.5
#Ground Shipping
cost = 20
if weight <= 2:
  cost += weight * 1.50
elif 2 <= weight <= 6:
  cost += weight * 3.00
elif 6 <= weight <= 10:
  cost += weight * 4.00
elif weight > 10:
  cost += weight * 4.75
else:
  print("")
print("Ground Shipping:", cost)
#Ground Shipping Premium
ground_premium_cost = 125.00
print("Ground Shipping Premium:", ground_premium_cost)
#Drone Shipping
drone_weight = 41.5
drone_cost = 0
if drone_weight <= 2:
  drone_cost = 4.5 * drone_weight
if 2 < drone_weight <= 6:
  drone_cost = 9.00 * drone_weight
if 6 < drone_weight <= 10:
  drone_cost = 12.00 * drone_weight
if drone_weight > 10:
  drone_cost = 14.25 * drone_weight
print("Drone Shipping:", drone_cost)


