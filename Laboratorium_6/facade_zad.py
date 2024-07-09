class Lighting:
    def on(self):
        """Turns the lights on."""
        print("Lights are on")

    def off(self):
        """Turns the lights off."""
        print("Lights are off")


class AirConditioning:
    def on(self):
        """Turns the air conditioning on."""
        print("Air conditioning is on")

    def off(self):
        """Turns the air conditioning off."""
        print("Air conditioning is off")


class SecuritySystem:
    def on(self):
        """Activates the security system."""
        print("Security system is activated")

    def off(self):
        """Deactivates the security system."""
        print("Security system is deactivated")


class SmartHomeFacade:
    def __init__(self, lighting, air_conditioning, security_system):
        """
        Initializes the facade with the components of the smart home system.

        Args:
            lighting (Lighting): The lighting component.
            air_conditioning (AirConditioning): The air conditioning component.
            security_system (SecuritySystem): The security system component.
        """
        self.lighting = lighting
        self.air_conditioning = air_conditioning
        self.security_system = security_system

    def activate(self):
        """Activates the smart home system."""
        print("Activating the smart home system...")
        self.lighting.on()
        self.air_conditioning.on()
        self.security_system.on()
        print("Smart home system activated")

    def deactivate(self):
        """Deactivates the smart home system."""
        print("Deactivating the smart home system...")
        self.lighting.off()
        self.air_conditioning.off()
        self.security_system.off()
        print("Smart home system deactivated")


if __name__ == "__main__":
    lighting = Lighting()
    air_conditioning = AirConditioning()
    security_system = SecuritySystem()

    smart_home = SmartHomeFacade(lighting, air_conditioning, security_system)

    smart_home.activate()
    print("\n\n")
    smart_home.deactivate()
