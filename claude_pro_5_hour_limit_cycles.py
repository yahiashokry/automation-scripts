"""
5-Hour Cycle Tracker

Purpose
-------
This script tracks a repeating 5-hour cycle that started at a known
datetime (for example: 2026-05-03 12:00:00) for claude pro limits.

The script can be run at any time and it will:
1. Read the last known cycle start from a file.
2. Calculate how many 5-hour cycles have passed until the current time.
3. Determine:
   - the last completed cycle
   - the next upcoming cycle
   - the remaining time until the next cycle
4. Print a recommended working window:
   from (next_cycle - 1 hour) to (next_cycle + 1 hour).
5. Update the stored cycle start in the file if newer cycles have passed.

File
----
cycle_start.txt

The file stores the last known cycle start time in the format:
YYYY-MM-DD HH:MM:SS

Example:
2026-05-03 12:00:00

Behavior
--------
The script prints the cycle information once and exits.
"""

from datetime import datetime, timedelta
import os

# File that stores the latest cycle start time
FILE_NAME = "cycle_start.txt"

# Length of each cycle in hours
CYCLE_HOURS = 5


# ------------------------------------------------------------
# STEP 1: Load the starting cycle time
# ------------------------------------------------------------
# If the file does not exist, create it with the initial known
# start time of the cycle system.
if not os.path.exists(FILE_NAME):

    # Initial fixed start time of the cycle system
    start_time = datetime(2026, 5, 3, 12, 0)

    # Save it to the file
    with open(FILE_NAME, "w") as f:
        f.write(start_time.strftime("%Y-%m-%d %H:%M:%S"))

else:
    # Read the stored cycle start time
    with open(FILE_NAME, "r") as f:
        start_time = datetime.strptime(
            f.read().strip(),
            "%Y-%m-%d %H:%M:%S"
        )


# ------------------------------------------------------------
# STEP 2: Get the current time
# ------------------------------------------------------------
now = datetime.now()


# ------------------------------------------------------------
# STEP 3: Calculate cycles that have passed
# ------------------------------------------------------------
cycle_duration = timedelta(hours=CYCLE_HOURS)

# Total elapsed time since the stored cycle start
elapsed = now - start_time

# Number of completed cycles
cycles_passed = elapsed // cycle_duration


# ------------------------------------------------------------
# STEP 4: Determine cycle boundaries
# ------------------------------------------------------------
# Start of the most recent cycle
last_cycle = start_time + cycles_passed * cycle_duration

# Start of the upcoming cycle
next_cycle = last_cycle + cycle_duration

# Time remaining until the next cycle
remaining = next_cycle - now


# ------------------------------------------------------------
# STEP 5: Calculate the best working window
# ------------------------------------------------------------
# One hour before and after the next cycle
best_start = next_cycle - timedelta(hours=1)
best_end = next_cycle + timedelta(hours=1)


# ------------------------------------------------------------
# STEP 6: Print results
# ------------------------------------------------------------
print("Last cycle start:", last_cycle)
print("Next cycle start:", next_cycle)
print("Remaining time:", remaining)
print(
    f"Best Working Times is from "
    f"{best_start.time()} to {best_end.time()}"
)


# ------------------------------------------------------------
# STEP 7: Update stored cycle start if needed
# ------------------------------------------------------------
# If newer cycles have passed, store the most recent cycle start
if last_cycle > start_time:
    with open(FILE_NAME, "w") as f:
        f.write(last_cycle.strftime("%Y-%m-%d %H:%M:%S"))
