#pole ktere ma 5 stringu
pole = ["oheň", "voda", "blesky", "kámen", "příroda"]
print("základní pole", pole)
#přidání prvku vítr
pole.append("vítr")
print("Po přidání větru", pole)
#odstrani vodu
pole.remove("voda")
print("Pole po odstranění druhého prvku:", pole)
#změní přírodu na země
pole[4] = "země"
print("Pole po změně 5. hodnoty", pole)