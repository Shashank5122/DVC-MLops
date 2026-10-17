"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";

import { clearWorkspace, readWorkspaceMeta } from "@/lib/workspace";

const LINKS = [
  { href: "/", label: "Overview" },
  { href: "/onboard", label: "Onboard brand" },
  { href: "/providers", label: "Providers" },
];

export function TopBar() {
  const pathname = usePathname();
  const router = useRouter();
  const [meta, setMeta] = useState(() => readWorkspaceMeta());

  useEffect(() => {
    setMeta(readWorkspaceMeta());
  }, [pathname]);

  function signOut() {
    clearWorkspace();
    setMeta(null);
    router.push("/setup");
    router.refresh();
  }

  return (
    <header className="topbar">
      <div className="topbar-inner">
        <Link href="/" className="brandmark">
          <span className="brandmark-dot" aria-hidden="true">
            SG
          </span>
          SignalGEO
        </Link>

        <nav className="nav" aria-label="Primary">
          {LINKS.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              data-active={pathname === link.href ? "true" : "false"}
            >
              {link.label}
            </Link>
          ))}
        </nav>

        {meta ? (
          <span className="workspace-chip" title={`Workspace ${meta.slug}`}>
            {meta.name}
            <span className="mono">····{meta.keyLast4}</span>
            <button type="button" onClick={signOut} title="Forget this workspace key on this device">
              switch
            </button>
          </span>
        ) : null}
      </div>
    </header>
  );
}
