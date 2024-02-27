import csv
import json
from tkinter import Tk, Button, messagebox

def load_and_process_csv(filepath):
    sales_data = []
    headers = ["Transaction_date", "Product", "Price", "Payment_Type", "Name", "City", "State", "Country"]
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=headers)
        for row in reader:
            # Cleaning and processing data if necessary
            cleaned_row = {k: v.strip() for k, v in row.items()}  # cleaning: strip whitespace
            sales_data.append(cleaned_row)
    return sales_data

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

def setup_ui():
    root = Tk()
    root.title("Sales Data Processing")
    
    # Set the background color of the main window
    root.configure(bg='#004F27')
    
    quit_button = Button(root, text="Quit", command=root.quit, fg='#FFD51D', bg='#004F27', activeforeground='#FFD51D', activebackground='#005F28')
    quit_button.pack()
    
    # Customize messagebox to match wayne state color scheme
    messagebox.showinfo("Info", "Load CSV and Convert to JSON by clicking 'ok'.")
    
    root.mainloop()

def main():
    csv_file_path = 'SalesJan2009.csv' 
    json_file_name = 'transaction_data.json'
    sales_data = load_and_process_csv(csv_file_path)
    save_to_json(sales_data, json_file_name)
    setup_ui()

if __name__ == "__main__":
    main()
