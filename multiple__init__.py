# Parent class 1
class Camera:
    def __init__(self):
        print("Camera ready")
    def take_photo(self):
        print("Taking a photo...")
# Parent class 2
class Phone:
    def __init__(self):
        print("Phone ready")
    def make_call(self):
        print("Making a call...")
# Child class inheriting from both
class Smartphone(Camera, Phone):
    def __init__(self):
        # Call constructors of both parents
        Camera.__init__(self)  # Explicit call
        Phone.__init__(self)  # Explicit call
        print("Smartphone ready")
    def browse_internet(self):
        print("Browsing the internet...")
# Create object
my_phone = Smartphone()
my_phone.take_photo()  # From Camera
my_phone.make_call()  # From Phone
my_phone.browse_internet()  # From Smartphone
