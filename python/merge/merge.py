"""
The merge function of the challenge

Functions:
    get_args() -> argparse.Namespace
    merge(tuple) -> list
"""
import argparse
from timeit import default_timer as timer
from guppy import hpy


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
    cli.add_argument(
        "--memory",
        "-m",
        action='store_true',
        help="Returns memory usage"
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

        if not len(intervals) >= 2:
            raise ValueError("Please provide at least 2 intervals to merge!")

        # Sorting intervals to make max starting interval last entry
        intervals_copy = list(intervals)
        intervals_copy.sort(key=lambda interval:interval[0])
        result = [intervals_copy[0]]

        for interval in intervals_copy:
            if len(interval) != 2:
                raise ValueError("Please provide valid intervals!" \
                    "\nAn interval has exact 2 values.")

            if interval[0] > interval[1]:
                raise ValueError("Please provide valid intervals!" \
                    "\nThe starting interval should not be higher then the ending interval.")

            # Compare last entry of results with iterated interval
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

        result.sort(key=lambda interval:interval[0])
        return result

    except TypeError as err:
        return f"TypeError: {err}"

    except ValueError as err:
        return f"ValueError: {err}"

if __name__ == "__main__":
    mem = hpy()
    args = get_args()

    if args.timer is True:
        start = timer()

    # Handle user inputs and provide feedback
    match args:
        case args if args.intervals is not None:
            print(f"Merged intervals:\n{merge(args.intervals)}")
        case args if args.example is not None:
            print(f"Merged intervals:\n{merge(args.example)}")
        case args if args.timer is True:
            print("Please provide further arguments, " +
                "enter intervals or start the example for valid runtime!")
        case args if args.memory is True:
            print("Please provide further arguments, " +
                "enter intervals or start the example for valid memory usage!")
        case _:
            print("Please provide arguments!")

    if args.timer is True:
        end = timer()
        print(f"\nRuntime:\n{end-start} seconds")

    if args.memory is True:
        print(f"\nCurrent memory heap:\n{mem.heap().size} bytes")
