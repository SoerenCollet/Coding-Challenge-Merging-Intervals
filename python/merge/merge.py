"""
The merge function of the challenge

Functions:
    get_args() -> argparse.Namespace
    merge(tuple) -> list
"""
import argparse
import timeit

def get_args() -> argparse.Namespace:
    """Getting user args from cli"""
    cli=argparse.ArgumentParser()
    cli.add_argument(
        "--intervals",
        "-i",
        nargs="+",
        type=int,
        action="append",
        help="Add min 2 intervals to get merged (-i 2 6 -i 3 10)"
    )
    cli.add_argument(
        "--example",
        "-e",
        nargs="?",
        const=[[25,30],[2,19],[14,23],[4,8]],
        help="Shows the challenge example"
    )
    cli.add_argument(
        "--timer",
        "-t",
        action='store_true',
        help="Returns execution time"
    )
    return cli.parse_args()

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
        for interval in intervals:
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
    args = get_args()

    if args.timer is True:
        start = timeit.default_timer()

    match args:
        case args if args.intervals is not None:
            print(merge(args.intervals))
        case args if args.example is not None:
            print(merge(args.example))
        case args if args.timer is True:
            print("Please profide further arguments, " +
                "running a timer without executed code is meaningless!")
        case _:
            print("Please profide arguments!")

    if args.timer is True:
        end = timeit.default_timer()
        print(end-start)
