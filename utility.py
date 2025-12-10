class Utility:
    @staticmethod
    def get_required_input(prompt: str)->str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print('This field is required. Please try again.')

    @staticmethod
    def get_required_int(prompt: str) -> int:
        """Get required integer input with validation"""
        while True:
            value = input(prompt).strip()
            if not value:
                print('This field is required. Please try again.')
                continue
            try:
                return int(value)
            except ValueError:
                print('Invalid input. Please enter a valid integer.')

    @staticmethod
    def get_menu_choice(prompt: str) -> int:
        """Get menu choice with validation"""
        while True:
            try:
                value = input(prompt).strip()
                if not value:
                    print('Please enter a choice.')
                    continue
                return int(value)
            except ValueError:
                print('Invalid input. Please enter a valid number.')
