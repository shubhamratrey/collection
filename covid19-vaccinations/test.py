from vaccine_slots_finder import VaccineSlotsFinder

if __name__ == '__main__':
    sf = VaccineSlotsFinder(district_id=125)
    print(sf.params, sf.headers)
    print(sf.AGE_AVAILABLE_CAPACITY)
    print(sf.is_18_plus_slot_available)
    print(sf.is_45_plus_slot_available)
