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
			{"name": "Steps", "description": ""},
			{"name": "Active Calories", "description": ""},
			{"name": "On Foot Distance", "description": ""},
			{"name": "Resting Energy", "description": ""},
			{"name": "Active Minutes", "description": ""},
			{"name": "Minutes Standing", "description": ""}
		]
	},
	{
		"name": "Mental Health",
		"id": "B",
		"color": utils.color.CYAN,
		"metrics": [
			{"name": "PHQ-9 Score (Depression Test)", "description": ""},
			{"name": "Y-BOCS Score (OCD Test)", "description": ""},
			{"name": "GAD-7 Score (Anxiety Test)", "description": ""},
			{"name": "MDQ Score (Bipolar Test)", "description": ""},
			{"name": "ASRS Score (ADHD Test)", "description": ""},
			{"name": "Mindful Minutes", "description": ""},
			{"name": "Mood", "description": ""},
			{"name": "Sexual Activity", "description": ""}
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
			{"name": "Weight", "description": ""},
			{"name": "Height", "description": ""},
			{"name": "Body Temperature", "description": ""},
			{"name": "Electrodermal Activity", "description": ""},
			{"name": "Waist Circumference", "description": ""},
			{"name": "Breathing Rate", "description": ""},
			{"name": "Oxygen Saturation", "description": ""},
			{"name": "Heart Rate", "description": ""},
			{"name": "Resting Heart Rate", "description": ""},
			{"name": "Walking Heart Rate", "description": ""},
			{"name": "Running Heart Rate", "description": ""},
			{"name": "Heart Rate Variability", "description": ""},
			{"name": "Peripheral Perfusion Index", "description": ""},
			{"name": "Lung Capacity", "description": ""},
			{"name": "VO2 Max", "description": ""},
			{"name": "Blood Pressure", "description": ""},
			{"name": "Blood Sugar", "description": ""},
			{"name": "Blood Alcohol Content", "description": ""},
			{"name": "Sound Exposure", "description": ""},
			{"name": "Sleep", "description": ""},
			{"name": "Atypical Pulse", "description": ""},
			{"name": "Audiogram", "description": ""}
		]
	}
]
