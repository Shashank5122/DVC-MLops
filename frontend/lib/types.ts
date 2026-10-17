/**
 * Types mirroring the backend Pydantic schemas (backend/app/schemas/*).
 * Kept hand-written and explicit: the API surface is small in M1 and a codegen dependency is
 * not justified yet. Every enum is a union of literal strings, matching the backend StrEnums.
 */

export type WorkspaceStatus = "active" | "suspended";

export type FactVerificationStatus = "unverified" | "in_progress" | "verified";

export type CompetitorRelationship = "direct" | "indirect" | "alternative" | "incumbent";

export interface Workspace {
  id: string;
  name: string;
  slug: string;
  status: WorkspaceStatus;
  key_last4: string;
  notes: string | null;
  created_at: string;
}

export interface WorkspaceCreated {
  workspace: Workspace;
  /** Shown exactly once. Never returned again by the API. */
  workspace_key: string;
}

export interface WorkspaceStats {
  workspace: string;
  brands: number;
}

export interface Brand {
  id: string;
  name: string;
  slug: string;
  website: string | null;
  normalised_domain: string | null;
  category: string | null;
  description: string | null;
  primary_language: string;
  primary_region: string;
  fact_verification_status: FactVerificationStatus;
  website_change_authorized: boolean;
  data_retention_permitted: boolean;
  created_at: string;
  updated_at: string;
}

export interface Competitor {
  id: string;
  brand_id: string;
  name: string;
  slug: string;
  website: string | null;
  normalised_domain: string | null;
  relationship_type: CompetitorRelationship;
  notes: string | null;
  created_at: string;
  updated_at: string;
}

export interface BrandDetail extends Brand {
  competitors: Competitor[];
  competitor_count: number;
}

export interface BrandCreateInput {
  name: string;
  website?: string | null;
  category?: string | null;
  description?: string | null;
  primary_language?: string;
  primary_region?: string;
  competitors?: CompetitorCreateInput[];
}

export interface CompetitorCreateInput {
  name: string;
  website?: string | null;
  relationship_type?: CompetitorRelationship;
  notes?: string | null;
}

export interface BrandUpdateInput {
  name?: string;
  website?: string | null;
  category?: string | null;
  description?: string | null;
  primary_language?: string;
  primary_region?: string;
  fact_verification_status?: FactVerificationStatus;
  website_change_authorized?: boolean;
  data_retention_permitted?: boolean;
}

export interface AuditEvent {
  id: string;
  action: string;
  entity_type: string;
  entity_id: string | null;
  actor: string;
  changes: Record<string, unknown>;
  correlation_id: string | null;
  created_at: string;
}

export interface Page<T> {
  items: T[];
  total: number;
  limit: number;
  offset: number;
}

export interface HealthResponse {
  status: string;
  version: string;
  environment: string;
  database: string;
  provider_calls_enabled: boolean;
}

export interface ProviderAdapter {
  provider_id: string;
  display_name: string;
  surface: string;
  collection_method: string;
  model_identifier: string;
  capability: {
    returns_citations: boolean;
    returns_raw_text: boolean;
    supports_region: boolean;
    supports_language: boolean;
    supports_repeat_runs: boolean;
    notes: string;
  };
  compliance_status: string;
  compliance_notes: string;
  permitted_now: boolean;
  permission_reason: string;
}

export interface ProviderInventory {
  provider_calls_enabled: boolean;
  adapters: ProviderAdapter[];
  denied_pending_authorization: string[];
  note: string;
}

export interface ApiErrorBody {
  error: {
    code: string;
    message: string;
    details: Record<string, unknown>;
    correlation_id: string | null;
  };
}
