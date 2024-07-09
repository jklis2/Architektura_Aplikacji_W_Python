from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """Executes the command."""
        pass

class Light:
    def on(self):
        """Turns the light on."""
        print("The light is on")

    def off(self):
        """Turns the light off."""
        print("The light is off")

    def half_on(self):
        """Sets the light to half brightness."""
        print("The light is half on")

class LightOnCommand(Command):
    def __init__(self, light):
        """
        Initializes the command with the light receiver.

        Args:
            light (Light): The light receiver.
        """
        self.light = light

    def execute(self):
        """Executes the command to turn on the light."""
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        """
        Initializes the command with the light receiver.

        Args:
            light (Light): The light receiver.
        """
        self.light = light

    def execute(self):
        """Executes the command to turn off the light."""
        self.light.off()

class LightHalfOnCommand(Command):
    def __init__(self, light):
        """
        Initializes the command with the light receiver.

        Args:
            light (Light): The light receiver.
        """
        self.light = light

    def execute(self):
        """Executes the command to set the light to half brightness."""
        self.light.half_on()

class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, button, command):
        """
        Sets a command for a specific button.

        Args:
            button (str): The button identifier.
            command (Command): The command to set.
        """
        self.commands[button] = command

    def press_button(self, button):
        """
        Presses a button to execute its command.

        Args:
            button (str): The button identifier.
        """
        if button in self.commands:
            self.commands[button].execute()
        else:
            print(f"No command assigned to button {button}")

if __name__ == "__main__":
    remote_control = RemoteControl()

    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    light_half_on = LightHalfOnCommand(light)

    remote_control.set_command("A", light_on)
    remote_control.set_command("B", light_off)
    remote_control.set_command("C", light_half_on)

    print("\nPressing button A:")
    remote_control.press_button("A")
    print("\nPressing button B:")
    remote_control.press_button("B")
    print("\nPressing button C:")
    remote_control.press_button("C")
    print("\nPressing button B again:")
    remote_control.press_button("B")
    print("\nPressing button C again:")
    remote_control.press_button("C")
