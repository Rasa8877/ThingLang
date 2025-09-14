# ThingLang

**ThingLang** is an esoteric programming language created by Rasa8877 in 2025.
It is playful, readable, and uses English-like keywords for variables, printing, functions, loops, and comments.

---

## Features

* **Variables**: Assign numbers or strings using `THIS <name> IS <value>`
  *Supports integer arithmetic and basic math expressions.*
* **Printing**: Output values with `THINGSAY <value>`
* **Functions**: Define reusable code blocks with `DOTHING <name> GONNA ... GONNAEND`
* **Loops**: Repeat code using `NOTAGAIN ... TIMES IS <n>`
* **Comments**: Any line starting with `!` is ignored

---

## Commands / Keywords

| Command                             | Description                                              |
| ----------------------------------- | -------------------------------------------------------- |
| `THIS <name> IS <value>`            | Assign a value to a variable (supports math expressions) |
| `THINGSAY <value>`                  | Print a string or the value of a variable                |
| `DOTHING <name> GONNA ... GONNAEND` | Define a function                                        |
| `<name>`                            | Call a previously defined function                       |
| `NOTAGAIN ... TIMES IS <n>`         | Loop over the block `<n>` times                          |
| `!`                                 | Comment; any line starting with `!` is ignored           |

---

## Example Program

```tl
! Example ThingLang program with comments
THIS a IS 5            ! define variable a
THIS b IS 10           ! define variable b
THIS c IS a + b * 2    ! compute c as a + b * 2

THINGSAY "Result is: "  ! print a string
THINGSAY c               ! print variable c (25)

DOTHING calc GONNA       ! define function calc
    THIS x IS 2 * 3      ! define variable x in function
    THINGSAY x           ! print x (6)
GONNAEND

calc                     ! call the function calc
```

**Output:**

```
Result is: 
25
6
```

---

## Quick Start

1. Clone this repository.
2. Create a `.tl` file (e.g., `thinglang.tl`) and write your ThingLang code.
3. Run your program with:

```bash
python thinglang.py thinglang.tl
```

4. Observe the output in your terminal.

---

## Running via stdin (Optional)

ThingLang also supports reading code from standard input, useful for online interpreters like [TIO](https://tio.run/):

```bash
cat thinglang.tl | python stdin_thinglang.py
```

Or interactively:

```bash
python stdin_thinglang.py
```

Type your code, then press `Ctrl+D` (Linux/macOS) or `Ctrl+Z` + Enter (Windows) to execute.

---

## Tips & Tricks

* Comments can appear anywhere using `!`.
* Loops and functions can be nested.
* Variables can be overwritten and used in multiple places.
* Functions can call other functions.
* Math expressions are computed as integers by default.

---

## License

This project is released under the MIT License.
