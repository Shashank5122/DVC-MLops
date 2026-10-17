import type { CompetitorRelationship, FactVerificationStatus } from "@/lib/types";

type Tone = "ok" | "warn" | "danger" | "neutral" | "accent";

export function Pill({ label, tone }: { label: string; tone: Tone }) {
  return (
    <span className="pill" data-tone={tone}>
      {label}
    </span>
  );
}

const VERIFICATION: Record<FactVerificationStatus, { label: string; tone: Tone }> = {
  unverified: { label: "facts unverified", tone: "warn" },
  in_progress: { label: "verification in progress", tone: "accent" },
  verified: { label: "facts verified", tone: "ok" },
};

export function VerificationPill({ status }: { status: FactVerificationStatus }) {
  const config = VERIFICATION[status];
  return <Pill label={config.label} tone={config.tone} />;
}

const RELATIONSHIP: Record<CompetitorRelationship, Tone> = {
  direct: "accent",
  indirect: "neutral",
  alternative: "neutral",
  incumbent: "warn",
};

export function RelationshipPill({ type }: { type: CompetitorRelationship }) {
  return <Pill label={type} tone={RELATIONSHIP[type]} />;
}

export function AuthorizationPills({
  websiteChange,
  dataRetention,
}: {
  websiteChange: boolean;
  dataRetention: boolean;
}) {
  return (
    <>
      <Pill
        label={websiteChange ? "site changes authorized" : "site changes NOT authorized"}
        tone={websiteChange ? "ok" : "danger"}
      />
      <Pill
        label={dataRetention ? "evidence retention permitted" : "retention NOT permitted"}
        tone={dataRetention ? "ok" : "warn"}
      />
    </>
  );
}
