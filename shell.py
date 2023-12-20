import meowthon

while True:
	text = input('∩.^• ᵕ •^.∩ > ')
	if text.strip() == "": continue
	result, error = meowthon.run('<stdin>', text)

	print()
	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
