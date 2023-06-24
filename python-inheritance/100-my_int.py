#!/usr/bin/python3
"""Task 12. My integer
"""


class MyInt(int):
    """MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
