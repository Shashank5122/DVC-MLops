import { ApiError } from "@/lib/api";

/** Renders a backend error envelope, including the correlation id needed to trace it. */
export function ErrorNotice({ error, title }: { error: unknown; title?: string }) {
  if (!error) return null;

  if (error instanceof ApiError) {
    const fields = error.fieldMessages();
    return (
      <div className="notice" data-tone="danger" role="alert">
        <strong>{title ?? `Request failed (${error.code})`}</strong>
        {error.message}
        {fields.length > 0 ? (
          <ul>
            {fields.map((field) => (
              <li key={field}>{field}</li>
            ))}
          </ul>
        ) : null}
        {error.correlationId ? (
          <div className="mono" style={{ marginTop: "0.4rem", opacity: 0.85 }}>
            correlation_id: {error.correlationId}
          </div>
        ) : null}
      </div>
    );
  }

  return (
    <div className="notice" data-tone="danger" role="alert">
      <strong>{title ?? "Unexpected error"}</strong>
      {error instanceof Error ? error.message : String(error)}
    </div>
  );
}
