import sys

class ThingLang:
    def __init__(self):
        self.vars = {}
        self.funcs = {}

    def run(self, lines, indent_level=0):
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            line = line.split('!', 1)[0].rstrip()  # remove inline comment
            stripped = line.strip()

            if not stripped:  # skip empty lines
                i += 1
                continue

            # Variable definition
            if stripped.startswith("THIS"):
                try:
                    _, name, _, value = stripped.split(maxsplit=3)
                    self.vars[name] = self._eval_expr(value)
                except ValueError:
                    raise Exception(f"Invalid variable definition: {stripped}")

            # Print
            elif stripped.startswith("THINGSAY"):
                _, value = stripped.split(maxsplit=1)
                print(self._eval_expr(value))

            # Function definition
            elif stripped.startswith("DOTHING"):
                parts = stripped.split(maxsplit=2)
                if len(parts) != 3:
                    raise Exception(f"Invalid function definition: {stripped}")
                _, name, _ = parts
                body, i = self._collect_block(lines, i + 1, "GONNAEND", indent_level + 1)
                self.funcs[name] = body

            # Function call
            elif stripped in self.funcs:
                self.run(self.funcs[stripped], indent_level + 1)

            # Loop
            elif stripped.startswith("NOTAGAIN"):
                body, i = self._collect_block(lines, i + 1, "TIMES IS", indent_level + 1)
                try:
                    count = int(lines[i].split('!', 1)[0].strip().split()[-1])
                except ValueError:
                    raise Exception(f"Invalid TIMES IS value: {lines[i]}")
                for _ in range(count):
                    self.run(body, indent_level + 1)

            i += 1

    def _collect_block(self, lines, start_index, end_keyword, expected_indent):
        block = []
        i = start_index
        while i < len(lines):
            line = lines[i].rstrip()
            line = line.split('!', 1)[0].rstrip()
            if not line.strip():
                i += 1
                continue
            current_indent = len(lines[i]) - len(lines[i].lstrip())
            if line.strip().startswith(end_keyword) and current_indent == expected_indent - 1:
                break
            block.append(lines[i])
            i += 1
        if i >= len(lines):
            raise Exception(f"Block missing ending '{end_keyword}'")
        return block, i

    def _eval_expr(self, value):
        """
        Evaluate expressions:
        - Strings in quotes are returned as-is
        - Variables are substituted
        - Basic math (+, -, *, /, %) is supported
        """
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            return value.strip('"')
        for var in self.vars:
            value = value.replace(var, str(self.vars[var]))
        try:
            return eval(value, {"__builtins__": {}})
        except Exception:
            return value

# --- MAIN: run a ThingLang file ---
if len(sys.argv) != 2:
    print("Usage: python thinglang.py filename.tl")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

ThingLang().run(lines)
