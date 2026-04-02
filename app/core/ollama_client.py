from __future__ import annotations

import httpx

from app.core.config import settings


class OllamaClient:
    def __init__(self) -> None:
        self._base_url = settings.OLLAMA_URL
        self._timeout = settings.REQUEST_TIMEOUT_SECONDS

    async def generate(self, prompt: str, model: str | None = None) -> str:
        payload = {
            "model": model or settings.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
        }
        async with httpx.AsyncClient(timeout=self._timeout) as client:
            response = await client.post(f"{self._base_url}/api/generate", json=payload)
            response.raise_for_status()
            data = response.json()
            return str(data.get("response", ""))
