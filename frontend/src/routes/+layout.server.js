// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = true;
const base = 'http://0.0.0.0:5555';

export async function load({ fetch }) {
	const response = await fetch(`${base}/ledgers`);
	const resWhitelisted = await fetch(`${base}/whitelisted`);
	const data = await response.json();
	const whitelisted = await resWhitelisted.json();

	return data?.ledgers
		? { ledgers: Object.keys(data?.ledgers).map((item) => data?.ledgers[item]), whitelisted }
		: { ledgers: [], whitelisted };
}
