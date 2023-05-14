class Pet:

    cinsler = ["dog", "cat", "bird"]
    def __init__(self, isim, cins):
        if cins in Pet.cinsler:
            raise ValueError(f"{cins} bir evcil hayvan değldir!")
        self.isim = isim
        self.cins = cins


    


mars = Pet("Mars", "cat")
ares = Pet("Ares", "dog")
leo = Pet("Leo", "bird")

Pet.cinsler.append("fish") # Bütün neseneler için eklenir!
# mars.cinsler.append("fish")
# ares.cinsler.append("fish")

leo.cins = "lion" 

print(Pet.cinsler)
print(mars.cinsler)
print(ares.cinsler)