from teg_config import *
from parser import Parser
import datetime
import sys
import os

class Create:
    def __init__(self):
      self.args = self.get_args_parsed()

    def get_args_parsed(self):
      parser = Parser(sys.argv)
      return parser.parse_arguments()

    def print_help(self):
      print("+","-"*45,"+ -- TeG -- +","-"*45,"+")
      print(helpstr)
      print("+","-"*45,"+ Arguments +","-"*45,"+\n")
      for e in possible_args:
        print(f"  $ {e}\n\t{possible_args[e]}\n")
      print("  Example:\n\t$ python3 TeG.py -i='assets/example.ms' -o='example_file'")
      print("+","-"*45,"+ --------- +","-"*45,"+")

    def check_config(self):
      if not template_strings:
        raise ValueError("template_strings array in 'create_config.py' is empty, therefor nothing to replace")

    def get_dotms_file(self):
      try:
        filename = self.args["args"]["input"]
      except:
        try:
          filename = self.args["args"]["i"]
        except:
          raise ValueError("input argument missing, please specify a file")
      try:
        with open(filename, "r") as f:
            content = f.read()
        return content
      except:
        raise FileExistsError(f"{filename} not found, check you spelling.")

    def replace_template_strings(self, file_content: str) -> str:
      for template in template_strings:
        if template == "_DATE_":
          template_value = datetime.date.today().strftime("%d.%m.%y")
        elif template == "_TIME_":
          template_value = datetime.datetime.now().strftime("%H:%M")
        else:
          template_display = template.replace("_"," ").title()
          template_value = input(f"{template_display}: ")

        file_content = file_content.replace(template, template_value)
      return file_content

    def write_tempfile(self, content) -> str:
      name = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
      with open(f"./cache/{name}_temp.ms", "w") as f:
        f.write(content)
      return name

    def compile_pdf(self, name):
      """
      compiles the given .ms file to pdf using groff:
      groff -ms <file>.ms -k -T pdf > <file>.pdf
      """
      try:
        filename = self.args["args"]["output"]
      except:
        try:
          filename = self.args["args"]["o"]
        except:
          filename = datetime.datetime.now().strftime("%d%m%Y%H%M%S")

      os.system(f"groff ./cache/{name}_temp.ms -ms -k -T pdf > ./output/{filename}.pdf")

    def remove_temp_files(self, name):
      print(self.args["flags"])
      if not "preserve-temp" in self.args["flags"] or not "pre" in self.args["flags"]:
        try:
          os.system(f"rm -r ./cache/{name}_temp.ms")
        except:
          print("couldn't remove temp file")

    def start(self):
      try:
        if "help" in self.args["flags"]:
          return self.print_help()
      except:
        return self.print_help()
      self.check_config()
      content = self.get_dotms_file()
      content = self.replace_template_strings(content)
      name = self.write_tempfile(content)
      self.compile_pdf(name)
      self.remove_temp_files(name)

create = Create()
create.start()
