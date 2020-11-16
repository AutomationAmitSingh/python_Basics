

ItemsInCart = 0
# two items will be added in the cart

if ItemsInCart != 2:# raise Exception("Product cart count is not matching")
    pass

assert (ItemsInCart == 0)

try:
    with open('tes.txt', 'r') as reader:
        reader.read()

except:
    print("file not found exception")


try:
    with open('tes.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up the resources")