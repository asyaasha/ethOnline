<script>
	export let selected = '';
	/**
	 * @type {any}
	 */
	export let data;
</script>

<select bind:value={selected}>
	<option value="" disabled selected>Select Ledger..</option>
	{#each data as option (option)}
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
