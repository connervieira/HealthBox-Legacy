# Metrics

This is a quick reference sheet of all of the health metrics HealthBox is capable of storing and managing. However, if you're a developer, you should also look at `metrics.py` for a more in-depth lay out of what information should be submitted for each metric.

## Activity

### Steps
[steps count, start time, end time]

### Active Calories
[calories burned, start time, end time]

### On Foot Distance
[kilometers traveled, start time, end time]

### Resting Calories
[calories burned, start time, end time]

### Active Minutes
[start time, end time]

### Wheelchair Pushes
[push count, start time, end time]

### Wheelchair Distance
[kilometers traveled, start time, end time]

### Minutes Standing
[start time, end time]

## Mental Health
### PHQ-9 Score
[score, date]

### Y-BOCS Score
[score, date]

### GAD-7 Score
[score, date]

### MDQ Score
[score, date]

### ASRS Score
[score, date]

### Mindful Minutes
[type of mindfulness (string), start time, end time]

### Mood
[mood (string), time]

### Sexual Activity
[safe (boolean), time]

## Nutrition
### Calories
[amount, time, meal id, food id]

### Water
[amount (ml), time, meal id, food id]

### Sugar
[amount (grams), time, meal id, food id]

### Fiber
[amount (grams), time, meal id, food id]

### Protein
[amount (grams), time, meal id, food id]

### Saturated Fat
[amount (grams), time, meal id, food id]

### Trans Fat
[amount (grams), time, meal id, food id]

### Monosaturated Fat
[amount (grams), time, meal id, food id]

### Polysaturated Fat
[amount (grams), time, meal id, food id]

### Calcium
[amount (mg), time, meal id, food id]

### Carbohydrates
[amount (grams), time, meal id, food id]

### Cholesterol
[amount (mg), time, meal id, food id]

### Iron
[amount (mg), time, meal id, food id]

### Sodium
[amount (mg), time, meal id, food id]

### Vitamin A
[amount (mcg), time, meal id, food id]

### Vitamin B6
[amount (mcg), time, meal id, food id]

### Vitamin B12
[amount (mcg), time, meal id, food id]

### Vitamin C
[amount (mcg), time, meal id, food id]

### Vitamin D
[amount (mcg), time, meal id, food id]

### Vitamin E
[amount (mcg), time, meal id, food id]

### Vitamin K
[amount (mcg), time, meal id, food id]

### Zinc
[amount (mg), time, meal id, food id]

### Biotin
[amount (mcg), time, meal id, food id]

### Caffeine
[amount (mg), time, meal id, food id]

### Chloride
[amount (mEq), time, meal id, food id]

### Copper
[amount (mg), time, meal id, food id]

### Folate
[amount (mcg), time, meal id, food id]

### Iodine
[amount (mcg), time, meal id, food id]

### Magnesium
[amount (mg), time, meal id, food id]

### Manganese
[amount (mg), time, meal id, food id]

### Molybdenum
[amount (mg), time, meal id, food id]

### Niacin
[amount (mg), time, meal id, food id]

### Pantothenic Acid
[amount (mg), time, meal id, food id]

### Phosphorous
[amount (mg), time, meal id, food id]

### Potassium
[amount (mg), time, meal id, food id]

### Riboflavin
[amount (mg), time, meal id, food id]

### Selenium
[amount (mcg), time, meal id, food id]

### Thiamin
[amount (mg), time, meal id, food id]


## Measurements

### Weight
[weight (kg), time measured]

### Height
[height (m), time measured]

### Biological Sex
[gender at birth]

### Gender
[gender identity]

### Body Temperature
[body temperature (c), time measured]

### Electrodermal Activity
[measurement (μS), time measured]

### Waist Circumference
[circumference (cm), time measured]

### Breathing Rate
[breathes per minute, time measured]

### Oxygen Saturation
[measurement percentage, time measured]

### Heart Rate
[beats per minute, time measured]

### Resting Heart Rate
[beats per minute, time measured]

### Walking Heart Rate
[beats per minute, time measured]

### Running Heart Rate
[beats per minute, time measured]

### Heart Rate Variability
[variation (ms), time measured]

### Peripheral Perfusion Inex
[measurement percentage, time measured]

### Lung Capacity
[measurement (L), time measured]

### VO2 Max
[measurement (mL/(kg\*min)), time measured]

### Ailments
[ailment, start time, approximate end time]

### Blood Pressure
[systolic measurement (mmHg), diastolic measurement (mmHg), time measured]

### Blood Sugar
[measurement (mg/dl), time measured]

### Blood Alcohol Content
[measurement (g/100mL), time measured]

### Sound Exposure
[average volume (dB), start time, end time]

### Sleep
[sleep stage, start time, end time]

### Times Fallen
[time]

### Atypical Pulse
[abnormal heart rate measurement, time]

### Audiogram
[minimum audible volume, ear (left/right), time]
