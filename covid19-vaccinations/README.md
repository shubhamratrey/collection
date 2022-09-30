# Find COVID Vaccination Slot

## Prerequisites

Add these dependencies before starting anything.

```groovy
requests
```

### Get Your District Id

1. Find your **cowin_state_id** by
   hitting [API](https://ratrey.in/v1/covid19/locations/) <br /> ``https://ratrey.in/v1/covid19/locations/``
2. Add **cowin_state_id** to param and hit [API](https://ratrey.in/v1/covid19/locations/)
   again <br /> ``https://ratrey.in/v1/covid19/locations/?state_id=7``
3. Use the **cowin_district_id** to check slots availability

### Check for slots

```
from vaccine_slots_finder import VaccineSlotsFinder
sf = VaccineSlotsFinder(district_id=125)
print(sf.params, sf.headers)
print(sf.AGE_AVAILABLE_CAPACITY)
print(sf.is_18_plus_slot_available)
print(sf.is_45_plus_slot_available)

```

### Or you can check by using this [API](https://ratrey.in/v1/covid19/slots/?district_slug=korba)

`https://ratrey.in/v1/covid19/slots/?district_slug=korba`


