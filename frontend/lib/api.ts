/**
 * Typed API client.
 *
 * Two rules drive this file:
 *  1. Every request goes to a RELATIVE path (/api/backend/...). The Next server proxies it to
 *     FastAPI, so the app works behind any host or preview origin and never hardcodes localhost
 *     in the browser.
 *  2. Errors are surfaced as ApiError with the backend's code, message and correlation_id, so a
 *     user-facing failure can be traced to a single server log line.
 */

import type {
  ApiErrorBody,
  AuditEvent,
  Brand,
  BrandCreateInput,
  BrandDetail,
  BrandUpdateInput,
  Competitor,
  CompetitorCreateInput,
  HealthResponse,
  Page,
  ProviderInventory,
  Workspace,
  WorkspaceCreated,
  WorkspaceStats,
} from "@/lib/types";

const BASE = "/api/backend";

export class ApiError extends Error {
  readonly code: string;
  readonly status: number;
  readonly details: Record<string, unknown>;
  readonly correlationId: string | null;

  constructor(
    status: number,
    code: string,
    message: string,
    details: Record<string, unknown>,
    correlationId: string | null,
  ) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.code = code;
    this.details = details;
    this.correlationId = correlationId;
  }

  /** Field-level messages from a 422, flattened for display next to inputs. */
  fieldMessages(): string[] {
    const errors = this.details["errors"];
    if (!Array.isArray(errors)) return [];
    return errors.map((entry: unknown) => {
      if (typeof entry !== "object" || entry === null) return String(entry);
      const record = entry as { loc?: string[]; msg?: string };
      const field = (record.loc ?? []).filter((part) => part !== "body").join(".") || "request";
      return `${field}: ${record.msg ?? "invalid"}`;
    });
  }
}

export interface RequestOptions {
  workspaceKey?: string | null;
  correlationId?: string;
  signal?: AbortSignal;
}

function newCorrelationId(): string {
  const random = globalThis.crypto?.randomUUID?.();
  return random ?? `web-${Date.now()}-${Math.random().toString(16).slice(2, 10)}`;
}

async function request<T>(
  method: "GET" | "POST" | "PATCH" | "DELETE",
  path: string,
  body?: unknown,
  options: RequestOptions = {},
): Promise<T> {
  const correlationId = options.correlationId ?? newCorrelationId();
  const headers: Record<string, string> = {
    Accept: "application/json",
    "X-Correlation-ID": correlationId,
  };
  if (body !== undefined) headers["Content-Type"] = "application/json";
  if (options.workspaceKey) headers["X-Workspace-Key"] = options.workspaceKey;

  let response: Response;
  try {
    response = await fetch(`${BASE}${path}`, {
      method,
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
      signal: options.signal,
      cache: "no-store",
    });
  } catch (cause) {
    throw new ApiError(
      0,
      "NETWORK_ERROR",
      "Could not reach the SignalGEO API. Is the backend running?",
      { cause: String(cause) },
      correlationId,
    );
  }

  if (response.status === 204) return undefined as T;

  const text = await response.text();
  const parsed: unknown = text ? JSON.parse(text) : null;

  if (!response.ok) {
    const envelope = parsed as ApiErrorBody | null;
    throw new ApiError(
      response.status,
      envelope?.error?.code ?? `HTTP_${response.status}`,
      envelope?.error?.message ?? response.statusText,
      envelope?.error?.details ?? {},
      envelope?.error?.correlation_id ?? response.headers.get("X-Correlation-ID"),
    );
  }
  return parsed as T;
}

export const api = {
  health: (options?: RequestOptions) => request<HealthResponse>("GET", "/health", undefined, options),

  providers: (options?: RequestOptions) =>
    request<ProviderInventory>("GET", "/providers", undefined, options),

  createWorkspace: (input: { name: string; slug?: string; notes?: string }) =>
    request<WorkspaceCreated>("POST", "/dev/workspaces", input),

  currentWorkspace: (workspaceKey: string, options?: RequestOptions) =>
    request<Workspace>("GET", "/workspaces/me", undefined, { ...options, workspaceKey }),

  workspaceStats: (workspaceKey: string, options?: RequestOptions) =>
    request<WorkspaceStats>("GET", "/workspaces/me/stats", undefined, { ...options, workspaceKey }),

  listBrands: (
    workspaceKey: string,
    options?: RequestOptions & { limit?: number; offset?: number; search?: string },
  ) => {
    const params = new URLSearchParams();
    if (options?.limit) params.set("limit", String(options.limit));
    if (options?.offset) params.set("offset", String(options.offset));
    if (options?.search) params.set("search", options.search);
    const query = params.toString();
    return request<Page<Brand>>(
      "GET",
      `/brands${query ? `?${query}` : ""}`,
      undefined,
      { ...options, workspaceKey },
    );
  },

  getBrand: (workspaceKey: string, brandId: string, options?: RequestOptions) =>
    request<BrandDetail>("GET", `/brands/${brandId}`, undefined, { ...options, workspaceKey }),

  createBrand: (workspaceKey: string, input: BrandCreateInput, options?: RequestOptions) =>
    request<Brand>("POST", "/brands", input, { ...options, workspaceKey }),

  updateBrand: (
    workspaceKey: string,
    brandId: string,
    input: BrandUpdateInput,
    options?: RequestOptions,
  ) => request<Brand>("PATCH", `/brands/${brandId}`, input, { ...options, workspaceKey }),

  deleteBrand: (workspaceKey: string, brandId: string, options?: RequestOptions) =>
    request<void>("DELETE", `/brands/${brandId}`, undefined, { ...options, workspaceKey }),

  listCompetitors: (workspaceKey: string, brandId: string, options?: RequestOptions) =>
    request<Competitor[]>("GET", `/brands/${brandId}/competitors`, undefined, {
      ...options,
      workspaceKey,
    }),

  addCompetitor: (
    workspaceKey: string,
    brandId: string,
    input: CompetitorCreateInput,
    options?: RequestOptions,
  ) =>
    request<Competitor>("POST", `/brands/${brandId}/competitors`, input, {
      ...options,
      workspaceKey,
    }),

  updateCompetitor: (
    workspaceKey: string,
    brandId: string,
    competitorId: string,
    input: Partial<CompetitorCreateInput>,
    options?: RequestOptions,
  ) =>
    request<Competitor>("PATCH", `/brands/${brandId}/competitors/${competitorId}`, input, {
      ...options,
      workspaceKey,
    }),

  removeCompetitor: (
    workspaceKey: string,
    brandId: string,
    competitorId: string,
    options?: RequestOptions,
  ) =>
    request<void>("DELETE", `/brands/${brandId}/competitors/${competitorId}`, undefined, {
      ...options,
      workspaceKey,
    }),

  listAuditEvents: (
    workspaceKey: string,
    options?: RequestOptions & { entityType?: string; entityId?: string; limit?: number },
  ) => {
    const params = new URLSearchParams();
    if (options?.entityType) params.set("entity_type", options.entityType);
    if (options?.entityId) params.set("entity_id", options.entityId);
    if (options?.limit) params.set("limit", String(options.limit));
    const query = params.toString();
    return request<Page<AuditEvent>>(
      "GET",
      `/audit-events${query ? `?${query}` : ""}`,
      undefined,
      { ...options, workspaceKey },
    );
  },
};
