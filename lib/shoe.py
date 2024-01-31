#!/usr/bin/env python3

class Shoe():
    
    def __init__(self, brand, size, condition = "Used"):
        self.brand = brand
        self.size = size
        self.condition = condition


    @property
    def brand(self):
        return self._brand 
    
    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, new_size):
        if type(new_size) == int:            
            self._size = new_size
        else:
            raise ValueError("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new")

stan_smith = Shoe("Adidas", 9)

print(stan_smith.size)
print(stan_smith.brand)
stan_smith.cobble()
print(stan_smith.condition)