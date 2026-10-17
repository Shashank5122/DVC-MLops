"use client";

import { FormEvent, useCallback, useEffect, useState } from "react";

import { ErrorNotice } from "@/components/ErrorNotice";
import { RelationshipPill } from "@/components/Pill";
import { api } from "@/lib/api";
import type { Competitor, CompetitorRelationship } from "@/lib/types";

const RELATIONSHIPS: CompetitorRelationship[] = ["direct", "indirect", "alternative", "incumbent"];

interface DraftState {
  name: string;
  website: string;
  relationship_type: CompetitorRelationship;
}

const EMPTY_DRAFT: DraftState = { name: "", website: "", relationship_type: "direct" };

export function CompetitorTable({
  workspaceKey,
  brandId,
  initial,
}: {
  workspaceKey: string;
  brandId: string;
  initial: Competitor[];
}) {
  const [rows, setRows] = useState<Competitor[]>(initial);
  const [draft, setDraft] = useState<DraftState>(EMPTY_DRAFT);
  const [error, setError] = useState<unknown>(null);
  const [busy, setBusy] = useState(false);
  const [editingId, setEditingId] = useState<string | null>(null);

  useEffect(() => setRows(initial), [initial]);

  const refresh = useCallback(async () => {
    try {
      setRows(await api.listCompetitors(workspaceKey, brandId));
      setError(null);
    } catch (cause) {
      setError(cause);
    }
  }, [workspaceKey, brandId]);

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError(null);
    try {
      if (editingId) {
        await api.updateCompetitor(workspaceKey, brandId, editingId, {
          name: draft.name.trim(),
          website: draft.website.trim() || null,
          relationship_type: draft.relationship_type,
        });
      } else {
        await api.addCompetitor(workspaceKey, brandId, {
          name: draft.name.trim(),
          website: draft.website.trim() || null,
          relationship_type: draft.relationship_type,
        });
      }
      setDraft(EMPTY_DRAFT);
      setEditingId(null);
      await refresh();
    } catch (cause) {
      setError(cause);
    } finally {
      setBusy(false);
    }
  }

  async function remove(competitor: Competitor) {
    const confirmed = window.confirm(`Remove ${competitor.name} from this brand's set?`);
    if (!confirmed) return;
    setBusy(true);
    try {
      await api.removeCompetitor(workspaceKey, brandId, competitor.id);
      await refresh();
      setError(null);
    } catch (cause) {
      setError(cause);
    } finally {
      setBusy(false);
    }
  }

  function startEdit(competitor: Competitor) {
    setEditingId(competitor.id);
    setDraft({
      name: competitor.name,
      website: competitor.website ?? "",
      relationship_type: competitor.relationship_type,
    });
  }

  return (
    <section className="card">
      <div className="card-head">
        <h2>Competitor set</h2>
        <p>
          {rows.length} tracked · the comparison set used in measurement (never blended into a
          single score)
        </p>
      </div>

      {error ? <ErrorNotice error={error} title="Competitor update failed" /> : null}

      {rows.length === 0 ? (
        <p style={{ color: "var(--text-muted)" }}>
          No competitors yet. Add at least two before measurement begins — a brand with no
          comparison set cannot produce a meaningful visibility reading.
        </p>
      ) : (
        <div className="table-wrap" style={{ marginBottom: "1rem" }}>
          <table>
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Domain</th>
                <th scope="col">Relationship</th>
                <th scope="col">
                  <span className="visually-hidden">Actions</span>
                </th>
              </tr>
            </thead>
            <tbody>
              {rows.map((competitor) => (
                <tr key={competitor.id}>
                  <td>{competitor.name}</td>
                  <td className="mono">{competitor.normalised_domain ?? "—"}</td>
                  <td>
                    <RelationshipPill type={competitor.relationship_type} />
                  </td>
                  <td style={{ textAlign: "right", whiteSpace: "nowrap" }}>
                    <button
                      type="button"
                      data-size="sm"
                      data-variant="ghost"
                      onClick={() => startEdit(competitor)}
                      disabled={busy}
                    >
                      edit
                    </button>{" "}
                    <button
                      type="button"
                      data-size="sm"
                      data-variant="danger"
                      onClick={() => void remove(competitor)}
                      disabled={busy}
                    >
                      remove
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}

      <form onSubmit={submit} className="competitor-row-form" aria-label="Add or edit a competitor">
        <div className="field" style={{ marginBottom: 0 }}>
          <label htmlFor="competitor-name">{editingId ? "Edit name" : "Competitor name"}</label>
          <input
            id="competitor-name"
            type="text"
            required
            minLength={2}
            maxLength={200}
            value={draft.name}
            onChange={(event) => setDraft({ ...draft, name: event.target.value })}
            placeholder="Northbeam"
            disabled={busy}
          />
        </div>
        <div className="field" style={{ marginBottom: 0 }}>
          <label htmlFor="competitor-website">Website (optional)</label>
          <input
            id="competitor-website"
            type="text"
            maxLength={300}
            value={draft.website}
            onChange={(event) => setDraft({ ...draft, website: event.target.value })}
            placeholder="northbeam.io"
            disabled={busy}
          />
        </div>
        <div className="field" style={{ marginBottom: 0 }}>
          <label htmlFor="competitor-rel">Relationship</label>
          <select
            id="competitor-rel"
            value={draft.relationship_type}
            onChange={(event) =>
              setDraft({
                ...draft,
                relationship_type: event.target.value as CompetitorRelationship,
              })
            }
            disabled={busy}
          >
            {RELATIONSHIPS.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </div>
        <div className="actions" style={{ marginTop: 0 }}>
          <button type="submit" data-variant="primary" disabled={busy || draft.name.trim().length < 2}>
            {busy ? <span className="spinner" /> : null}
            {editingId ? "Save" : "Add"}
          </button>
          {editingId ? (
            <button
              type="button"
              data-variant="ghost"
              onClick={() => {
                setEditingId(null);
                setDraft(EMPTY_DRAFT);
              }}
              disabled={busy}
            >
              cancel
            </button>
          ) : null}
        </div>
      </form>
    </section>
  );
}
