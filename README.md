# Generate a 'Bewerbungsanschreiben' based on given arguments

_text in `<>` is meant to be viewed as a placeholder and has to be replaced by
the user_

## Usage:

1. install `'groff'` with your fav package manager
2. modify the template file containing the substrings to replace in
   `assets/example.ms`
3. check if your file is written correctly by compiling it:
   `cat assets/example.ms | groff -ms -k -T pdf > test.pdf` and taking a look at
   it and the console output from groff
4. if `3.` was successfull, start the script by running the following commands:

```
python3 TeG.py -i="assets/example.ms"
```

5. follow the instructions and prompts included in the script

## Documentation included in the script:

```
+ --------------------------------------------- + -- TeG -- + --------------------------------------------- +
                                        Template generator (TeG) by xnacly

                This script is intended to simplify the process of applying to several companies.
                                        (And similar repetitive tasks)

                This is archived by inserting values into template files which contain preconfigured variables.
                                        (And compiling them into *.pdf files.)


                This script makes use of 'groff' and 'groff_ms', make sure to install these before usage.
                                        (I would suggest looking into the groff_ms macros)
                                        (Luke Smith made a good video about groff)


                                        Source: https://github.com/xnacly


+ --------------------------------------------- + Arguments + --------------------------------------------- +

  $ -input / -i
        [required] file to feed into create.py (must be .ms format and valid groff_ms macro format)

  $ -output / -o
        [optional] file to output the compiled pdf to (will replace already existing matching file)

  $ -preserve-temp / -pre
        [optional] preserves the <date:time>_temp.ms files in /cache

  Example:
        $ python3 TeG.py -i='assets/example.ms' -o='example_file'
+ --------------------------------------------- + --------- + --------------------------------------------- +
```
