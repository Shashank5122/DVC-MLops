/**
 * Pilot tenancy in the browser: the workspace key lives in localStorage for this device only.
 *
 * This is deliberately NOT a session, cookie or user account. It matches the backend's
 * pilot-grade boundary and is documented as a limitation in the M1 report. Anyone holding the
 * key can read the workspace, so keys are generated per pilot workspace and revocable by
 * deleting the workspace row.
 */

const KEY_STORAGE = "signalgeo.workspace_key";
const META_STORAGE = "signalgeo.workspace_meta";

export interface StoredWorkspaceMeta {
  name: string;
  slug: string;
  keyLast4: string;
  storedAt: string;
}

export function isBrowser(): boolean {
  return typeof window !== "undefined";
}

export function readWorkspaceKey(): string | null {
  if (!isBrowser()) return null;
  return window.localStorage.getItem(KEY_STORAGE);
}

export function readWorkspaceMeta(): StoredWorkspaceMeta | null {
  if (!isBrowser()) return null;
  const raw = window.localStorage.getItem(META_STORAGE);
  if (!raw) return null;
  try {
    return JSON.parse(raw) as StoredWorkspaceMeta;
  } catch {
    return null;
  }
}

export function writeWorkspace(key: string, meta: Omit<StoredWorkspaceMeta, "storedAt">): void {
  if (!isBrowser()) return;
  window.localStorage.setItem(KEY_STORAGE, key);
  window.localStorage.setItem(
    META_STORAGE,
    JSON.stringify({ ...meta, storedAt: new Date().toISOString() }),
  );
}

export function writeWorkspaceKeyOnly(key: string): void {
  if (!isBrowser()) return;
  window.localStorage.setItem(KEY_STORAGE, key);
  window.localStorage.removeItem(META_STORAGE);
}

export function clearWorkspace(): void {
  if (!isBrowser()) return;
  window.localStorage.removeItem(KEY_STORAGE);
  window.localStorage.removeItem(META_STORAGE);
}
