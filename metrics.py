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
			{"name": "Minutes Standing", "description": "How many minutes are spent standing"}
		]
	},
	{
		"name": "Mental Health",
		"id": "B",
		"color": utils.color.CYAN,
		"metrics": [
			{"name": "PHQ-9 Score (Depression Test)", "description": "PHQ-9 scores can be an indicator of depression, and its severity."},
			{"name": "Y-BOCS Score (OCD Test)", "description": "Y-BOCS scores can be an indicator of obessive-compulsive disorder, and its severity."},
			{"name": "GAD-7 Score (Anxiety Test)", "description": "GAD-7 scores can be an indicator of anxiety, and its severity."},
			{"name": "MDQ Score (Bipolar Test)", "description": "MDQ scores can be an indicator of bipolar disorder, and its severity."},
			{"name": "ASRS Score (ADHD Test)", "description": "ASRS scores can be an indicator of ADHD, and its severity."},
			{"name": "Mindful Minutes", "description": "This is how many minutes are spent being mindful of thoughts, emotions, and feelings."},
			{"name": "Mood", "description": "This is simply the current mood, at any given time."},
			{"name": "Sexual Activity", "description": "This is sexual activity with a partner."}
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
			{"name": "Body Temperature", "description": "Measure of the temperature of the body "},
			{"name": "Electrodermal Activity", "description": "Electrodermal activity serves as an indicator of how much sweat is on the skin."},
			{"name": "Waist Circumference", "description": ""},
			{"name": "Breathing Rate", "description": "How many breaths taken each minute"},
			{"name": "Oxygen Saturation", "description": "How much oxygen in present in the blood"},
			{"name": "Heart Rate", "description": ""},
			{"name": "Resting Heart Rate", "description": "Heart rate, measured while sitting, and inactive"},
			{"name": "Walking Heart Rate", "description": "Heart rate, measured at a steady walking pace"},
			{"name": "Running Heart Rate", "description": "Heart race, measured at a steady run"},
			{"name": "Heart Rate Variability", "description": ""},
			{"name": "Peripheral Perfusion Index", "description": ""},
			{"name": "Lung Capacity", "description": "How much air the lungs are capable of holding"},
			{"name": "VO2 Max", "description": "The maximum amount of oxygen burned while exercising"},
			{"name": "Blood Pressure", "description": ""},
			{"name": "Blood Sugar", "description": ""},
			{"name": "Blood Alcohol Content", "description": ""},
			{"name": "Sound Exposure", "description": ""},
			{"name": "Sleep", "description": ""},
			{"name": "Atypical Pulse", "description": "A record of occasions on which heart rate was atypically fast or slow."},
			{"name": "Audiogram", "description": "A test used to determine how loud a sound has to be to be heard."}
		]
	}
]
