Please Read the **docs/Algorithom Documentation.md** to get details about 

### ![#1589F0](https://via.placeholder.com/15/1589F0/000000?text=+)  **Algorithm, Issues, Next Steps** 

## Installation
- setup [venv](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- pip install -r requirements.txt 


## How to run Training
run one of following commands from project root
- -f for input file

`python3 app/main.py -f data/input1.txt`
`python3 app/main.py -f data/input4.txt`


Folder Structure
============================

### top-level directory layout

    .
    ├── app                     # all the source code to run the curry wholesaler
    ├── data                    # sample input data
    ├── docs                    # Documentation details about the main algorithm
    ├── test                    # unit tests folder
    ├── venv                    # python and dependencies                 
    ├── .gitignore              # gitignore                  
    ├── README.md               # project documenation                   
    └── requirments.txt         # all dependencies list



### Source files
    .
    ├── ...
    ├── app
    │   ├── __init__.py             
    │   ├── curry               # all curry related methods, codes
    │   ├── customer            # all customer related methods, codes        
    │   ├── order               # all order/preference related methods, codes
    │   ├── utils               # argument parser, txt file reader
    │   ├── constants.py        # constants and msg
    │   ├── input_validator.py  # checks if valid input data or not
    │   └── main.py             # main scripts                  
    └── ...


### Tests files
    .
    ├── ...
    ├── test
    │   ├── __init__.py         
    │   ├── test_main.py                        # Unit tests to check if main algo works
    │   └── test_check_input_validity.py        # Unit tests to check if input is valid
    └── ...

### Data folder
    .
    ├── ...
    ├── data
    │   ├── input1.txt                # example valid input 1 
    │   ├── input2.txt                # example valid input 2 
    │   ├── input3.txt                # example valid input 3 
    │   ├── input4.txt                # example invalid input 4 
    │   └── invalid_input.txt         # example invalid input 5
    └── ...

### Documentation files
    .
    ├── ...
    ├── docs
    │   ├── Algorithom Documentation.md         # Brief discussion about the Algorithm
    └── ...