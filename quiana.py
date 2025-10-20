def find_homeless(homeless):
    """Recursively find the word 'homeless' in a string or list."""
    if not homeless:
        return False  # base case: empty input means word not found
    
    # Join homeless if it is a list of characters
    if isinstance(homeless, list):
        homeless = ''.join(homeless)
    
    # Base case: check if the current substring starts with 'homeless'
    if homeless.startswith("homeless"):
        return True
    
    # Recursive case: check starting from the next character
    return find_homeless(homeless[1:])
