# eecs484-p3-bug-catcher

Bug Catcher for EECS 484 (Database Management Systems) Project #3 B+ Trees, inspired by an anonymous EECS 484 classmate on Piazza. Currently supports reporting runtime errors and comparing "find" outputs with correct ones ("print" output check not supported).

To make full use of this Bug Catcher, write as many invariants as possible in satisfiesInvariant() of your **LeafNode** class and **InnerNode** class.

Happy Debugging!

## Usage
* Test your own executable file.
     * Clone the repo: `git clone https://github.com/zianke/eecs484-p3-bug-catcher.git`.
     * Copy your executable file `proj3exe` into the same directory as `main.py`.
     * Run the python script: `python3 main.py`.

* Diff your output with another executable file.
     * Clone the repo: `git clone https://github.com/zianke/eecs484-p3-bug-catcher.git`.
     * Copy two executable files `<proj3exe_1>` and `<proj3exe_2>` into the same directory as `diff.py`.
     * Run the python script: `python3 diff.py <proj3exe_1> <proj3exe_2>`.

## Program Outputs
* Test your own executable file.
     * For each testcase, if `testcase #<n> error` is printed, a runtime error occurs, with error message in `my_error_<n>.txt`, your output in `my_output_<n>.txt`, testcase input in `random_test_<n>.txt`, correct output in `correct_output_<n>.txt`.
     * If `testcase #<n> failed` is printed, you can try to debug with `random_test_<n>.txt`, `correct_output_<n>.txt` and `my_output_<n>.txt`.
     * If `testcase #<n> passed` is printed, no `*<n>.txt` file is saved.

* Diff your output with another executable file.
     * For each testcase, if the outputs of `<proj3exe_1>` and `<proj3exe_2>` are different, the testcase and two outputs are saved in `random_test_<n>.txt`, `<proj3exe_1>_output_<n>.txt`, `<proj3exe_2>_output_<n>.txt`. You can find the difference using `diff <proj3exe_1>_output_<n>.txt <proj3exe_2>_output_<n>.txt`.
