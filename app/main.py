from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Pagamentos API", version="0.1.0")


class PagamentoIn(BaseModel):
    pedido_id: int
    valor: float


class Pagamento(PagamentoIn):
    id: int
    autorizado: bool


_pagamentos: list[Pagamento] = []


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/pagamentos", status_code=201)
def autorizar(data: PagamentoIn) -> Pagamento:
    pagamento = Pagamento(id=len(_pagamentos) + 1, autorizado=data.valor <= 10_000, **data.model_dump())
    _pagamentos.append(pagamento)
    return pagamento
