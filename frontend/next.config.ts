import type { NextConfig } from "next";

/**
 * The browser only ever calls relative `/api/backend/*` paths; the Next server proxies them to
 * the FastAPI backend. This keeps the app working behind a reverse proxy or preview host and
 * means no backend origin is ever baked into client bundles.
 *
 * BACKEND_ORIGIN is read at build/start time on the SERVER only.
 */
const backendOrigin = process.env.BACKEND_ORIGIN ?? "http://127.0.0.1:8000";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  // The app is served behind a sandbox/preview hostname as well as localhost. Listing the
  // origins keeps Next's dev server from rejecting cross-origin asset and HMR requests.
  allowedDevOrigins: ["*.e2b.app", "localhost", "127.0.0.1"],
  poweredByHeader: false,
  output: "standalone",
  async rewrites() {
    return [
      {
        source: "/api/backend/:path*",
        destination: `${backendOrigin}/api/v1/:path*`,
      },
    ];
  },
  async headers() {
    return [
      {
        source: "/:path*",
        headers: [
          { key: "X-Content-Type-Options", value: "nosniff" },
          { key: "X-Frame-Options", value: "DENY" },
          { key: "Referrer-Policy", value: "strict-origin-when-cross-origin" },
        ],
      },
    ];
  },
};

export default nextConfig;
