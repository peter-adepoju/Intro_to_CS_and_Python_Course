# ============================================================
# ANSWER KEY FOR DAY 12 PRACTICE EXERCISES
# ============================================================
"""
# Exercise 1:
def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

print(rectangle_area(6, 4))        # 24
print(rectangle_perimeter(6, 4))   # 20

# Exercise 2:
def power(base, exponent=2):
    return base ** exponent

print(power(5))        # 25
print(power(2, 10))    # 1024

# Exercise 3:
order_summary("Widget", 3, 5.00)              # all positional
order_summary("Gadget", 2)                     # uses default price
order_summary(price_each=12.50, item="Gizmo", quantity=4)  # all keyword, reordered

# Exercise 4:
def clamp(value, minimum=0, maximum=100):
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

print(clamp(50))         # 50 (within range)
print(clamp(-10))        # 0  (clamped to minimum)
print(clamp(150))        # 100 (clamped to maximum)
print(clamp(5, 10, 20))  # 10 (custom range, clamped to minimum)

# Challenge:
def bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi_value):
    if bmi_value < 18.5:
        return "Underweight"
    elif bmi_value < 25:
        return "Normal"
    elif bmi_value < 30:
        return "Overweight"
    else:
        return "Obese"

category = bmi_category(bmi(70, 1.75))
print(category)   # Normal
"""