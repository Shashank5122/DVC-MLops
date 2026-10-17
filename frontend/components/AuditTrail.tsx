"use client";

import { useCallback, useEffect, useState } from "react";

import { api } from "@/lib/api";
import type { AuditEvent } from "@/lib/types";
import { ErrorNotice } from "@/components/ErrorNotice";

function formatChange(value: unknown): string {
  if (value && typeof value === "object") {
    const record = value as Record<string, unknown>;
    if ("from" in record && "to" in record) return `${String(record.from)} → ${String(record.to)}`;
    return JSON.stringify(record);
  }
  return String(value);
}

export function AuditTrail({
  workspaceKey,
  entityType,
  entityId,
  limit = 25,
}: {
  workspaceKey: string;
  entityType?: string;
  entityId?: string;
  limit?: number;
}) {
  const [events, setEvents] = useState<AuditEvent[]>([]);
  const [total, setTotal] = useState(0);
  const [error, setError] = useState<unknown>(null);
  const [loading, setLoading] = useState(true);

  const load = useCallback(
    async (signal: AbortSignal) => {
      setLoading(true);
      try {
        const page = await api.listAuditEvents(workspaceKey, {
          entityType,
          entityId,
          limit,
          signal,
        });
        setEvents(page.items);
        setTotal(page.total);
        setError(null);
      } catch (cause) {
        if (cause instanceof DOMException && cause.name === "AbortError") return;
        setError(cause);
      } finally {
        setLoading(false);
      }
    },
    [workspaceKey, entityType, entityId, limit],
  );

  useEffect(() => {
    const controller = new AbortController();
    void load(controller.signal);
    return () => controller.abort();
  }, [load]);

  return (
    <section className="card">
      <div className="card-head">
        <h2>Audit trail</h2>
        <p>
          {loading ? <span className="spinner" aria-label="loading" /> : null} {total} event
          {total === 1 ? "" : "s"} · append-only
        </p>
      </div>
      {error ? <ErrorNotice error={error} title="Could not load the audit trail" /> : null}
      {events.length === 0 && !loading ? (
        <p style={{ color: "var(--text-muted)", margin: 0 }}>No events recorded yet.</p>
      ) : (
        <div>
          {events.map((event) => (
            <div className="audit-item" key={event.id}>
              <time dateTime={event.created_at}>
                {new Date(event.created_at).toLocaleString(undefined, {
                  dateStyle: "medium",
                  timeStyle: "short",
                })}
              </time>
              <div>
                <strong className="mono">{event.action}</strong>{" "}
                <span style={{ color: "var(--text-muted)" }}>
                  {event.entity_type}
                  {event.entity_id ? ` · ${event.entity_id.slice(0, 8)}` : ""} · by {event.actor}
                </span>
                {Object.keys(event.changes).length > 0 ? (
                  <div className="changes">
                    {Object.entries(event.changes)
                      .map(([key, value]) => `${key}: ${formatChange(value)}`)
                      .join("  |  ")}
                  </div>
                ) : null}
              </div>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}
