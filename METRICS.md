# Metrics

This is a quick reference sheet of all of the health metrics HealthBox is capable of storing and managing. However, if you're a developer, you should also look at `metrics.py` for a more in-depth lay out of what information should be submitted for each metric.

## Notes

- In general, a sample that overlaps midnight (For example, 11:57 PM to 12:03 AM), should try to be avoided, since it can lead to confusion when programs read the metric data back.
- `meal id` and `food id` are used to keep track of which nutrition samples are part of the same foods and meals. For example, if a user has cereal for breakfast, a program would submit nutritional data for the cereal and milk with the same `meal ID`, but differing `food IDs`. This makes it considerably easier for programs to read back information, and determine which nutrient samples are tied back to the same instance of food. `meal IDs` and `food IDs` are unique, and don't overlap, even if the same food is logged twice. For example, if the user eats cereal two days in a row, both instances of the meal would have different meal IDs and food IDs, even though the actual food consumed is the same.

---

## Activity

### Steps

[steps count, start time, end time]

The `steps` metric is used to keep track of steps over a defined span of time. For example, this metric may be used to submit data that 'the user took 35 steps from 10:15 AM to 10:18 AM'. Ideally, the span of time between 'start time' and 'end time' should be just a few minutes at most for sake of more precise data.

### Active Calories

[calories burned, start time, end time]

The `active calories` metric contains information about how many calories are burned during activity. If the user is at rest and sitting down, this number should be about 0. `Active calories` only includes calories burned above the normal amount of calories burned at rest.

### On Foot Distance

[kilometers traveled, start time, end time]

`On foot distance` is the measure of the distance traveled unassisted through walking or running in kilometers. This does not include distance travelled on bicycles, cars, or other vehicles.

### Resting Calories

[calories burned, start time, end time]

`Resting calories` are calories burned at rest, while not participating in physical activity. `Resting calories` is the baseline of how many calories are burned before exercising in order to determine how many additional calories are being burned by physical activity.

### Active Minutes

[start time, end time]

`Active minutes` are any minutes spent up and moving around.

### Wheelchair Pushes

[push count, start time, end time]

`Wheelchair pushes` keeps track of how many times a user in a wheelchair pushes to move. Ideally, the span of time between 'start time' and 'end time' should be just a few minutes at most.

### Wheelchair Distance

[kilometers traveled, start time, end time]

`Wheelchair distance` measures the distance travelled unassisted by wheelchair, measured in kilometers.

### Minutes Standing

[start time, end time]

`Minutes standing` specifies a stretch of time during which the user was standing. There is no requirement for the user to be moving around during this time, just as long as they are standing. Samples for this metric should stretch from the time the user stood up to the time the user sat down. Breaking up a session of standing into different samples can lead to confusion when reading the metric data.


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

`Mindful minutes` are any time spent being mindful. This includes time spend focused on breathing, time spend meditating, etc. Samples for this metric should stretch from the time the user started being mindful to the time the user went back to their day as normal.

### Mood

[mood (string), time]

`Mood` specifies the users mood at a given time as a single word emotion. For example, you may specify that the user is feeling 'happy', or 'stressed'.

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
