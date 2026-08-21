"""Minimal example for DateParseLib."""

from dateparselib import dateparselib


def main():
 runner = dateparselib({"name": "DateParseLib", "dry_run": False})
 result = runner.execute()
 print(result)


if __name__ == "__main__":
 main()