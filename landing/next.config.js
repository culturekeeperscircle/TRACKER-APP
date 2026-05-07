/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Cap response payloads on the chat route. Streaming responses already
  // open-ended, but this hedges against retrieval ballooning.
  experimental: {
    serverActions: { bodySizeLimit: '2mb' },
  },
};

module.exports = nextConfig;
