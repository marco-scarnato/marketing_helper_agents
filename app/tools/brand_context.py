from __future__ import annotations

import asyncpg

from app.core.config import settings


async def load_brand_context(client_id: str) -> dict[str, object]:
    query = """
        SELECT business_description, mission, vision, unique_value_proposition
        FROM brand_identity
        WHERE client_id = $1
        LIMIT 1
    """
    conn = await asyncpg.connect(settings.POSTGRES_URL)
    try:
        row = await conn.fetchrow(query, client_id)
        return dict(row) if row else {}
    finally:
        await conn.close()
