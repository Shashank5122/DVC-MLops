"use client";

import { useEffect, useState } from "react";

import { ErrorNotice } from "@/components/ErrorNotice";
import { Pill } from "@/components/Pill";
import { api } from "@/lib/api";
import type { ProviderInventory } from "@/lib/types";

export function ProviderTable() {
  const [inventory, setInventory] = useState<ProviderInventory | null>(null);
  const [error, setError] = useState<unknown>(null);

  useEffect(() => {
    const controller = new AbortController();
    api
      .providers({ signal: controller.signal })
      .then((result) => {
        setInventory(result);
        setError(null);
      })
      .catch((cause: unknown) => {
        if (cause instanceof DOMException && cause.name === "AbortError") return;
        setError(cause);
      });
    return () => controller.abort();
  }, []);

  if (error) return <ErrorNotice error={error} title="Could not load the provider inventory" />;
  if (!inventory)
    return (
      <p style={{ color: "var(--text-muted)" }}>
        <span className="spinner" /> Loading provider inventory…
      </p>
    );

  return (
    <div className="stack">
      <div
        className="notice"
        data-tone={inventory.provider_calls_enabled ? "danger" : "ok"}
        role="status"
      >
        <strong>
          External provider calls: {inventory.provider_calls_enabled ? "ENABLED" : "DISABLED"}
        </strong>
        {inventory.note}
      </div>

      {inventory.denied_pending_authorization.length > 0 ? (
        <div className="notice" data-tone="warn">
          <strong>Denied pending written authorization</strong>
          <ul>
            {inventory.denied_pending_authorization.map((provider) => (
              <li key={provider} className="mono">
                {provider}
              </li>
            ))}
          </ul>
          These are refused in configuration, not merely unused. Enabling one requires a code
          change plus separate authorization (gate M5) and, for Perplexity, written commercial
          clarification (gate W2).
        </div>
      ) : null}

      <div className="table-wrap">
        <table>
          <thead>
            <tr>
              <th scope="col">Adapter</th>
              <th scope="col">Surface</th>
              <th scope="col">Collection method</th>
              <th scope="col">Model identifier</th>
              <th scope="col">Citations</th>
              <th scope="col">Permitted now</th>
            </tr>
          </thead>
          <tbody>
            {inventory.adapters.map((adapter) => (
              <tr key={adapter.provider_id}>
                <td>
                  <strong>{adapter.display_name}</strong>
                  <div className="mono" style={{ color: "var(--text-faint)" }}>
                    {adapter.provider_id}
                  </div>
                </td>
                <td className="mono">{adapter.surface}</td>
                <td className="mono">{adapter.collection_method}</td>
                <td className="mono">{adapter.model_identifier}</td>
                <td>
                  <Pill
                    label={adapter.capability.returns_citations ? "yes" : "no"}
                    tone={adapter.capability.returns_citations ? "ok" : "neutral"}
                  />
                </td>
                <td>
                  <Pill
                    label={adapter.permitted_now ? "permitted" : "blocked"}
                    tone={adapter.permitted_now ? "ok" : "danger"}
                  />
                  <div style={{ color: "var(--text-faint)", fontSize: "0.78rem", marginTop: "0.2rem" }}>
                    {adapter.permission_reason}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
