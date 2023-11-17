import { fail } from '@sveltejs/kit';
import { invalidateAll } from '$app/navigation';
import { applyAction, deserialize } from '$app/forms';
import { env } from '$env/dynamic/public';

/** @type {any} */
export let form;

const BASE_URL = `http:${env.PUBLIC_AGENT_URL}` || 'http://0.0.0.0:5555';

/** @param {{ currentTarget: EventTarget & HTMLFormElement}} event */
async function postClaim(event) {
	const formData = new FormData(event.currentTarget);

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
		return fail(response.status, { result: 'Failed to post claim' });
	}

	/** @type {import('@sveltejs/kit').ActionResult} */
	const result = deserialize(await response.text());

	if (result.type === 'success') {
		// rerun all `load` functions, following the successful update
		await invalidateAll();
	}

	applyAction(result);

	return { data: result };
}

export default postClaim;
