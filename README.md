# pitchstack

A learning repo that builds a football club data platform, one module at a time.

## Mission

<!-- BALTHA: write this -->

## Architecture (to be)

Diagram arrives in M2.

## Data sources

| Source | Coverage and access | Licence and terms |
| --- | --- | --- |
| StatsBomb Open Data | Public on GitHub | Attribution required |
| IDSSE (Sportec/DFL) | 7 matches, Bundesliga and 2. Bundesliga 2022/23, event + 25 Hz tracking | CC-BY 4.0 |
| SkillCorner Open Data | 10 A-League 2024/25 matches | Credit SkillCorner |
| Gradient World Cup 2022 | Free on request | Terms to be checked before publishing derived data |
| API-Football dump | Local only, never committed | Derived aggregates only |

Raw and derived data live under `data/` and are gitignored. Code must be able to re-download
public data.

## How to run

Prerequisites: [uv](https://docs.astral.sh/uv/) and `make`.

```sh
make setup   # create the virtualenv and install the locked dependencies
make lint    # ruff lint and format check
make test    # run the test suite
```

## Repo layout

| Folder | What lives there |
| --- | --- |
| `ingest/` | Download raw data from each source and land it under `data/`. |
| `orchestration/` | Schedule and run the pipelines. |
| `lakehouse/` | Table storage and query engine setup. |
| `models/` | dbt models and SQL: staging, dimensional and identity-resolution logic. |
| `semantic/` | Semantic layer and metric definitions in YAML. |
| `contracts/` | Data contracts between producers and consumers. |
| `catalog/` | Data catalog and metadata. |
| `tracking/` | Tracking-data processing. |
| `streaming/` | Streaming pipelines and streaming SQL. |
| `mcp/` | MCP server that exposes the platform to agents. |
| `evals/` | Eval questions and the harness that scores answers. |
| `docs/` | Blueprint, architecture decision records (`adr/`) and lesson writeups (`writeups/`). |
| `tests/` | Repo-level tests. |
