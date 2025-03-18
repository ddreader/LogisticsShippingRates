# shipping cost calculator 

## input package weight and shipping rate
weight = float(input('Enter the package weight in kilograms: '))
rate = float(input('Enter the shippinh rate per kilogram: '))

# calculate shipping cost
shipping_cost = weight * rate

## display the results
print(f'Shipping Cost: {shipping_cost} USD')
