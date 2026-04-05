Advanced Savings & Email Management System
A robust Python-based application designed to manage personal savings and user mailing lists with persistent data storage and administrative controls. This project demonstrates an evolution from a simple script to a functional, file-based management tool.
🌟 Evolution: From Basic to Advanced
This version represents a significant upgrade from the initial prototype. Key improvements include:
Persistent Storage: Transitioned from volatile memory to permanent JSON storage (balance.json, email_list.json).
Enhanced Security: Implemented a dedicated "Creator Mode" with password protection for sensitive administrative actions.
Robust Error Handling: Added try-except blocks and input validation to handle JSON corruption and user input errors gracefully.
Modular Logic: Refactored code into clean, reusable functions for better maintainability.
🚀 Key Features
Financial Tracking: Perform deposits and withdrawals with real-time updates to a local database.
User Authentication: Integrated login system that distinguishes between regular users and system administrators.
Creator Dashboard: Specialized interface for administrators to:
View and modify the entire user database.
Perform a "Global Reset" of all stored data.
State Management: Automatically initializes data files if they are missing or corrupted.
🛠️ Technical Stack
Language: Python 3.x
Data Format: JSON (for lightweight, structured data persistence)
Libraries: os, json (Built-in standard libraries)
📖 How to Use
Start the App: Run money_calculator.py.
Accessing your Account:
Enter your registered email to log in.
Type create to register a new account.
Managing Funds:
Use append to add money to your savings.
Use remove to withdraw funds.
Admin Access:
Enter the secret key at the login prompt to access the Creator Menu.
📂 Project Structure
money_calculator.py - The core logic and UI.
balance.json - Stores financial data (Auto-generated).
email_list.json - Stores user credentials (Auto-generated).
