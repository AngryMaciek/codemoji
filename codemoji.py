"""
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
"""

# imports
import os
import time
import logging
import logging.handlers
from argparse import ArgumentParser, RawTextHelpFormatter


def parse_arguments():
    """Parser of the command-line arguments."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "-v",
        "--verbosity",
        dest="verbosity",
        choices=("DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"),
        default="ERROR",
        help="Verbosity/Log level. Defaults to ERROR",
    )
    parser.add_argument(
        "-l", "--logfile", dest="logfile", help="Store log to this file."
    )
    parser.add_argument(
        "--dictionary",
        dest="dictionary",
        required=True,
        help="Mapping between ASCII characters and emojis.",
    )
    parser.add_argument(
        "--input", dest="input", required=True, help="Path to the input file.",
    )
    parser.add_argument(
        "--output", dest="output", required=True, help="Path for the output file.",
    )
    return parser


##############################################################################


def main():
    """Main body of the script."""

    with open(options.dictionary) as f:
        mapping = {line[0]: line[-1] for line in f.read().splitlines()}

    with open(options.input, "r") as f_in, open(options.output, "w") as f_out:
        for line in f_in.read().splitlines():
            for character in line:
                try:
                    f_out.write(mapping[character])
                except KeyError as key_error:
                    f_out.write(character)
            f_out.write(os.linesep)


##############################################################################

if __name__ == "__main__":

    try:
        # parse the command-line arguments
        options = parse_arguments().parse_args()

        # set up logging during the execution
        formatter = logging.Formatter(
            fmt="[%(asctime)s] %(levelname)s - %(message)s",
            datefmt="%d-%b-%Y %H:%M:%S",
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger = logging.getLogger("logger")
        logger.setLevel(logging.getLevelName(options.verbosity))
        logger.addHandler(console_handler)
        if options.logfile is not None:
            logfile_handler = logging.handlers.RotatingFileHandler(
                options.logfile, maxBytes=50000, backupCount=2
            )
            logfile_handler.setFormatter(formatter)
            logger.addHandler(logfile_handler)

        # execute the body of the script
        start_time = time.time()
        logger.info("Starting script")
        main()
        seconds = time.time() - start_time

        # log the execution time
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        logger.info(
            "Successfully finished in {hours}h:{minutes}m:{seconds}s",
            hours=int(hours),
            minutes=int(minutes),
            seconds=int(seconds) if seconds > 1.0 else 1,
        )
    # log the exception in case it happens
    except Exception as e:
        logger.exception(str(e))
        raise e
