"""
the merge function of the challenge

Functions:
    merge(tuple) -> list
"""
def merge(intervals: tuple) -> list:
    """
    The merge function accepts a list of intervals and returns a list of intervals.
    The returning intervals are the intervals which overlapps.
    The remaining intervals keep untouched.
    """
    try:
        if not isinstance(intervals, list):
            raise TypeError("Intervals is not a list!")

        # Sorting intervals to make max interval last entry
        intervals.sort()
        result = [intervals[0]]

        # Compare last entry of results with iterated interval
        for index, interval in enumerate(intervals):
            last_index = len(result)-1
            last_value = result[last_index]
            if (interval[0] <= last_value[0] <= interval[1]) or \
                (interval[0] <= last_value[1] <= interval[1]) or \
                (last_value[0] <= interval[0] <= last_value[1]) or \
                (last_value[0] <= interval[1] <= last_value[1]):

                # Replace last entry with merged overlapping interval
                result.pop(last_index)
                merged_intervals = interval[0:] + last_value[0:]
                result.append([min(merged_intervals), max(merged_intervals)])
            else:
                result.append(interval)

        result.sort()
        return result
    
    except TypeError as err:
        return f"TypeError: {err}"

    except Exception as err:
        return f"Error: {err}"


if __name__ == "__main__":
    print(merge([[25,30],[2,19],[14,23],[4,8]]))
