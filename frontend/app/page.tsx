"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";
import { useCallback, useEffect, useState } from "react";

import { BrandTile } from "@/components/BrandTile";
import { ErrorNotice } from "@/components/ErrorNotice";
import { PageHeader } from "@/components/PageHeader";
import { AuditTrail } from "@/components/AuditTrail";
import { TopBar } from "@/components/TopBar";
import { ApiError, api } from "@/lib/api";
import type { Brand, HealthResponse, Workspace, WorkspaceStats } from "@/lib/types";
import { clearWorkspace, readWorkspaceKey, readWorkspaceMeta } from "@/lib/workspace";

export default function OverviewPage() {
  const router = useRouter();
  const [key, setKey] = useState<string | null>(null);
  const [ready, setReady] = useState(false);
  const [workspace, setWorkspace] = useState<Workspace | null>(null);
  const [stats, setStats] = useState<WorkspaceStats | null>(null);
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [brands, setBrands] = useState<Brand[]>([]);
  const [search, setSearch] = useState("");
  const [error, setError] = useState<unknown>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const stored = readWorkspaceKey();
    setKey(stored);
    setReady(true);
    if (!stored) {
      setLoading(false);
      router.replace("/setup");
    }
  }, [router]);

  const load = useCallback(
    async (workspaceKey: string, term: string, signal: AbortSignal) => {
      setLoading(true);
      try {
        const [healthResult, workspaceResult, statsResult, page] = await Promise.all([
          api.health({ signal }),
          api.currentWorkspace(workspaceKey, { signal }),
          api.workspaceStats(workspaceKey, { signal }),
          api.listBrands(workspaceKey, { limit: 50, search: term || undefined, signal }),
        ]);
        setHealth(healthResult);
        setWorkspace(workspaceResult);
        setStats(statsResult);
        setBrands(page.items);
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
    [router],
  );

  useEffect(() => {
    if (!ready || !key) return;
    const controller = new AbortController();
    const timer = setTimeout(() => void load(key, search, controller.signal), search ? 250 : 0);
    return () => {
      clearTimeout(timer);
      controller.abort();
    };
  }, [ready, key, search, load]);

  if (!ready) return null;

  const meta = readWorkspaceMeta();

  return (
    <>
      <TopBar />
      <main>
        <PageHeader
          title={workspace ? workspace.name : "Overview"}
          description="Milestone 1 scope: workspace tenancy and brand onboarding. No measurement has been collected yet, and no external provider calls are made anywhere in this build."
          actions={
            <Link href="/onboard">
              <button type="button" data-variant="primary">
                Onboard a brand
              </button>
            </Link>
          }
        />

        {error ? <ErrorNotice error={error} /> : null}

        <div className="grid grid-3" style={{ marginBottom: "1rem" }}>
          <div className="card stat">
            <span className="stat-value">{stats ? stats.brands : "—"}</span>
            <span className="stat-label">Brands onboarded</span>
          </div>
          <div className="card stat">
            <span className="stat-value">{health ? health.version : "—"}</span>
            <span className="stat-label">API version · {health?.environment ?? "…"}</span>
          </div>
          <div className="card stat">
            <span className="stat-value">
              {health ? (health.provider_calls_enabled ? "ON" : "OFF") : "—"}
            </span>
            <span className="stat-label">External provider calls</span>
          </div>
        </div>

        <section className="card" style={{ marginBottom: "1rem" }}>
          <div className="card-head">
            <h2>Brands</h2>
            <p>
              {loading ? <span className="spinner" aria-label="loading" /> : null}{" "}
              <input
                type="search"
                value={search}
                onChange={(event) => setSearch(event.target.value)}
                placeholder="Search by name"
                aria-label="Search brands"
                style={{ maxWidth: "220px" }}
              />
            </p>
          </div>

          {brands.length === 0 && !loading ? (
            <div className="empty">
              <h3>No brands yet</h3>
              <p>
                Onboard the first brand to establish its identity, domain, category, region and
                competitor set. Fact-verification status starts at <strong>unverified</strong> and
                both authorization flags start <strong>off</strong>.
              </p>
              <Link href="/onboard">
                <button type="button" data-variant="primary">
                  Onboard a brand
                </button>
              </Link>
            </div>
          ) : (
            <div className="brand-list">
              {brands.map((brand) => (
                <BrandTile key={brand.id} brand={brand} />
              ))}
            </div>
          )}
        </section>

        {key ? <AuditTrail workspaceKey={key} limit={15} /> : null}

        <p className="hint" style={{ color: "var(--text-faint)", marginTop: "1rem" }}>
          Workspace {meta?.slug ?? workspace?.slug ?? "unknown"} · key stored on this device only
        </p>
      </main>
    </>
  );
}
