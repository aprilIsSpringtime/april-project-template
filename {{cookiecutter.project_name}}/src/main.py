######### This is how your codes should be documented ###########################

#usr/bin/env/python3
"""
One line summary of the module. Keep it short.

Go into the details of the module and outline the scope.

Methods:
*list the modules*
eg. get_edgemap() - Returns the edgemap of the image.
    get_area() - Returns the image containing the area passed as a parameter.
    
Usage:
  $ python example.py
"""

module_level_variable = 98765 # describe the variable

def function_with_types_in_docstring(param1, param2 = 8):
    """Example function. Have a single line summary.
    
    For more detailed description. Add here.
    Args:
        param1 (int): The first parameter.
        param2 (int, optional): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    
    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    ""
    if param1 == param2:
        raise ValueError('param1 may not be equal to param2')
    return True

############################ IN CASE OF A CLASS ########################################

class ExampleClass(object):
    """The summary line for a class docstring should fit on one line.
   
    Add more detailed description here.
    
    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.
    """

    def __init__(self, param1, param2, param3):
        """Example of docstring on the __init__ method.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1 (str): Description of `param1`.
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`): Description of `param3`.

        """
        self.attr1 = param1
        self.attr2 = param2
        self.attr3 = param3  #: Doc comment *inline* with attribute
