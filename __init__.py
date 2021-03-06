from execution import *

'''
patterns = [
    "a = ~\nfor i in range(~):\n\ta += i\nprint(a)",
    "a = ~ * 10\nb = ~\nwhile a - b > ~:\n\ta -= ~\n\tb += ~\nprint(a)"
]
'''


def compute_pattern(pattern, pattern_sign):
    '''
    :param pattern: Gets a pattern for execution
    :param pattern_sign: Gets a sign for pattern
    :return: Returns code with numbers without parameters and pattern execution result
    '''

    final_code = replace_sign(pattern, pattern_sign)
    execution_result = execute_code(final_code)

    return final_code, execution_result




