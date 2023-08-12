# integrantes do grupo:
#   Caco Abud
#   Gabriel Adelungue
#   Henrique Carvalho de Souza


class ModuleConverter:

  def __init__(self):
    self.define_conversion = {
        ("jarda", "metro"): 0.9144,
        ("jarda", "pé"): 3,
        ("pé", "jarda"): 0.33,
        ("pé", "metro"): 0.3048,
        ("metro", "pé"): 3.281,
        ("metro", "jarda"): 1.0936
    }

  def convert(self, value, origin_unit, destiny_unit):
    if origin_unit == destiny_unit:
      return value

    conversion = (origin_unit, destiny_unit)
    if conversion in self.define_conversion:
      return value * self.define_conversion[conversion]

    return None


def main():
  converter = ModuleConverter()

  value = float(input("Digite o valor a ser convertido: "))
  origin_unit = input("Digite a unidade de origem (jarda/metro/pé): ")
  destiny_unit = input("Digite a unidade de destino (jarda/metro/pé): ")

  result = converter.convert(value, origin_unit, destiny_unit)

  if result is not None:
    print(f"Conversão: {result:.2f} {destiny_unit}s")
    print("-----------------------------------------------")
    main()
  else:
    print("As unidades digitas não são válidas")


if __name__ == "__main__":
  main()


