# ThingLang

**ThingLang** is an esoteric programming language created by [Rasa8877](https://esolangs.org/wiki/User:Rasa8877) in 2025.  
It is designed to be playful and readable, using English-like keywords for variables, printing, functions, loops, and comments.

---

## Features

- **Variables**: Assign numbers or strings using `THIS <name> IS <value>`  
- **Printing**: Output values with `THINGSAY <value>`  
- **Functions**: Define blocks of code with `DOTHING <name> GONNA ... GONNAEND`  
- **Loops**: Repeat code using `NOTAGAIN ... TIMES IS <n>`  
- **Comments**: Any line starting with `!` or trailing `!` is ignored  

---

## Commands / Keywords

| Command | Description |
|---------|-------------|
| `THIS <name> IS <value>` | Assign a value to a variable |
| `THINGSAY <value>` | Print the value of a variable or string literal |
| `DOTHING <name> GONNA ... GONNAEND` | Define a function |
| `<name>` | Call a previously defined function |
| `NOTAGAIN ... TIMES IS <n>` | Loop over the block `<n>` times |
| `!` | Comment; anything after `!` is ignored |

---

## Example Program

```tl
! Example ThingLang program
THIS x IS 5
THINGSAY x
THINGSAY "Hello ThingLang!"

DOTHING greet GONNA
    THINGSAY "Hello from a function!"
GONNAEND

greet

NOTAGAIN
    THINGSAY "Looping..."
TIMES IS 3
````

**Output:**

```
5
Hello ThingLang!
Hello from a function!
Looping...
Looping...
Looping...
```

---

## Running Programs

Clone this repository, type your code in a `.tl` file (e.g., `thinglang.tl`), and run:

```bash
python thinglang.py thinglang.tl
```

---

## Tips & Tricks

* Comments can appear anywhere using `!`.
* Loops and functions can be nested.
* Variables can be overwritten and used in multiple places.
* Functions can call other functions.

---

## License

This project is released under the MIT License.
