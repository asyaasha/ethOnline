import { fail } from '@sveltejs/kit';
const BASE_URL = 'http://0.0.0.0:5555';

export const actions = {
	postClaim: async ({ request }) => {
		const formData = await request.formData();
		const ledger_id = formData.get('ledger_id');
		const public_address = formData.get('address');

		const response = await fetch(`${BASE_URL}/claim`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				ledger_id,
				public_address
			})
		});

		if (!response.ok) {
			return fail(response.status, { message: 'Failed to post claim' });
		}

		const data = await response.json();
		return data;
	}
};
