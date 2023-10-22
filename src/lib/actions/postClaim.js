// todo: update url
const BASE_URL = 'http://46.101.6.36:8001';

/**
 * @param {string} ledger_id
 * @param {string} public_address
 */
export async function postClaim(ledger_id, public_address) {
	const response = await fetch(`${BASE_URL}/claim`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'Access-Control-Allow-Origin': '*'
		},
		body: JSON.stringify({
			ledger_id,
			public_address
		})
	});

	const json = await response.json();
	console.log('json ', json);
	return json;
}
