def custom_input(label, _type = str):
    _input = None 

    while type(_input) != _type:
        try:
            _input = input(label)
            _input = _type(_input)
        except:
            print("Input must be", _type.__name__)
    return _input 


