import Link from "next/link";

import { TopBar } from "@/components/TopBar";

export default function NotFound() {
  return (
    <>
      <TopBar />
      <main>
        <div className="empty">
          <h3>Page not found</h3>
          <p>That route does not exist in the M1 console.</p>
          <Link href="/">
            <button type="button" data-variant="primary">
              Back to overview
            </button>
          </Link>
        </div>
      </main>
    </>
  );
}
