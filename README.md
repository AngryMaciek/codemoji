[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Codemoji 💥

> *Emojify your code away!*

*Maciek Bak*

## About

**Do you also hate reading someone else's code?**  

How many times did you have to dwell into a complete nonsense? But eventually the job needs to be done so you spent days trying to work things out all by yourself and there was nothing you could do about it...

Now you have your chance to retaliate! Prior sharing, convert your work into a beautiful sequence of colorful images and watch your adversaries cry blood while trying to decypther the source code :)

![Screenshot.png](Screenshot.png)

## Execution

Codemoji is implemented as a [Python] script, works well with interpreter version +3.5.

The interface of the script is pretty straightforward:
```text
$ python codemoji.py --help
usage: codemoji.py [-h] [-v {DEBUG,INFO,WARN,ERROR,CRITICAL}] [-l LOGFILE] --dictionary DICTIONARY --input INPUT --output OUTPUT

##############################################################################
#
#   Codemoji: Emojify your code away!
#
#   AUTHOR: Maciek_Bak
#   AFFILIATION: Swiss_Institute_of_Bioinformatics
#   CONTACT: very.angry.maciek@gmail.com
#   CREATED: 27-07-2020
#   LICENSE: MIT
#
##############################################################################

optional arguments:
  -h, --help            show this help message and exit
  -v {DEBUG,INFO,WARN,ERROR,CRITICAL}, --verbosity {DEBUG,INFO,WARN,ERROR,CRITICAL}
                        Verbosity/Log level. Defaults to ERROR
  -l LOGFILE, --logfile LOGFILE
                        Store log to this file.
  --dictionary DICTIONARY
                        Mapping between ASCII characters and emojis.
  --input INPUT         Path to the input file.
  --output OUTPUT       Path for the output file.
```

In its original form Codemoji converts all alphanumerical characters from the standard ASCII table into emojis of my choice (my personal favourites), however the user might specify custom mapping file. Have Fun!

## License

MIT License

[Python]: https://www.python.org/download/releases/3.0/
[git]: https://git-scm.com/
