# my-heritage

Telegram bot for searching archival photos by location via [PastVu](https://pastvu.com/).

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

Create a `.env` with `TG_TOKEN` and `ADMIN_CHAT_ID`.

## Commands

```bash
make run        # start the bot
make lint       # ruff check + format check
make fmt        # auto-fix with ruff
make typecheck  # ty
make test       # pytest
```
