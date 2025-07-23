airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
airports['RIC'] = "Richmond"
airports['IAD'] = "Herndon"

print(f"{'IAD' in airports = }")
print(f"{airports['MCO'] = }")
print(f"{airports.get('VCE') = }")
print(f"{airports.get('VCE', 'NOT FOUND') = }")
print(f"{airports.get('MCO', 'NOT FOUND') = }")
print(f"{airports.setdefault('VCE', 'Venice') = }")
print(f"{airports = }")


for code, location in airports.items():
    print(code, location)
print('-' * 60)
for code in airports:
    print(code)
print('-' * 60)
print(f"{airports.values() = }")



