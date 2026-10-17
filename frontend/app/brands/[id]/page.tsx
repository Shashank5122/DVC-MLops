"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { FormEvent, use, useCallback, useEffect, useState } from "react";

import { AuditTrail } from "@/components/AuditTrail";
import { CompetitorTable } from "@/components/CompetitorTable";
import { ErrorNotice } from "@/components/ErrorNotice";
import { PageHeader } from "@/components/PageHeader";
import { AuthorizationPills, VerificationPill } from "@/components/Pill";
import { TopBar } from "@/components/TopBar";
import { ApiError, api } from "@/lib/api";
import type { BrandDetail, FactVerificationStatus } from "@/lib/types";
import { clearWorkspace, readWorkspaceKey } from "@/lib/workspace";

const STATUSES: FactVerificationStatus[] = ["unverified", "in_progress", "verified"];

export default function BrandPage({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  const router = useRouter();
  const [key, setKey] = useState<string | null>(null);
  const [brand, setBrand] = useState<BrandDetail | null>(null);
  const [error, setError] = useState<unknown>(null);
  const [saving, setSaving] = useState(false);
  const [loading, setLoading] = useState(true);
  const [auditNonce, setAuditNonce] = useState(0);

  // Editable authorization / verification controls.
  const [status, setStatus] = useState<FactVerificationStatus>("unverified");
  const [siteAuth, setSiteAuth] = useState(false);
  const [retention, setRetention] = useState(false);
  const [category, setCategory] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    const stored = readWorkspaceKey();
    setKey(stored);
    if (!stored) router.replace("/setup");
  }, [router]);

  const load = useCallback(
    async (workspaceKey: string, signal: AbortSignal) => {
      setLoading(true);
      try {
        const detail = await api.getBrand(workspaceKey, id, { signal });
        setBrand(detail);
        setStatus(detail.fact_verification_status);
        setSiteAuth(detail.website_change_authorized);
        setRetention(detail.data_retention_permitted);
        setCategory(detail.category ?? "");
        setDescription(detail.description ?? "");
        setError(null);
      } catch (cause) {
        if (cause instanceof DOMException && cause.name === "AbortError") return;
        if (cause instanceof ApiError && cause.status === 401) {
          clearWorkspace();
          router.replace("/setup");
          return;
        }
        setError(cause);
      } finally {
        setLoading(false);
      }
    },
    [id, router],
  );

  useEffect(() => {
    if (!key) return;
    const controller = new AbortController();
    void load(key, controller.signal);
    return () => controller.abort();
  }, [key, load, auditNonce]);

  async function save(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!key || !brand) return;
    setSaving(true);
    setError(null);
    try {
      const updated = await api.updateBrand(key, brand.id, {
        fact_verification_status: status,
        website_change_authorized: siteAuth,
        data_retention_permitted: retention,
        category: category.trim() || null,
        description: description.trim() || null,
      });
      setBrand({ ...brand, ...updated });
      setAuditNonce((value) => value + 1);
    } catch (cause) {
      setError(cause);
    } finally {
      setSaving(false);
    }
  }

  async function remove() {
    if (!key || !brand) return;
    const confirmed = window.confirm(
      `Soft-delete ${brand.name}? Measurement history and the audit trail are retained.`,
    );
    if (!confirmed) return;
    setSaving(true);
    try {
      await api.deleteBrand(key, brand.id);
      router.push("/");
      router.refresh();
    } catch (cause) {
      setError(cause);
      setSaving(false);
    }
  }

  return (
    <>
      <TopBar />
      <main>
        {loading && !brand ? (
          <p style={{ color: "var(--text-muted)" }}>
            <span className="spinner" /> Loading brand…
          </p>
        ) : null}

        {brand ? (
          <>
            <PageHeader
              title={brand.name}
              description={`${brand.normalised_domain ?? "no domain recorded"} · ${brand.primary_region} / ${brand.primary_language}`}
              actions={
                <>
                  <Link href="/">
                    <button type="button" data-variant="ghost">
                      ← all brands
                    </button>
                  </Link>
                  <button
                    type="button"
                    data-variant="danger"
                    onClick={() => void remove()}
                    disabled={saving}
                  >
                    Soft-delete
                  </button>
                </>
              }
            />

            <div className="stack">
              <div className="notice" data-tone="info">
                <strong>Measurement not yet available</strong>
                This page records brand identity and authorizations only. Query registry, evidence
                ingestion, observations and visibility reporting arrive in Milestone 2 — and only
                from sources we are permitted to use. No external provider call is made by this
                build.
              </div>

              {error ? <ErrorNotice error={error} /> : null}

              <div className="grid grid-2">
                <section className="card">
                  <h2>Record</h2>
                  <dl className="kv">
                    <dt>Brand ID</dt>
                    <dd className="mono">{brand.id}</dd>
                    <dt>Slug</dt>
                    <dd className="mono">{brand.slug}</dd>
                    <dt>Website</dt>
                    <dd>{brand.website ?? "—"}</dd>
                    <dt>Normalised domain</dt>
                    <dd className="mono">{brand.normalised_domain ?? "—"}</dd>
                    <dt>Category</dt>
                    <dd>{brand.category ?? "—"}</dd>
                    <dt>Description</dt>
                    <dd>{brand.description ?? "—"}</dd>
                    <dt>Created</dt>
                    <dd>{new Date(brand.created_at).toLocaleString()}</dd>
                    <dt>Updated</dt>
                    <dd>{new Date(brand.updated_at).toLocaleString()}</dd>
                  </dl>
                  <div className="pills" style={{ display: "flex", gap: "0.35rem", flexWrap: "wrap", marginTop: "0.75rem" }}>
                    <VerificationPill status={brand.fact_verification_status} />
                    <AuthorizationPills
                      websiteChange={brand.website_change_authorized}
                      dataRetention={brand.data_retention_permitted}
                    />
                  </div>
                </section>

                <form className="card" onSubmit={save}>
                  <h2>Authorization &amp; verification</h2>
                  <p style={{ color: "var(--text-muted)", fontSize: "0.88rem" }}>
                    Every change here is written to the audit trail with a before/after value.
                  </p>

                  <div className="field">
                    <label htmlFor="status">Fact verification status</label>
                    <select
                      id="status"
                      value={status}
                      onChange={(event) =>
                        setStatus(event.target.value as FactVerificationStatus)
                      }
                      disabled={saving}
                    >
                      {STATUSES.map((option) => (
                        <option key={option} value={option}>
                          {option}
                        </option>
                      ))}
                    </select>
                    <span className="hint">
                      Only <strong>verified</strong> facts may appear in a client-facing report.
                    </span>
                  </div>

                  <label className="checkbox">
                    <input
                      type="checkbox"
                      checked={siteAuth}
                      onChange={(event) => setSiteAuth(event.target.checked)}
                      disabled={saving}
                    />
                    <span>
                      <strong>Client authorized website changes</strong>
                      Required before any optimization touches a client property. Revocable at any
                      time.
                    </span>
                  </label>

                  <label className="checkbox">
                    <input
                      type="checkbox"
                      checked={retention}
                      onChange={(event) => setRetention(event.target.checked)}
                      disabled={saving}
                    />
                    <span>
                      <strong>Evidence retention permitted</strong>
                      Required before raw response evidence is stored for this brand.
                    </span>
                  </label>

                  <div className="field">
                    <label htmlFor="edit-category">Category</label>
                    <input
                      id="edit-category"
                      type="text"
                      maxLength={200}
                      value={category}
                      onChange={(event) => setCategory(event.target.value)}
                      disabled={saving}
                    />
                  </div>

                  <div className="field">
                    <label htmlFor="edit-description">Description</label>
                    <textarea
                      id="edit-description"
                      maxLength={4000}
                      value={description}
                      onChange={(event) => setDescription(event.target.value)}
                      disabled={saving}
                    />
                  </div>

                  <div className="actions">
                    <button type="submit" data-variant="primary" disabled={saving}>
                      {saving ? <span className="spinner" /> : null} Save changes
                    </button>
                    <button
                      type="button"
                      data-variant="ghost"
                      disabled={saving}
                      onClick={() => key && void load(key, new AbortController().signal)}
                    >
                      reset
                    </button>
                  </div>
                </form>
              </div>

              {key ? (
                <CompetitorTable workspaceKey={key} brandId={brand.id} initial={brand.competitors} />
              ) : null}

              {key ? (
                <AuditTrail
                  key={`${brand.id}-${auditNonce}`}
                  workspaceKey={key}
                  entityType="brand"
                  entityId={brand.id}
                  limit={25}
                />
              ) : null}
            </div>
          </>
        ) : !loading ? (
          <div className="empty">
            <h3>Brand not found</h3>
            <p>It may belong to another workspace, or it has been soft-deleted.</p>
            <Link href="/">
              <button type="button" data-variant="primary">
                Back to overview
              </button>
            </Link>
          </div>
        ) : null}
      </main>
    </>
  );
}
