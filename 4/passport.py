import re
import fire
from typing import List, Dict


def check_height(hgt_str: str) -> int:
    if hgt_str.endswith("cm"):
        height_cm = int(hgt_str[:-2])
        return 150 <= height_cm <= 193
    elif hgt_str.endswith("in"):
        height_in = int(hgt_str[:-2])
        return 59 <= height_in <= 76
    return False


REQUIRED_FIELDS = {
    "byr": {"type": int, "length": 4, "min": 1920, "max": 2002},
    "iyr": {
        "type": int,
        "length": 4,
        "min": 2010,
        "max": 2020,
    },
    "eyr": {"type": int, "length": 4, "min": 2020, "max": 2030},
    "hgt": {"check_override": check_height, "type": int},
    "hcl": {"type": str, "length": 7, "regex": r"\#[a-z0-9]{6}"},
    "ecl": {"type": str, "length": 3, "accepted_values": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]},
    "pid": {"length": 9, "type": int, "regex": r"[0-9]{9}"},
}


def read_input(filename: str) -> List[Dict]:
    with open(filename, "r") as f:
        passports = []
        curr = {}
        for line in f.readlines():
            if line == "\n":
                passports.append(curr)
                curr = {}
            else:
                new_key_values = dict(kv.split(":") for kv in line.strip().split())
                curr.update(new_key_values)
        new_key_values = dict(kv.split(":") for kv in line.strip().split())
        curr.update(new_key_values)
        passports.append(curr)
        return passports


def is_valid(passport: Dict[str, str]):
    if not all(field in passport for field in REQUIRED_FIELDS):
        return False
    for field, reqs in REQUIRED_FIELDS.items():
        try:
            check = reqs.get("check_override")
            
            if check:
                assert check(passport[field]), "check override failed"
                continue

            type_cast = reqs.get("type")

            value = type_cast(passport[field])

            length = reqs.get("length")
            min = reqs.get("min")
            max = reqs.get("max")
            regex = reqs.get("regex")

            accepted_values = reqs.get("accepted_values")

            if length:
                assert len(passport[field]) == length, f"{field}: len check failed"

            if min:
                assert value >= min, f"{field}: value: {value}, min: {min}; check failed"
            if max:
                assert value <= max, f"{field}: max check failed"

            if regex:
                match = re.match(regex, passport[field])
                assert match is not None, f"{field}: Regex"

            if accepted_values:
                assert value in accepted_values, f"{field}: accepted_values"

        except (AssertionError, ValueError) as e:
            return False
    return True


def count_valid(filename: str) -> int:
    return sum(1 if is_valid(passport) else 0 for passport in read_input(filename))


if __name__ == "__main__":
    fire.Fire()