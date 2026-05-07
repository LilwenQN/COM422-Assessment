# Part 2
## Assumptions
- Wind speeds can only be integers: it is not type-hinted, but the range() function is used.
- I do not need to test for negative (or other unreasonable) inputs: logical, but not specified in the brief or attempted anywhere in the code.

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
Issue: upper bound for cat1 not inside bound
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

## Tornado
### Fail 1
![image](/screenshots/test_create_f0_LB_in.png)
```python
def test_create_f0_LB_in():
    tornado = Tornado("Gerard", 40)
    assert tornado.calculate_classification() == "F0"
    assert tornado.get_advice() == "Find safe room/shelter, shield yourself from debris"
```
Issue: lower bound for f0 not inside bound
Fix: use less than
```python
def calculate_classification(self) -> str:
        if self.wind_speed < 40: # changed <= to <
            return "Unclassified"
        elif self.wind_speed <= 72:
            return "F0"
        elif self.wind_speed in range(73, 113):
            return "F1"
        elif self.wind_speed in range(113, 158):
            return "F2"
        elif self.wind_speed in range(158, 206):
            return "F3"
        elif self.wind_speed in range(206, 261):
            return "F4"
        elif self.wind_speed >= 261:
            return "F5"
        return "Unclassified"
```
![image](/screenshots/test_create_f0_LB_in_FIX.png)

### Fail 2
![image](/screenshots/test_create_f4.png)
```python
def test_create_f4():
    tornado = Tornado("Kasia", 250)
    assert tornado.calculate_classification() == "F4"
    assert tornado.get_advice() == "Find underground shelter, crouch near to the floor covering your head with your hands"
```
Issue: F4 in wrong group
Fix: Add comma
```python
def get_advice(self) -> str:
        classification = self.calculate_classification()

        if classification in ["Unclassified", "F0", "F1"]:
            return "Find safe room/shelter, shield yourself from debris"
        elif classification in ["F2", "F3", "F4", "F5"]: # added comma between "F4" and "F5"
            return "Find underground shelter, crouch near to the floor covering your head with your hands"
        return "There is no need to panic"
```
![image](/screenshots/test_create_f4_FIX.png)

### Fail 3
![image](/screenshots/test_create_unclassified_tornado.png)
```python
def test_create_unclassified_tornado():
    tornado = Tornado("Marty", 0)
    assert tornado.calculate_classification() == "Unclassified"
    assert tornado.get_advice() == "There is no need to panic"
```
Issue: Unclassified in wrong group
Fix: Remove "Unclassified" from wrong group
```python
def get_advice(self) -> str:
    classification = self.calculate_classification()

    if classification in ["F0", "F1"]: # removed "Unclassified"
        return "Find safe room/shelter, shield yourself from debris"
    elif classification in ["F2", "F3", "F4", "F5"]: # added comma between "F4" and "F5"
        return "Find underground shelter, crouch near to the floor covering your head with your hands"
    return "There is no need to panic"
```
![image](/screenshots/test_create_unclassified_tornado_FIX.png)

## Blizzard
### Fail 1
![image](/screenshots/test_create_blizzard.png)
```python
def test_create_blizzard():
    blizzard = Blizzard("Oscar", 40, 10)
    assert blizzard.calculate_classification() == "Blizzard"
    assert blizzard.get_advice() == "Keep warm, Do not travel unless absolutely essential."
```
Issue: "Blizzard" is not capitalised
Fix: capitalise it
```python
def calculate_classification(self) -> str:
    if self.wind_speed >= 35:
        return "Blizzard" # capitalised "blizzard"
    elif self.wind_speed >= 45 and self.temp <= -12:
        return "Severe Blizzard"
    return "Snow Storm"
```
![image](/screenshots/test_create_blizzard_FIX1.png)
Initial issue was fixed.
New issue: Blizzard in wrong category
Fix: Create category for blizzard
```python
def get_advice(self) -> str:
    classification = self.calculate_classification()

    if classification == "Severe Blizzard":
        return "Keep warm, avoid all travel."
    # inserted below condition for Blizzard
    elif classification == "Blizzard":
        return "Keep warm, Do not travel unless absolutely essential."
    return "Take care and avoid travel if possible."
```
![image](/screenshots/test_create_blizzard_FIX2.png)

### Fail 2
![image](/screenshots/test_create_severe_blizzard.png)
```python
def test_create_severe_blizzard():
    blizzard = Blizzard("Patrick", 400, -100)
    assert blizzard.calculate_classification() == "Severe Blizzard"
    assert blizzard.get_advice() == "Keep warm, avoid all travel."
```
Issue: Severe Blizzard not being identified
Fix: Check for Severe Blizzard before Blizzard
```python
def calculate_classification(self) -> str:
    if self.wind_speed >= 45 and self.temp <= -12: # moved this condition to top
        return "Severe Blizzard"
    elif self.wind_speed >= 35:
        return "Blizzard" # capitalised "blizzard"
    return "Snow Storm"
```
![image](/screenshots/test_create_severe_blizzard_FIX.png)