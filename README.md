# eecs484-p3-bug-catcher

Bug Catcher for EECS 484 Project #3 B+ Trees, inspired by an anonymous EECS 484 classmate. Currently supports reporting runtime errors and comparing "find" outputs with correct ones ("print" output check not supported).

Happy Debugging!

## Usage
 * Clone the repo: `git clone https://github.com/zianke/eecs484-p3-bug-catcher.git`
 * Copy your executable file `proj3exe` into the same directory as `main.py`
 * Run the python script: `python3 main.py`

## Program Outputs
 * For each testcase, if `testcase #<n> error` is printed, a runtime error occurs, with error message in `my_error_<n>.txt`, your output in `my_output_<n>.txt`, testcase input in `random_test_<n>.txt`, correct output in `correct_output_<n>.txt`.
 * If `testcase #<n> failed` is printed, you can try to debug with `random_test_<n>.txt`, `correct_output_<n>.txt` and `my_output_<n>.txt`.
 * If `testcase #<n> passed` is printed, no `*<n>.txt` file is saved.