bad_ingredients = [
  'coconut oil',
  'isopropyl myristate',
  'algae extract',
  'wheat germ oil',
  'cocoa butter',
  'linseed oil',
  'laureth-4',
  'almond oil',
  'soybean oil',
  'D & C Red Dyes'
]

def is_bad_ingredient(ingredient):
  return ingredient.lower() in bad_ingredients

# Example usage:
makeup_ingredient = 'talc'
if is_bad_ingredient(makeup_ingredient):
  print(f"{makeup_ingredient} is a bad makeup ingredient.")
else:
  print(f"{makeup_ingredient} is not a bad makeup ingredient.")