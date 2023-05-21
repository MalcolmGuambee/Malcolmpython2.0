#scope= is a variable that is recognized
#       It can either be :
      #local,enclosing,global,built-in
      # the computer follows this sequence when recognizing a variable:
      #L,E,G,B
name="Guambe" #Global scop(available inside and outside the function)

def dispalay_name():
    name="Malcolm" #Local scop(Only available inside the function)
    print(name)


dispalay_name()
print(name)