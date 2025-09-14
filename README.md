# E-commerce-App

A modern and sleek user profile section for a mobile e-commerce application built with Python and KivyMD.

## Features

- Modern and responsive UI design
- Profile management with photo, name, and email
- Order history with tabbed interface (Delivered, Processing, Cancelled)
- Detailed order view with product information
- Settings management with personal information and notification preferences
- Dark mode support
- Toast messages for user feedback

## Requirements

- Python 3.7+
- Kivy 2.2.1
- KivyMD 1.1.1
- Pillow 10.0.0

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python main.py
```

## Project Structure

```
.
├── main.py                 # Main application entry point
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
└── screens/               # Screen implementations
    ├── profile_screen.py  # Profile screen implementation
    ├── profile_screen.kv  # Profile screen styling
    ├── orders_screen.py   # Orders screen implementation
    ├── orders_screen.kv   # Orders screen styling
    ├── settings_screen.py # Settings screen implementation
    └── settings_screen.kv # Settings screen styling
```

## Usage

1. The application starts with the profile screen showing the user's information
2. Navigate through different sections using the menu items
3. View order history in the Orders section with different tabs
4. Manage personal information and notification preferences in Settings

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 