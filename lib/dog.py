# # #!/usr/bin/env python3


# # class Dog:
# #     def __init__(self, name):
# #         print(f"{name} dog is born!")

# #     def bark(self):
# #         print("Woof!")

# #     def showing_self(self):
# #         return self
# #         pass


# # fido = Dog("fido")

# # # print(fido is fido.showing_self())


# class Dog:
#   def __init__(self, name):
#     self.name = name
# zack = Dog("zack")

# def adopt(dog , owner_name):
#     dog.owner = owner_name

# adopt(zack,"joy")
# print(zack.owner)


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        pass
