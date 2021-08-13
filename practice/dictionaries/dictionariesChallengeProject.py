# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


def convert_damages(damages):
    converted_damages = []
    for record in damages:
        if record == 'Damages not recorded':
            converted_damages.append(record)
        elif record[-1:] == 'M':
            temp_record = float(record[0:-1]) * conversion["M"]
            converted_damages.append(temp_record)
        else:
            temp_record = float(record[0:-1]) * conversion["B"]
            converted_damages.append(temp_record)
    return converted_damages


# test function by updating damages
conv_damages = convert_damages(damages)
print(conv_damages)

# 2
# Create a Table


def create_dict(names, months, years, max_wind, areas_affected, conv_damages, deaths):
    hurricanes = {}
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        hurricanes[names[i]] = {"Name": names[i],
                                "Month": months[i],
                                "Year": years[i],
                                "Max Sustained Wind": max_sustained_winds[i],
                                "Areas Affected": areas_affected[i],
                                "Damage": conv_damages[i],
                                "Deaths": deaths[i]}
    return hurricanes


# Create and view the hurricanes dictionary
hurricane_dict = create_dict(
    names, months, years, max_sustained_winds, areas_affected, conv_damages, deaths)
print(hurricane_dict)

# 3
# Organizing by Year


def year_cane(cane_dict):
    year_cane = {}
    for cane in cane_dict:
        current_year = cane_dict[cane]["Year"]
        current_cane = cane_dict[cane]
        if current_year in year_cane:
            year_cane[current_year].append(current_cane)
        else:
            year_cane[current_year] = [current_cane]
    return year_cane


# create a new dictionary of hurricanes with year and key
hurricanes_by_year = year_cane(hurricane_dict)
print(hurricanes_by_year)
print(hurricanes_by_year[1932])

# 4
# Counting Damaged Areas


def count_areas(cane_dict):
    area_dict = {}
    for cane in cane_dict:
        for area in cane_dict[cane]["Areas Affected"]:
            if area not in area_dict:
                area_dict[area] = 1
            else:
                area_dict[area] += 1
    return area_dict


# create dictionary of areas to store the number of hurricanes involved in
hurricane_areas = count_areas(hurricane_dict)
print(hurricane_areas)
# 5
# Calculating Maximum Hurricane Count


def most_affected(area_dict):
    max_area = ''
    max_area_count = 0
    for area in area_dict:
        if area_dict[area] > max_area_count:
            max_area = area
            max_area_count = area_dict[area]
    return max_area, max_area_count


# find most frequently affected area and the number of hurricanes involved in
most_affected_area, most_affected_area_count = most_affected(hurricane_areas)
print(most_affected_area, most_affected_area_count)

# 6
# Calculating the Deadliest Hurricane


def deadliest_cane(cane_dict):
    deadliest_cane = ''
    deadliest_cane_deaths = 0
    for cane in cane_dict:
        if cane_dict[cane]["Deaths"] > deadliest_cane_deaths:
            deadliest_cane = cane_dict[cane]["Name"]
            deadliest_cane_deaths = cane_dict[cane]["Deaths"]
    return deadliest_cane, deadliest_cane_deaths


# find highest mortality hurricane and the number of deaths
deadliest_hurricane, most_deaths = deadliest_cane(hurricane_dict)
print(deadliest_hurricane, most_deaths)
# 7
# Rating Hurricanes by Mortality


def mortality_rating(cane_dict):
    mortality_scale = {0: 0,
                       1: 100,
                       2: 500,
                       3: 1000,
                       4: 10000}
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in cane_dict:
        death_count = cane_dict[cane]['Deaths']
        if death_count == mortality_scale[0]:
            hurricanes_by_mortality[0].append(cane_dict[cane])
        elif death_count > mortality_scale[0] and death_count <= mortality_scale[1]:
            hurricanes_by_mortality[1].append(cane_dict[cane])
        elif death_count > mortality_scale[1] and death_count <= mortality_scale[2]:
            hurricanes_by_mortality[2].append(cane_dict[cane])
        elif death_count > mortality_scale[2] and death_count <= mortality_scale[3]:
            hurricanes_by_mortality[3].append(cane_dict[cane])
        elif death_count > mortality_scale[3] and death_count <= mortality_scale[4]:
            hurricanes_by_mortality[4].append(cane_dict[cane])
        elif death_count > mortality_scale[4]:
            hurricanes_by_mortality[5].append(cane_dict[cane])
    return hurricanes_by_mortality


# categorize hurricanes in new dictionary with mortality severity as key
mortality_dict = mortality_rating(hurricane_dict)
print(mortality_dict)

# 8 Calculating Hurricane Maximum Damage


def most_destructive_cane(cane_dict):
    most_destructive_cane = ''
    most_destructive_cane_damage = 0
    for cane in cane_dict:
        if cane_dict[cane]["Damage"] == "Damages not recorded":
            pass
        elif cane_dict[cane]["Damage"] > most_destructive_cane_damage:
            most_destructive_cane = cane_dict[cane]["Name"]
            most_destructive_cane_damage = cane_dict[cane]["Damage"]
    return most_destructive_cane, most_destructive_cane_damage


# find highest damage inducing hurricane and its total cost
most_destructive_cane, most_damage = most_destructive_cane(hurricane_dict)
print(most_destructive_cane, most_damage)

# 9
# Rating Hurricanes by Damage


def damage_scale(cane_dict):
    damage_scale = {0: 0,
                    1: 100000000,
                    2: 1000000000,
                    3: 10000000000,
                    4: 50000000000}
    canes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for cane in cane_dict:
        damage = cane_dict[cane]["Damage"]
        if damage == damage_scale[0] or damage == "Damages not recorded":
            canes_by_damage[0].append(cane_dict[cane])
        elif damage > damage_scale[0] and damage <= damage_scale[1]:
            canes_by_damage[1].append(cane_dict[cane])
        elif damage > damage_scale[1] and damage <= damage_scale[2]:
            canes_by_damage[2].append(cane_dict[cane])
        elif damage > damage_scale[2] and damage <= damage_scale[3]:
            canes_by_damage[3].append(cane_dict[cane])
        elif damage > damage_scale[3] and damage <= damage_scale[4]:
            canes_by_damage[4].append(cane_dict[cane])
        elif damage > damage_scale[4]:
            canes_by_damage[5].append(cane_dict[cane])
    return canes_by_damage


# categorize hurricanes in new dictionary with damage severity as key
destruction_dict = damage_scale(hurricane_dict)
print(destruction_dict)
