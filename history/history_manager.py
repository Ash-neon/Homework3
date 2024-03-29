import pandas as pd
import logging
import os

class HistoryManager:
    def __init__(self, file_path='history.csv'):
        self.file_path = file_path
        self.history_df = self.load_history()  # Load history when instantiated


    def load_history(self):
        # Load history from CSV file
        if not os.path.exists(self.file_path):
            print(f"CSV file '{self.file_path}' not found or is empty.")
            return pd.DataFrame(columns=['Operand1', 'Operand2', 'Operation', 'Result'])

        try:
            history_df = pd.read_csv(self.file_path)
            if history_df.empty:
                print(f"CSV file '{self.file_path}' is empty.")
            #print("Loaded history DataFrame:", history_df)  # Add this line for debugging
            return history_df
        except pd.errors.EmptyDataError:
            print(f"CSV file '{self.file_path}' is empty.")
            return pd.DataFrame(columns=['Operand1', 'Operand2', 'Operation', 'Result'])

    
    def save_history(self):
        self.history_df.to_csv(self.file_path, index=False)

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operand1', 'Operand2', 'Operation', 'Result'])  # Reset to an empty DataFrame
        self.save_history()  # Save the changes to the CSV file
        logging.info("History cleared.")



    def delete_record(self, record_id):
        if record_id in self.history_df.index:
            self.history_df = self.history_df.drop(index=record_id)
            self.save_history()
        else:
            print("Record ID not found in history.")

    def add_record(self, operand1, operand2, operation, result):
        try:
            # Load the existing history DataFrame
            self.history_df = self.load_history()

            # Add a new row to the DataFrame using loc
            new_index = len(self.history_df)
            self.history_df.loc[new_index] = [operand1, operand2, operation, result]

            logging.info(f"Record added: Operation - {operation}, Operand1 - {operand1}, Operand2 - {operand2}, Result - {result}")
            # Save DataFrame to CSV
            self.save_history()  # Just call save_history without any arguments
        except Exception as e:
            logging.error(f"Error adding record: {e}")

    def get_history(self):
    # Reload the history DataFrame
        self.history_df = self.load_history()
        return self.history_df


