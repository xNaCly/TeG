# to add your own just add a new string ("_EXAMPLE_") to this array and to ./assets/example.ms
# TeG will automaticly prompt you for a value and insert the given content into your specified file
template_strings=["_DATE_", "_TIME_", "_PERSON_", "_FIRMA_NAME_", "_FIRMA_STREET_", "_FIRMA_EMAIL_", "_FIRMA_CITY_"]
possible_args={
  "-input / -i": "[required] file to feed into create.py (must be .ms format and valid groff_ms macro format)",
  "-output / -o":"[optional] file to output the compiled pdf to (will replace already existing matching file)",
  "-preserve-temp / -pre": "[optional] preserves the <date:time>_temp.ms files in /cache"
}
helpstr="""\t\t\t\t\tTemplate generator (TeG) by xnacly

      \t\tThis script is intended to simplify the process of applying to several companies.
      \t\t\t\t\t(And similar repetitive tasks)

      \t\tThis is archived by inserting values into template files which contain preconfigured variables.
      \t\t\t\t\t(And compiling them into *.pdf files.)\n

      \t\tThis script makes use of 'groff' and 'groff_ms', make sure to install these before usage.
      \t\t\t\t\t(I would suggest looking into the groff_ms macros)
      \t\t\t\t\t(Luke Smith made a good video about groff)


      \t\t\t\t\tSource: https://github.com/xnacly\n
      """