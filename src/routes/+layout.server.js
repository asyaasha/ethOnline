// since there's no dynamic data here, we can prerender
// it so that it gets served as a static asset in production
//export const prerender = true;
const base = 'http://0.0.0.0:5555';

export async function load({ fetch }) {
	const response = await fetch(`${base}/ledgers`);
	const data = await response.json();

	return data?.ledgers
		? { data: Object.keys(data?.ledgers).map((item) => data?.ledgers[item]) }
		: { data: [] };
}
