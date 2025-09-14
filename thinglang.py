import sys

class ThingLang:
    def __init__(self):
        self.vars = {}
        self.funcs = {}

    def run(self, lines):
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line.startswith('!'):  # skip empty lines or comments
                i += 1
                continue

            # Variable definition
            if line.startswith("THIS"):
                _, name, _, value = line.split(maxsplit=3)
                self.vars[name] = self._eval(value)

            # Print
            elif line.startswith("THINGSAY"):
                _, value = line.split(maxsplit=1)
                print(self._eval(value))

            # Function definition
            elif line.startswith("DOTHING"):
                _, name, _ = line.split(maxsplit=2)
                body = []
                i += 1
                while not lines[i].startswith("GONNAEND"):
                    body.append(lines[i])
                    i += 1
                self.funcs[name] = body

            # Function call
            elif line in self.funcs:
                self.run(self.funcs[line])

            # Loop
            elif line.startswith("NOTAGAIN"):
                body = []
                i += 1
                while not lines[i].startswith("TIMES IS"):
                    body.append(lines[i])
                    i += 1
                count = int(lines[i].split()[-1])
                for _ in range(count):
                    self.run(body)

            i += 1

    def _eval(self, value):
        if value.startswith('"') and value.endswith('"'):
            return value.strip('"')
        if value in self.vars:
            return self.vars[value]
        try:
            return int(value)
        except ValueError:
            return value

# --- MAIN: run a ThingLang file ---
if len(sys.argv) != 2:
    print("Usage: python thinglang.py filename.tl")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()

ThingLang().run(lines)
