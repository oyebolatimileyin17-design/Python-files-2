# Day 26 - Debugging Skills
#
# For this day, I practiced debugging using my EXISTING Day 3 file
# (the calculator) rather than writing a brand new script.
#
# What I did:
# - Intentionally introduced a bug: renamed "num2" to "nfm2" by mistake
# - Ran the file and read the resulting traceback:
#       NameError: name 'num2' is not defined. Did you mean: 'num1'?
# - Learned to read tracebacks from the bottom up:
#     1. Last line = the actual error type and message
#     2. Line above = the exact line of code that caused it
#     3. Line number = where in the file
# - Fixed the typo bug (renamed "nfm2" back to "num2")
# - Tested a real edge case afterward (dividing by 0) and confirmed my
#   existing "except ZeroDivisionError" block caught it gracefully
# - Set a breakpoint on a line inside the calculator, then used VS Code's
#   debugger (F5 / Run and Debug) to pause execution and inspect the
#   live values of num1, num2, and operation before the calculation ran
# - Had to troubleshoot: an accidentally disabled breakpoint (unchecked
#   in the Breakpoints panel) was why it kept running straight through
#   without pausing - re-checking it fixed the issue
#
# Why this matters:
# - Reading tracebacks properly is a core, everyday developer skill
# - Breakpoints let me inspect exactly what my code is doing, instead
#   of guessing or relying only on print statements
