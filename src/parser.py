class Parser:
  """
  parses given sys.argv as params to flags and arguments:

  - Input:

  ```
  python3 test.py -input=assets/anschreiben.ms -output=output -preserve-temp
  -->
  [
    'test.py',
    '-input=assets/anschreiben.ms',
    '-output=output',
    '-preserve-temp'
  ]
  ```

  - Output:

  ```
  python3 test.py -input=assets/anschreiben.ms -output=output -preserve-temp
  -->
  {
    'args': {
      'input': 'assets/anschreiben.ms',
      'output': 'output'
    },
    'flags': ['preservetemp']
  }
  ```
  """
  def __init__(self, args: list):
    args.pop(0)
    self.args = args

  def parse_arguments(self):
    if not self.args:
      return []
    flags = []
    args={}
    for item in self.args:
      if item[:1] == "-":
        if "=" in item:
          item = item.split("=")
          args[item[0][1:]] = item[1]
        else:
          flags.append(item[1:])
      else:
          continue
    return {
        "args": args,
        "flags": flags
    }
