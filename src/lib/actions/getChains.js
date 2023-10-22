export const base = 'http://46.101.6.36:8001';
import chainsData from '$lib/mock.json';
import { json } from '@sveltejs/kit';

export async function getChains() {
	// const response = await fetch(`${base}/claim`);
	// const { data } = await response.json();
	return json({ data: chainsData.data.map((item) => item.Ledger) });
}
