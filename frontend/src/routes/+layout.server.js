import { env } from '$env/dynamic/public';

const BASE_URL = `http:${env.PUBLIC_AGENT_URL}` || 'http://0.0.0.0:5555';

export const prerender = true;

export async function load({ fetch }) {
	const response = await fetch(`${BASE_URL}/ledgers`);
	const resWhitelisted = await fetch(`${BASE_URL}/whitelisted`);
	const data = await response.json();
	const whitelisted = await resWhitelisted.json();

	return data?.ledgers
		? { ledgers: Object.keys(data?.ledgers).map((item) => data?.ledgers[item]), whitelisted }
		: { ledgers: [], whitelisted };
}
