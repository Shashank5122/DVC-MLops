import Link from "next/link";

import { AuthorizationPills, VerificationPill } from "@/components/Pill";
import type { Brand } from "@/lib/types";

export function BrandTile({ brand }: { brand: Brand }) {
  return (
    <article className="brand-tile">
      <h3>
        <Link href={`/brands/${brand.id}`}>{brand.name}</Link>
      </h3>
      <div className="meta">
        {brand.normalised_domain ?? "no website recorded"} · {brand.primary_region.toUpperCase()} /{" "}
        {brand.primary_language}
      </div>
      {brand.category ? <div className="meta">{brand.category}</div> : null}
      <div className="pills">
        <VerificationPill status={brand.fact_verification_status} />
        <AuthorizationPills
          websiteChange={brand.website_change_authorized}
          dataRetention={brand.data_retention_permitted}
        />
      </div>
    </article>
  );
}
