from dataclasses import dataclass


@dataclass(frozen=True)
class Actor:
    tenant: str
    admin: bool


def delete_document(actor: Actor, doc_id: str, documents: dict[str, str]) -> tuple[str, dict[str, str]]:
    """Pure, illustrative state transition; documents maps ID to tenant."""
    if doc_id not in documents:
        return "NOT_FOUND", documents.copy()
    if not actor.admin or documents[doc_id] != actor.tenant:
        return "DENIED", documents.copy()
    return "DELETED", {key: tenant for key, tenant in documents.items() if key != doc_id}
