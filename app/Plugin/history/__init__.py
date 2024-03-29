import logging
from app.command import Command
from history.history_manager import HistoryManager

# Configure logging for this module
logger = logging.getLogger(__name__)

class HistoryCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self):
        action = input("Choose history action (load, save, clear, delete, print): ").lower()
        
        # Split the action into separate parts if it contains spaces
        parts = action.split()
        command = parts[0]
        
        if command == 'load':
            self.history_manager.load_history()
            logger.info("History loaded.")
        elif action == 'save':
            self.history_manager.save_history()
            logger.info("History saved.")
        elif command == 'clear':
            self.history_manager.clear_history()
            logger.info("History cleared.")
        elif command == 'delete':
            record_id = input("Enter record ID to delete: ")
            self.history_manager.delete_record(int(record_id))
            logger.info("Record deleted.")
        elif action == 'print':
            history_df = self.history_manager.get_history()
            if not history_df.empty:
                print(history_df.to_string(index=False))
            else:
                print("History is empty.")
        else:
            logger.error("Invalid history action")
