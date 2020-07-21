# Contributing
## Goals
* To make a privacy respecting, completely open source, health information management system that is fully capable of working offline.
* To make it easy for 3rd party developers to build programs around the HealthBox platform.
* To provide useful health metrics that will be fitting for a wide variety of people, regardless of race, gender, sexuality, or physical/mental disability.
* To give the user full control over their information, and to decide what programs should be able to access it.
* To create a clean and professional system, both in functionality, and in the code that runs it.

## Guidelines
* Ensure that comments are professional and consistent.
    * Use proper capitalization, grammar, and punctuation.
    * Avoid slang terms where possible.
    * Avoid expletives, slurs, and other hateful, non professional language.
    * For sake of consistency, put a space between the '#' and your comment.
        * \# Comments should look like this.
        * \#comments shouldnt look like dis
* Keep variable names consistent.
    * Separate words in variable names with underscores (\_).
    * All words in variable names should be lowercase.
        * variable_names_should_look_like_this
        * variableNamesShouldNotLookLikeThis
* When describing health metrics, do not refer to the user.
	* Avoid saying "your", "someone's", "the person's", etc.
		* Instead of `How many steps you take`, say `How many steps are taken`
		* Instead of `How many calories the person burns`, say `How many calories are burned`
* If a disability could prevent a health metric from being applicable, also add an an alternative metric.
	* For example, if you add the "Steps" metric, also add the "Wheelchair Pushes" metric.