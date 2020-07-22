import utils # utils.py

# List of metric categories
metric_categories = [
 	# Metric category: dictionary with various attributes of each category of metric
	{
		"name": "Activity",
		"id": "A", # Just for the user to be able to pick this one
		"color": utils.color.RED,
		# List of each metric in this category;
		# currently just contains names but may want types as well in the future
		# for input validation when storing metric data
		"metrics": [
			{"name": "Steps", "description": "How many steps are taken"},
			{"name": "Active Calories", "description": "How many calories have been burned, not including calories burned while resting."},
			{"name": "On Foot Distance", "description": "Distance traveled through walking, running, or otherwise on foot"},
			{"name": "Resting Calories", "description": "How much energy is burned while resting"},
			{"name": "Active Minutes", "description": "How many minutes are spent moving around, being active"},
			{"name": "Wheelchair Pushes", "description": "How many times the wheels on a wheelchair are pushed"},
			{"name": "Wheelchair Distance", "description": "Total distance traveled by manual wheel chair movement"},
			{"name": "Minutes Standing", "description": "Minutes spent standing"}
		]
	},
	{
		"name": "Mental Health",
		"id": "B",
		"color": utils.color.CYAN,
		"metrics": [
			{"name": "PHQ-9 Score (Depression Test)", "description": "PHQ-9 scores can be an indicator of depression, and its severity"},
			{"name": "Y-BOCS Score (OCD Test)", "description": "Y-BOCS scores can be an indicator of obessive-compulsive disorder, and its severity."},
			{"name": "GAD-7 Score (Anxiety Test)", "description": "GAD-7 scores can be an indicator of anxiety, and its severity"},
			{"name": "MDQ Score (Bipolar Test)", "description": "MDQ scores can be an indicator of bipolar disorder, and its severity"},
			{"name": "ASRS Score (ADHD Test)", "description": "ASRS scores can be an indicator of ADHD, and its severity"},
			{"name": "Mindful Minutes", "description": "Minutes spent being mindful of thoughts, emotions, and feelings"},
			{"name": "Mood", "description": "The current mood at a point in time"},
			{"name": "Sexual Activity", "description": "Sexual activity with a partner"}
		]
	},
	{
		"name": "Nutrition",
		"id": "C",
		"color": utils.color.GREEN,
		"metrics": [
			{"name": "Calories", "description": ""},
			{"name": "Water", "description": ""},
			{"name": "Sugar", "description": ""},
			{"name": "Fiber", "description": ""},
			{"name": "Protein", "description": ""},
			{"name": "Saturated Fat", "description": ""},
			{"name": "Trans Fat", "description": ""},
			{"name": "Monosaturated Fat", "description": ""},
			{"name": "Polysaturated Fat", "description": ""},
			{"name": "Unspecified Fat", "description": ""},
			{"name": "Calcium", "description": ""},
			{"name": "Carbohydrates", "description": ""},
			{"name": "Cholesterol", "description": ""},
			{"name": "Iron", "description": ""},
			{"name": "Sodium", "description": ""},
			{"name": "Vitamin A", "description": ""},
			{"name": "Vitamin B6", "description": ""},
			{"name": "Vitamin B12", "description": ""},
			{"name": "Vitamin C", "description": ""},
			{"name": "Vitamin D", "description": ""},
			{"name": "Vitamin E", "description": ""},
			{"name": "Vitamin K", "description": ""},
			{"name": "Zinc", "description": ""},
			{"name": "Biotin", "description": ""},
			{"name": "Caffeine", "description": ""},
			{"name": "Chloride", "description": ""},
			{"name": "Copper", "description": ""},
			{"name": "Folate", "description": ""},
			{"name": "Iodine", "description": ""},
			{"name": "Magnesium", "description": ""},
			{"name": "Manganese", "description": ""},
			{"name": "Molybdenum", "description": ""},
			{"name": "Niacin", "description": ""},
			{"name": "Pantothenic Acid", "description": ""},
			{"name": "Phosphorus", "description": ""},
			{"name": "Potassium", "description": ""},
			{"name": "Riboflavin", "description": ""},
			{"name": "Selenium", "description": ""},
			{"name": "Thiamin", "description": ""}
		]
	},
	{
		"name": "Measurements",
		"id": "D",
		"color": utils.color.YELLOW,
		"metrics": [
			{"name": "Weight", "description": "Total body weight"},
			{"name": "Height", "description": "Total height when standing straight upright"},
			{"name": "Biological Sex", "description": "Gender as identified at birth"},
			{"name": "Gender", "description": "Gender as defined by which gender one identifies with"},
			{"name": "Sexuality", "description": "Who one is attracted to sexually"},
			{"name": "Body Temperature", "description": "Measure of the temperature of the body "},
			{"name": "Electrodermal Activity", "description": "Electrodermal activity serves as an indicator of how much sweat is on the skin."},
			{"name": "Waist Circumference", "description": "The measurement of the circumference of the waist"},
			{"name": "Breathing Rate", "description": "How many breaths taken each minute"},
			{"name": "Oxygen Saturation", "description": "How much oxygen in present in the blood"},
			{"name": "Heart Rate", "description": "How many times per minute the heart beats"},
			{"name": "Resting Heart Rate", "description": "Heart rate, measured while sitting, and inactive"},
			{"name": "Walking Heart Rate", "description": "Heart rate, measured at a steady walking pace"},
			{"name": "Running Heart Rate", "description": "Heart race, measured at a steady run"},
			{"name": "Heart Rate Variability", "description": "Variation in the time interval between heart beats"},
			{"name": "Peripheral Perfusion Index", "description": "Relative strength of the pulse at various points on the body"},
			{"name": "Lung Capacity", "description": "How much air the lungs are capable of holding"},
			{"name": "VO2 Max", "description": "The maximum amount of oxygen burned while exercising"},
			{"name": "Ailments", "description": "A record of injuries and illnesses, both mental and physical"},
			{"name": "Blood Pressure", "description": "The pressure at which blood pushes against the walls of the arteries"},
			{"name": "Blood Sugar", "description": "The amount of glucose in the blood"},
			{"name": "Blood Alcohol Content", "description": "The amount of alcohol in the blood"},
			{"name": "Sound Exposure", "description": "Periods of time exposed to sounds of a certain volume"},
			{"name": "Sleep", "description": "Record of periods of sleep in its various stages"},
			{"name": "Times Fallen", "description": "Times unintentionally fallen, with or without injury"},
			{"name": "Atypical Pulse", "description": "A record of occasions on which heart rate was atypically fast or slow."},
			{"name": "Audiogram", "description": "A test used to determine how loud a sound has to be to be heard."}
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

	metric = matched_category ["metrics"] [metric_number]
	return True, MetricIDType.METRIC, matched_category, metric

def verify_metric_id (id): # Like resolve_metric_id, but only returns a True or False on whether or not the ID is valid
	return resolve_metric_id (id) [0] # Calls resolve_metric_id, preserving only the "success" value
