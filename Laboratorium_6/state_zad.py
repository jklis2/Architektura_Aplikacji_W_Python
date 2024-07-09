from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def insert_coin(self):
        """Handles the action of inserting a coin."""
        pass

    @abstractmethod
    def eject_coin(self):
        """Handles the action of ejecting a coin."""
        pass

    @abstractmethod
    def press_button(self):
        """Handles the action of pressing the button."""
        pass

    @abstractmethod
    def dispense(self):
        """Handles the action of dispensing a ticket."""
        pass

class NoCoinState(State):
    def __init__(self, ticket_machine):
        """
        Initializes the NoCoinState with a reference to the ticket machine.

        Args:
            ticket_machine (TicketMachine): The ticket machine instance.
        """
        self.ticket_machine = ticket_machine

    def insert_coin(self):
        """Handles inserting a coin when no coin is currently inserted."""
        print("Coin inserted.")
        self.ticket_machine.set_state(self.ticket_machine.has_coin_state)

    def eject_coin(self):
        """Handles attempting to eject a coin when no coin is inserted."""
        print("No coin to eject.")

    def press_button(self):
        """Handles pressing the button when no coin is inserted."""
        print("No coin inserted.")

    def dispense(self):
        """Handles attempting to dispense a ticket when no coin is inserted."""
        print("No coin inserted, cannot dispense ticket.")

class HasCoinState(State):
    def __init__(self, ticket_machine):
        """
        Initializes the HasCoinState with a reference to the ticket machine.

        Args:
            ticket_machine (TicketMachine): The ticket machine instance.
        """
        self.ticket_machine = ticket_machine

    def insert_coin(self):
        """Handles attempting to insert a coin when a coin is already inserted."""
        print("Coin already inserted.")

    def eject_coin(self):
        """Handles ejecting a coin when a coin is inserted."""
        print("Coin ejected.")
        self.ticket_machine.set_state(self.ticket_machine.no_coin_state)

    def press_button(self):
        """Handles pressing the button when a coin is inserted."""
        print("Button pressed.")
        self.ticket_machine.set_state(self.ticket_machine.dispense_state)

    def dispense(self):
        """Handles attempting to dispense a ticket before the button is pressed."""
        print("Press the button to get a ticket.")

class DispenseState(State):
    def __init__(self, ticket_machine):
        """
        Initializes the DispenseState with a reference to the ticket machine.

        Args:
            ticket_machine (TicketMachine): The ticket machine instance.
        """
        self.ticket_machine = ticket_machine

    def insert_coin(self):
        """Handles attempting to insert a coin while dispensing a ticket."""
        print("Wait, dispensing ticket.")

    def eject_coin(self):
        """Handles attempting to eject a coin while dispensing a ticket."""
        print("Wait, dispensing ticket.")

    def press_button(self):
        """Handles attempting to press the button while dispensing a ticket."""
        print("Wait, dispensing ticket.")

    def dispense(self):
        """Handles dispensing the ticket."""
        print("Dispensing ticket.")
        self.ticket_machine.set_state(self.ticket_machine.no_coin_state)

class TicketMachine:
    def __init__(self):
        """Initializes the ticket machine with its states and sets the initial state to NoCoinState."""
        self.no_coin_state = NoCoinState(self)
        self.has_coin_state = HasCoinState(self)
        self.dispense_state = DispenseState(self)
        self.state = self.no_coin_state

    def set_state(self, state):
        """
        Sets the current state of the ticket machine.

        Args:
            state (State): The state to set.
        """
        self.state = state

    def insert_coin(self):
        """Delegates the insert_coin action to the current state."""
        self.state.insert_coin()

    def eject_coin(self):
        """Delegates the eject_coin action to the current state."""
        self.state.eject_coin()

    def press_button(self):
        """Delegates the press_button action to the current state and triggers dispensing."""
        self.state.press_button()
        self.state.dispense()

    def dispense(self):
        """Delegates the dispense action to the current state."""
        self.state.dispense()

if __name__ == "__main__":
    ticket_machine = TicketMachine()

    print("\nInserting coin...")
    ticket_machine.insert_coin()

    print("\nPressing button...")
    ticket_machine.press_button()

    print("\nInserting coin...")
    ticket_machine.insert_coin()

    print("\nEjecting coin...")
    ticket_machine.eject_coin()

    print("\nInserting coin again...")
    ticket_machine.insert_coin()

    print("\nTrying to insert another coin...")
    ticket_machine.insert_coin()

    print("\nPressing button...")
    ticket_machine.press_button()

    print("\nTrying to eject coin after pressing button...")
    ticket_machine.eject_coin()
