def convert_if_int(value: str) -> str | int:
	"""
	Convert a string to integer if it is a digit, or return the string as it is otherwise.

	:param value: The string to be converted.
	:return: The converted integer or the original string.
	"""

	return int(value) if value.isdigit() else value


def parse_option_set(options: str) -> dict[str, str]:
	"""
	Parse a comma-separated key-value pair into ``dict`` object. Whitespaces around equal signs,
	commas and adjacent commas will be ignored.

	:param options: The comma-separated key-value pair to be parsed.
	:return: The parsed ``dict`` object.
	"""

	result = {}

	for pair in options.split(','):
		if not pair or pair.isspace():
			continue

		key, value = pair.split('=', 1)
		result[key.strip()] = value.strip()

	return result
