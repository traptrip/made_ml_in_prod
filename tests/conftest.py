from pathlib import Path

import pytest
from hydra import initialize, compose

from .generate_fake_dataset import generate_dataset


@pytest.fixture
def config():
    with initialize(config_path="../ml_project/conf"):
        cfg = compose(
            config_name="config",
            return_hydra_config=True,
            overrides=["general.project_dir=${hydra.runtime.cwd}"],
        )
    return cfg


@pytest.fixture
def fake_dataset(config):
    df = generate_dataset(10, config.dataset.datapath)
    return df


@pytest.fixture
def fake_dataset_path(tmpdir, fake_dataset):
    dataset_fio = tmpdir.join("fake_dataset.csv")
    fake_dataset.to_csv(dataset_fio, index=False)
    return str(dataset_fio)