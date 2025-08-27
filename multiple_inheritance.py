# Parent class 1
class Camera:
    def take_photo(self):
        print("Taking a photo...")
# Parent class 2
class Phone:
    def make_call(self):
        print("Making a call...")
# Child class inheriting from both
class Smartphone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the internet...")
# Create object
my_phone = Smartphone()
my_phone.take_photo()     # From Camera
my_phone.make_call()      # From Phone
my_phone.browse_internet() # From Smartphone
