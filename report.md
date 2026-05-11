<style>
    body {
        font-family: "Helvetica";
    }

    h1, h2, h3 {
        font-weight: bold;
        color: #043952
    }
</style>

<center><h1>Part 1</h1></center>

## Testing and Development Overview
For the development of this system, a shift-left approach is recommended.

> The main idea behind Shift-Left is to start testing earlier in the process. By being proactive, you can catch problems sooner and fix them right away, which saves […] money and effort compared to finding bugs later.

_(Kesavan, 2024, p.1 [^1])_ REFERENCE

Implement this by testing at all stages of an agile development process with CI/CD. Agile allows discrepancies found by tests to be factored into the plan and workload. Agile also gives flexibility to change the plan if requirements are changed, which is crucial for a system responding to natural disasters. Additionally, as an emergency response system, users will not know when the system is required, and continuous deployment allows a Minimum Viable Product to be available as soon as possible, and the most up-to-date version to always be used.

To effectively implement CI/CD, a pipeline should be set up which allows changes to be merged, then tested in various environments before being deployed. Locally, a developer should write and test changes to a small update. Then, the changes can be merged and tested on development environments. This can be one environment, or multiple environments, depending on the nature of the tests (see Automated CI/CD pipeline overview LINK). Finally, it can be sent to production environments. Again, this can be one or multiple (see Production environment(s)) LINK.

## Local Testing
In the local stage, TDD should be used, bringing testing early in the process. Writing unit and contract tests before the code is developed encourages the testing to be as extensive as possible and encourages developers to consider the testability of the code as they implement it. Contract tests are used to test API requests and responses _(Pact and Fellows, 2023)_ REFERENCE. These can be mocked or complete (depending on whether the API call is internal or external). In addition to TDD, developers should write integration tests in order to capture the interactions between different parts of the code. The simplicity and durability of unit, contract and integration tests means they can cover large amounts of scope with minimal time and maintenance. As the application is data-based and requires accuracy, these tests are vital to ensure that small discrepancies and unexpected results don’t go unnoticed.

BDD should not be used here as it takes a lot of time and does not cover the majority of this system (as it is primarily data import and analysis). It could be useful for checking that results are returned in the correct places, but it cannot check that they are the correct results. BDD is better suited where the front-end is central to the application, and user experience can be used to evaluate the correct functionality of the system.

Automated UI tests could be used at this stage, but they are volatile and take a long time to both write and run. If components are moved, renamed or changed, they can break easily. Manual testing is better suited for this system as it is more flexible. At this stage, simple sense checks and exploratory tests can be carried out by developers on features they have changed, and wider exploratory testing can be carried out later in the process (see Staging environment) LINK.
 
In addition to these code tests, SAST and SCA should be run on all code before merging. These are light on resource, as pre-built SAST and SCA packages can be used and run. This may cost money depending on the frameworks and languages being used, but are important nonetheless, as security is essential to this system. It has significance to social and life-threatening issues, and high media coverage, making this a desirable system to target.

## Automated CI/CD Pipeline Overview
Once changes are pushed, they should be tested on development environments. Three environments are recommended: one for lighter smoke tests which can be run on each merge but need to be tested with more reliable components than can be done locally (the “integration environment” below); one for more comprehensive testing, which can be run on groups of changes before a deployment (the “staging environment” below); one for destructive tests, which is designed to be safe to break (the “security environment” below). This allows the CI/CD process to be run continuously with comprehensive testing, without different stages affecting each other.

The integration environment can be lighter-weight, as it is not a production-like environment. The staging and security environments should be as similar to production environments as possible, with well-simulated/mocked versions of the external services. Lots of the external data sources are unpredictable and inconsistent, with periods of high and low activity. They may come with unexpected noise or badly formatted data. They are likely to have spikes at similar times to each other, as they are responsive to natural disasters. While this cannot be perfectly mocked, you should attempt to simulate this variation and inconsistency.

## Integration Environment
The integration environment sits earlier in the CI/CD pipeline than the other development environments and should be used for simple smoke tests. This should include integration tests (both at the service level and the API level), unit tests and contract tests.

In a system with many interacting components, integration testing is critical for exposing issues which are not apparent during isolated testing by an individual developer pre-commit.

## Security Environment
The security environment is for destructive security tests. As stated earlier, the system is a target for attack and should be thoroughly security-tested. Dynamic Application Security Testing is an easy way to test for vulnerabilities without requiring tester/developer time, as pre-built frameworks can be set up in the pipeline. It simulates malicious attacks, covering data/input vulnerability, authentication checks, and session management _(CrowdStrike, 2025)_ REFERENCE. This is not sufficient alone but it allows human testers to focus on more complex tests.
 
There are many potential weak points in the system, as it links to many external services, including both front-ends, Twitter, external agencies, and other parts of the internet being scraped for data. All of these should be covered by penetration tests (where testers attempt to breach security _(National Cyber Security Centre, 2017)_ REFERENCE). These are time-consuming, but necessary on a public-facing and critical system. To increase the effectiveness of penetration testing, Interactive Application Security Testing (IAST) can be injected into the application while the tests are being run _(Crowdstrike, 2025)_ REFERENCE. This is a low-cost way to increase the insight gained by tests, by looking at the internal application as it is running.
 
Fuzzing, which runs random/generative input/output tests _(BlackDuck, c.2026)_ REFERENCE, could also be used at this stage, but the results are often unclear and can take a lot of time for developers/testers to interpret and fix. With the above security testing in place, fuzzing is not necessary, given the time overhead.

## Staging Environment
The staging environment is a production-like environment for tests. The primary focus should be load testing. The application will have a high load on all of its endpoints, so all of these should be tested, both isolated and as a whole system. Benchmarks should be set based on expected traffic, which can be discussed with local authorities. This testing should also ensure that denial of service attacks can be flagged, and that mitigations for them are sufficient.
 
In addition to load testing, the user interfaces should be tested at this stage. In this case, exploratory testing is more appropriate than UAT, as the product owner is not the end user. Both UIs should be tested while attempting to simulate a high-stress environment, with different focuses. The call-centre site should allow users to quickly retrieve and convey information with a high volume of calls, and the public-facing site should be easy to navigate and prioritise showing easily digested advice over more complex details.

## Production Environment(s)
Finally, the application can be deployed. Beta testing versions could be released at this stage, or A/B tests could be used, but they are not necessary for this system. The focus of the application is to be functional and resilient in times of emergency, which is covered by the testing outlined above. While beta or A/B testing could find some usability issues, their primary function is to identify user preferences and refine UX. It would take lots of time and resource to find users, gather data, allow them to use the system, and respond to their results. It would not be worth the cost and it is more important that this system has reliable versions released quickly than having extra UI/usability testing. It is also important that advice being given is consistent, which could not be guaranteed with multiple versions in use at the same time. The agile process involves regular communication with the product owner, so most issues which could have been found in these stages of testing can be reported back and resolved this way instead.

---

<center><h2>References</h2></center>

[^1]: Black Duck. “Glossary: Fuzz Testing.” _Black Duck, c. 2026_, <https://www.blackduck.com/glossary/what-is-fuzz-testing.html>.

[^2]: Gale, Jamie. “Dynamic Application Security Testing (DAST) Explained.” _CrowdStrike, 15-04-2025_, <https://www.crowdstrike.com/en-us/cybersecurity-101/cloud-security/dynamic-application-security-testing-dast/>.

[^3]: Gale, Jamie. “Introduction to Interactive Application Security Testing (IAST).” _CrowdStrike, 10-04-2025_, <https://www.crowdstrike.com/en-us/cybersecurity-101/cloud-security/interactive-application-security-testing-iast/>.

[^4]: Kesavan, Elavarasi. “Shift-Left and Continuous Testing in Quality Assurance Engineering Ops and DevOps.” _International Journal of Scientific Research and Modern Technology, vol. 3, no. 1, p. 1, 2024_, <https://www.researchgate.net/publication/396863242_Shift-Left_and_Continuous_Testing_in_Quality_Assurance_Engineering_Ops_and_DevOps>.

[^5]: National Cyber Security Centre. “Penetration testing.” _National Cyber Security Centre, 08-08-2017_, <https://www.ncsc.gov.uk/guidance/penetration-testing>.

[^6]: Fellows, Matt. “What is contract testing and why should I try it?” _Pact Flow, 02-09-2023_, <https://pactflow.io/blog/what-is-contract-testing/>.

---
<br/>
<br/>

<center><h1>Part 2</h1></center>

## Assumptions
- Wind speeds can only be integers: it is not type-hinted, but the range() function is used.
- I do not need to test for negative (or other unreasonable) inputs: logical, but not specified in the brief or attempted anywhere in the code.
- I do not need to type check (except for a dictionary in update_storm): There is very little type hinting or attempt to type check throughout the code and I assume this is not intended to be a large number of the same bug.
- update_storm is for updating temperature and windspeed: Both of these might change. Name shouldn't

## Initial bug fixes
I think the below errors were just my linter being strict so I made some initial changes to prevent this from being an issue before starting testing, which I have outlined below.

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
Issue: Upper bound for category 1 not inside bound
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
Issue: Lower bound for f0 not inside bound
Fix: Use less than
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
Fix: Capitalise it
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

## Add storm
### Fail 1
![image](/screenshots/test_add_storm_duplicate_name_different_type.png)
```python
def test_add_storm_duplicate_name_different_type(storm_centre):
    storm_centre.add_storm(Hurricane("Ruby", 100))
    assert storm_centre.add_storm(Tornado("Ruby", 10)) == False
```
Issue: Duplicate name allowed when one of the types is a Hurricane
Fix: Correctly assign name in Hurricane
```python
def __init__(self, name, wind_speed):
        super().__init__(name, wind_speed) # replaced "none" with name
```
![image](/screenshots/test_add_storm_duplicate_name_different_type_FIX.png)

### Fail 2
![image](/screenshots/test_add_storm_invalid.png)
```python
class Cyclone (Storm):
    def __init__(self, name, wind_speed):
        super().__init__(name, wind_speed)
        
    def calculate_classification(self) -> str: # type hint
        return "Tropical"

    def get_advice(self) -> str: #type hint
        return "RUN"
    
def test_add_storm_invalid_type(storm_centre):
    assert storm_centre.add_storm(Cyclone("cyclone", 30)) == False
```
Issue: Storms which are not a Blizzard, Tornado or Hurricane can be added
Fix: Fix condition
```python
def add_storm(self, storm: Storm) -> bool:
    if (len(self.storm_list) <= 20
            and (isinstance(storm, Blizzard) or isinstance(storm, Tornado) or isinstance(storm, Hurricane)) # fixed this check
            and not self.already_exists(storm.name)): # refactored this line for ease of reading
        self.storm_list.append(storm)
        return True
    return False
```
![image](/screenshots/test_add_storm_invalid_FIX.png)

### Fail 3
![image](/screenshots/test_add_storm_21.png)
```python
def test_add_storm_21(storm_centre):
    for i in range(20):
        assert storm_centre.add_storm(Hurricane(str(i), 100)) == True
    assert storm_centre.add_storm(Hurricane("21", 100)) == False
```
Issue: More than 20 storms can be added
Fix: Ensure less than 20 storms are in centre before adding
```python
def add_storm(self, storm: Storm) -> bool:
    if (len(self.storm_list) < 20 # changed <= to <
            and (isinstance(storm, Blizzard) or isinstance(storm, Tornado) or isinstance(storm, Hurricane))
            and not self.already_exists(storm.name)):
        self.storm_list.append(storm)
        return True
    return False
```
![image](/screenshots/test_add_storm_21_FIX.png)

## Remove storm
### Fail 1
![image](/screenshots/test_remove_storm_doesnt_exist.png)
```python
def test_remove_storm_doesnt_exist(full_storm_centre):
    assert full_storm_centre.remove_storm("hello") == False
```
Issue: Does not indicate if removed storm not found
Fix: Make return value conditional
```python
def remove_storm(self, name: str) -> bool:
    for storm in self.storm_list:
        if name == storm.name:
            self.storm_list.remove(storm)
            return True # made this conditional
    return False # added default false return
```
![image](/screenshots/test_remove_storm_doesnt_exist_FIX.png)

## Update storm
I have created a helper function to test whether storms are equivalent
```python
def _equivalent(actual: Storm, expected: Storm) -> bool:
    if type(actual) != type (expected):
        return False
    if type(actual) == Blizzard and type(expected) == Blizzard:
        if (actual.wind_speed == expected.wind_speed
            and actual.temp == expected.temp
            and actual.name == expected.name):
            return True
        return False
    else:
        if (actual.wind_speed == expected.wind_speed
            and actual.name == expected.name):
            return True
        return False
```

### Fail 1
![image](/screenshots/test_update_storm_blizzard_temperature.png)
```python
def test_update_storm_blizzard_temperature(full_storm_centre):
    changes = {
        "temperature" : 30
    }
    assert full_storm_centre.update_storm("Ashley", changes) == True
    actual = full_storm_centre.view_storm("Ashley")
    expected = Blizzard("Ashley", 25, 30)
    assert _equivalent(actual, expected) == True
```
Issue: Update method using windspeed when it is not given
Fix: Make update conditional
```python
def update_storm(self, name, values) -> bool:
    if isinstance(values, dict):
        for storm in self.storm_list:
            if storm.name == name:
                if ("windspeed" in values): # added condition
                    storm.wind_speed = values["windspeed"]
                    return True
    else:
        raise Exception("Values must be provided as a dictionary")
    return False
```
![image](/screenshots/test_update_storm_blizzard_temperature_FIX1.png)
Initial issue was fixed.
New issue: Updating the temperature does not work
Fix: Add condition to update temperature
```python
def update_storm(self, name, values) -> bool:
    if isinstance(values, dict):
        for storm in self.storm_list:
            if storm.name == name:
                if ("temperature" in values): # added condition for temperature
                    if isinstance(storm, Blizzard):
                        storm.temp = values["temperature"]
                    else:
                        return False
                if ("windspeed" in values): # added condition
                    storm.wind_speed = values["windspeed"]
    else:
        raise Exception("Values must be provided as a dictionary")
    return True # replaced default with True and use False returns for error
```
![image](/screenshots/test_update_storm_blizzard_temperature_FIX2.png)

### Fail 2
![image](/screenshots/test_update_storm_nonexistent.png)
```python
def test_update_storm_nonexistent(full_storm_centre):
    changes = {
        "hello" : 30
    }
    assert full_storm_centre.update_storm("Violet", changes) == False
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 25)
    assert _equivalent(actual, expected) == True
```
Issue: Update returning true when key is invalid
Fix: Add check for valid keys only
```python
def update_storm(self, name, values) -> bool:
    if isinstance(values, dict):
        if (not (set(values.keys()).issubset({"temperature", "windspeed"}))): # added check for valid keys
            return False
        for storm in self.storm_list:
            if storm.name == name:
                if ("temperature" in values): # added condition for temperature
                    if isinstance(storm, Blizzard):
                        storm.temp = values["temperature"]
                    else:
                        return False
                if ("windspeed" in values): # added condition
                    storm.wind_speed = values["windspeed"]
    else:
        raise Exception("Values must be provided as a dictionary")
    return True # replaced default with True and use False returns for errors
```
![image](/screenshots/test_update_storm_nonexistent_FIX.png)

### Fail 3
![image](/screenshots/test_update_storm_doesnt_exist.png)
```python
def test_update_storm_doesnt_exist(full_storm_centre):
    changes = {
        "temperature" : 30
    }
    assert full_storm_centre.update_storm("hello", changes) == False
    actual_violet = full_storm_centre.view_storm("Violet")
    actual_wubbo = full_storm_centre.view_storm("Wubbo")
    actual_ashley = full_storm_centre.view_storm("Ashley")
    expected = [Hurricane("Violet", 25), Tornado("Wubbo", 25), Blizzard("Ashley", 25, -12)]
    assert _equivalent(actual_violet, expected[0]) == True
    assert _equivalent(actual_wubbo, expected[1]) == True
    assert _equivalent(actual_ashley, expected[2]) == True
```
Issue: Not returning False when updating storm which doesn't exist
Fix: Check storm exists before updating
```python
def update_storm(self, name, values) -> bool:
    if isinstance(values, dict):
        if (not self.already_exists(name)): # added check for storm existence
            return False
        if (not (set(values.keys()).issubset({"temperature", "windspeed"}))): # added check for valid keys
            return False
        for storm in self.storm_list:
            if storm.name == name:
                if ("temperature" in values): # added condition for temperature
                    if isinstance(storm, Blizzard):
                        storm.temp = values["temperature"]
                    else:
                        return False
                if ("windspeed" in values): # added condition
                    storm.wind_speed = values["windspeed"]
    else:
        raise Exception("Values must be provided as a dictionary")
    return True # replaced default with True and use False returns for errors
```
![image](/screenshots/test_update_storm_doesnt_exist_FIX.png)

### Fail 4
![image](/screenshots/test_update_storm_empty_dict.png)
```python
def test_update_storm_empty_dict(full_storm_centre):
    changes: dict = {}
    assert full_storm_centre.update_storm("Violet", changes) == False
    actual = full_storm_centre.view_storm("Violet")
    expected = Hurricane("Violet", 25)
    assert _equivalent(actual, expected) == True
```
Issue: Update with an empty dict returns True
Fix: Add check for empty dict
```python
def update_storm(self, name, values) -> bool:
    if isinstance(values, dict):
        if (not self.already_exists(name)): # added check for storm existence
            return False
        if (not (set(values.keys()).issubset({"temperature", "windspeed"})) # added check for valid keys
            or len(values.keys()) == 0): # added check for empty dict
            return False
        for storm in self.storm_list:
            if storm.name == name:
                if ("temperature" in values): # added condition for temperature
                    if isinstance(storm, Blizzard):
                        storm.temp = values["temperature"]
                    else:
                        return False
                if ("windspeed" in values): # added condition
                    storm.wind_speed = values["windspeed"]
    else:
        raise Exception("Values must be provided as a dictionary")
    return True # replaced default with True and use False returns for errors
```
![image](/screenshots/test_update_storm_empty_dict_FIX.png)

## All tests
![image](screenshots/complete_tests.png)