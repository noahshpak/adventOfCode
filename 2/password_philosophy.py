import fire
from typing import NamedTuple, Tuple, Callable


class Policy(NamedTuple):
    i: int
    j: int
    char: str


def read_input(filename: str) -> Tuple[Policy, str]:
    with open(filename, "r") as f:
        for line in f.readlines():
            policy, password = line.split(": ")
            i, j, char = policy.replace("-", " ").split(" ")
            yield Policy(i=int(i), j=int(j), char=char), password


def _sled_shop_policy(policy: Policy, password: str) -> bool:
    return policy.i <= password.count(policy.char) <= policy.j

def _toboggan_policy(policy: Policy, password: str) -> bool:
    return (password[policy.i - 1] == policy.char) != (password[policy.j - 1] == policy.char)


def count_valid_passwords(filename: str, policy_rule: Callable[[Policy, str], bool] = _toboggan_policy) -> int:
    return sum(
        1 if policy_rule(policy=policy, password=password) else 0
        for policy, password in read_input(filename)
    )


if __name__ == "__main__":
    fire.Fire()
