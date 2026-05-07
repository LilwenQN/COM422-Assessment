# Part 2
## Assumptions
- Wind speeds can only be integers: it is not type-hinted, but the range() function is used.
- I do not need to test for negative inputs: logical, but not specified in the brief or attempted anywhere in the code.

## Initial bug fixes
I wasn't sure if the below were supposed to be found in the tests, or if they were just my linter, so I made the following changes without a test.

### Type hinting Storm
```python
    @abstractmethod
    def calculate_classification(self) -> str: # type hint
        pass

    @abstractmethod
    def get_advice(self) -> str: #type hint
        pass
```

### Replacing 'or' with '|'
```python
def view_storm(self, name: str) -> Storm | None: #replace "or" with "|"
        for storm in self.storm_list:
            if storm.name == name:
                return storm
        return None
```

## Hurricane
### Fail 1
![image](/screenshots/test_create_tropical_storm.png)
```python
def test_create_tropical_storm():
    hurricane = Hurricane("Amy", 70)
    assert hurricane.calculate_classification() == "Tropical Storm"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"
```
Issue: Identifying Tropical Storms as "Unclassified"
Fix: Set default to Tropical Storm
```python
def calculate_classification(self) -> str:
        if self.wind_speed in range(74, 95):
            return "Category one"
        elif self.wind_speed in range(96, 111):
            return "Category two"
        elif self.wind_speed in range(111, 130):
            return "Category three"
        elif self.wind_speed in range(130, 157):
            return "Category four"
        elif self.wind_speed > 156:
            return "Category five"
        return "Tropical Storm" # replaced "Unclassified" with "Tropical Storm"
```
![image](/screenshots/test_create_tropical_storm_FIX.png)

### Fail 2
![image](/screenshots/test_create_category_one_UB_in.png)
```python
def test_create_category_one_UB_in():
    hurricane = Hurricane("Bram", 95)
    assert hurricane.calculate_classification() == "Category one"
    assert hurricane.get_advice() == "Close storm shutters and stay away from windows"
```
Issue: inner upper bound for cat1 not inside bound
Fix: Use exclusive upper bound
```python
    def calculate_classification(self) -> str:
        if self.wind_speed in range(74, 96): # replaced 95 with 96
            return "Category one"
        elif self.wind_speed in range(96, 111):
            return "Category two"
        elif self.wind_speed in range(111, 130):
            return "Category three"
        elif self.wind_speed in range(130, 157):
            return "Category four"
        elif self.wind_speed > 156:
            return "Category five"
        return "Tropical Storm" # replaced "Unclassified" with "Tropical Storm"
```
![image](/screenshots/test_create_category_one_UB_in_FIX.png)