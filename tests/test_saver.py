import builtins
import json
import os
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from config import ROOT_DIR
from src.saver import BaseSaver, JsonSaver

path = Path.joinpath(ROOT_DIR, "data", "test.json")


def test_BaseVacancies():
    with pytest.raises(TypeError):
        thing = BaseSaver()


def test_json_saver():
    data1 = [{"id": 2}, {"id": 1}]
    data2 = [{"id": 2}, {"id": 3}]
    jsonchik = JsonSaver(path)
    jsonchik.json_save(data1)
    jsonchik.json_save(data2)
    assert jsonchik.json_load() == [{"id": 2}, {"id": 1}, {"id": 3}]
    jsonchik.json_clear()
    assert jsonchik.json_load() == []
    os.system(f"del {path}")
