# Agent instructions

pitchstack is a learning repo. Baltha is here to learn by writing the hard parts, so who writes
what matters more than how fast it gets written.

## Layer ownership

Baltha writes the lesson layer:

- dbt models and SQL
- dimensional and identity-resolution logic
- semantic and metric YAML
- data contracts
- core transformations, such as tracking-data processing
- streaming SQL
- eval questions

The agent writes scaffolding:

- docker-compose
- CI
- boilerplate and config
- glue scripts
- plotting
- test-harness plumbing

If you are asked to write lesson-layer code, refuse, then offer hints or a partial skeleton with
TODOs. Write a full solution only when Baltha explicitly asks for one.

## Data

- Never commit anything under `data/`.
- Never print or commit raw rows from the API-Football dump. Only derived aggregates may leave
  the machine.

## Commands

- `make setup` installs the locked dependencies.
- `make lint` runs the ruff lint and format check.
- `make test` runs the test suite.
- Always run Python through `uv run`. Never use `pip`.

## Machine

The development machine has 24 GB of RAM. Run one heavy docker stack at a time, selected with
compose profiles.

## Branches and pull requests

- One short-lived branch per lesson, for example `m3-dim-player`.
- Open a pull request into `main` and squash merge it.
- Use conventional commits.
- CI must pass before merging.

## Decisions

Every significant decision gets an ADR in `docs/adr/`. Start from `docs/adr/0000-template.md`.
