import time
from abc import ABC, abstractmethod
from typing import Any, Dict, NewType
import json
import os

JSON = NewType("Json", Dict[str, Any])


class DatabaseError(Exception):
    pass


class Engine(ABC):

    @abstractmethod
    def insert(self, table: str, data: JSON) -> None:
        pass

    @abstractmethod
    def read_all(self, table: str) -> JSON:
        pass


class JSONFileEngine(Engine):

    def __init__(self, path: str):
        self.path = path
        assert os.path.exists(self.path) and os.path.isfile(self.path), \
            f"Invalid path: `{self.path}`"
        self._data = self._read_file()

    def insert(self, table: str, data: JSON) -> None:
        """Insert data."""
        table_data = self._data.get(table)
        if table_data is None:
            self._data[table] = {}

        self._data[table][time.time()] = data
        self._write_file(self._data)

    def read_all(self, table: str) -> JSON:
        """Read all data."""
        try:
            return self._data[table]
        except KeyError:
            raise DatabaseError(f"Provided table does not exist: `{table}`")

    def _write_file(self, data: JSON) -> None:
        """Write JSON file."""

        with open(self.path, "w") as f:
            json.dump(data, f, indent=4, sort_keys=True)

    def _read_file(self) -> JSON:
        """Read JSON file."""
        with open(self.path, "r") as f:
            return json.load(f)
