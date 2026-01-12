class Hello:

    @property
    def name(self):
        name=self._name
        return name

    @name.setter
    def name(self, value):
        self._name = value

obj = Hello()
 # Accessing the property
obj.name = "Rohan"  # Modifying the property
print(obj.name)
print(Hello.name)  # Accessing the modified property