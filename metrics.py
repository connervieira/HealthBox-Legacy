import utils # utils.py


# The metrics are broken up into individual categories: Activity, Mental Health, Nutrition, and Measurements
# Should you want to add metrics, this is where to do it. However, only add metrics at the end of the categories. Adding metrics at the top or in the middle of categories will shift other metrics down, changing the ID they use. This will break compatibility with programs.


# Each metric contains its name, description, a template containing what information should be in each submission, and in what order, for sake of input validation, and a list of what the 'keys' of submitted data should be.
# Below is a list of validation terms, and what they correspond to. This template only contains what type of information should be in each submission. If you'd like to see what each piece of submission data actually represents, see METRICS.md and the 'keys' value in the database

# int: A positive whole number
# float: A positive decimal number
# start_time: A Unix timestamp before end_time
# end_time: A Unix timestamp after start_time
# datetime: A Unix timestamp
# short_string: A string under 20 characters
# long_string: A string under 150 characters
# boolean: A 'true' or 'false' value
# uuid: An 32 hexidecimal character long UUID
# sex: A 1 character string: M, F, or I
# sexuality: A 1 character string: S, G, B, or A
# temperature: A positive or negative float, above -273
# percentage: A decimal number ranged 0 to 100, including 0 and 100
# side: A 1 character string: L or R



# List of metric categories and the metrics they contain
metric_categories = [
 	# Metric category: dictionary with various attributes of each category of metric
	{
		"name": "Activity",
		"id": "A",
		"color": utils.color.RED,
		"metrics": [
			{"name": "Steps", "description": "How many steps are taken", "validation": ["int", "start_time", "end_time"], "keys": ["steps_count", "start_time", "end_time"]},
			{"name": "Active Calories", "description": "How many calories have been burned, not including calories burned while resting.", "validation": ["int", "start_time", "end_time"], "keys": ["calories", "start_time", "end_time"]},
			{"name": "On Foot Distance", "description": "Distance traveled through walking, running, or otherwise on foot", "validation": ["float", "start_time", "end_time"], "keys": ["distance", "start_time", "end_time"]},
			{"name": "Resting Calories", "description": "How much energy is burned while resting", "validation": ["int", "start_time", "end_time"], "keys": ["calories", "start_time", "end_time"]},
			{"name": "Active Minutes", "description": "How many minutes are spent moving around, being active", "validation": ["start_time", "end_time"], "keys": ["minutes", "start_time", "end_time"]},
			{"name": "Wheelchair Pushes", "description": "How many times the wheels on a wheelchair are pushed", "validation": ["int", "start_time", "end_time"], "keys": ["pushes", "start_time", "end_time"]},
			{"name": "Wheelchair Distance", "description": "Total distance traveled by manual wheel chair movement", "validation": ["int", "start_time", "end_time"]},
			{"name": "Minutes Standing", "description": "Minutes spent standing", "validation": ["start_time", "end_time"], "keys": ["start_time", "end_time"]}
		]
	},
	{
		"name": "Mental Health",
		"id": "B",
		"color": utils.color.CYAN,
		"metrics": [
			{"name": "PHQ-9 Score (Depression Test)", "description": "PHQ-9 scores can be an indicator of depression, and its severity", "validation": ["int", "datetime"], "keys": ["score", "time"]},
			{"name": "Y-BOCS Score (OCD Test)", "description": "Y-BOCS scores can be an indicator of obessive-compulsive disorder, and its severity.", "validation": ["int", "datetime"], "keys": ["score", "time"]},
			{"name": "GAD-7 Score (Anxiety Test)", "description": "GAD-7 scores can be an indicator of anxiety, and its severity", "validation": ["int", "datetime"], "keys": ["score", "time"]},
			{"name": "MDQ Score (Bipolar Test)", "description": "MDQ scores can be an indicator of bipolar disorder, and its severity", "validation": ["int", "datetime"], "keys": ["score", "time"]},
			{"name": "ASRS Score (ADHD Test)", "description": "ASRS scores can be an indicator of ADHD, and its severity", "validation": ["int", "datetime"], "keys": ["score", "time"]},
			{"name": "Mindful Minutes", "description": "Minutes spent being mindful of thoughts, emotions, and feelings", "validation": ["short_string", "start_time", "end_time"], "keys": ["type_of_mindfulness", "start_time", "end_time"]},
			{"name": "Mood", "description": "The current mood at a point in time", "validation": ["short_string", "datetime"], "keys": ["mood", "time"]},
			{"name": "Sexual Activity", "description": "Sexual activity with a partner", "validation": ["boolean", "datetime"], "keys": ["safe", "time"]}
		]
	},
	{
		"name": "Nutrition",
		"id": "C",
		"color": utils.color.GREEN,
		"metrics": [
			{"name": "Calories", "description": "", "validation": ["int", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Water", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Sugar", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Fiber", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Protein", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Saturated Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Trans Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Monosaturated Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Polysaturated Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Unspecified Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Calcium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Carbohydrates", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Cholesterol", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Iron", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Sodium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Vitamin A", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Vitamin B6", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Vitamin B12", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Vitamin C", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Vitamin D", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Vitamin E", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Vitamin K", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Zinc", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Biotin", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Caffeine", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Chloride", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Copper", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Folate", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Iodine", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Magnesium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Manganese", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Molybdenum", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Niacin", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Pantothenic Acid", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Phosphorus", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Potassium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Riboflavin", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Selenium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"], "keys": ["amount", "time", "mealid", "foodid"]},
			{"name": "Thiamin", "description": "", "validation": ["float", "datetime", "uuid", "uuid",], "keys": ["amount", "time", "mealid", "foodid"]}
		]
	},
	{
		"name": "Measurements",
		"id": "D",
		"color": utils.color.YELLOW,
		"metrics": [
			{"name": "Weight", "description": "Total body weight", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Height", "description": "Total height when standing straight upright", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Biological Sex", "description": "Gender as identified at birth", "validation": ["sex"], "keys": ["sex"]},
			{"name": "Gender", "description": "Gender as defined by which gender one identifies with", "validation": ["short_string"], "keys": ["gender"]},
			{"name": "Sexuality", "description": "Who one is attracted to sexually", "validation": ["sexuality"], "keys": ["sexuality"]},
			{"name": "Body Temperature", "description": "Measure of the temperature of the body ", "validation": ["measurement", "datetime"], "keys": ["temperature", "time"]},
			{"name": "Electrodermal Activity", "description": "Electrodermal activity serves as an indicator of how much sweat is on the skin.", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Waist Circumference", "description": "The measurement of the circumference of the waist", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Breathing Rate", "description": "How many breaths taken each minute", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Oxygen Saturation", "description": "How much oxygen in present in the blood", "validation": ["percentage", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Heart Rate", "description": "How many times per minute the heart beats", "validation": ["int", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Resting Heart Rate", "description": "Heart rate, measured while sitting, and inactive", "validation": ["int", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Walking Heart Rate", "description": "Heart rate, measured at a steady walking pace", "validation": ["int", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Running Heart Rate", "description": "Heart race, measured at a steady run", "validation": ["int", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Heart Rate Variability", "description": "Variation in the time interval between heart beats", "validation": ["int", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Peripheral Perfusion Index", "description": "Relative strength of the pulse at various points on the body", "validation": ["percentage", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Lung Capacity", "description": "How much air the lungs are capable of holding", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "VO2 Max", "description": "The maximum amount of oxygen burned while exercising", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Ailments", "description": "A record of injuries and illnesses, both mental and physical", "validation": ["long_string", "start_time", "end_time"], "keys": ["ailment", "start_time", "end_time"]},
			{"name": "Blood Pressure", "description": "The pressure at which blood pushes against the walls of the arteries", "validation": ["int", "int", "datetime"], "keys": ["systolic", "diastolic", "time"]},
			{"name": "Blood Sugar", "description": "The amount of glucose in the blood", "validation": ["int", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Blood Alcohol Content", "description": "The amount of alcohol in the blood", "validation": ["float", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Sound Exposure", "description": "Periods of time exposed to sounds of a certain volume", "validation": ["int", "start_time", "end_time"], "keys": ["decibles", "start_time", "end_time"]},
			{"name": "Sleep", "description": "Record of periods of sleep in its various stages", "validation": ["short_string", "start_time", "end_time"], "keys": ["sleep_stage", "start_time", "end_time"]},
			{"name": "Times Fallen", "description": "Times unintentionally fallen, with or without injury", "validation": ["datetime"], "keys": ["time"]},
			{"name": "Atypical Pulse", "description": "A record of occasions on which heart rate was atypically fast or slow.", "validation": ["int", "datetime"], "keys": ["measurement", "time"]},
			{"name": "Audiogram", "description": "A test used to determine how loud a sound has to be to be heard.", "validation": ["int", "side", "datetime"], "keys": ["decibles", "side", "time"]}
		]
	}
]

def generate_metric_printout (): # Returns a string with color-formatted metric categories and metrics, intended to be printed
	printout = ""
	for category in metric_categories:
		printout += f"{utils.color.BOLD}{category ['color']}{category ['id']}. {category ['name']}{utils.color.END * 2}\n"
		metric_number = 1
		for metric in category ["metrics"]:
			printout += f"{category ['color']}{category ['id']}{metric_number}. {metric ['name']}{utils.color.END}\n"
			metric_number += 1
		printout += "\n"
	return printout

class MetricIDType:
	METRIC_CATEGORY = 0
	METRIC = 1

def resolve_metric_id (id, to_upper = True): # Resolves a metric ID, e.g. 'A1', or metric category ID, e.g. 'A'
	# The argument to_upper specifies whether or not to convert the given ID to uppercase before processing.
	# Returns:
	# success (bool), id_type (MetricIDType or None), resolved_category (dict of metric category or None), resolved_metric (dict of metric or None)
	if to_upper:
		modified_id = id.upper ()
	else:
		modified_id = id
	matched_category = None # Assume we don't have a category that matches
	for category in metric_categories: # Iterate over the categories until we find one that matches
		if modified_id.startswith (category ["id"].upper () if to_upper else category ["id"]): # e.g. 'a1'.startswith ('a')
			matched_category = category
	if matched_category is None:
		return False, None, None, None
	metric_number_string = modified_id.replace (matched_category ["id"].upper () if to_upper else matched_category ["id"], "") # 'a1' -> '1'
	if metric_number_string == "": # There's no number to specify the metric, so assume a category was the selection
		return True, MetricIDType.METRIC_CATEGORY, matched_category, None
	try:
		metric_number = int (metric_number_string) # fails if not integer
		assert metric_number >= 1 and metric_number <= len (matched_category ["metrics"]) # fails if integer isn't a metric number
	except (ValueError, AssertionError):
		return False, None, None, None

	metric = matched_category ["metrics"] [metric_number - 1]
	return True, MetricIDType.METRIC, matched_category, metric

def verify_metric_id (id): # Like resolve_metric_id, but only returns a True or False on whether or not the ID is valid
	return resolve_metric_id (id) [0] # Calls resolve_metric_id, preserving only the "success" value
