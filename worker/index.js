/**
 * Cloudflare Worker — Instagram proxy for zoukcal-socal.surge.sh
 *
 * Two endpoints:
 *   GET /?username=<handle>   — fetch latest posts (JSON)
 *   GET /?imageurl=<url>      — proxy CDN image, stripping CORP header
 *
 * Instagram's CDN sends `Cross-Origin-Resource-Policy: same-origin`,
 * which blocks <img> tags on external domains. This proxy re-serves
 * the image without that header so browsers can display it.
 *
 * Deploy: npx wrangler deploy  (from worker/ directory)
 */

const IG_UA =
  'Instagram 219.0.0.12.117 Android (26/8.0.0; 480dpi; 1080x1920; ' +
  'OnePlus; 6T; devitron; qcom; en_US; 314665256)';

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
};

export default {
  async fetch(request) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    const url      = new URL(request.url);
    const username = url.searchParams.get('username');
    const imageUrl = url.searchParams.get('imageurl');

    // ── Image proxy ──────────────────────────────────────────────────
    if (imageUrl) {
      let imgRes;
      try {
        imgRes = await fetch(imageUrl, { headers: { 'User-Agent': IG_UA } });
      } catch {
        return new Response('upstream fetch failed', { status: 502 });
      }

      // Forward the image but override the blocking CORP header
      const headers = new Headers(imgRes.headers);
      headers.set('Cross-Origin-Resource-Policy', 'cross-origin');
      headers.set('Access-Control-Allow-Origin', '*');
      headers.set('Cache-Control', 'public, max-age=86400'); // cache 24h

      return new Response(imgRes.body, { status: imgRes.status, headers });
    }

    // ── Post data ─────────────────────────────────────────────────────
    if (!username) {
      return new Response(
        JSON.stringify({ error: 'missing username or imageurl param' }),
        { status: 400, headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
      );
    }

    const igUrl =
      'https://i.instagram.com/api/v1/users/web_profile_info/?username=' +
      encodeURIComponent(username);

    let igRes;
    try {
      igRes = await fetch(igUrl, {
        headers: {
          'User-Agent':      IG_UA,
          'Accept':          '*/*',
          'Accept-Language': 'en-US',
        },
      });
    } catch {
      return new Response(
        JSON.stringify({ error: 'upstream fetch failed' }),
        { status: 502, headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
      );
    }

    if (!igRes.ok) {
      return new Response(
        JSON.stringify({ error: 'instagram returned ' + igRes.status }),
        { status: igRes.status, headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' } }
      );
    }

    const body = await igRes.json();
    return new Response(JSON.stringify(body), {
      status: 200,
      headers: {
        ...CORS_HEADERS,
        'Content-Type':  'application/json',
        'Cache-Control': 'public, max-age=900', // cache 15 min at edge
      },
    });
  },
};
