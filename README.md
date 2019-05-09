# Grade Calculator

A Python3 script that takes a YAML file with grade information (see `sample-class.yml`), and gives your final grade.

## Usage
```shell
    python3 grade_calculator.py sample-class.yml
```
 where `sample-class.yml` is file with assignment information, weights for each assignment, and scores.

This works in classes that use both a "points" system, and a weight-based system.

It factors in drops, as well as extra credit!