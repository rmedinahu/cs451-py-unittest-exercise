# cs 451 In Class Exercise: Python Unit Testing and Geopy
This exercise is designed to give you a chance, in class, to implement functionality in a given python module then design and implement unit tests for your implementation. 

## Getting Started

1. Fork this project to your repository.
2. Clone **your fork** to your computer.
3. Complete the development tasks listed below then commit and push your changes back up to your GitHub repo.

## Development Tasks: Using Python unittest module.
This project contains a src directory that contains the definition for a class named *GeoLocWrapper* (geolocwrapper.py) and a file for implementing **unittests** for the GeoLocWrapper class methods (test_geolocwrapper.py).

### Step 0:
The project *requires* geopy package. Create a virtual environment for this project and install geopy in it. *Make sure to update the requirements.txt file to reflect that this project requires geopy!*

### Step 1:
Implement the two unit tests for the GeoLocWrapper constructor. One that tests a successful instantiation and one that tests instantiation with an invalid geolocation. (E.g., When an address is not found the constructor should raise a ```GeopyError```)

**Run the tests.**

```python test_geolocwrapper.py```

### Step 2:
Implement the methods ```get_distance_miles``` and ```get_distance_kilometers``` in the GeoLocWrapper class.

### Step 3:
Design and implement a set of unit tests that provides *full test coverage* of the class.

> You must make sure that at least one of your unit tests verifies that an exception is raised under certain conditions.

### Step 4. 
Commit your changes and push to your remote repository. Let instructor know when your project changes are commited and pushed.

## Resources:
- [geopy docs](https://geopy.readthedocs.io/en/stable/)
- [about git fork](https://help.github.com/articles/fork-a-repo/)
- [Python unittest module (builtin)](https://docs.python.org/3/library/unittest.html)