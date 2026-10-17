# Frontend image: multi-stage, Next standalone output, non-root runtime.
FROM node:22-alpine AS deps
WORKDIR /srv/signalgeo-frontend
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund

FROM node:22-alpine AS build
WORKDIR /srv/signalgeo-frontend
COPY --from=deps /srv/signalgeo-frontend/node_modules ./node_modules
COPY . .
# The API origin is a SERVER-side value: the Next server proxies /api/backend/* to it.
# The browser never sees it and only ever uses relative paths.
ARG BACKEND_ORIGIN=http://backend:8000
ENV BACKEND_ORIGIN=$BACKEND_ORIGIN \
    NEXT_TELEMETRY_DISABLED=1
RUN npm run build

FROM node:22-alpine AS runtime
WORKDIR /srv/signalgeo-frontend
ENV NODE_ENV=production \
    NEXT_TELEMETRY_DISABLED=1 \
    PORT=3000 \
    HOSTNAME=0.0.0.0
RUN addgroup -g 1001 nodejs && adduser -u 1001 -G nodejs -D nextjs
COPY --from=build --chown=nextjs:nodejs /srv/signalgeo-frontend/.next/standalone ./
COPY --from=build --chown=nextjs:nodejs /srv/signalgeo-frontend/.next/static ./.next/static
COPY --from=build --chown=nextjs:nodejs /srv/signalgeo-frontend/public ./public
USER nextjs
EXPOSE 3000
CMD ["node", "server.js"]
