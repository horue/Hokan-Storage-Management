# Hokan: Storage Management Program

## Overview

**Hokan** is a Python-based storage management program that utilizes SQLite for efficient and reliable data storage. This application is designed to help users manage and organize their storage units, track inventory, and maintain records with ease.

## Features

-   **Inventory Management**: Add, update, and delete items in the inventory.
-   **Storage Unit Tracking**: Monitor and organize multiple storage units.
-   **Search Functionality**: Quickly find items and storage units.
-   **Database Integration**: Persistent data storage using SQLite.

## Installation

1.  Clone the repository:
    
    bash
    
    Copiar código
    
    `git clone https://github.com/yourusername/hokan.git
    cd hokan` 
    
2.  Create a virtual environment and activate it:
    
    bash
    
    Copiar código
    
    ``python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate` `` 
    
3.  Install the required dependencies:
    
    bash
    
    Copiar código
    
    `pip install -r requirements.txt` 
    

## Usage

1.  Initialize the SQLite database:
    
    bash
    
    Copiar código
    
    `python init_db.py` 
    
2.  Run the main program:
    
    bash
    
    Copiar código
    
    `python main.py` 
    

## Contributing

1.  Fork the repository.
2.  Create a new feature branch (`git checkout -b feature-name`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature-name`).
5.  Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.