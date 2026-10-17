"use client";

import { useRouter } from "next/navigation";
import { FormEvent, useEffect, useState } from "react";

import { ErrorNotice } from "@/components/ErrorNotice";
import { PageHeader } from "@/components/PageHeader";
import { RelationshipPill } from "@/components/Pill";
import { TopBar } from "@/components/TopBar";
import { ApiError, api } from "@/lib/api";
import type { CompetitorCreateInput, CompetitorRelationship } from "@/lib/types";
import { clearWorkspace, readWorkspaceKey } from "@/lib/workspace";

const RELATIONSHIPS: CompetitorRelationship[] = ["direct", "indirect", "alternative", "incumbent"];

const REGIONS = ["US", "GB", "DE", "IN", "AU", "CA", "SG"];
const LANGUAGES = ["en", "de", "fr", "es", "hi"];

interface CompetitorDraft {
  name: string;
  website: string;
  relationship_type: CompetitorRelationship;
}

export default function OnboardBrandPage() {
  const router = useRouter();
  const [key, setKey] = useState<string | null>(null);
  const [ready, setReady] = useState(false);

  const [name, setName] = useState("");
  const [website, setWebsite] = useState("");
  const [category, setCategory] = useState("");
  const [description, setDescription] = useState("");
  const [language, setLanguage] = useState("en");
  const [region, setRegion] = useState("US");
  const [competitors, setCompetitors] = useState<CompetitorDraft[]>([]);
  const [draft, setDraft] = useState<CompetitorDraft>({
    name: "",
    website: "",
    relationship_type: "direct",
  });

  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<unknown>(null);

  useEffect(() => {
    const stored = readWorkspaceKey();
    setKey(stored);
    setReady(true);
    if (!stored) router.replace("/setup");
  }, [router]);

  function addCompetitor() {
    const trimmed = draft.name.trim();
    if (trimmed.length < 2) return;
    if (competitors.some((item) => item.name.toLowerCase() === trimmed.toLowerCase())) {
      setError(new Error(`"${trimmed}" is already in the list.`));
      return;
    }
    setCompetitors([...competitors, { ...draft, name: trimmed, website: draft.website.trim() }]);
    setDraft({ name: "", website: "", relationship_type: "direct" });
    setError(null);
  }

  function removeCompetitor(index: number) {
    setCompetitors(competitors.filter((_, position) => position !== index));
  }

  async function submit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!key) return;
    setBusy(true);
    setError(null);
    const payload: CompetitorCreateInput[] = competitors.map((item) => ({
      name: item.name,
      website: item.website || null,
      relationship_type: item.relationship_type,
    }));
    try {
      const brand = await api.createBrand(key, {
        name: name.trim(),
        website: website.trim() || null,
        category: category.trim() || null,
        description: description.trim() || null,
        primary_language: language,
        primary_region: region,
        competitors: payload,
      });
      router.push(`/brands/${brand.id}`);
      router.refresh();
    } catch (cause) {
      if (cause instanceof ApiError && cause.status === 401) {
        clearWorkspace();
        router.replace("/setup");
        return;
      }
      setError(cause);
    } finally {
      setBusy(false);
    }
  }

  if (!ready) return null;

  return (
    <>
      <TopBar />
      <main>
        <PageHeader
          title="Onboard a brand"
          description="Brand identity is the foundation of every later measurement: the domain and competitor set determine what can be compared, and the flags below determine what we are allowed to do."
        />

        {!key ? (
          <div className="notice" data-tone="warn">
            <strong>No workspace connected</strong>
            <a href="/setup">Connect a workspace</a> to continue.
          </div>
        ) : (
          <form onSubmit={submit} className="stack">
            <section className="card">
              <h2>Identity</h2>
              <div className="row">
                <div className="field">
                  <label htmlFor="brand-name">Brand name *</label>
                  <input
                    id="brand-name"
                    type="text"
                    required
                    minLength={2}
                    maxLength={200}
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                    placeholder="Acme Analytics"
                    disabled={busy}
                  />
                  <span className="hint">Unique within this workspace (case-insensitive).</span>
                </div>
                <div className="field">
                  <label htmlFor="brand-website">Website</label>
                  <input
                    id="brand-website"
                    type="text"
                    maxLength={300}
                    value={website}
                    onChange={(event) => setWebsite(event.target.value)}
                    placeholder="https://www.acme-analytics.com"
                    disabled={busy}
                  />
                  <span className="hint">
                    Normalised to a registrable domain; used for entity resolution in M2.
                  </span>
                </div>
              </div>
              <div className="row">
                <div className="field">
                  <label htmlFor="brand-category">Category</label>
                  <input
                    id="brand-category"
                    type="text"
                    maxLength={200}
                    value={category}
                    onChange={(event) => setCategory(event.target.value)}
                    placeholder="Marketing analytics"
                    disabled={busy}
                  />
                </div>
                <div className="field">
                  <label htmlFor="brand-language">Primary language</label>
                  <select
                    id="brand-language"
                    value={language}
                    onChange={(event) => setLanguage(event.target.value)}
                    disabled={busy}
                  >
                    {LANGUAGES.map((option) => (
                      <option key={option} value={option}>
                        {option}
                      </option>
                    ))}
                  </select>
                </div>
                <div className="field">
                  <label htmlFor="brand-region">Primary region</label>
                  <select
                    id="brand-region"
                    value={region}
                    onChange={(event) => setRegion(event.target.value)}
                    disabled={busy}
                  >
                    {REGIONS.map((option) => (
                      <option key={option} value={option}>
                        {option}
                      </option>
                    ))}
                  </select>
                </div>
              </div>
              <div className="field">
                <label htmlFor="brand-description">What the brand does</label>
                <textarea
                  id="brand-description"
                  maxLength={4000}
                  value={description}
                  onChange={(event) => setDescription(event.target.value)}
                  placeholder="Attribution and marketing-mix modelling for mid-market SaaS teams."
                  disabled={busy}
                />
                <span className="hint">
                  Recorded as a client-supplied statement. It is not treated as a verified fact
                  until fact verification is completed.
                </span>
              </div>
            </section>

            <section className="card">
              <h2>Competitor set</h2>
              <p style={{ color: "var(--text-muted)", fontSize: "0.9rem" }}>
                Optional at onboarding, required before measurement. Comparisons are reported per
                surface and never blended into a single score.
              </p>

              {competitors.length > 0 ? (
                <div className="table-wrap" style={{ marginBottom: "0.9rem" }}>
                  <table>
                    <thead>
                      <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Website</th>
                        <th scope="col">Relationship</th>
                        <th scope="col">
                          <span className="visually-hidden">Remove</span>
                        </th>
                      </tr>
                    </thead>
                    <tbody>
                      {competitors.map((item, index) => (
                        <tr key={`${item.name}-${index}`}>
                          <td>{item.name}</td>
                          <td className="mono">{item.website || "—"}</td>
                          <td>
                            <RelationshipPill type={item.relationship_type} />
                          </td>
                          <td style={{ textAlign: "right" }}>
                            <button
                              type="button"
                              data-size="sm"
                              data-variant="danger"
                              onClick={() => removeCompetitor(index)}
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
              ) : null}

              <div className="competitor-row-form">
                <div className="field" style={{ marginBottom: 0 }}>
                  <label htmlFor="draft-name">Competitor name</label>
                  <input
                    id="draft-name"
                    type="text"
                    maxLength={200}
                    value={draft.name}
                    onChange={(event) => setDraft({ ...draft, name: event.target.value })}
                    placeholder="Northbeam"
                    disabled={busy}
                  />
                </div>
                <div className="field" style={{ marginBottom: 0 }}>
                  <label htmlFor="draft-website">Website</label>
                  <input
                    id="draft-website"
                    type="text"
                    maxLength={300}
                    value={draft.website}
                    onChange={(event) => setDraft({ ...draft, website: event.target.value })}
                    placeholder="northbeam.io"
                    disabled={busy}
                  />
                </div>
                <div className="field" style={{ marginBottom: 0 }}>
                  <label htmlFor="draft-rel">Relationship</label>
                  <select
                    id="draft-rel"
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
                  <button
                    type="button"
                    onClick={addCompetitor}
                    disabled={busy || draft.name.trim().length < 2}
                  >
                    Add to set
                  </button>
                </div>
              </div>
            </section>

            <section className="card">
              <h2>Authorization &amp; verification</h2>
              <p style={{ color: "var(--text-muted)", fontSize: "0.9rem" }}>
                These start closed on purpose and can only be changed later from the brand page,
                where every change is written to the audit trail.
              </p>
              <label className="checkbox">
                <input type="checkbox" checked={false} disabled readOnly />
                <span>
                  <strong>Website changes authorized</strong>
                  Off. Explicit, logged, revocable client authorization is required before anything
                  touches a client website.
                </span>
              </label>
              <label className="checkbox">
                <input type="checkbox" checked={false} disabled readOnly />
                <span>
                  <strong>Evidence retention permitted</strong>
                  Off. Raw response evidence is retained only where collection and retention are
                  permitted for that source.
                </span>
              </label>
              <label className="checkbox">
                <input type="checkbox" checked={false} disabled readOnly />
                <span>
                  <strong>Fact verification</strong>
                  Unverified. No client-facing report may present unverified statements as facts.
                </span>
              </label>
            </section>

            {error ? <ErrorNotice error={error} title="Could not onboard this brand" /> : null}

            <div className="actions">
              <button type="submit" data-variant="primary" disabled={busy || name.trim().length < 2}>
                {busy ? <span className="spinner" /> : null} Create brand
              </button>
              <button type="button" data-variant="ghost" onClick={() => router.back()} disabled={busy}>
                cancel
              </button>
            </div>
          </form>
        )}
      </main>
    </>
  );
}
