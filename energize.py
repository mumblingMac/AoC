#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import json
import logging
import pathlib
import string
import sys
import threading
import time
from textwrap import TextWrapper

import click
import requests
from bs4 import BeautifulSoup
from jinja2 import Template

SOLUTION_FILE = "run.py"
PUZZLE_FILE = "input.txt"
PROBLEM_FILE = "scenario.txt"

CONFIG_OPTIONS = [
    "DOWNLOAD_INPUT",
    "DOWNLOAD_PROBLEM",
    "DOWNLOAD_TEMPLATE",
    "SESSION_ID",
]

logger = logging.getLogger(__name__)


class AdventOfCode:
    """Interact with the Advent Of Code Website."""

    def __init__(self, session: requests.Session = None):
        self.__base_url = "https://adventofcode.com"
        self.__user_agent = "advent_of_code_directory_energizer"
        self.__session = session

    @property
    def base_url(self) -> str:
        """Retrieve the base_url."""
        return self.__base_url

    @property
    def session(self) -> requests.Session:
        """Retrieve the session object."""
        if self.__session is None:
            self.__session = requests.Session()
        return self.__session

    def get_puzzle_input(self, date) -> str:
        url = f"{self.base_url}/{date.year}/day/{date.day}/input"
        response = self.session.get(url)
        if response.ok:
            puzzle_input = response.text
        else:
            puzzle_input = None
        return puzzle_input

    def get_statement(self, date) -> str:
        url = f"{self.base_url}/{date.year}/day/{date.day}"
        response = self.session.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text, "html.parser")
            wrapper = TextWrapper()

            statement = ""
            for article in soup("article"):
                contexts = article.get_text().replace(" ---", " ---\n")
                for paragraph in contexts.splitlines():
                    paragraph = wrapper.fill(paragraph)
                    if paragraph and paragraph[-1] in string.punctuation:
                        paragraph += "\n"
                    statement += f"{paragraph}\n"
        else:
            statement = None
        return statement


class AoCEnergizer:
    """Advent of Code Energizer for creating working directories."""

    __instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
            cls.__instance.__config_file = (
                pathlib.Path(__file__).parent.resolve().joinpath(f".{pathlib.Path(__file__).stem}")
            )
            cls.__instance.__config_data = None
            cls.__advent_of_code = None
        return cls.__instance

    @property
    def config(self) -> dict:
        """Retrieve the config data."""
        if self.__config_data is None:
            if self.__config_file.exists():
                with open(self.__config_file, "r") as data:
                    self.__config_data = json.load(data)
            else:
                self.__config_data = {}
        return self.__config_data

    @config.setter
    def config(self, data: dict) -> dict:
        self.__config_data = data
        with open(self.__config_file, "w") as file:
            json.dump(self.__config_data, file, indent=4)

    @property
    def advent_of_code(self) -> AdventOfCode:
        """Retrieve AdventOfCode object."""
        if self.__advent_of_code is None:
            session = requests.Session()
            if self.config.get("SESSION_ID"):
                session.cookies.set(
                    "session",
                    self.config.get("SESSION_ID"),
                )
            self.__advent_of_code = AdventOfCode(session)
        return self.__advent_of_code

    def process_day(self, date) -> None:
        """Process Advent of Code for a given date."""
        folder = pathlib.Path(f"{date.year}") / f"{date.day:02d}"
        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)

        if self.config.get("DOWNLOAD_PROBLEM"):
            problem_file = folder.joinpath(PROBLEM_FILE)
            if problem_file.exists():
                with open(problem_file, "r") as file:
                    problem_statement = file.read()
            else:
                problem_statement = ""

            if "--- Part Two ---" not in problem_statement:
                problem_statement = self.advent_of_code.get_statement(date)
                if problem_statement is not None:
                    with open(problem_file, "w") as file:
                        file.write(problem_statement)

        if self.config.get("DOWNLOAD_INPUT"):
            puzzle_file = folder.joinpath(PUZZLE_FILE)
            if puzzle_file.exists():
                pass
            elif not self.config.get("SESSION_ID"):
                logger.warning("SESSION_ID is required. " "Your puzzle input is specific to your account.")
            else:
                puzzle_input = self.advent_of_code.get_puzzle_input(date)
                if puzzle_input is not None:
                    with open(puzzle_file, "w") as file:
                        file.write(puzzle_input)

        if self.config.get("DOWNLOAD_TEMPLATE"):
            solution_file = folder.joinpath(SOLUTION_FILE)
            if solution_file.exists():
                logger.debug("Solution file has been previously written.")
            else:
                template_file = pathlib.Path(__file__).parent.resolve().joinpath("code.tmpl")
                with open(template_file, "r") as file:
                    template = Template(file.read())
                with open(solution_file, "w") as code:
                    code.write(template.render(date=date, input_file=PUZZLE_FILE))


class Spinner:
    busy = False
    delay = 0.25

    @staticmethod
    def spinning_cursor():
        while 1:
            for cursor in "|/-\\":
                yield cursor

    def __init__(self, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay):
            self.delay = delay

    def spinner_task(self):
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write("\b")
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, value, tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False


@click.group(invoke_without_command=True)
@click.pass_context
def cli(context):
    context.obj = AoCEnergizer.instance()
    if context.invoked_subcommand is None:
        today = datetime.datetime.now()
        opening_day = datetime.datetime.strptime(f"12 01 {today.year}", "%m %d %Y")

        if today.month == 12 and today.day >= 26:
            opening_day = datetime.datetime.strptime(f"12 01 {today.year + 1}", "%m %d %Y")

        days_until_start = (opening_day - today).days

        if days_until_start > 0:
            click.echo(f"{days_until_start} days till Advent of Code {today.year}")
        else:
            context.obj.process_day(datetime.datetime.now())
    else:
        context.invoked_subcommand


@cli.command()
@click.argument(
    "year",
    type=int,
    nargs=1,
)
@click.pass_obj
def download(energizer, year):
    start_date = datetime.datetime.strptime(f"12 01 {year}", "%m %d %Y")
    today = datetime.datetime.now()

    with Spinner():
        for i in range(25):
            date = start_date + datetime.timedelta(days=i)
            if date < today:
                energizer.process_day(date)


@cli.command()
@click.argument("key", nargs=1, required=False)
@click.argument("value", nargs=1, required=False)
@click.pass_obj
def config(energizer, key, value):

    if key and key.upper() not in CONFIG_OPTIONS:
        click.echo("Invalid key.")
        sys.exit(1)

    config = energizer.config

    if not key:
        for k, v in config.items():
            click.echo(f"{k} : {v}")
    elif not value:

        click.echo(f"{key.upper()} : {config[key.upper()]}")
    else:
        if key.upper().startswith("DOWNLOAD"):
            if value.lower() == "true":
                value = True
            else:
                value = False
        config[key.upper()] = value

        energizer.config = config


if __name__ == "__main__":
    cli()
