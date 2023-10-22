<script>
	import { onMount } from 'svelte';
	import { getChains } from '$lib/actions/getChains';
	import { postClaim } from '$lib/actions/postClaim';
	/**
	 * @type {any[]}
	 */
	let options = [];
	export let selected = '';

	onMount(() => {
		async function main() {
			const response = await getChains();
			const data = await response?.json();
			options = data?.data;
		}

		main();
	});
	$: console.log(selected);
</script>

<select bind:value={selected}>
	<option value="" disabled selected>Select Ledger..</option>
	{#each options as option (option)}
		<option value={option}>{option.chain_name}</option>
	{/each}
</select>

<style>
	select {
		padding: 5px;
		border: 0.8px solid #ddddddb7;
		border-radius: 5px;
		font-size: 14px;
		width: 100%;
		background: rgb(0, 5, 8);
		color: rgb(251, 251, 251);
		font-weight: 500;
	}
</style>
