/**
 * Cloudflare Worker — Instagram post proxy for zoukcal-socal.surge.sh
 *
 * Fetches the latest posts from a public Instagram account using the
 * Instagram mobile API (requires Android user-agent, which browsers
 * cannot set directly). Returns CORS-enabled JSON to the website.
 *
 * Deploy: wrangler deploy
 * Endpoint: GET /?username=<handle>
 */

const IG_UA =
  'Instagram 219.0.0.12.117 Android (26/8.0.0; 480dpi; 1080x1920; ' +
  'OnePlus; 6T; devitron; qcom; en_US; 314665256)';

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, OPTIONS',
  'Content-Type': 'application/json',
};

export default {
  async fetch(request) {
    // Handle CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: CORS_HEADERS });
    }

    const url      = new URL(request.url);
    const username = url.searchParams.get('username');
    if (!username) {
      return new Response(JSON.stringify({ error: 'missing username' }), {
        status: 400, headers: CORS_HEADERS,
      });
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
    } catch (err) {
      return new Response(JSON.stringify({ error: 'upstream fetch failed' }), {
        status: 502, headers: CORS_HEADERS,
      });
    }

    if (!igRes.ok) {
      return new Response(
        JSON.stringify({ error: 'instagram returned ' + igRes.status }),
        { status: igRes.status, headers: CORS_HEADERS }
      );
    }

    const body = await igRes.json();
    return new Response(JSON.stringify(body), {
      status: 200,
      headers: {
        ...CORS_HEADERS,
        'Cache-Control': 'public, max-age=900', // cache 15 min at edge
      },
    });
  },
};
