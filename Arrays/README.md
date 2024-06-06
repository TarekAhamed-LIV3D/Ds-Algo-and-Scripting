# Static Array

First things first, In Python you cannot change the size of the array and mimicking the behavior of a static array in languages like C or C++. 

# Using List with fixed size

In Python, you can create a list and treat it as a static array by ensuring you do not change its size after creation. Here’s an example:

                Create a list with a fixed size of 5, initialized with zeros
                                    numbers = [0] * 5

                Access and modify elements
                                    numbers[0] = 10
                                    numbers[1] = 20

# Using Module  

The 'array' module of python provides a way to create arrays that are more memory-efficient than lists, especially when dealing with large numbers of elements of the same type. Here’s an example:

                                    import array
                Create an array of integers with a fixed size of 5
                                    numbers = array.array('i', [0] * 5)
                
                Access and modify elements
                                    numbers[0] = 10
                                    numbers[1] = 20

# Advantages & Disadvantages

Advantages:
    Performance: Static arrays are generally faster than dynamic arrays because they don’t require dynamic  memory allocation.
    Memory Efficiency: No overhead for memory management operations.

Disadvantages:
    Lack of Flexibility: The size is fixed, so you cannot resize the array if you need more or less space.
    Wasted Space: If you allocate more space than needed, it can lead to wasted memory.

## Static arrays are fundamental data structures used in various applications where the size of the array is known beforehand and does not need to change during execution.