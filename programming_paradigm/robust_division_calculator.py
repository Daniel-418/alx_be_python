def safe_divide(numerator, denominator):
    try:
        return ("The result of the division is {}"
                .format(float(numerator) / float(denominator)))
    except (ZeroDivisionError, ValueError) as e:
        if isinstance(e, ValueError):
            return("Error: Please enter numeric values only.")
        elif isinstance(e, ZeroDivisionError):
            return("Error: Cannot divide by zero.")
