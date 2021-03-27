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

The `on foot distance` metric measures how far the user walked or ran between two stretches of time without outside physical assistance. Distance travelled by car, bike, or wheelchair does not belong in this metric. For sake of precise data, you should try to submit data in smaller time increments, around 5 to 15 minutes. However, the start and end time can be hours apart if your tracking method doesn't allow for data this precise.

`On foot distance` is the measure of the distance traveled unassisted through walking or running in kilometers. This does not include distance travelled on bicycles, cars, or other vehicles.

### Resting Calories

[calories burned, start time, end time]

`Resting calories` are calories burned at rest, while not participating in physical activity. `Resting calories` is the baseline of how many calories are burned before exercising in order to determine how many additional calories are being burned by physical activity.

### Active Minutes

[start time, end time]

`Active minutes` are any minutes spent up and moving around. This includes time walking, running, riding a bike, or moving in a wheel chair. Physically taxing activities like working out or driving a car in a sport context are also included even if they don't explicitly involve standing and moving.

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

The `weight` metric is for recording the user's weight over time, in kilograms.

### Height

[height (m), time measured]

The `height` metric is for recording the user's height over time, in meters.

### Biological Sex

[gender at birth]

The `biological sex` metric is used to store the user's biological gender, at birth. It is a one character string that can be 'M' for male, 'F' for female, or 'I' for intersex. This metric is seperate from the `gender` metric, and they shouldn't be used interchangably. For calculations dependent on sex, like motabolism, this metric should be used instead of the `gender` metric.

### Gender

[gender identity]

The `gender` metric is used to define the user's psychological gender identity. It can be any short string, but for sake of standardization it's advised to be something like "male", "female", "non-binary", or another commonly defined gender identity.

### Sexuality

[sexuality]

The `sexuality` metric is used to define the user's sexuality, in terms of who they are attracted to. It is represented by a 1 character string, and can be "S" for straight (attracted to the opposite biological sex), "G" for gay (attracted to the same biological sex), "B" for bi-sexual (attracted to both biological sexes), or "A" for asexual (not attracted to either biological gender).

### Body Temperature

[body temperature (c), time measured]

This metric stores a measurement of the user's body temperature at a given time, measured in Celcius.

### Electrodermal Activity

[measurement (μS), time measured]

The `electrodermal activity` metric measures the user's skin's electrodermal activity, which is an indicator of how much sweat is present.

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

`Walking heart rate` measurements are heart rate measurements recorded after the user has been walking for a moderate period of time. These measurements should be made while the user is walking after about 2 minutes of consistent pace.

### Running Heart Rate

[beats per minute, time measured]

`Running heart rate` measurements are heart rate measurements recorded after the user has been running for a moderate period of time. These measurements should be made while the user is running after about 5 minutes of consistent pace.

### Heart Rate Variability

[variation (ms), time measured]

`Heart rate variability` measures the variation in the length of time between heart beats. For example, if the length of time between beat 1 and 2 is 900ms, and the length of time between beat 2 and 3 is 850ms, the heart rate variabilty would be considered to be 50ms.

### Peripheral Perfusion Index

[measurement percentage, time measured]

The `peripheral perfusion index` is a measure of how much the strength of the pulse changes based on where on the body it is measured.

### Lung Capacity

[measurement (L), time measured]

### VO2 Max

[measurement (mL/(kg\*min)), time measured]

### Ailments

[ailment, start time, approximate end time]

The `ailments` metric is used to store generic information about physical and mental ailments. The `ailment` should be a relatively short string that concisely defines the ailment. For example, 'broken ankle', or 'dislocated thumb' would be appropriate. The `start time` should be the time and date the ailment occured, and the `end date` should be the approximate date and time where the ailment no longer had a signficant impact on the user's daily activities. Many ailments, especially mental ones, very frequently don't have a concern start or end time. Therefore, you should be careful when using the `start time` and `end time` fields for anything more than a general idea of which ailments a user has at a given point in time.

### Blood Pressure

[systolic measurement (mmHg), diastolic measurement (mmHg), time measured]

### Blood Sugar

[measurement (mg/dl), time measured]

### Blood Alcohol Content

[measurement (g/100mL), time measured]

### Sound Exposure

[average volume (dB), start time, end time]

`Sound exposure` records periods of time in which the user was exposed to certain sound levels. This information is useful in identifying causes of hearing loss. The span of time between `start time` and `end time` should be very short, unless the sound level was very continuously loud. For example, at a concert, sound levels change dramatically and rapidly depending on parts in the song, so sound exposure should be recorded in increments of a few seconds. If the sound is instantaneous, like in the case of a gun shot, the `start time` and `end time` may even be the same.

### Sleep

[sleep stage, start time, end time]

### Times Fallen

[time]

### Atypical Pulse

[abnormal heart rate measurement, time]

An `atypical pulse` is any time that the user's pulse is inconsistent with what it would usually be given current physical activity. For example, if a user has a resting heart rate of 60 BPM, and they haven't been moving for an hour, but their heart rate increases to 100 BPM, this would be considered an abnormal heart rate. Likewise, a heart rate lower than usual would also be considered an atypical pulse. These instances of abnormal heart rate are often correlated with mental stimulation, like when watching a horror movie, but could also be correlated to serious health issues.

### Audiogram

[minimum audible volume, ear (left/right), time]

An `audiogram` can help detect hearing loss by determining how loud a sound has to be before the user can hear it. These measurements should be taken individually for each ear.
