#!/usr/bin/env python

from __future__ import annotations

import re

from dataclasses import dataclass
from typing import Dict, Self
from types import MethodType


@dataclass
class Rating:
    x: int
    m: int
    a: int
    s: int

    def total(self) -> int:
        return self.x + self.m + self.a + self.s

    @classmethod
    def from_str(cls, s: str) -> Rating:
        if m := re.match(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", s):
            return Rating(
                int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
            )
        raise Exception(f"Invalid Rating <{s}>")


def _compile(name: str, expressions: list[str]) -> str:
    code = f"def rule_{name}(self, r: Rating) -> bool:\n"
    indent = "    "
    for expression in expressions:
        match re.findall(r"(\w+|<|>|:)", expression):
            case [part, "<", value, ":", "A"]:
                code += indent + f"if r.{part} < {value}:\n"
                code += indent + "    return True\n"
                code += indent + "else:\n"
            case [part, ">", value, ":", "A"]:
                code += indent + f"if r.{part} > {value}:\n"
                code += indent + "    return True\n"
                code += indent + "else:\n"

            case [part, "<", value, ":", "R"]:
                code += indent + f"if r.{part} < {value}:\n"
                code += indent + "    return False\n"
                code += indent + "else:\n"
            case [part, ">", value, ":", "R"]:
                code += indent + f"if r.{part} > {value}:\n"
                code += indent + "    return False\n"
                code += indent + "else:\n"

            case [part, "<", value, ":", workflow]:
                code += indent + f"if r.{part} < {value}:\n"
                code += indent + f"    return self.rule_{workflow}(r)\n"
                code += indent + "else:\n"
            case [part, ">", value, ":", workflow]:
                code += indent + f"if r.{part} > {value}:\n"
                code += indent + f"    return self.rule_{workflow}(r)\n"
                code += indent + "else:\n"

            case ["A"]:
                code += indent + "return True\n"
            case ["R"]:
                code += indent + "return False\n"

            case [workflow]:
                code += indent + f"return self.rule_{workflow}(r)\n"
        indent += "    "
    return code


class WorkflowEngine:
    def __init__(self, workflows: list[str]):
        for workflow in workflows:
            self.compile(workflow)

    def compile(self, workflow: str):
        if m := re.match(r"(\w+){(.+)}", workflow):
            name, expressions = m.group(1), m.group(2).split(",")
            code = _compile(name, expressions)
            environment: Dict = {}
            exec(code, environment)
            setattr(self, f"rule_{name}", MethodType(environment[f"rule_{name}"], self))

    def process(self, rating: Rating) -> bool:
        return self.rule_in(rating)


def read_input() -> tuple[WorkflowEngine, list[Rating]]:
    with open("day19.txt") as f:
        workflows, ratings = f.read().split("\n\n")
        return (
            WorkflowEngine(workflows.split("\n")),
            [Rating.from_str(s) for s in ratings.split("\n")],
        )


def part1() -> int:
    engine, ratings = read_input()
    return sum(rating.total() for rating in ratings if engine.process(rating))


if __name__ == "__main__":
    print("Part 1:", part1())
