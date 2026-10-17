"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useState } from "react";

import { ErrorNotice } from "@/components/ErrorNotice";
import { PageHeader } from "@/components/PageHeader";
import { TopBar } from "@/components/TopBar";
import { api } from "@/lib/api";
import { readWorkspaceKey, writeWorkspace, writeWorkspaceKeyOnly } from "@/lib/workspace";

export default function SetupPage() {
  const router = useRouter();
  const [name, setName] = useState("");
  const [existingKey, setExistingKey] = useState("");
  const [createdKey, setCreatedKey] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<unknown>(null);
  const [notice, setNotice] = useState<string | null>(null);

  async function createWorkspace(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError(null);
    try {
      const result = await api.createWorkspace({ name: name.trim() });
      writeWorkspace(result.workspace_key, {
        name: result.workspace.name,
        slug: result.workspace.slug,
        keyLast4: result.workspace.key_last4,
      });
      setCreatedKey(result.workspace_key);
      router.push("/");
      router.refresh();
    } catch (cause) {
      setError(cause);
    } finally {
      setBusy(false);
    }
  }

  async function useExistingKey(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setBusy(true);
    setError(null);
    setNotice(null);
    const key = existingKey.trim();
    try {
      const workspace = await api.currentWorkspace(key);
      writeWorkspace(key, {
        name: workspace.name,
        slug: workspace.slug,
        keyLast4: workspace.key_last4,
      });
      router.push("/");
      router.refresh();
    } catch (cause) {
      setError(cause);
    } finally {
      setBusy(false);
    }
  }

  return (
    <>
      <TopBar />
      <main>
        <PageHeader
          title="Connect a workspace"
          description="A workspace is one tenant: a client company, or your own test tenant. The key identifies the workspace on every request and is stored only in this browser's local storage for the pilot."
        />

        <div className="grid grid-2">
          <section className="card">
            <h2>Create a workspace</h2>
            <p style={{ color: "var(--text-muted)", fontSize: "0.9rem" }}>
              Uses the development bootstrap endpoint. It is disabled in staging and production,
              where workspaces are created by an operator with{" "}
              <code>python -m scripts.bootstrap_workspace</code>.
            </p>
            <form onSubmit={createWorkspace}>
              <div className="field">
                <label htmlFor="workspace-name">Workspace name</label>
                <input
                  id="workspace-name"
                  type="text"
                  required
                  minLength={2}
                  maxLength={200}
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                  placeholder="Acme Analytics (pilot)"
                  disabled={busy}
                />
                <span className="hint">The slug is derived from this name.</span>
              </div>
              <div className="actions">
                <button type="submit" data-variant="primary" disabled={busy || name.trim().length < 2}>
                  {busy ? <span className="spinner" /> : null} Create workspace
                </button>
              </div>
            </form>
            {createdKey ? (
              <div className="notice" data-tone="warn" style={{ marginTop: "1rem" }}>
                <strong>Copy this key now — it is shown once</strong>
                <div className="mono" style={{ wordBreak: "break-all" }}>
                  {createdKey}
                </div>
                The backend stores only its SHA-256 hash. It cannot be retrieved again.
              </div>
            ) : null}
          </section>

          <section className="card">
            <h2>Use an existing key</h2>
            <p style={{ color: "var(--text-muted)", fontSize: "0.9rem" }}>
              Paste a key issued earlier by the bootstrap script or the dev endpoint.
            </p>
            <form onSubmit={useExistingKey}>
              <div className="field">
                <label htmlFor="existing-key">Workspace key</label>
                <input
                  id="existing-key"
                  type="text"
                  required
                  value={existingKey}
                  onChange={(event) => setExistingKey(event.target.value)}
                  placeholder="sg_…"
                  autoComplete="off"
                  spellCheck={false}
                  disabled={busy}
                />
                <span className="hint">
                  Stored in this browser only. Nothing is sent anywhere except the SignalGEO
                  backend.
                </span>
              </div>
              <div className="actions">
                <button type="submit" disabled={busy || !existingKey.trim()}>
                  {busy ? <span className="spinner" /> : null} Connect
                </button>
                {readWorkspaceKey() ? (
                  <span className="hint">A key is already stored on this device.</span>
                ) : null}
              </div>
            </form>
            {notice ? (
              <div className="notice" data-tone="info" style={{ marginTop: "1rem" }}>
                {notice}
              </div>
            ) : null}
          </section>
        </div>

        <div style={{ marginTop: "1rem" }}>
          <ErrorNotice error={error} title="Could not connect to a workspace" />
        </div>

        <div className="notice" data-tone="info" style={{ marginTop: "1rem" }}>
          <strong>Pilot limitation, stated plainly</strong>
          This is not user authentication. There are no accounts, roles, sessions or SSO. Anyone
          holding a workspace key can read and write that workspace, so keys must be treated as
          secrets and rotated by deleting the workspace. Real auth is deferred until after the
          pilot.
        </div>

        <div className="actions" style={{ marginTop: "1rem" }}>
          <button type="button" data-variant="ghost" onClick={() => router.push("/providers")}>
            view provider &amp; compliance status →
          </button>
          <button type="button" data-variant="ghost" onClick={() => { setNotice(null); void api.health().then((h) => setNotice(`API ${h.version} · environment ${h.environment} · database ${h.database}`)).catch((cause: unknown) => setError(cause)); }}>
            ping backend
          </button>
        </div>
      </main>
    </>
  );
}
