from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

MODULE_FOLDERS = [
    "ingest",
    "orchestration",
    "lakehouse",
    "models",
    "semantic",
    "contracts",
    "catalog",
    "tracking",
    "streaming",
    "mcp",
    "evals",
]


def test_repo_layout():
    missing_folders = [name for name in MODULE_FOLDERS if not (REPO_ROOT / name).is_dir()]
    assert not missing_folders, f"missing module folders: {missing_folders}"

    missing_readmes = [
        name for name in MODULE_FOLDERS if not (REPO_ROOT / name / "README.md").is_file()
    ]
    assert not missing_readmes, f"module folders without a README.md: {missing_readmes}"
