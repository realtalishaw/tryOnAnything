class ErrorHandler:
    @staticmethod
    def handle_error(e, custom_message=None):
        # Custom message for logging
        if custom_message:
            print(f"Custom Message: {custom_message}")
        
        # Log the exception
        print(f"Exception occurred: {e}")

        # Add more handling logic here if needed