test_score = int(input("What's your test score"))

if test_score >= 90:
    print("The grade is A.")
elif test_score >= 80:
    print("The grade is B.")
elif test_score >= 70:
    print("The grade is C.")
elif test_score >= 60:
    print("The grade is D.")
else:
    print("Oh Shucks....You failed!!")

for number in range(10):
    print(number)

counties = ["Greene","Motgomery","Akron","Mason"]

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe":422829, "Denver":463353, "Jefferson":498715}
for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))

for key, value in counties_dict.items():
    print(key,value)

for key, value in counties_dict.items():
    print(key," county has ",value," voters.")

voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":498715}]
print("*****************")
for county_dict in voting_data:
    print(county_dict)
print("**********************")
for i in range(len(voting_data)):
      print(voting_data[i].get("county"))

print("*$*$*$*$*$*$*$")
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

print("*$*$*$*$*$*$*$")
for county_dict in voting_data:
    print(county_dict['registered_voters'])

print("*$*$*$*$*$*$*$")
county_dict = {"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for (key,value) in county_dict.items():
    print(f"{key} county has {value} registered voters.")

print("*$*$*$*$*$*$*$")
voting_data = [{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]
for i in range(len(voting_data)):
      County = voting_data[i].get("county")
      Voters = voting_data[i].get("registered_voters")
      print(f"{County} county has {Voters:,} registered voters")

