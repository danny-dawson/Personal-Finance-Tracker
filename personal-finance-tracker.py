#Personal Finance Tracker
import tkinter as tk
from tkinter import ttk, messagebox 
import tkinter.font as tkfont
import sqlite3

class Finance_Tracker:
    def __init__(self, root):

        self.root = root
        self.root.title("Personal Finance Tracker")

        #Header Font
        italized_font = tkfont.Font(family="Arial", size=16, slant="italic", underline = 1)

        #Theme
        style = ttk.Style()
        style.theme_use("clam")

        #Border for Table  
        style.configure(
            "Treeview",
            rowheight=25,              
            bordercolor="black",      
            borderwidth=1,             
            background="white",
            foreground="black"  
        )

        #Frame for title
        self.title_frame = ttk.Frame(self.root, padding=(40, 40))
        self.title_frame.pack(fill='x')
        self.title_label = ttk.Label(self.title_frame, text="Personal Finance Tracker", font=italized_font)
        self.title_label.pack()

        #Frame for input section
        self.input_frame = ttk.Frame(self.root, padding=(10, 10))
        self.input_frame.pack(side='left', fill='y')

        #Month Label
        self.month_label = ttk.Label(self.input_frame, text="Month:")
        self.month_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.month_combobox = ttk.Combobox(self.input_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], state="readonly")
        self.month_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.month_combobox.set("Select Month")

        #Year Label
        self.year_label = ttk.Label(self.input_frame, text="Year:")
        self.year_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.year_entry = ttk.Entry(self.input_frame, width=20)
        self.year_entry.grid(row=1, column=1, padx=5, pady=5)

        #Rent Label
        self.rent_label = ttk.Label(self.input_frame, text="Rent:")
        self.rent_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.rent_entry = ttk.Entry(self.input_frame, width=20)
        self.rent_entry.grid(row=2, column=1, padx=5, pady=5)

        #Gas Label
        self.gas_label = ttk.Label(self.input_frame, text="Gas:")
        self.gas_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.gas_entry = ttk.Entry(self.input_frame, width=20)
        self.gas_entry.grid(row=3, column=1, padx=5, pady=5)

        #Groceries Label 
        self.groceries_label = ttk.Label(self.input_frame, text="Groceries:")
        self.groceries_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
        self.groceries_entry = ttk.Entry(self.input_frame, width=20)
        self.groceries_entry.grid(row=4, column=1, padx=5, pady=5)

        #Food Label
        self.food_label = ttk.Label(self.input_frame, text="Food:")
        self.food_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
        self.food_entry = ttk.Entry(self.input_frame, width=20)
        self.food_entry.grid(row=5, column=1, padx=5, pady=5)

        #Entertainment Label
        self.entertainment_label = ttk.Label(self.input_frame, text="Entertainment:")
        self.entertainment_label.grid(row=6, column=0, padx=5, pady=5, sticky='w')
        self.entertainment_entry = ttk.Entry(self.input_frame, width=20)
        self.entertainment_entry.grid(row=6, column=1, padx=5, pady=5)

        #Car Payment Label 
        self.car_label = ttk.Label(self.input_frame, text="Car Payment:")
        self.car_label.grid(row=7, column=0, padx=5, pady=5, sticky='w')
        self.car_entry = ttk.Entry(self.input_frame, width=20)
        self.car_entry.grid(row=7, column=1, padx=5, pady=5)

        #Misc Label
        self.misc_label = ttk.Label(self.input_frame, text="Misc:")
        self.misc_label.grid(row=8, column=0, padx=5, pady=5, sticky='w')
        self.misc_entry = ttk.Entry(self.input_frame, width=20)
        self.misc_entry.grid(row=8, column=1, padx=5, pady=5)

        #Income Label
        self.income_label = ttk.Label(self.input_frame, text="Income:")
        self.income_label.grid(row=9, column=0, padx=5, pady=5, sticky='w')
        self.income_entry = ttk.Entry(self.input_frame, width=20)
        self.income_entry.grid(row=9, column=1, padx=5, pady=5)

        #Update Database Button
        self.add_button = ttk.Button(self.input_frame, text="Update Database", command=self.update_database)
        self.add_button.grid(row=11, column=0, columnspan=2, pady=10)

        #Delete Button 
        self.delete_button = ttk.Button(self.input_frame, text="Delete Last Entry", command=self.delete_last_entry)
        self.delete_button.grid(row=12, column=0, columnspan=2, pady=10)

        #YTD Report Button
        self.ytd_button = ttk.Button(self.input_frame, text="YTD Report", command=self.ytd_report)
        self.ytd_button.grid(row=13, column=0, columnspan=2, pady=10)

        #Display Frame
        self.display_frame = ttk.Frame(self.root, padding=(10, 10))
        self.display_frame.pack(side = 'right',fill='both', expand=True)

        #Table
        self.tree = ttk.Treeview(self.display_frame, columns=("month", "year", "rent", "gas", "groceries", "food", 
                                                              "entertainment", "car_payment", "misc", "income", 
                                                              "expenses", "profit"), show="headings", height=10)
        self.tree.pack(fill="both", expand=True)

        #Columns
        self.tree.heading("month", text="Month")
        self.tree.heading("year", text="Year")
        self.tree.heading("rent", text="Rent")
        self.tree.heading("gas", text="Gas")
        self.tree.heading("groceries", text="Groceries")
        self.tree.heading("food", text="Food")
        self.tree.heading("entertainment", text="Entertainment")
        self.tree.heading("car_payment", text="Car Payment")
        self.tree.heading("misc", text="Misc")
        self.tree.heading("income", text="Income")
        self.tree.heading("expenses", text="Expenses")
        self.tree.heading("profit", text="Profit")

        #Column width
        for col in self.tree["columns"]:
            self.tree.column(col, width=90, anchor="center")

        #Initial table fill
        self.fill_table()


    def fill_table(self):
        #Clear the table
        for row in self.tree.get_children():
            self.tree.delete(row)

        try:
            #Connect to DB
            conn = sqlite3.connect("Personal_Finance_Tracker_DB.db")
            cursor = conn.cursor()

            #Search the 12 most recent entries
            cursor.execute("""
            SELECT month, year, rent, gas, groceries, food, entertainment, car_payment, misc, income, expenses, profit
            FROM Personal_Finance_Tracker
            ORDER BY CAST(year AS INTEGER) DESC,
                CASE
                    WHEN month = 'January' THEN 1
                    WHEN month = 'February' THEN 2
                    WHEN month = 'March' THEN 3
                    WHEN month = 'April' THEN 4
                    WHEN month = 'May' THEN 5
                    WHEN month = 'June' THEN 6
                    WHEN month = 'July' THEN 7
                    WHEN month = 'August' THEN 8
                    WHEN month = 'September' THEN 9
                    WHEN month = 'October' THEN 10
                    WHEN month = 'November' THEN 11
                    WHEN month = 'December' THEN 12
                END DESC
            LIMIT 12
            """)

            rows = cursor.fetchall()

            #Insert data into treeview
            for row in rows:
                self.tree.insert("", "end", values=row)

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")

        finally:
            conn.close()


    def update_database(self):
        #Update SQL Database

        #Initialize vars = 0        
        month, year, rent, gas, groceries, food, entertainment, car_payment, misc, income = 0,0,0,0,0,0,0,0,0,0 

        #Extract vals and convert text into float when necessary
        month = self.month_combobox.get() 
        year = self.year_entry.get()
        rent = float(self.rent_entry.get()) if self.rent_entry.get() else 0.0 
        gas = float(self.gas_entry.get()) if self.gas_entry.get() else 0.0 
        groceries = float(self.groceries_entry.get()) if self.groceries_entry.get() else 0.0
        food = float(self.food_entry.get()) if self.food_entry.get() else 0.0
        entertainment = float(self.entertainment_entry.get()) if self.entertainment_entry.get() else 0.0
        car_payment = float(self.car_entry.get()) if self.car_entry.get() else 0.0 
        misc = float(self.misc_entry.get()) if self.misc_entry.get() else 0.0
        income = float(self.income_entry.get()) if self.income_entry.get() else 0.0

        #Expenses and Profit Formulas
        expenses = rent + gas + groceries + food + entertainment + car_payment + misc
        profit = income - expenses
        
        try:
            #Connect to Database
            conn = sqlite3.connect("Personal_Finance_Tracker_DB.db")
            cursor = conn.cursor()

            #Check if any input field is empty

            if(month == "Select Month" or not year or not rent or not gas or not groceries
                                       or not food or not entertainment or not
                                       car_payment or not misc or not income):
                messagebox.showerror("Error", "One or more input fields is empty")
                return

            #Insert data into database
            cursor.execute("""
                INSERT INTO Personal_Finance_Tracker (month, year, rent, gas, groceries, food, entertainment, car_payment, misc, income, expenses, profit)           
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (month, year, rent, gas, groceries, food, entertainment, car_payment, misc, income, expenses, profit))                                    
            conn.commit()

            #Confirmation message and profit/expenses figures for the month
            messagebox.showinfo("New Data Added", f"Database Updated\n\nExpenses for this Month: ${expenses:.2f}\nProfit for this Month: ${profit:.2f}")

            self.fill_table()

        except sqlite3.Error as e:
            #Error message 
            messagebox.showerror("Database Error", f"Error: {e}")

        finally: 
            conn.close()


    def delete_last_entry(self):
        #Function that deletes the most recent entry into the DB 
        try:
            conn = sqlite3.connect("Personal_Finance_Tracker_DB.db")
            cursor = conn.cursor()

            cursor.execute("""
            SELECT month, year FROM Personal_Finance_Tracker
            ORDER BY CAST(year AS INTEGER) DESC, 
                CASE
                    WHEN month = 'January' THEN 1
                    WHEN month = 'February' THEN 2
                    WHEN month = 'March' THEN 3
                    WHEN month = 'April' THEN 4
                    WHEN month = 'May' THEN 5
                    WHEN month = 'June' THEN 6
                    WHEN month = 'July' THEN 7
                    WHEN month = 'August' THEN 8
                    WHEN month = 'September' THEN 9
                    WHEN month = 'October' THEN 10
                    WHEN month = 'November' THEN 11
                    WHEN month = 'December' THEN 12
                END DESC
            LIMIT 1
            """)
            last_entry = cursor.fetchone()

            if last_entry:

                confirmation = messagebox.askyesno(
                    "Are you sure?", f"Confirm you want to delete the records from:\n\n {last_entry[0]} {last_entry[1]}"
                )

                if confirmation:

                    cursor.execute("DELETE FROM Personal_Finance_Tracker WHERE month = ? AND year = ?", last_entry)
                    conn.commit()
                    messagebox.showinfo("Entry Deleted", f"Deleted the entry from: {last_entry[0]} {last_entry[1]}")

                    self.fill_table()

                else:
                    messagebox.showinfo("Cancelled", "Deletion was Cancelled")
            else:
                messagebox.showinfo("Empty DB", "Database is Empty")
        
        except sqlite3.Error as e:

            messagebox.showerror("Database Error", f"Error: {e}") 

        finally:
            conn.close()


    def ytd_report(self):
        
        #Initialize vars = 0
        ytd_rent, ytd_gas, ytd_groceries, ytd_food, ytd_entertainment, ytd_car_payment, ytd_misc, ytd_income, ytd_expenses, ytd_profit = 0,0,0,0,0,0,0,0,0,0

        try:
            conn = sqlite3.connect("Personal_Finance_Tracker_DB.db")
            cursor = conn.cursor()

            #Use same query for the table to get YTD entries 
            cursor.execute("""
                SELECT month, year, rent, gas, groceries, food, entertainment, car_payment, misc, income, expenses, profit
                FROM Personal_Finance_Tracker
                ORDER BY CAST(year AS INTEGER) DESC,
                    CASE
                        WHEN month = 'January' THEN 1
                        WHEN month = 'February' THEN 2
                        WHEN month = 'March' THEN 3
                        WHEN month = 'April' THEN 4
                        WHEN month = 'May' THEN 5
                        WHEN month = 'June' THEN 6
                        WHEN month = 'July' THEN 7
                        WHEN month = 'August' THEN 8
                        WHEN month = 'September' THEN 9
                        WHEN month = 'October' THEN 10
                        WHEN month = 'November' THEN 11
                        WHEN month = 'December' THEN 12
                    END DESC
                LIMIT 12           
            """)

            rows = cursor.fetchall()

            #sum all vars 
            for row in rows:
                ytd_rent += float(row[2])
                ytd_gas += float(row[3])
                ytd_groceries += float(row[4])
                ytd_food += float(row[5])
                ytd_entertainment += float(row[6])
                ytd_car_payment += float(row[7])
                ytd_misc += float(row[8])
                ytd_income += float(row[9])
                ytd_expenses += float(row[10])
                ytd_profit += float(row[11])

            messagebox.showinfo(
                "YTD Report",
                f"Year-To-Date Report (Last 12 Entries):\n\n"
                f"Total Rent: ${ytd_rent:.2f}\n\n"
                f"Total Gas: ${ytd_gas:.2f}\n\n"
                f"Total Groceries: ${ytd_groceries:.2f}\n\n"
                f"Total Food: ${ytd_food:.2f}\n\n"
                f"Total Entertainment: ${ytd_entertainment:.2f}\n\n"
                f"Total Car Payment: ${ytd_car_payment:.2f}\n\n"
                f"Total Miscellaneous: ${ytd_misc:.2f}\n\n"
                f"Total Income: ${ytd_income:.2f}\n\n"
                f"Total Expenses: ${ytd_expenses:.2f}\n\n"
                f"Total Profit: ${ytd_profit:.2f}"
            )

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

        finally:
            conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = Finance_Tracker(root)
    root.mainloop()