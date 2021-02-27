import { getAssetFromKV, serveSinglePageApp } from '@cloudflare/kv-asset-handler'

addEventListener('fetch', (event) => {
  try {
    event.respondWith(handleEvent(event));
  } catch (e) {
    event.respondWith(new Response('Internal Error', { status: 500 }));
  }
});

async function handleEvent(event) {
  try {
    return await getAssetFromKV(event, { mapRequestToAsset: serveSinglePageApp });
  } catch (e) {
    // if an error is thrown try to serve the asset at 404.html
    try {
      let notFoundResponse = await getAssetFromKV(event, {
        mapRequestToAsset: (req) =>
          new Request(`${new URL(req.url).origin}`, req),
      });
      return new Response(notFoundResponse.body,   { status: 404 });
    } catch (e) {}
    return new Response(e.message || e.toString(), { status: 500 });
  }
}
