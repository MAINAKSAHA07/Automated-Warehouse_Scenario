# Automated Warehouse Simulation

This project simulates an automated warehouse environment using Answer Set Programming (ASP) to optimize robot movements and task completion.

## Project Structure

```
.
├── warehouse_simulator.py    # Main Python script to run simulations
├── warehouse_logic.asp      # Core ASP program with warehouse rules
├── input_parser.asp         # ASP program for parsing input data
├── input_converter.asp      # ASP program for converting input data
├── simpleInstances/         # Directory containing test instances
│   ├── inst1.asp
│   ├── inst2.asp
│   ├── inst3.asp
│   ├── inst4.asp
│   └── inst5.asp
└── robot_paths/            # Directory for storing robot movement logs
```

## Prerequisites

- Python 3.x
- Clingo (Answer Set Programming solver)
  - Installation instructions: https://potassco.org/clingo/

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Automated-Warehouse
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the warehouse simulator:
```bash
python warehouse_simulator.py
```

2. Select an instance file (1-5) when prompted

3. The program will:
   - Run the simulation using Clingo
   - Display the results
   - Save robot paths to JSON files in the `robot_paths` directory

## Output Format

The robot paths are saved in JSON format with the following structure:
```json
{
  "robot_id": [
    {
      "time": <timestamp>,
      "action": "<action_type>"
    },
    ...
  ],
  ...
}
```

Where action types can be:
- `move(dx,dy)`: Robot movement
- `pickup`: Picking up a shelf
- `putdown`: Putting down a shelf
- `deliver(order_id,product_id,quantity)`: Delivering products

## Features

- Multi-robot coordination
- Shelf handling
- Product delivery optimization
- Path tracking and logging
- Multiple test instances

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 