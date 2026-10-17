"use client";

import { PageHeader } from "@/components/PageHeader";
import { ProviderTable } from "@/components/ProviderTable";
import { TopBar } from "@/components/TopBar";

export default function ProvidersPage() {
  return (
    <>
      <TopBar />
      <main>
        <PageHeader
          title="Providers & compliance"
          description="What this build can talk to, and what it refuses to. The inventory is read-only: no endpoint here can trigger a provider call."
        />
        <ProviderTable />
        <div className="notice" data-tone="info" style={{ marginTop: "1rem" }}>
          <strong>Why two providers are denied in configuration</strong>
          <ul>
            <li>
              <code>gemini-grounding-google-search</code> — the Gemini API Additional Terms permit
              Grounding with Google Search only inside an application you own and operate, and
              prohibit analysing, collecting, monitoring or storing Grounded Results and Links for
              a purpose like visibility benchmarking. Grounded collection will not be initiated.
            </li>
            <li>
              <code>perplexity-agent-api</code> — the API Terms of Service are materially better
              (customer owns Output; no training on customer content), but three items are still
              unverified: the full licence grant, the Acceptable Use Policy, and whether{" "}
              <code>web_search</code> output counts as a Search Service (which would deny Output
              ownership). Blocked pending written clarification (gate W2).
            </li>
          </ul>
          Adapter interfaces exist so a permitted integration can be added later without redesign —
          but adding one requires a code change plus separate authorization (gate M5).
        </div>
      </main>
    </>
  );
}
