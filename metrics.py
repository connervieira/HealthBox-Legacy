import utils


# The metrics are broken up into individual categories: Activity, Mental Health, Nutrition, and Measurements


# Each metric contains its name, description, and a template containing what information should be in each submission, and in what order, for sake of input validation. Below is a list of validation terms, and what they correspond to. This template only contains what type of information should be in each submission. If you'd like to see what each piece of submission data actually represents, see METRICS.md

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
# sexuality: A 1 character string: S, G, or B
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
			{"name": "Steps", "description": "How many steps are taken", "validation": ["int", "start_time", "end_time"]},
			{"name": "Active Calories", "description": "How many calories have been burned, not including calories burned while resting.", "validation": ["int", "start_time", "end_time"]},
			{"name": "On Foot Distance", "description": "Distance traveled through walking, running, or otherwise on foot", "validation": ["float", "start_time", "end_time"]},
			{"name": "Resting Calories", "description": "How much energy is burned while resting", "validation": ["int", "start_time", "end_time"]},
			{"name": "Active Minutes", "description": "How many minutes are spent moving around, being active", "validation": ["start_time", "end_time"]},
			{"name": "Wheelchair Pushes", "description": "How many times the wheels on a wheelchair are pushed", "validation": ["int", "start_time", "end_time"]},
			{"name": "Wheelchair Distance", "description": "Total distance traveled by manual wheel chair movement", "validation": ["int", "start_time", "end_time"]},
			{"name": "Minutes Standing", "description": "Minutes spent standing", "validation": ["start_time", "end_time"]}
		]
	},
	{
		"name": "Mental Health",
		"id": "B",
		"color": utils.color.CYAN,
		"metrics": [
			{"name": "PHQ-9 Score (Depression Test)", "description": "PHQ-9 scores can be an indicator of depression, and its severity", "validation": ["int", "datetime"]},
			{"name": "Y-BOCS Score (OCD Test)", "description": "Y-BOCS scores can be an indicator of obessive-compulsive disorder, and its severity.", "validation": ["int", "datetime"]},
			{"name": "GAD-7 Score (Anxiety Test)", "description": "GAD-7 scores can be an indicator of anxiety, and its severity", "validation": ["int", "datetime"]},
			{"name": "MDQ Score (Bipolar Test)", "description": "MDQ scores can be an indicator of bipolar disorder, and its severity", "validation": ["int", "datetime"]},
			{"name": "ASRS Score (ADHD Test)", "description": "ASRS scores can be an indicator of ADHD, and its severity", "validation": ["int", "datetime"]},
			{"name": "Mindful Minutes", "description": "Minutes spent being mindful of thoughts, emotions, and feelings", "validation": ["short_string", "start_time", "end_time"]},
			{"name": "Mood", "description": "The current mood at a point in time", "validation": ["short_string", "datetime"]},
			{"name": "Sexual Activity", "description": "Sexual activity with a partner", "validation": ["boolean", "datetime"]}
		]
	},
	{
		"name": "Nutrition",
		"id": "C",
		"color": utils.color.GREEN,
		"metrics": [
			{"name": "Calories", "description": "", "validation": ["int", "datetime", "uuid", "uuid"]},
			{"name": "Water", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Sugar", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Fiber", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Protein", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Saturated Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Trans Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Monosaturated Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Polysaturated Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Unspecified Fat", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Calcium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Carbohydrates", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Cholesterol", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Iron", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Sodium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Vitamin A", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Vitamin B6", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Vitamin B12", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Vitamin C", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Vitamin D", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Vitamin E", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Vitamin K", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Zinc", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Biotin", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Caffeine", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Chloride", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Copper", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Folate", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Iodine", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Magnesium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Manganese", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Molybdenum", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Niacin", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Pantothenic Acid", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Phosphorus", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Potassium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Riboflavin", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Selenium", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]},
			{"name": "Thiamin", "description": "", "validation": ["float", "datetime", "uuid", "uuid"]}
		]
	},
	{
		"name": "Measurements",
		"id": "D",
		"color": utils.color.YELLOW,
		"metrics": [
			{"name": "Weight", "description": "Total body weight", "validation": ["float", "datetime"]},
			{"name": "Height", "description": "Total height when standing straight upright", "validation": ["float", "datetime"]},
			{"name": "Biological Sex", "description": "Gender as identified at birth", "validation": ["sex"]},
			{"name": "Gender", "description": "Gender as defined by which gender one identifies with", "validation": ["short_string"]},
			{"name": "Sexuality", "description": "Who one is attracted to sexually", "validation": ["sexuality"]},
			{"name": "Body Temperature", "description": "Measure of the temperature of the body ", "validation": ["temperature", "datetime"]},
			{"name": "Electrodermal Activity", "description": "Electrodermal activity serves as an indicator of how much sweat is on the skin.", "validation": ["float", "datetime"]},
			{"name": "Waist Circumference", "description": "The measurement of the circumference of the waist", "validation": ["float", "datetime"]},
			{"name": "Breathing Rate", "description": "How many breaths taken each minute", "validation": ["float", "datetime"]},
			{"name": "Oxygen Saturation", "description": "How much oxygen in present in the blood", "validation": ["percentage", "datetime"]},
			{"name": "Heart Rate", "description": "How many times per minute the heart beats", "validation": ["int", "datetime"]},
			{"name": "Resting Heart Rate", "description": "Heart rate, measured while sitting, and inactive", "validation": ["int", "datetime"]},
			{"name": "Walking Heart Rate", "description": "Heart rate, measured at a steady walking pace", "validation": ["int", "datetime"]},
			{"name": "Running Heart Rate", "description": "Heart race, measured at a steady run", "validation": ["int", "datetime"]},
			{"name": "Heart Rate Variability", "description": "Variation in the time interval between heart beats", "validation": ["int", "datetime"]},
			{"name": "Peripheral Perfusion Index", "description": "Relative strength of the pulse at various points on the body", "validation": ["percentage", "datetime"]},
			{"name": "Lung Capacity", "description": "How much air the lungs are capable of holding", "validation": ["float", "datetime"]},
			{"name": "VO2 Max", "description": "The maximum amount of oxygen burned while exercising", "validation": ["float", "datetime"]},
			{"name": "Ailments", "description": "A record of injuries and illnesses, both mental and physical", "validation": ["long_string", "start_time", "end_time"]},
			{"name": "Blood Pressure", "description": "The pressure at which blood pushes against the walls of the arteries", "validation": ["int", "int", "datetime"]},
			{"name": "Blood Sugar", "description": "The amount of glucose in the blood", "validation": ["int", "datetime"]},
			{"name": "Blood Alcohol Content", "description": "The amount of alcohol in the blood", "validation": ["float", "datetime"]},
			{"name": "Sound Exposure", "description": "Periods of time exposed to sounds of a certain volume", "validation": ["int", "start_time", "end_time"]},
			{"name": "Sleep", "description": "Record of periods of sleep in its various stages", "validation": ["short_string", "start_time", "end_time"]},
			{"name": "Times Fallen", "description": "Times unintentionally fallen, with or without injury", "validation": ["datetime"]},
			{"name": "Atypical Pulse", "description": "A record of occasions on which heart rate was atypically fast or slow.", "validation": ["int", "datetime"]},
			{"name": "Audiogram", "description": "A test used to determine how loud a sound has to be to be heard.", "validation": ["int", "side", "datetime"]}
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
