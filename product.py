def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices
products = ["bag", "book", "pen", "bag", "note", "bag"]
target = "bag"
target2="boat"
result = target
print(result)