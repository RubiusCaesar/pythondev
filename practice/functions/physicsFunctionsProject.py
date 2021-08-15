# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

# Temperature calculations
# fahrenheit to celcius
def f_to_c(f_temp):
    c_temp = round(float((f_temp - 32) * (5/9)), 2)
    return c_temp


f100_in_celcius = f_to_c(100)
print(f100_in_celcius)

# celcius to fahrenheit


def c_to_f(c_temp):
    f_temp = round(float(c_temp * (9/5) + 32), 2)
    return f_temp


c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Force and Energy Calculations
# Force equation F = M x A


def get_force(mass, acceleration):
    return mass * acceleration


train_force = get_force(train_mass, train_acceleration)
print(train_force)
print("The GE train supplies {force} Newtons of force.".format(
    force=train_force))

# Energy Equation
c = 3*10**8


def get_energy(mass):
    return mass * c**2


bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies {en} Joules of energy.".format(en=bomb_energy))

# Work Equation


def get_work(mass, acceleration, distance):
    temp_force = get_force(mass, acceleration)
    return temp_force * distance


train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does {wk} Joules of work over {ds} meters.".format(
    wk=train_work, ds=train_distance))
