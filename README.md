# ioet-exercise

Developed using Python Standard Library and [Replit](https://replit.com).

It outputs the employee payment amount using a custom-format string that contains the name and the amount of hours.

An Employee user defined type is instantiated with this custom-format string.

The input data is handled by splitting it using the delimiting characters (e.g. `=`, `,`, `:`, `-`) and substrings to obtain the name, days and hours. Days are classified in weekdays and weekends.

Timeslot interval is transformed to `datetime.time` basic data type. Limits of the interval are used to classify the rate and sum up the total number of hours.

## Requisites
- Python 3.8.9
- Text file that contains the employee string line by line

## Running
```
python main.py
```

## Testing
The main conversion amount can be tested using `unittest`.
```
python -m unittest test_acme
```

## Limitations
- Assumes 24-hour format.

## Future Work
- [x] Range of hours to set rate.
- [ ] Use datetime
- [x] Read a txt file.